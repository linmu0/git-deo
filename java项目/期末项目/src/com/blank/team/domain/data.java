package com.blank.team.domain;

public class data {
    public String deposit=null;      //开户银行
    public int balance;
    public String account;
    public String password;
    public String id_card;
    public String phone_number;
    public String name;

    public data(String account,String password,String id_card,String phone_number,String name,int balance,String deposit){

        this.account=account;
        this.password=password;
        this.id_card=id_card;
        this.phone_number=phone_number;
        this.name=name;
        this.balance=balance;
        this.deposit=deposit;
    }
    public data(){}
}
