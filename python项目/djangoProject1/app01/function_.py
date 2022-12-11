import pymysql
import random
import sys  # 导入sys模块
sys.setrecursionlimit(2000)  # 将默认的递归深度修改为3000

class Mysql_operate():
    def __init__(self):
        # python需要管理员权限，打开mysql cmd(管理员模式)输入: net start mysql
        try :
            self.conn = pymysql.connect(
                host='localhost', # 连接本地mysql
                user='root', #本地用户名
                password='123123', # 你自己的密码(没有就不管)
                db='Student', # 你连入的数据库名
                charset='utf8', # 编码
                # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
            )
            # 2. 创建游标对象，
            self.cur = self.conn.cursor()
        except Exception as e:
            print("连接失败:", e)
        else:
            print("连接成功成功;")
        # python, 必须有一个游标对象， 用来给数据库发送sql语句， 并执行的.
        # self.Creat()
    def account_Creat(self):    #创建所需求的表格
        """
        创建账户表格
        :return:True
        """
        try:
            create_sql2 = "create table Account (account varchar(11) not NULL unique," \
                         "password varchar(15)" \
                         ");"  # 默认表格元素，可添加
            self.cur.execute(create_sql2)
        except Exception as e:
            print("创建数据表失败:", e)
            return False
        else:
            print("创建数据表成功;")
            return True

    def student_information_creat(self,ID):
        """
        一个账户对应一个student_information
        :param ID: 账户名
        :return:
        """
        try:
            create_sql1 = "create table {} (id int not NULL unique, " \
                         "stuname varchar(30) not NULL," \
                         "stuphone varchar(12)," \
                         "point float," \
                         "high float," \
                         "address varchar(30)" \
                         ");".format("student_information"+ID)  # 默认表格元素，可添加
            self.cur.execute(create_sql1)
        except Exception as e:
            print("创建数据表失败:", e)
            return False
        else:
            print("创建数据表成功;")
            return True

    def stu_Insert(self,Account,Id,Stuname,Stuphone,point,high,address):
        try:
            insert_sql="INSERT into {0} VALUES( {1},'{2}',{3},'{4}','{5}','{6}');".format(
                        "student_information"+Account,
                        Id,
                        Stuname,
                        Stuphone,
                        float(point),
                        float(high),
                        address)

            self.cur.execute(insert_sql)
            self.cur.connection.commit()  # 执行commit操作，插入语句才能生效
            # self.cur.close()
            # self.conn.close()
        except Exception as e:
            print("数据插入失败:", e)

        else:
            print("数据插入成功！！！")

    def account_Insert(self,account,password):
        try:
            insert_sql="INSERT into account VALUES( {0},'{1}');".format(account,password)

            self.cur.execute(insert_sql)
            self.cur.connection.commit()  # 执行commit操作，插入语句才能生效
            # self.cur.close()
            # self.conn.close()
        except Exception as e:
            print("数据插入失败:", e)

        else:
            print("数据插入成功！！！")

    def Delete(self,Id,Account):
        try:
            delete_sql="delete from {0} where id ={1};".format("student_information"+Account,Id)
            self.cur.execute(delete_sql)
            self.cur.connection.commit()  # 执行commit操作，插入语句才能生效
            # self.cur.close()
            # self.conn.close()
        except Exception as e:
            print("数据删除失败:", e)
        else:
            print("数据删除成功！！！")
