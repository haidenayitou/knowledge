#nginx 
##nginx 命令行控制
`pid 文件的作用就是防止启动多个进程的副本：每个pid文件中只有一行只包含一个进程的pid号，只有获得pid文件的写入权限的进程才能正常启动并且把自身的pid写入到pid文件中，其它同一程序的进程都统一退出`

```
默认方式开启nginx服务： nginx
指定配置文件的启动方式：nginx -c filepath
测试配置文件是否有效： nginx -t (可以用来查看默认配置文件的路径)
在测试配置阶段不输出信息：nginx -t -q
显示版本信息： nginx -v
显示编译阶段的参数： nginx -V
快速停止服务(相当于发送了TERM或者INT信号)：nginx -s stop ｜ kill -s SIGTERM  pid | kill -s SIGINT pid
优雅地停止服务(可以处理完当前请求在停止服务)：nginx -s quit |kill -s SIGOUT master pid 
停止某个worker进程： nginx -s SIGWICH (worker pid)
使运行中的Nginx重读配置文件项并且生效(首先会检查新的配置文件的错误，如果全部正确则以优雅的方式关闭，并且重新启动Nginx服务)：nginx -s reload ｜ nginx -s SIGUP master pid 
日志文件回滚：nginx -s reopen
```


#nginx配置

 **部署Nginx服务都适用一个master进程来管理多个worker进程，一般情况下，worker进程的数量与服务器上的CPU核数相等（进程切换代价最小），每个worker 进程都是繁忙的，在真正地提供互联网服务，master进程则很悠闲，只用来监控管理worker 进程**
 
 Nginx 运行的时候至少必须交在几个核心模块和一个事件类模块，配置项比较多，可以分为4类：	
 1. 用于调试，定位问题的配置项
 2. 正常运行的必备配置项
 3. 优化性能的配置项
 4. 事件类配置项
 
 **用于调试的配置项**
 
 1. 是否以守护进程运行： `daemon on|off` 默认是on 
 	
 2. 是否以master/worker方式工作： `master_process on|off` 默认是on	
 3. error日志的设置： `error_log: /path/file level`,   level 的范围是debug、info、notice、warn error  crit alert emerg，级别依次增大，当设定一个级别时，大于或等于该级别的日志都会被输出到／path/file中去，小于该级别的日志不会输出
 		
4. 是否处理几个特殊的调试点(如果设置为stop,那么Nginx的代码执行到这些调试点时就会发出SIGSTOP信号以用于调试，如果设置为abort，就会产生了一个coredump文件，可以使用gdb查看Nginx当时的各种信息):`debug_point [stop:abort]` 
 
 5. 仅对指定的客户端输出debug日志：`debug_connection:[IP|CIDR]` 
 
    ```
 	events {
 		debug_connection 10.223.66.14;
 		debug_connection 10.224.57.0/24;
 	}
    ```
6. 限制coredump核心转储文件的大小：`worker_rlimit_core size`

  ```
   核心转储文件是在linux系统中，当进程发生错误或者接收到信号终止时，系统会讲进程执行时的内存内容写入到一个文件中，以作为调试之用，这就是所谓的核心转储，当Nginx进程出现一些非法操作导致进程直接被操作系统强制关闭时，就会生成核心转储文件，可以从文件中获取当时的堆栈、寄存器等信息。
   ```
   
   
7. 指定coredump文件生成目录 `working_directory path` 

**正常运行的配置项**
	
1. 定义环境变量： `env var = value`
	
	```
		env TESTPATH=/tmp/;
	```
2. 嵌入其他配置文件：`include mime.types`

	```
		include vhost/*.conf
	```
3. pid文件的路径： `pid path/file;`
	
	```
		#必须确保Nginx有权在相应的目标中创建pid文件
		pid logs/nginx.pid;
	```
4. Nginx进程运行的用户及用户组： `user username [groupname]`
	
	```
		#user用于设置master进程启动后，fork出的worker进程运行在哪个用户和用户组下
		user nobody nobody;
	```
5. 指定Nginx worker进程可以打开的最大句柄描述符个数：`worker_rlimit_nofile limit`
6. 限制信号队列：`worker_rlimit_sigpending limit`
	
	```
		#设置每个用户发给Nginx的信息队列的大小，也就是说，当某个用户的信息队列满了，这个用户再发送的信息量就会被丢弃
	```

**优化性能的配置项**

1. Nginx worker进程个数:`worker_processes number` 默认情况下是1

2. 绑定 Nginx worker到指定的cpu 内核：`worker_cpu_affinity cpumask[cuumask]`

	```
		＃如果有4个内核，就可以进行如下配置
		worker_processes 4;
		worker_cpu_affinity 1000 0100 0010 0001;
	```
3. SSL 硬件加速： `ssl_engine device;`

	```
		#可以通过OpenSSL提供的命令来查看是否有SSL硬件加速设备
		openssl engine -t
	```
4. Nginx worker 进程优先级设置：｀worker_priority 0｀
 
 	```
 		在 linux操作系统中，当许多进程处于可执行状态的时候，将按照所有进程的优先级来决定本次内核选择哪个进程执行，进程所分配的CPU时间片大小也与进程的优先级有关，优先级越高，进程分配到的时间片也就越大，（在默认配置下，最小的时间片时5ms,最大的时间片时800ms,）优先级更高的进程会占有更多的系统资源
 		如果希望用户Nginx占有更多的系统资源，那么可以把优先级设置得更小一点，但不建议比内核进程的值（通常为－5）更小
 	```
 
**事件类配置项**

1. 是否打开accept锁：`accept_mutex [on|off]` 默认是打开的

	```
		#accept_mutex时Nginx的负载均衡锁，accept_mutex这把锁可以让多个worker进程轮流地、序列化地与新的客户端建立TCP连接，当某一个worker进程建立的连接数量达到worker_connection配置的最大连接数的7/8时，会大大减少该worker进程试图建立新TCP连接的机会，依次实现所有worker进程之上处理的客户端请求数尽量接近。
	```
2. lock文件的路径：`lock_file logs/nginx.lock`

	```
		当系统不支持原子锁的时候，就使用文件锁实现accept锁
	```
3. 使用accept锁后到真正建立连接之间的延迟时间： `accept_mutex_delay 500nm`

	```
		在使用了accept锁之后，同一时间只有一个进程获得锁，这个锁不是阻塞锁，如果取不到会立刻返回，如果有一个worker进程试图取accept锁而没有取到，它至少要等待accept_mutex_delay定义的时间间隔之后才能再次获得锁
	```
4. 选择事件模型： `use poll|select|epoll` 默认情况下会自动使用最合适的事件模型
5. 每个worker的最大连接数

	```
		定义每个worker进程可以同时处理的最大连接数
	```




























 
  



 
 