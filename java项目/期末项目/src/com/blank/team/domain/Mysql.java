package com.blank.team.domain;

import java.sql.*;
import com.blank.team.domain.*;

public class Mysql {
    //        2.用户信息和url
    String url = "jdbc:mysql://localhost:3306/bankuser?useUnicode=true&characterEncoding=utf8&useSSL=true";
    String username = "root";
    String password = "123123";



    public static void main(String[] args) throws SQLException, ClassNotFoundException {
        Mysql m=new Mysql();
        //        1.加载驱动
        Class.forName("com.mysql.cj.jdbc.Driver");
//        String sql = "SELECT *FROM studentinfo;";
//        ResultSet resultSet = statement.executeQuery(sql);
//        while(resultSet.next()){
//            System.out.println("SNo="+resultSet.getString("SNo"));
//        }

//        //创建数据库
//        m.creat_table();
//        //插入数据
//        String a=m.insetUser("123123","010258","78945","张三");
////        System.out.println(a);
//        //删除用户
//        m.deleteUser("1101");
//        //判断对应账户是否存在
//        m.search("1102");
//        //对余额进行增加或者减少
//        m.updata_banlace("1101","-",9);
//        //修改密码
//        m.updata_password("1101","1111");
//        //统计该身份证下的我行卡的个数
        int s=m.statistics("010258");
        System.out.println(s);
//        //获取用户信息,返回一个对象
//        data user=m.inquire("1101");
//        System.out.println(user.account);
//        //统计现有卡数
//        String a1 = m.statisticsAll();
//        //开户
//        m.updata_deposit("1101");
    }


    //创建数据库表
    /*
     *创建一个银行卡的类，类属性具有1.开户银行（判断该卡是否启用）；2.余额 float；3.账号 string；
     *4.密码 string；5. 身份证号码 string；6.手机号 string；7. 所有人姓名。
     */
    public void creat_table() throws SQLException {
//        3.连接成功，数据库对象 Connection
        Connection connection = DriverManager.getConnection(url, username, password);
//        4.执行SQL对象Statement，执行SQL的对象
        Statement statement = connection.createStatement();
        String create_sql = "create table bankUser (" +
                "account varchar(30) not NULL unique," +
                "password varchar(20) not NULL," +
                "id_card varchar(19) not NULL," +
                "phone_number varchar(12) not NULL," +
                "name varchar(10) not NULL," +
                "balance int default 0," +
                "deposit varchar(30));";
        if(0 == statement.executeLargeUpdate(create_sql)){
            System.out.println("数据创建成功！");
        }
        else {
            System.out.println("数据创建失败！");
        }
        //关闭请求
        statement.close();
        connection.close();
    }
//插入数据
    public String insetUser(String p, String id_card, String phoneNnmber, String name)throws SQLException {
        Mysql m=new Mysql();
//        3.连接成功，数据库对象 Connection
        Connection connection = DriverManager.getConnection(url, username, password);
//        4.执行SQL对象Statement，执行SQL的对象
        Statement statement = connection.createStatement();
        String a = m.statisticsAll();
        int account =10000000;
        account+=Integer.parseInt(a);
        String insert_sql=String.format("INSERT into bankUser(account,password,id_card,phone_number,name) " +
                        "VALUES( '%s','%s','%s','%s','%s');",""+account,p,id_card,phoneNnmber,name);
        if(1 == statement.executeLargeUpdate(insert_sql)){
            System.out.println("数据插入成功！");
        }
        else {
            System.out.println("数据插入失败！");
        }
        //关闭请求
        statement.close();
        connection.close();
        return ""+account;
    };
//删除数据
public void deleteUser(String account)throws SQLException {
//        3.连接成功，数据库对象 Connection
    Connection connection = DriverManager.getConnection(url, username, password);
//        4.执行SQL对象Statement，执行SQL的对象
    Statement statement = connection.createStatement();
    String insert_sql=String.format("delete from bankUser where account=%s;",account);
    statement.executeLargeUpdate(insert_sql);
    //关闭请求
    statement.close();
    connection.close();

};

//判断数据是否存在
public String search(String account)throws SQLException{
    //        3.连接成功，数据库对象 Connection
    String a="0";
    Connection connection = DriverManager.getConnection(url, username, password);
//        4.执行SQL对象Statement，执行SQL的对象
    Statement statement = connection.createStatement();
    String search_sql=String.format("select count(*) as '结果' from bankUser where account=%s",account);
    ResultSet resultSet = statement.executeQuery(search_sql);
            while(resultSet.next()){
            a=resultSet.getString("结果");
        }
    //关闭请求
    statement.close();
    connection.close();
    return a;

}

