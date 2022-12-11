package com.blank.team.domain;

public class User {
    /*
     *创建一个银行卡的类，类属性具有1.开户银行（判断该卡是否启用）；2.余额 float；3.账号 string；
     *4.密码 string；5. 身份证号码 string；6.手机号 string；7. 所有人姓名。
     */
    public String deposit=null;      //开户银行
    public int balance;
    public String account;
    public String password;
    public String id_card;
    public String phone_number;
    public String name;

    public User(String account,String password,String id_card,String phone_number,String name,int balance,String deposit){

        this.account=account;
        this.password=password;
        this.id_card=id_card;
        this.phone_number=phone_number;
        this.name=name;
        this.balance=balance;
        this.deposit=deposit;
    }



}