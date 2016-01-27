第一标题
===========
第二标题
-------------

#第一标题
##第二标题
###第三标题
#####第四标题

> 区块饮用
> #第一标题

>> 区块嵌套

+ 苹果
+ 桃子
+ 西瓜

* 	苹果
* 	桃子
* 	西瓜

1. 苹果
2. 桃子
3. 西瓜


```
这是一个普通段落:
			房间看
```

分割线
-------
d
============
f
************************

Use the `printf()` function.

jlfdj ___kdjfk___ kjlfd

	
#spark论文小节
##概论
> 1. 为了更有效率地实现容错，提供了一种受限的共享内存的方式，是`粗粒度的转换`而不是`细粒度的对共享状态的改变`
> 2. 提供了一种很好的方式重用分布式计算的中间结果，在相同的数据集上进行多次运算，mapreduce是通过将结果写到外部文件上来进行数据的共享（这会导致大量的开销overhead,数据副本，磁盘I/O，序列化，这些都会影响任务的执行时间），rdd可以显示地调用将数据存储到内存中，控制数据的分区，优化数据的存储
> 3. rdd不需要立即去进行计算，只需要知道足够的关于它的依赖关系的信息（lineage）,用户可以去控制数据存储的persistence策略和partitioning方式
> 4. rdd和共享内存的系统相比有两个大的优势：
> >	 *  粗粒度的转换在容错的过程中，一旦失败，只需要根据lineage计算丢失的数据块，而不需要回滚整个进程
> >  *  rdd的不变性，而分布式内存则需要对并发访问进行控制
> 5. rdd不适用的地方是对细粒度共享状态的更新操作，如web应用

##编程接口

* rdd结构 
 
```
1. `Partitions（）`partition列表 
2. `preferedLocation(p)` 传入一个partition，根据数据位置返回数据能够访问到的节点信息 
3. dependencies(),返回依赖关系
4. iterator(p,parentIters),根据父partition计算给定数据块
4. partitioner()返回原数据（rdd是否被hash/range patitioned）
```
操作类型:只有action才会计算真正的结果

```
1. transformation:（map, filter, flatmap, sample,groupByKey,reduceByKey,union,join,cogroup,crossProduct,mapValues,sort,partitionBy）
2. action: (count,collect,reduce,lookup,save)
```

*  依赖类型，窄依赖可以在集群上进行流水线的操作，宽依赖则要求所有数据都是可用的，进行一次数据的shuffle操作，同时容错的时候，一旦一块数据丢失，对于窄依赖来说可以对每一块数据在分布式集群上，进行并行计算，但对于宽依赖来说任何一块数据的丢失都需要所有的祖先rdd重新计算一次

```
1. 宽依赖：对于父rdd中的一块数据最多只能被子rdd中的一块数据使用
2. 窄依赖：对于父rdd中的一块数据可以被子rdd中的多块数据使用
```

* 调度

```
当用户进行执行一次action的时候，调度程序根据rdd的lineage关系去构建一个DAG去执行，每个DAG的单元是一个stage,每个stage包含尽可能多的窄依赖可以流水线运行的转换，stage边界部分则是一些shuffle操作或者是一些早已经计算的数据块，调度器然后启动一个task 去计算所有没有计算完成的partition(每个stage中的)，对于宽依赖中的容错我们进行想mapreduce一样父数据存在节点上，
```

#一些go的函数调用

* os.GetPageSize()获得内存页的大小

#boltdb

* 缓存

```
开始4页：1，2meta页 3，freelist页 4，leafpage
```











































