
## 要求三

### ● 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。   
    mysql> INSERT INTO `member` (`name`,`username`,`password`, `follower_count`) VALUES ('小明','test','test',100);   
    mysql> INSERT INTO `member` (`name`,`username`,`password`, `follower_count`) VALUES ('小花','123','123',80);   
    mysql> INSERT INTO `member` (`name`,`username`,`password`, `follower_count`) VALUES ('小竹','456','456',60);   
    mysql> INSERT INTO `member` (`name`,`username`,`password`, `follower_count`) VALUES ('小梅','789','789',50);   
    mysql> INSERT INTO `member` (`name`,`username`,`password`, `follower_count`) VALUES ('小蘭','741','741',30);     
    mysql> INSERT INTO `member` (`name`,`username`,`password`, `follower_count`) VALUES ('小菊','852','852',20);    
    mysql> INSERT INTO `member` (`name`,`username`,`password`, `follower_count`) VALUES ('小美','963','963',60);    
![image](https://user-images.githubusercontent.com/94776718/150919893-329a6e74-bf87-4619-a6f2-d51a34e5109e.png)


### ● 使用 SELECT 指令取得所有在 member 資料表中的會員資料。  
    mysql> SELECT * FROM `member`; 　　  
![image](https://user-images.githubusercontent.com/94776718/150919934-6de51614-b6c5-4914-8205-a06e4eccebb3.png)


### ● 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
    mysql> SELECT *
        -> FROM `member`
        -> ORDER BY `time` DESC;
![image](https://user-images.githubusercontent.com/94776718/150920653-7c99c1dd-19a4-4f10-bf97-e6baee39b009.png)

### ● 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。
    mysql> SELECT * FROM `member`    
        -> ORDER BY `time` DESC   
        -> LIMIT 1,3;  
![image](https://user-images.githubusercontent.com/94776718/150931606-c31709b2-fdb7-4d56-b584-b85a12894311.png)

### ● 使用 SELECT 指令取得欄位 username 是 test 的會員資料。    
    mysql> SELECT * FROM `member`      
        -> WHERE `username`= 'test';     
![image](https://user-images.githubusercontent.com/94776718/150934306-99686f54-ea28-4541-bfa7-aa72819804c6.png)

### ● 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。    
    mysql> SELECT * FROM `member`    
        -> WHERE `username`= 'test' and `password`='test';   
![image](https://user-images.githubusercontent.com/94776718/150934354-485e6a42-02c0-4e45-bcf4-a2845e845040.png)

### ● 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。   
    mysql> UPDATE `member`   
        -> SET `name`='test2'    
        -> WHERE `username`='test';   
![image](https://user-images.githubusercontent.com/94776718/150935274-f1e69c97-5a2c-44e4-9170-8af4574c1fca.png)
![image](https://user-images.githubusercontent.com/94776718/150935329-96c32aa5-186d-4670-a559-9089a936bd3b.png)



## 要求四    
### ● 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
### ● 取得 member 資料表中，所有會員 follower_count 欄位的總和。
### ● 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
## 要求五
### ● 在資料庫中，建立新資料表，取名字為message。


### ● 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。
### ● 使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名。
