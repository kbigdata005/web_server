# flask를 이용한 웹서버

가상환경을 구성 하기 위해서 

```powershell
python -m venv web_server
cd web_server

Scripts\activate

>>> (web_server) C:\apps\web_server>
```

.gitignore 파일 생성후

```powershell
/Lib
/Include
/Scripts
pyvenv.cfg
```

파이썬을 이용해서 웹서버를 구현하기 위해 flask 라이브러리 및 framework 를 사용한다.

pip를 이용해서 설치 한다.

```powershell
pip install flask 
```

라이브러리 설치 목록을 따로 만들어 관리하면 다른 곳에서 프로젝트를 구현할때 편리하다.

```powershell
pip freeze > requirements.txt
```

requirements.txt 에 있는 내용대로 라이브러리를 설치하는 방법은 다음과 같다.

```powershell
pip install -r requirements.txt
```

![image](https://github.com/kbigdata005/web_server/assets/139095086/ae2a74f9-df59-447e-b0ca-249d26dd935e)


위와 같은 구조로 웹서버를 만든다.

![image](https://github.com/kbigdata005/web_server/assets/139095086/15a7cc1e-aaa6-4129-9b7e-47ccc859d982)

다음과 같은 기능을 구현하기 위해

url : http://localhost:5000

method : GET 방식

data : Hello World!! 텍스트 데이터가 클라이언트에 전송되도록 한다.

app.py를 생성후 다음과 같이 코드를 추가한다.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!!"

if __name__ == '__main__':
    app.run()
```

파이썬에서 index.html 템플릿 파일을 읽어서 문서데이터 변형후 클라이언트에 전송한다.

url : http://localhost:5000

method : GET 방식

data : Hello World!! 에 포함되어 있는 html 문서 데이터를 전송한다.

templates/index.html 파일을 생성후 다음과 같이 코드를 추가

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>웹페이지</title>
</head>
<body>
    <h1>Hello World!!</h1>
</body>
</html>
```

[app.py](http://app.py) 파일을 다음과 같이 수정한다.

```python
....

@app.route('/')
def index():
    
    return render_template('index.html')

...
```

jinja2 문법과 데이터를 연결하는 방법을 알아 보기 위해서 

app.py의 @app.route(’/’)을 다음과 같이 수정한다.

```python

...

@app.route('/')
def index():
    os_info = dict(request.headers)
    print(os_info) 
    return render_template('index.html',header=os_info )

...
```

index.html 또한 header값을 받아서 단순하게 화면에 보여주기 위해서 다음과 같이 수정한다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>웹페이지</title>
</head>
<body>
    <h1>Hello World!!</h1>
    <span> {{ header }} </span>
</body>
</html>
```

위의 코드와 같이  {{ }} 를 포함해서 {% %} , {# #} 등을 이용하여 jinja2 문법에 맞도로 작성을 하면

데이터 값을 탬플릿에 표현할 수 있다.

크롬 브라우저에서  GET 방식으로 요청 했을때 다음과 같은 결과를 볼 수 있다.

![image](https://github.com/kbigdata005/web_server/assets/139095086/b2855f1f-d297-43ad-a4f8-391b49daa147)

다음 과정은 요청 방식에 대해서 GET 방식과 POST 방식을 구분해서 받는 방법을 테스트 하기 위해

url : http://localhost:5000

method: GET 

에서는 위와 같은 페이지가 랜더링 되고

url: http://localhost:5000

method : POST 

일때는 다음과 같은  페이지가 랜더링 되도록 하기 위해 app.py를 다음과 같이 수정한다.

```python

....

@app.route('/' , methods=['GET','POST'])
def index():
    if request.method == "GET":
        os_info = dict(request.headers)
        print(os_info) 
        return render_template('index.html',header=os_info )
    
    elif request.method == "POST":
        return render_template('index.html',header= "안녕하세요 김태경입니다.!!!")
...
```

 [http://localhost:500](http://localhost:500)0 으로 get방식으로 요청을 할때

즉 , query로 [http://localhost:5000?name=김태경](http://localhost:5000?name=김태경)&hello=안녕하세요

request 하였을때 

![image](https://github.com/kbigdata005/web_server/assets/139095086/82dd0a92-1bdc-4789-ba3e-f831ac8de359)

위와 같이 나타나기 위해서 

app.py를 수정한다.

```python
...

@app.route('/' , methods=['GET','POST'])
def index():
    if request.method == "GET":
        os_info = dict(request.headers)
        print(os_info) 
        name = request.args.get("name")
        print(name)
        hello = request.args.get("hello")
        print(hello)
        return render_template('index.html',header=f'{name}님 {hello}!!' )

...
```

이번에는 GET 방식의 아닌 POST 방식으로 form 데이터 형식으로 일정한 데이터를 보내기위해서

index.html 에 다음과 같이 코드를 변경한다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>웹페이지</title>
</head>
<body>
    <h1>Hello World!!</h1>
    <form action="/" method="POST">
        <div>
          <label for="say">이름을 입력하세요!</label>
          <input name="name" id="say" placeholder="이름" />
        </div>
        <div>
          <label for="to">인사할 내용을 적어주세요</label>
          <input name="hello" id="to" placeholder="인사할내용" />
        </div>
        <div>
          <button>제출</button>
        </div>
      </form>
      
</body>
</html>
```

제출 버튼을 눌렀을때 console 창에 ‘인사할 내용’부분에 적었던 내용이 잘 나오는지 확인한다.

![image](https://github.com/kbigdata005/web_server/assets/139095086/5155b0c4-3262-4b7b-bd6a-f2ab4124fa9d)

위와 같이 구현을 하기 위해 

helllo.html 파일 생성후 다음과 같은 코드를 추가한다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>웹페이지</title>
</head>
<body>
    <form action="/hello" method="POST">
        <div>
          <label for="say">이름 : </label>
          <input name="name" id="say" placeholder="이름" />
        </div>
        <div>
          <label for="to">내용 : </label>
          <input name="hello" id="to" placeholder="인사할내용" />
        </div>
        <div>
          <button>제출</button>
        </div>
      </form>
      
</body>
</html>
```

[app.py](http://app.py) 에서 @app.route(’/hello’, methods =[’GET’, ‘POST’] 

을 작성하고 다음과 같이 GET , POST 방식을 구현한다.

```python
...

@app.route('/', methods=['GET', 'POST'])

....

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method =="GET":
        return render_template('hello.html')
    
    elif request.method =="POST":
        name = request.form['name']
        hello = request.form['hello']
        return render_template('index.html', name=name , hello = hello)

.....
```

index.html을 다음과 같이 수정한다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>웹페이지</title>
</head>
<body>
    <h1>Hello World!!</h1>
    <h3> {{ name }} 님 {{ hello }} </h3>
      
</body>
</html>
```

http://localhost;5000 접속시 name , hello 가 없다면 다른 메세지를 랜더링 할 수 있도록 기능을 구현한다.

index.html을 다음과 같이 수정한다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>웹페이지</title>
</head>
<body>
    <h1>Hello World!!</h1>
    {% if name and hello %}
    <h3> {{ name }} 님 {{ hello }} </h3>

    {% else %}
    <h3>입력한 데이터가 없습니다....</h3>
    {% endif %}
</body>
</html>
```

![image](https://github.com/kbigdata005/web_server/assets/139095086/a89b6d38-38c4-49c9-ae37-641de102bef6)

위와 같은 기능을 구현하기 위하여 app.py를 다음과 같이 코드를 추가한다.

```python

...

@app.route('/list', methods=['GET' , 'POST'])
def list():
    data = Articles()
    return render_template('list.html' , data=data)
...
```

list.html파일을 생성후 다음과 같은 코드를 생성한다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>list page</title>
</head>
<body>
    <h1>List</h1>
    <ul>
        {% for x in data %}
        <div style="margin-bottom: 40px;">
            <li>ID: {{x['id']}}</li>
            <li>TITLE: {{x['title']}}</li>
            <li>DESC: {{x['desc']}}</li>
            <li>AUTHOR: {{x['author']}}</li>
            <li>CREATED AT: {{x['create_at']}}</li>
        </div>
        {% endfor %}
    </ul>
    
</body>
</html>

```

아래와 같은 사이트를 확인 할 수 있다.

![image](https://github.com/kbigdata005/web_server/assets/139095086/cf084cf8-921a-4765-9493-d297c63ba16f)

mysql workbench 를 이용해서 user SChema를 생성한다.

```sql
CREATE SCHEMA `os` DEFAULT CHARACTER SET utf8 ;
```

user 스키마  username ,email, phone, password , create_at 컬럼을 가진 테이블 생성한다.

```sql
CREATE TABLE `os`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `phone` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  `create_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;
```

import pymysql —> pymysql.connect(데이터베이스 연결을 위한 config ) —> cusor() —> excute(쿼리문) —> fetchall()

mysql.py파일을 생성후 다음과 같은 코드를 생성한다.

```python
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

# mysql.del_user("2@naver.com")
```

비밀번호 저장할때는 Hash코드로 변환해서 보안성을 강화할 필요가 있다.

[mysql.py](http://mysql.py) 파일을 다음과 같이 코드를 수정한다.

```python
import pymysql
# 암호화 알고리즘. 256을 제일 많이 사용한다.
from passlib.hash import pbkdf2_sha256 

# 원문 비밀번호를, 암호화 하는 함수

def hash_password(original_password):
    salt = 'eungok'
    password = original_password + salt
    password = pbkdf2_sha256.hash(password)
    return password

def check_password(input_password , hashed_password):
    salt= 'eungok'
    password = input_password + salt
    result = pbkdf2_sha256.verify(password , hashed_password)
    return result

class Mysql:
    def __init__(self , host='localhost', user='root', db='os', password='', charset='utf8'):
        self.host = host
        self.user = user
        self.db = db
        self.password = password
        self.charset = charset

    def get_user(self):
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
        hashed_password = hash_password(password)
        result = curs.execute(sql,(username, email, phone,hashed_password))
        print(result)
        db.commit()
        db.close()

    def verify_password(self ,email, password):
        db = pymysql.connect(host=self.host, user=self.user, db=self.db, password=self.password, charset=self.charset)
        curs = db.cursor()

        sql = f'SELECT * FROM user WHERE email = %s;'
        curs.execute(sql , email)
        
        rows = curs.fetchall()
        print(rows)
        # db.commit()
        db.close()
        if len(rows) != 0:
            hashed_password = rows[0][4]
            result = check_password(password , hashed_password)
            if result:
                print("Welcome to My World!!")
            else:
                print("MissMatch Password")
        else:
            print("User isnot founded")

    def del_user(self, email):
        db = pymysql.connect(host=self.host, user=self.user, db=self.db, password=self.password, charset=self.charset)
        curs = db.cursor()
        
        sql = f"delete from user where email= %s"
        result = curs.execute(sql,email)
        print(result)
        db.commit()
        
        db.close()
    
mysql = Mysql(password='java')
# rows = mysql.get_user()
# print(rows)

# mysql.insert_user("garykim", "1@naver.com", "010-8496-9889", "1234")

# mysql.del_user("2@naver.com")
# password = hash_password("1234")
# print(password)

# result = check_password("1234", "$pbkdf2-sha256$29000$AYBwrhWidI5xbk2pNYbQWg$U1d6Gvc5MS8abctTSauFIaJNyXyRiDPfcGFGsy3uvwY")
# print(result) 

# mysql.verify_password(f"2@naver.com", "1234")
# mysql.verify_password("1@naver.com", "1234")
```

로그인 기능 세션처리 전까지 기록 남겨야 돼!!!!

유저가 로그인 할때 SESSION 처리를 통해서 로그인 유지하는 기능을 구현한다.

[app.py](http://app.py) @app.route(’/login’ ….) 에서 

다음과 같이 코드를 수정한다.

```python
....

@app.route('/login',  methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        db = pymysql.connect(host=mysql.host, user=mysql.user, db=mysql.db, password=mysql.password, charset=mysql.charset)
        curs = db.cursor()

        sql = f'SELECT * FROM user WHERE email = %s;'
        curs.execute(sql , email)
        
        rows = curs.fetchall()
        print(rows)

        if rows:
            result = mysql.verify_password(password, rows[0][4])
            if result:
                session['is_loged_in'] = True
                session['username'] = rows[0][1]
                return redirect('/')
                # return render_template('index.html', is_loged_in = session['is_loged_in'] , username=session['username'] )
            else:
                return redirect('/login')
        else:
            return render_template('login.html')
        

....
```

로그아웃 버튼을 클릭시 세션이 삭제 되면서 로그아웃이 되는 기능을 구현하기 위해 app.py에 다음과 같은 코드를 추가한다.

```jsx
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
```

flask 에서는 html template를 extends 및 include 기능을 이용하여

코드를 최소화 할 수 있는 기능이 있다.

layouts.html파일을 생성 후 다음과 같은 코드를 생성한다.

```html
<!doctype html>
<html lang="en">
  <head>
  	<title>Website menu 04</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

	<link href='https://fonts.googleapis.com/css?family=Roboto:400,100,300,700' rel='stylesheet' type='text/css'>

	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
	
	<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">

	</head>
	<body>
	<section class="ftco-section">
		<div class="container">
			<div class="row justify-content-center">
				<div class="col-md-6 text-center mb-5">
					<h2 class="heading-section">Web_Server #01</h2>
				</div>
			</div>
		</div>
		<div class="container">
		{% block nav %}
        {% endblock %}	
        </div>
  </div>
  {% block body %}

  {% endblock %}
	</section>

    <script src="{{ url_for('static', filename='js/jquery.min.js') }}"></script>
    <script src="{{ url_for('static', filename='js/popper.js') }}"></script>
    <script src="{{ url_for('static', filename='js/bootstrap.min.js') }}"></script>
    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
    

	</body>
</html>
```

nav.html 파일을 생성후 코드 생성

```html
<nav class="navbar navbar-expand-lg ftco_navbar ftco-navbar-light" id="ftco-navbar">
    <div class="container">
        <a class="navbar-brand" href="/">EunGok</a>
        <div class="social-media order-lg-last">
            <p class="mb-0 d-flex">
                <a href="#" class="d-flex align-items-center justify-content-center"><span class="fa fa-facebook"><i class="sr-only">Facebook</i></span></a>
                <a href="#" class="d-flex align-items-center justify-content-center"><span class="fa fa-twitter"><i class="sr-only">Twitter</i></span></a>
                <a href="#" class="d-flex align-items-center justify-content-center"><span class="fa fa-instagram"><i class="sr-only">Instagram</i></span></a>
                <a href="#" class="d-flex align-items-center justify-content-center"><span class="fa fa-dribbble"><i class="sr-only">Dribbble</i></span></a>
            </p>
    </div>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#ftco-nav" aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="fa fa-bars"></span> Menu
      </button>
      <div class="collapse navbar-collapse" id="ftco-nav">
        <ul class="navbar-nav ml-auto mr-md-3">
            <li class="nav-item active"><a href="/" class="nav-link">Home</a></li>
            <li class="nav-item"><a href="/list" class="nav-link">Articles</a></li>
            <li class="nav-item"><a href="/login" class="nav-link">Login</a></li>
            <li class="nav-item"><a href="/register" class="nav-link">register</a></li>
        </ul>
      </div>
    </div>
  </nav>
```

index.html의 코드를 수정한다.

```html
{% extends "layouts.html" %}
{% block nav %}
{% include 'nav.html' %}
{% endblock %}
{% block body %}
<div class="container" style="margin-top: 3rem;">
    <h1>Hello World!!</h1>
    {% if session['is_loged_in'] %}
    <h3> {{ session['username'] }} 님 환영합니다. </h3>
    <a href="/logout"><button class="btn bg-danger">로그아웃</button></a>
    {% else %}
    <h3>게스트로 접속하셨습니다.</h3>
    <a href="/register"><button class="btn bg-warning">회원가입</button></a>
    <a href="/login"><button class="btn bg-primary">로그인</button></a>
</div>

{% endif %}
{% endblock %}
```

login.html

```html
{% extends "layouts.html" %}
{% block nav %}
{% include 'nav.html' %}
{% endblock %}
{% block body %}
<div class="container">
	<section class="vh-100" style="background-color: #9A616D;">
		<div class="container py-5 h-100">
		  <div class="row d-flex justify-content-center align-items-center h-100">
			<div class="col col-xl-10">
			  <div class="card" style="border-radius: 1rem;">
				<div class="row g-0">
				  <div class="col-md-6 col-lg-5 d-none d-md-block">
					<img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/img1.webp"
					  alt="login form" class="img-fluid" style="border-radius: 1rem 0 0 1rem;" />
				  </div>
				  <div class="col-md-6 col-lg-7 d-flex align-items-center">
					<div class="card-body p-4 p-lg-5 text-black">
	  
					  <form action="/login" method="POST">
	  
						<div class="d-flex align-items-center mb-3 pb-1">
						  <i class="fas fa-cubes fa-2x me-3" style="color: #ff6219;"></i>
						  <span class="h1 fw-bold mb-0">Logo</span>
						</div>
	  
						<h5 class="fw-normal mb-3 pb-3" style="letter-spacing: 1px;">Sign into your account</h5>
						
						<div class="form-outline mb-4">
						  <input type="email" name="email" id="form2Example17" class="form-control form-control-lg" />
						  <label class="form-label" for="form2Example17">Email address</label>
						</div>
	  
						<div class="form-outline mb-4">
						  <input type="password"  name="password" id="form2Example27" class="form-control form-control-lg" />
						  <label class="form-label" for="form2Example27">Password</label>
						</div>
	  
						<div class="pt-1 mb-4">
						  <button class="btn btn-dark btn-lg btn-block" type="submit">Login</button>
						</div>
	  
						<a class="small text-muted" href="#!">Forgot password?</a>
						<p class="mb-5 pb-lg-2" style="color: #393f81;">Don't have an account? <a href="/register"
							style="color: #393f81;">Register here</a></p>
						<a href="#!" class="small text-muted">Terms of use.</a>
						<a href="#!" class="small text-muted">Privacy policy</a>
					  </form>
	  
					</div>
				  </div>
				</div>
			  </div>
			</div>
		  </div>
		</div>
	  </section>
</div>

{% endblock %}
```

register.html 

```html
{% extends "layouts.html" %}
{% block nav %}
{% include 'nav.html' %}
{% endblock %}
{% block body %}
<div class="container">
	<section class="vh-100" style="background-color: #9A616D;">
		<div class="container py-5 h-100">
		  <div class="row d-flex justify-content-center align-items-center h-100">
			<div class="col col-xl-10">
			  <div class="card" style="border-radius: 1rem;">
				<div class="row g-0">
				  <div class="col-md-6 col-lg-5 d-none d-md-block">
					<img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-registration/img4.webp"
					  alt="login form" class="img-fluid" style="border-radius: 1rem 0 0 1rem;" />
				  </div>
				  <div class="col-md-6 col-lg-7 d-flex align-items-center">
					<div class="card-body p-4 p-lg-5 text-black">
	  
					  <form action="/register" method="POST">
	  
						<div class="d-flex align-items-center mb-3 pb-1">
						  <i class="fas fa-cubes fa-2x me-3" style="color: #ff6219;"></i>
						  <span class="h1 fw-bold mb-0">Logo</span>
						</div>
	  
						<h5 class="fw-normal mb-3 pb-3" style="letter-spacing: 1px;">Sign Up your account</h5>

						<div class="form-outline mb-6">
							<input type="text" name="username" id="form2Example17" class="form-control form-control-lg" />
							<label class="form-label" for="form2Example17">User Name</label>
						</div>

						<div class="form-outline mb-6">
						  <input type="email" name="email" id="form2Example17" class="form-control form-control-lg" />
						  <label class="form-label" for="form2Example17">Email address</label>
						</div>

						<div class="form-outline mb-6">
							<input type="text" name="phone" id="cellPhone" class="form-control form-control-lg" maxlength="13" />
							<label class="form-label" for="cellPhone" >Phone Number</label>
						</div>

						<div class="form-outline mb-6">
						  <input type="password"  name="password" id="form2Example27" class="form-control form-control-lg" />
						  <label class="form-label" for="form2Example27">Password</label>
						</div>
	  
						<div class="pt-1 mb-4">
						  <button class="btn btn-primary btn-lg btn-block" type="submit">Register</button>
						</div>
						
						<a href="#!" class="small text-muted">Terms of use.</a>
						<a href="#!" class="small text-muted">Privacy policy</a>
					  </form>
	  
					</div>
				  </div>
				</div>
			  </div>
			</div>
		  </div>
		</div>
	  </section>
</div>
<script>
	function autoHypenPhone(str){
            str = str.replace(/[^0-9]/g, '');
            var tmp = '';
            if( str.length < 4){
                return str;
            }else if(str.length < 7){
                tmp += str.substr(0, 3);
                tmp += '-';
                tmp += str.substr(3);
                return tmp;
            }else if(str.length < 11){
                tmp += str.substr(0, 3);
                tmp += '-';
                tmp += str.substr(3, 3);
                tmp += '-';
                tmp += str.substr(6);
                return tmp;
            }else{              
                tmp += str.substr(0, 3);
                tmp += '-';
                tmp += str.substr(3, 4);
                tmp += '-';
                tmp += str.substr(7);
                return tmp;
            }
            return str;
        }

var cellPhone = document.getElementById('cellPhone');
cellPhone.onkeyup = function(event){
        event = event || window.event;
        var _val = this.value.trim();
        this.value = autoHypenPhone(_val) ;
}
</script>

{% endblock %}
```

navigation bar에 로그인했을때와 로그아웃 했을때의 UI를 다르게 보여주기 위해서 nav.html을 다음과 같이 수정한다.

```html
<nav class="navbar navbar-expand-lg ftco_navbar ftco-navbar-light" id="ftco-navbar">
    <div class="container">
        <a class="navbar-brand" href="/">EunGok</a>
        <div class="social-media order-lg-last">
            <p class="mb-0 d-flex">
                <a href="#" class="d-flex align-items-center justify-content-center"><span class="fa fa-facebook"><i class="sr-only">Facebook</i></span></a>
                <a href="#" class="d-flex align-items-center justify-content-center"><span class="fa fa-twitter"><i class="sr-only">Twitter</i></span></a>
                <a href="#" class="d-flex align-items-center justify-content-center"><span class="fa fa-instagram"><i class="sr-only">Instagram</i></span></a>
                <a href="#" class="d-flex align-items-center justify-content-center"><span class="fa fa-dribbble"><i class="sr-only">Dribbble</i></span></a>
            </p>
    </div>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#ftco-nav" aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="fa fa-bars"></span> Menu
      </button>
      <div class="collapse navbar-collapse" id="ftco-nav">
        <ul class="navbar-nav ml-auto mr-md-3">
            <li class="nav-item active"><a href="/" class="nav-link">Home</a></li>
            <li class="nav-item"><a href="/list" class="nav-link">Articles</a></li>
            {% if session['is_loged_in'] %}
                <li class="nav-item"><a href="/logout" class="nav-link">logout</a></li>
                {% else %}
                <li class="nav-item"><a href="/login" class="nav-link">Login</a></li>
                <li class="nav-item"><a href="/register" class="nav-link">register</a></li>
            {% endif %}
            
        </ul>
      </div>
    </div>
  </nav>
```

index.html로 수정을 통하여 UI를 고쳐 보기 위해서 다음과 같이 수정한다.

```html
{% extends "layouts.html" %}
{% block nav %}
{% include 'nav.html' %}
{% endblock %}
{% block body %}

<main>
    <div class="position-relative overflow-hidden p-3 p-md-5 m-md-3 text-center bg-light">
      <div class="col-md-5 p-lg-5 mx-auto my-5">
        <h1 class="display-4 fw-normal">
            {% if session['is_loged_in'] %}
                Welcome {{ session['username'] }} !
                {% else %}
                You Are Guest!
            {% endif %}
        </h1>
        <p class="lead fw-normal">And an even wittier subheading to boot. Jumpstart your marketing efforts with this example based on Apple’s marketing pages.</p>
        <a class="btn btn-outline-secondary" href="#">Coming soon</a>
      </div>
      <div class="product-device shadow-sm d-none d-md-block"></div>
      <div class="product-device product-device-2 shadow-sm d-none d-md-block"></div>
    </div>
  
  </main>
{% endblock %}
```

list.html 커스터마이징

```jsx
{% extends "layouts.html" %}
{% block nav %}
{% include 'nav.html' %}
{% endblock %}
{% block body %}
<div class="container" style="margin-top: 3rem;">
<!-- Begin Page Content -->
<div class="container-fluid">

    <!-- Page Heading -->
    <h1 class="h3 mb-2 text-gray-800">Data Info</h1>
    <p class="mb-4">Are U Hungry? <a target="_blank"
            href="https://datatables.net">This data is important</a>.</p>

    <!-- DataTales Example -->
    <div class="card shadow mb-4">
        <div class="card-header py-3">
            <h6 class="m-0 font-weight-bold text-primary">게시판</h6>
        </div>
        <div class="card-body">
            <div class="table-responsive">
                <table class="table table-bordered" id="dataTable" width="100%" cellspacing="0">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>TITLE</th>
                            <th>DESCRIPTION</th>
                            <th>Author</th>
                            <th>Date</th>
                            <th>Edit</th>
                            <th>Delete</th>
                        </tr>
                    </thead>
                    <tfoot>
                        <tr>
                            <th>ID</th>
                            <th>TITLE</th>
                            <th>DESCRIPTION</th>
                            <th>Author</th>
                            <th>Date</th>
                            <th>Edit</th>
                            <th>Delete</th>
                        </tr>
                    </tfoot>
                    <tbody>
                        {% for x in data %}
                        <tr>
                            <td>{{ x['id'] }}</td>
                            <td>{{ x['title'] }}</td>
                            <td>{{ x['desc'] }}</td>
                            <td>{{ x['author'] }}</td>
                            <td>{{ x['create_at'] }}</td>
                            <td><a href="/edit/{{ x['id'] }}"><button class="btn bg-primary">편집</button></a></td>
                            <td><a href="/delete/{{ x['id'] }}"><button class="btn bg-danger"
                                        onclick="return confirm_func()">삭제</button></a></td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
    </div>

</div>
<!-- /.container-fluid -->
    <script>
        function confirm_func() {
            result = confirm('정말 삭제 하시겠습니까?')
            console.log(result)
            return result
        }
    </script>

</div>

{% endblock %}
```

mysql의 os 스키마에 list 테이블을 생성하기 위하여 다음과 같은 sql문 실행한다.

```sql
CREATE TABLE `os`.`list` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(100) NULL,
  `desc` LONGTEXT NULL,
  `author` VARCHAR(45) NULL,
  `create_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;
```

[http://localhost:5000/list](http://localhost:5000/list) 

POST 방식으로 title , desc , author 의 키값을 가지는 form 형식으로 전송시

mysql os의 list테이블에 저장이 될 수 있도록 [mysql.py](http://mysql.py) 파일에 Mysql class 다음과 같은 코드를 추가한다.

```python
...
def insert_list(self , title , desc , author):
        db = pymysql.connect(host=self.host, user=self.user, db=self.db, password=self.password, charset=self.charset)
        curs = db.cursor()
        
        sql = '''insert into `list` (`title` , `desc` , `author`) values(%s,%s,%s)'''
        result = curs.execute(sql,[title , desc , author])
        print(result)
        db.commit()
        db.close()

        return result

....
```

app.py파일에 다음과 같은 코드를 추가한다.

```python
@app.route('/list', methods=['GET' , 'POST'])
def list():
    if request.method == "GET":
        # data = Articles()
        result = mysql.get_data()
        # print(result)
        return render_template('list.html' , data=result)
    
    elif request.method =="POST":
        title = request.form['title']
        desc = request.form['desc']
        author = request.form['author']
        result = mysql.insert_list(title , desc , author)
        print(result)
        return redirect('/list')
```

게시판 작성 기능을 구현하기 위해서 

dashboard.html 파일을 생성후 다음과 같이 코드를 생성한다.

```html
{% extends "layouts.html" %}
{% block nav %}
{% include 'nav.html' %}
{% endblock %}
{% block body %}
<div class="container" style="margin-top: 3rem;">
    <div class="alert alert-success" role="alert">
        <h4 class="alert-heading">게시판 작성페이지</h4>
        <p>Aww yeah, you successfully read this important alert message. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.</p>
        <hr>
        <p class="mb-0">Whenever you need to, be sure to use margin utilities to keep things nice and tidy.</p>
      </div>
<form action="/list", method="POST">
    
    <!-- Text input -->
    <div class="form-outline mb-4">
      <input type="text" name="title" id="form6Example3" class="form-control" />
      <label class="form-label" for="form6Example3">TITLE</label>
    </div>
  
    <!-- Message input -->
    <div class="form-outline mb-4">
      <textarea class="form-control" name="desc" id="form6Example7" rows="4"></textarea>
      <label class="form-label" for="form6Example7">Additional information</label>
    </div>

    <!-- Text input -->
    <div class="form-outline mb-4">
        <input type="text" name="author" id="form6Example4" class="form-control" />
        <label class="form-label" for="form6Example4">Athor</label>
    </div>

    <!-- Submit button -->
    <button type="submit" class="btn btn-primary btn-block mb-4">Submit</button>
  </form>
</div>
{% endblock %}
```

[http://localhost:5000/create_list](http://localhost:5000/create_list) 

GET 방식으로 요청시 dashboard.html 랜더링 되도록

[app.py](http://app.py) 다음과 코드를 추가한다.

```python
@app.route('/create_list', methods=['GET', 'POST'])
def create_list():
    if request.method == "GET":
        return render_template('dashboard.html')
```

list.html 에 게시판 작성 버튼을 추가한다.

다음과 같은 부분을 수정한다.

```html
<div class="card-header py-3">
            <h6 class="m-0 font-weight-bold text-primary">게시판 <a  style="text-align:right;" href="/create_list" type="button" class="btn btn-success">게시글 작성</a></h6>
        </div>
```

![image](https://github.com/kbigdata005/web_server/assets/139095086/9abfa784-7b55-4d9b-9a1d-7e7492818548)
위에서 편집 버튼을 클릭시 해당 게시글에 대한 정보를 편집할 수 있는 기능을 구현한다.

[app.py](http://app.py) 파일에서 @app.route(’/edit/<ids>’) 부분을 다음과 같이 코드를 수정한다.

```python
@app.route('/edit/<ids>' , methods=['GET', "POST"])
def edit(ids):
    db = pymysql.connect(host=mysql.host, user=mysql.user, db=mysql.db, password=mysql.password, charset=mysql.charset)
    curs = db.cursor()

    sql = f'SELECT * FROM list WHERE `id` = %s;'
    curs.execute(sql , ids )
    
    rows = curs.fetchall()
    print(rows)
    db.close()
    return render_template('list_edit.html' , data=rows)
```

list_edit.html 파일 생성후 다음과 같이 코드를 생성한다.

```html
{% extends "layouts.html" %}
{% block nav %}
{% include 'nav.html' %}
{% endblock %}
{% block body %}
<div class="container" style="margin-top: 3rem;">
    <div class="alert alert-danger" role="alert">
        <h4 class="alert-heading">게시판 편집페이지</h4>
        <p>Aww yeah, you successfully read this important alert message. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.</p>
        <hr>
        <p class="mb-0">Whenever you need to, be sure to use margin utilities to keep things nice and tidy.</p>
      </div>
<form  action="/edit/{{ data[0][0]}}", method="POST">
    
    <!-- Text input -->
    <div class="form-outline mb-4">
      <input type="text" name="title" id="form6Example3" class="form-control"  value="{{ data[0][1] }}" />
      <label class="form-label" for="form6Example3">TITLE</label>
    </div>
  
    <!-- Message input -->
    <div class="form-outline mb-4">
      <textarea class="form-control" name="desc" id="form6Example7" rows="4" >{{ data[0][2] }}</textarea>
      <label class="form-label" for="form6Example7">Additional information</label>
    </div>

    <!-- Text input -->
    <div class="form-outline mb-4">
        <input type="text" name="author" id="form6Example4" class="form-control"  value="{{ data[0][3] }}"/>
        <label class="form-label" for="form6Example4">Athor</label>
    </div>

    <!-- Submit button -->
    <button type="submit" class="btn btn-primary btn-block mb-4">Submit</button>
  </form>
</div>
{% endblock %}
```

[http://localhost:5000/edit/<ids>](http://localhost:5000/edit/<ids>) 

POST 방식으로 편집한 데이터를 전송하면 mysql에 테이블이 편집되도록

[mysql.py](http://mysql.py) 의 Mysql 클래스에 update_list 메소드를 생성하여 준다.

```python
def update_list(self , id, title , desc , author):
        db = pymysql.connect(host=self.host, user=self.user, db=self.db, password=self.password, charset=self.charset)
        curs = db.cursor()
        
        sql = f'UPDATE `list` SET `title`=%s , `desc`=%s , `author`=%s  WHERE `id` = %s;'
        result = curs.execute(sql,[title , desc , author ,id])
        print(result)
        db.commit()
        db.close()

        return result
```

[app.py](http://app.py) 파일에서 @app.route(’/edit/<ids>’) 부분을 다음과 같이 코드를 수정한다. 

```python
@app.route('/edit/<ids>' , methods=['GET', "POST"])
def edit(ids):
    if request.method == 'GET':
        db = pymysql.connect(host=mysql.host, user=mysql.user, db=mysql.db, password=mysql.password, charset=mysql.charset)
        curs = db.cursor()

        sql = f'SELECT * FROM list WHERE `id` = %s;'
        curs.execute(sql , ids )
        
        rows = curs.fetchall()
        print(rows[0][2])
        db.close()
        return render_template('list_edit.html' , data=rows)
    
    elif request.method == 'POST':

        title = request.form['title']
        desc = request.form['desc']
        author = request.form['author']
        print(type(desc))
        result = mysql.update_list(ids, title, desc , author)
        print(result)
        return redirect('/list')
```

게시판 삭제 기능을 구현하기 위해 

[mysql.py](http://mysql.py) 의 Mysql 클래스 delete_list 메소드를 구현다.

```python
def delete_list(self , id):
        db = pymysql.connect(host=self.host, user=self.user, db=self.db, password=self.password, charset=self.charset)
        curs = db.cursor()
        sql = f'DELETE  FROM `list` WHERE `id` = %s;'
        result = curs.execute(sql,[id])
        print(result)
        db.commit()
        db.close()

        return result
```

app.py의 @app.route(’/delete/<ids>) 부분을 

다음과 같이 수정한다.

```python
@app.route('/delete/<ids>')
def delete(ids):
    result = mysql.delete_list(ids)
    print(result)
    return redirect('/list')
```