# 用id进行查找,用于指定查找
    def account_password_Comparison(self,Account,Password):
        """
        存储的id，在数据库里面默认是有序的，采用二分法进行查找
        :param Password: 密码
        :param Account: 对应账户
        :return: 找到数据则返回对应数据，否则则返回空
        """
        # 指定账户的信息
        all_data=self.All_data_account()
        for i in range(len(all_data)):
            if all_data[i][0]==Account and all_data[i][1]==Password:
                return True
        return False
    def account_judgment(self,Account):
        """
        存储的id，在数据库里面默认是有序的，采用二分法进行查找
        :param Account: 对应账户
        :return: 找到数据则返回对应数据，否则则返回空
        """
        # 指定账户的信息
        all_data=self.All_data_account()
        # print(all_data)
        for i in range(len(all_data)):
            if all_data[i][0]==Account:
                return False
            return True

    def sort_stu(self,choose):
        '''

        :param choose: 选择对学号还是身高
        :return:
        '''
        pass
    def Update_account(self,account,new_password):
        try:
            update_sql = "update account set account ={0},password='{1}'where account={2};"\
                .format(account,
                        new_password,
                        account
                        )
            self.cur.execute(update_sql)
            print(update_sql)
            self.cur.connection.commit()  # 执行commit操作，插入语句才能生效
            # self.cur.close()
            # self.conn.close()
        except Exception as e:
            print("数据修改失败:", e)
            return e
        else:
            print("数据修改成功！！！")

    def Update_stu(self,Account,Id,new_id,Stuname,Stuphone,point,high,address):
        try:
            update_sql = "update {0} set" \
                         " id ={1},stuname='{2}', stuphone={3},point='{4}',high='{5}',address='{6}' " \
                         "where id={7};"\
                .format("student_information"+Account,
                        new_id,
                        Stuname,
                        Stuphone,
                        float(point),
                        float(high),
                        address,
                        Id)
            self.cur.execute(update_sql)
            self.cur.connection.commit()  # 执行commit操作，插入语句才能生效
            # self.cur.close()
            # self.conn.close()
        except Exception as e:
            print("数据修改失败:", e)
            return e
        else:
            print("数据修改成功！！！")

    def All_data_stu(self,Account):
        """

        :param Account: 账户名
        :return: resList数据库对应数据
        """
        try:
            All_sql="select * from {}".format("student_information"+Account)
            self.cur.execute(All_sql)
            resList = self.cur.fetchall()      #数据存储到元组中
            # self.cur.close()
            # self.conn.close()
        except Exception as e:
            print("查询数据失败",e)
        else:
            print("查询成功")
            return resList

    def All_data_account(self):
        """

        :return: 元组，所有账户数据
        """
        try:
            All_sql="select * from account"
            self.cur.execute(All_sql)
            resList = self.cur.fetchall()      #数据存储到元组中
            # self.cur.close()
            # self.conn.close()
        except Exception as e:
            print("查询数据失败",e)
        else:
            print("查询成功")
            return resList

        def quick_sort(self, low, high):  # 0-5
            '''

            :param low: 开始参数索引
            :param high: 结束参数索引
            :return: True
            '''
            if low < high:
                pi = self.partition(low, high)  # 1
                print("pi=", pi)
                self.quick_sort(low, pi)  # 0-5
                self.quick_sort(pi + 1, high)
            return True

        # 找到正确索引位置并进行排序  low 0 high 5
        def partition(self, low, high):
            '''

            :param low: 开始参数索引
            :param high: 结束参数索引
            :return: 找到元素正确的索引并返回
            '''
            j = low + 1
            for i in range(low, high):  # 1 len
                if self.list[i] < self.list[low]:
                    self.list[i], self.list[j] = self.list[j], self.list[i]
                    j += 1
            self.list[low], self.list[j - 1] = self.list[j - 1], self.list[low]
            print("更改的数据", self.list)
            return j - 1
# 选择对应数据排序默认升序
class sort_stu:
    # 转为列表
    def __init__(self,Account,choose):
        #所有学生信息
        self.lis=list(Mysql_operate().All_data_stu(Account))
        self.choose=choose
        self.quick_sort(0,len(self.lis),self.choose)

    def quick_sort(self,low,high,num): #0-5
        '''
        :param num   对比的数据
        :param low: 开始参数索引
        :param high: 结束参数索引
        :return: True
        '''
        if low<high:
            pi=self.partition(low,high,num) #1
            self.quick_sort(low,pi,num) #0-5
            self.quick_sort(pi+1,high,num)
        return True

    # 找到正确索引位置并进行排序  low 0 high 5
    def partition(self,low, high,num):
        '''
        :param num   对比的数据
        :param low: 开始参数索引
        :param high: 结束参数索引
        :return: 找到元素正确的索引并返回
        '''
        j=low+1
        for i in range(low,high): # 1 len
            if self.lis[i][num]<self.lis[low][num]:
                self.lis[i],self.lis[j]=self.lis[j],self.lis[i]
                j+=1
        self.lis[low], self.lis[j-1]= self.lis[j-1], self.lis[low]
        return j-1

class search:

    def __init__(self,Data,Id):
        self.Data=Data
        self.Id=Id
        self.data=self.id_search(0,len(self.Data))
    def id_search(self,row,high):
        if row<high:

            n=row+(high-row)//2
            if self.Id<self.Data[n][0]:
                high=n
                return  self.id_search(row,high-1)
            elif self.Id>self.Data[n][0]:
                row=n
                #6-12
                return self.id_search(row+1, high)
            else:
                return self.Data[n]
        return False



