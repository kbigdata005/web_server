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