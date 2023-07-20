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

![image](https://github.com/kbigdata005/web_server/assets/139095086/31561cd1-9e9b-415a-a193-b80c3c80b95d)


위와 같은 구조로 웹서버를 만든다.

![image](https://github.com/kbigdata005/web_server/assets/139095086/dd26b6fe-5f88-4a07-bc42-87c638eca178)
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