class Node(object): #结点类
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.lchild = None
        self.rchild = None


class BST(object):
    """
    inset:实现搜索树的创建
    intermediateTraversal:中序遍历运用长度来保证精确度
    self.result:模糊查询的结果
    """
    # 实现中序遍历
    def __init__(self,node_list,keyword,choose):
        """

        :param node_list:数据 list
        :param keyword: str 查询的关键字
        """
        # 根节点
        self.keyword=keyword
        self.choose=choose
        self.root = Node(node_list[0])
        # 保留根节点
        self.root1=self.root
        for data in node_list[1:]:
            self.insert(data)
        self.result=[]
        self.intermediateTraversal(self.root1)

    def insert(self,data):
        while True:
            # 比根节点小，在左边
            if len(str(data[self.choose]))<=len(str(self.root.data[self.choose])):
                # 左节点存在
                if self.root.lchild:

                    self.root=self.root.lchild
                else:
                    self.root.lchild=Node(data)
                    #回归到顶点
                    self.root=self.root1
                    # print("l",self.root.lchild.data)
                    break
            else:
                if self.root.rchild:
                    self.root=self.root.rchild

                else:
                    self.root.rchild = Node(data)
                    #回归到顶点
                    self.root = self.root1
                    # print("r", self.root.rchild.data)
                    break
    def intermediateTraversal(self, now):
        if now is None:
            return
        # 到达最下面一个左节点
        self.intermediateTraversal(now.lchild)
        if self.keyword in str(now.data[self.choose]):
            self.result.append(now.data)
        self.intermediateTraversal(now.rchild)
        return

def Data_injection():
    a =list( "2681545")
    b=list("4561545")
    c=list("1151545")
    d=list("7894615")
    print(a)
    for i in range(0,1000,4):

        random.shuffle(a)
        random.shuffle(b)
        random.shuffle(c)
        random.shuffle(d)
        Mysql_operate().stu_Insert("1314520",str(1001+i),"李五","".join(a),round(random.uniform(0, 5),2),168.6+random.randint(-10, 10),random.choice(["重庆","湖南","湖北","安徽","江苏","北京","广东","福建"]) )
        Mysql_operate().stu_Insert("1314520",str(1002+i),"李六","".join(b),round(random.uniform(0, 5),2),158.3+random.randint(-10, 10),random.choice(["重庆","湖南","湖北","安徽","江苏","北京","广东","福建"]) )
        Mysql_operate().stu_Insert("1314520",str(1003+i),"李七","".join(c),round(random.uniform(0, 5),2),168.6+random.randint(-10, 10),random.choice(["重庆","湖南","湖北","安徽","江苏","北京","广东","福建"]) )
        Mysql_operate().stu_Insert("1314520",str(1004+i),"李八","".join(d),round(random.uniform(0, 5),2),178.1+random.randint(-10, 10),random.choice(["重庆","湖南","湖北","安徽","江苏","北京","广东","福建"]) )



if __name__ == '__main__':
    #创建账户表格
        # Mysql_operate().account_Creat()
    # 创建账户
    # Mysql_operate().account_Insert("11111","12312")
    #创建账户对应的表格
    # Mysql_operate().student_information_creat("1314520")
    # 对应账户表中注入数据
    # Data_injection()
    # 获取全部数据
        # result=Mysql_operate().All_data_stu("11111")
    # 排序3,对绩点排序，4对身高排序，返回列表，里面是元组封装的数据，采用快速排序
    # print(sort_stu("1314520",4).lis)
    # 搜索对应数据，包含模糊查询，以精度组成顺序，id则为准确查询，采用二分法遍历。
    # 1. id精确查询
    # result=Mysql_operate().All_data_stu("11111")
    # outcome = search(result,1001).data
    # print(outcome)
    # 搜索二叉树的创建,实现模糊搜索
    # data=["134","1785","98489","657998","12","1","01","001"]
    # text=BST(data,"1")
    # print(text.result)
    # 账号密码比对
    # print(Mysql_operate().All_data_account())
    # a=Mysql_operate().account_password_Comparison('1314520', '123123')
    # print(a)
    # Mysql_operate().Delete("1003","1314520")
    data = list(Mysql_operate().All_data_stu('1314520'))
    # print(data)
    text=BST(data, '160', 4)
    print(text.result)
    # # pass
