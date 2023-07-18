import pymysql
class Mysql:
    def __init__(self , host='localhost', user='root', db='os', password='', charset='utf8'):
        self.host = host
        self.user = user
        self.db = db
        self.password = password
        self.charset = charset

    def get_user(self):
        ret = []
        db = pymysql.connect(host=self.host, user=self.user, db=self.db, password=self.password, charset=self.charset)
        curs = db.cursor()
        
        sql = "select * from user";
        curs.execute(sql)
        
        rows = curs.fetchall()
        # db.commit()
        db.close()
        return rows
    
    def insert_user(self , username , email , phone , password):
        db = pymysql.connect(host=self.host, user=self.user, db=self.db, password=self.password, charset=self.charset)
        curs = db.cursor()
        
        sql = '''insert into user (username, email, phone, password) values(%s,%s,%s,%s)'''
        result = curs.execute(sql,(username, email, phone,password))
        print(result)
        db.commit()
        db.close()

    def del_user(self, email):
        db = pymysql.connect(host=self.host, user=self.user, db=self.db, password=self.password, charset=self.charset)
        curs = db.cursor()
        
        sql = "delete from user where email=%s"
        result = curs.execute(sql,email)
        print(result)
        db.commit()
        
        db.close()
    
mysql = Mysql(password='java')
# rows = mysql.get_user()
# print(rows)

# mysql.insert_user("garykim", "1@naver.com", "010-8496-9889", "1234")

mysql.del_user("2@naver.com")

    