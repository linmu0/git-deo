package service;


import com.blank.team.domain.*;

import java.sql.SQLException;
import java.util.Objects;
import java.util.Scanner;
/*登录
* 1.判断账户是否开户
* 2.判断账号密码是否正确
* */
//开户：启用银行卡，将银行卡的开户银行改为本行，如果开户银行为空，则代表该卡未使用


public class operateView {
    private static boolean sta=true;
    Mysql mysql=new Mysql();
    Scanner input=new Scanner(System.in);
    Scanner scan=new Scanner(System.in);

    public static void main(String[] args) throws SQLException, InterruptedException {
        operateView view=new operateView();
        view.login();
    }
    //初始界面，含有4个选项
    public void login() throws SQLException, InterruptedException {
        while (true){
            System.out.println("❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅");
            System.out.println("❅❅❅❅❅❅❅❅❅❅❅❅❅菜单栏❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅");
              System.out.print(" ❅  1-登录  2-账户启用  3-银行卡办理 4-退出  ❅\n");
            System.out.println("❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅");
            System.out.print("\n❅请选择：");
            //创建一个银行卡的类，类属性具有1.开户银行（判断该卡是否启用）；2.余额 float；3.账号 string；
            //4.密码 string；5. 身份证号码 string；6.手机号 string；7. 所有人姓名。
            int choose1=input.nextInt();
            System.out.println("\n❅❅❅❅❅❅❅❅❅❅❅❅❅操作栏❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅");
            if(choose1>0 &choose1<5) {
                switch (choose1) {
                    case 1:
                        //用登录的账户，把对应账户的信息赋值给一个用户对象，然后输出余额数学
                        /*
                        * 1.获取账号密码
                        * 2.判断银行卡是否已开户，没有则返回提示
                        * 3.登录成功跳转操作界面
                        * */
                        System.out.print("请输入卡号：");
                        String account=new Scanner(System.in).nextLine();
                        System.out.print("请输入密码：");
                        String p=new Scanner(System.in).nextLine();
                        //判断对应账户是否存在
                        String a=mysql.search(account);
                        if(Objects.equals(a,"1")){
                            data user=mysql.inquire(account);
                            if(Objects.equals(user.password,p)){
                                System.out.println("登录成功");
                                new operateView().enterMainMenu(account);

                            }
                            else {
                                System.out.println("密码错误!!!");
//                                Thread.sleep(1);
                            }
                        }
                        else {
                            System.out.println("账户不存在");
                            Thread.sleep(1);
                        }
                        break;
                    case 2:
                        /*
                         * 1.判断该卡是否已经开户
                         * 已经开户则返回提示
                         * 未开户则进行开户，输入办卡的手机号，正确则进行开户，对数据库的开户银行进行修改
                         * */
                        System.out.print("请输入卡号：");
                        String account2=new Scanner(System.in).nextLine();
                        System.out.print("请输入密码：");
                        String p1=new Scanner(System.in).nextLine();
                        //判断对应账户是否存在
                        String a1=mysql.search(account2);
                        if(Objects.equals(a1,"1")){
                            User user=mysql.inquire(account2);
                            if(Objects.equals(user.password,p1)){
                                if(Objects.equals(user.deposit,null)){
                                    mysql.updata_deposit(account2);
                                    System.out.println("开户成功!!!");
                                }
                                else {
                                    System.out.printf("该账户已开通，开户银为:%s",user.deposit);
                                }

                            }
                            else {
                                System.out.println("密码错误!!!");
                            }
                        }
                        else {
                            System.out.println("账户不存在");
                        }
                        System.out.println("输入回车下一步");
                        scan.nextLine();
                        break;
                    case 3:
                        /*开户
                         * 1.输入身份证号
                         * 2.判断该身份证拥有本行的卡数是否超过4
                         * 3.输入密码，手机号，用户名
                         * 4.随机生成卡号，返回
                         * 5.数据库插入信息
                         * */
                        System.out.printf("请输入姓名：");
                        String name=new Scanner(System.in).nextLine();
                        System.out.print("请输入您的身份证号：");
                        String id_card=new Scanner(System.in).nextLine();
                        int count=mysql.statistics(id_card);
                        if(count<5){
                            System.out.print("请输入手机号，该手机号将绑定于该卡：");
                            String phoneNumber=new Scanner(System.in).nextLine();
                            System.out.print("请设置密码：");
                            String p2=new Scanner(System.in).nextLine();
                            System.out.print("请再次输入密码：");
                            String p3=new Scanner(System.in).nextLine();
                            if(Objects.equals(p2,p3)){
                                String newAccount=mysql.insetUser(p2,id_card,phoneNumber,name);
                                System.out.println("银行卡办理成功");
                                System.out.printf("您的卡号为：%s",newAccount);
                            }
                            else {
                                System.out.println("俩次输入的密码不同！！！");
                            }
                        }
                        else {
                            System.out.println("您的身份证下已有五张银行卡，本行规定\n每个用户在本行的账户数，不因超过五个。");
                        }
                        System.out.print("\n输入回车下一步");
                        new Scanner(System.in).nextLine();
                        break;
                    case 4:
                        System.out.println("感谢使用！！！");
                        Thread.sleep(2);
                        return;

                }
            }
            else {
                System.out.println("输入错误!!!");
            }
        }
    }
//    用户选择列表
    public void enterMainMenu(String account) throws SQLException, InterruptedException {
//        用户数据
        data user=mysql.inquire(account);
//       选择列表
        while (true){
            System.out.println("\n❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅");
            System.out.println("❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅功能选择区❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅");
              System.out.print(" ❅❅  1-查询账户余额  2-存款  3-取款  4-转账  5-修改银行卡密码  6-销毁用户  7-退出  ❅❅");
            System.out.println("\n❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅");
            System.out.print("\n❅请选择(1-7)：");
        //创建一个银行卡的类，类属性具有1.开户银行（判断该卡是否启用）；2.余额 float；3.账号 string；
        //4.密码 string；5. 身份证号码 string；6.手机号 string；7. 所有人姓名。
         int choose=input.nextInt();
            System.out.println("\n❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅操作栏❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅\n");
            if(choose>0 &choose<8){
            switch (choose){
                case 1:
                    //用登录的账户，把对应账户的信息赋值给一个用户对象，然后输出余额数学
                    System.out.println("余额查询成功！！！");
                    System.out.printf("您当前余额为：%s\n",user.balance);
                    System.out.print("输入回车下一步");
                    new Scanner(System.in).nextLine();
                    break;
                case 2:
                    //用登录的账户，把对应账户的信息赋值给一个用户对象，然后输出余额数学
                    System.out.print("存入金额为：");
                    int amount=new Scanner(System.in).nextInt();
                    /*
                    *1.该用户对象余额属性增加对应值
                    *2.对数据库的余额进行增加
                    */
                    user.balance=user.balance+amount;
                    mysql.updata_banlace(account,"+",amount);
                    System.out.println("存款成功");
                    System.out.println("输入回车下一步:");
                    scan.nextLine();
                    break;
                case 3:
                    System.out.print("所取金额为：");
                    int amount1=new Scanner(System.in).nextInt();
                    /*
                    *1.判断金额是否足够
                    *2.该用户对象余额属性减少对应值
                    *3.对数据库的余额进行减少
                    *4.输出变更后的余额
                    */
                    if(user.balance>=amount1){
                        user.balance=user.balance-amount1;
                        mysql.updata_banlace(account,"-",amount1);
                        System.out.println("取款完成");
                    }
                    else {
                        System.out.println("您的余额不足");
                    }
                    System.out.print("输入回车下一步");
                    new Scanner(System.in).nextLine();
                    break;
                case 4:
                    System.out.print("持卡人姓名：");
                    String name1=new Scanner(System.in).nextLine();
                    System.out.print("请输入需要转账的账户：");
                    String account1=new Scanner(System.in).nextLine();
                    System.out.print("转款金额为：");
                    int amount3=new Scanner(System.in).nextInt();
                    /*
                    *1.判断所转银行卡是否存在，拥有者姓名是否正确
                    *2.判断金额是否足够
                    *3.该用户对象余额属性减少对应值
                    *4.对数据库的余额进行减少
                    *5.判断所转卡号是否为本卡
                    */
                    //判断对应账户是否存在
                    if(user.balance<amount3){
                        System.out.println("您的余额不足");
                        Thread.sleep(1);
                        break;
                    }
                    if(Objects.equals(user.account,account1)){
                        System.out.println("您的输入的账户就是当前您使用的账户");
                        Thread.sleep(1);
                        break;
                    }
                    String a=mysql.search(account1);
                    if(Objects.equals(a,"1")){
                        data user1=mysql.inquire(account1);
                        if(Objects.equals(user1.name,name1)){
                            user.balance=user.balance-amount3;
                            mysql.updata_banlace(account,"-",amount3);
                            mysql.updata_banlace(account1,"+",amount3);
                            System.out.println("转账完成");
                        }
                        else {
                            System.out.println("用户名和账户不匹配!!!");
                        }
                    }
                    else {
                        System.out.println("账户不存在");
                    }

                    System.out.println("输入回车下一步");
                    new Scanner(System.in).nextLine();
                    break;
                case 5:
                    System.out.print("原始密码为：");
                    String password1=new Scanner(System.in).nextLine();
                    System.out.print("新密码为：");
                    String password2=new Scanner(System.in).nextLine();
                    /*
                     *1.判断密码是否正确
                     *2.该用户对象的密码修改
                     *3.对数据库的密码进行修改
                     *4.重新登录
                     */
                    if(Objects.equals(user.password,password1)){
                        mysql.updata_password(account,password2);
                        System.out.println("密码修改完成完成，请重新登录");
                        System.out.println("输入回车下一步");
                        new Scanner(System.in).nextLine();
                        return;
                    }
                    else {
                        System.out.println("您输入的密码错误");
                    }

                    System.out.print("输入回车下一步");
                    new Scanner(System.in).nextLine();
                    break;
                case 6:
                    /*
                    * 1.判断银行卡的金额是否小于一个定值，如果小于则进行下一步
                    * 2.判断输入的信息是否与持卡者信息一致
                    * 3.用户再次确认请求
                    * 4.对数据库该人的信息进行删除
                    * */
                    System.out.print("请输入持卡人姓名：");
                    String name=new Scanner(System.in).nextLine();
                    System.out.print("请输入持卡者身份证号码：");
                    String card=new Scanner(System.in).nextLine();
                    if(Objects.equals(user.name,name) & Objects.equals(user.id_card,card)){
                        if(user.balance>=50){
                            System.out.println("您的账户余额过多，不支持注销，请取走您的余额，以免照成财产损失");
                            Thread.sleep(1);
                            break;
                        }
                        System.out.print("\n确定是否注销\n温馨提示：如果注销您将会失去对这张银行卡Y/N：");
                        String c=new Scanner(System.in).nextLine();
                        if(Objects.equals(c,"Y")){
                            mysql.deleteUser(account);
                            System.out.println("注销成功,感谢您的使用!!!");
                            System.out.println("输入回车下一步");
                            new  Scanner(System.in).nextLine();
                            return;
                        }
                    }
                    else {
                        System.out.println("您输入的信息有误");
                    }

                    System.out.println("输入回车下一步");
                    new  Scanner(System.in).nextLine();
                    break;
                case 7:

                    return;
            }

            }
        else {
            System.out.println("输入错误!!!");
        }
        }

    }

}