    //统计身份证下的我行卡的个数
    public int statistics(String id_card)throws SQLException{
        //        3.连接成功，数据库对象 Connection
        String a="0";
        String deposit="本地银行";
        Connection connection = DriverManager.getConnection(url, username, password);
//        4.执行SQL对象Statement，执行SQL的对象
        Statement statement = connection.createStatement();
        String search_sql=String.format("select count(*) as '结果' from bankUser where id_card=%s and deposit='%s'",id_card,deposit);
        ResultSet resultSet = statement.executeQuery(search_sql);
        while(resultSet.next()){
            a=resultSet.getString("结果");
        }
        //关闭请求
        statement.close();
        connection.close();
        return Integer.parseInt(a);

    }
//统计现有银行卡数
    public String statisticsAll()throws SQLException{
        //        3.连接成功，数据库对象 Connection
        String a="0";
        String deposit="本地银行";
        Connection connection = DriverManager.getConnection(url, username, password);
//        4.执行SQL对象Statement，执行SQL的对象
        Statement statement = connection.createStatement();
        String search_sql="select count(*) as '结果' from bankUser";
        ResultSet resultSet = statement.executeQuery(search_sql);
        while(resultSet.next()){
            a=resultSet.getString("结果");
        }
        //关闭请求
        statement.close();
        connection.close();
        return a;

    }

    public void updata_banlace(String account,String symbol,int balance)throws SQLException{
        //        3.连接成功，数据库对象 Connection
        String a="0";
        Connection connection = DriverManager.getConnection(url, username, password);
//        4.执行SQL对象Statement，执行SQL的对象
        Statement statement = connection.createStatement();
        String updataBlance_sql=String.format("UPDATE bankUser SET balance=balance%s%d where account=%s;",symbol,balance,account);
        statement.executeLargeUpdate(updataBlance_sql);
        //关闭请求
        statement.close();
        connection.close();
    }

    public void updata_password(String account,String p)throws SQLException{
        //        3.连接成功，数据库对象 Connection
        String a="0";
        Connection connection = DriverManager.getConnection(url, username, password);
//        4.执行SQL对象Statement，执行SQL的对象
        Statement statement = connection.createStatement();
        String updataBlance_sql=String.format("UPDATE bankUser SET password=%s where account=%s;",p,account);
        statement.executeLargeUpdate(updataBlance_sql);
        //关闭请求
        statement.close();
        connection.close();
    }
    public void updata_deposit(String account)throws SQLException{
        //        3.连接成功，数据库对象 Connection
        String a="0";
        Connection connection = DriverManager.getConnection(url, username, password);
//        4.执行SQL对象Statement，执行SQL的对象
        Statement statement = connection.createStatement();
        String updataBlance_sql=String.format("UPDATE bankUser SET deposit='本地银行' where account=%s;",account);
        statement.executeLargeUpdate(updataBlance_sql);
        //关闭请求
        statement.close();
        connection.close();
    }

    public data inquire(String account) throws SQLException {
        //        3.连接成功，数据库对象 Connection
        String a="";
        String p="";
        String id="";
        String ph="";
        String n="";
        String b="";
        String d="";
        Connection connection = DriverManager.getConnection(url, username, password);
//        4.执行SQL对象Statement，执行SQL的对象
        Statement statement = connection.createStatement();
        String search_sql=String.format("select * from bankUser where account=%s",account);
        ResultSet resultSet = statement.executeQuery(search_sql);

        while(resultSet.next()){
            a=resultSet.getString("account");
            p=resultSet.getString("password");
            id=resultSet.getString("id_card");
            ph=resultSet.getString("phone_number");
            n=resultSet.getString("name");
            b=resultSet.getString("balance");
            d=resultSet.getString("deposit");
        }
        data user = new data(a,p,id,ph,n,Integer.parseInt(b),d);
        //关闭请求
        statement.close();
        connection.close();
        return user;
    }

}

