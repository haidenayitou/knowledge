#mysql

##连接数据库和SHOW语句
`mysql -h 主机名 －p 端口号 -u 用户名 －p密码`    
`SHOW COLUMNS FROM customers`	
`SHOW STATUS` 用于显示服务器状态信息
`SHOW GRANTS` 用于显示授权用户的安全权限
`show ERRORS和SHOW WARNING` 用于显示服务器错误或者警告信息

##查询
`SELECT DISTINCT vend_id FROM products LIMIT 5,5` LIMIT 语句可以指定检索的开始行和行	
`DESC `降序排列 默认`ASC`是升序排列的	
`SELECT prod_id, prod_name FROM products WHERE prod_name LIKE 'jet%'` %表示任何字符出现任意次数	
`SELECT prod_id, prod_name FROM products WHERE prod_name LIKE '_ ton anvil'` _用来表示单个任意字符	

	


 