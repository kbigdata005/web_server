from flask import Flask , render_template ,request
from data import Articles
# print(Articles())

app = Flask(__name__)

@app.route('/' , methods=['GET','POST'])
def index():
    # if request.method == "GET":
    #     os_info = dict(request.headers)
    #     print(os_info) 
    #     name = request.args.get("name")
    #     print(name)
    #     hello = request.args.get("hello")
    #     print(hello)
    #     return render_template('index.html',header=f'{name}님 {hello}!!' )
    
    # elif request.method == "POST":
    #     data  = request.form.get("name")
    #     data_2 = request.form['hello']
    #     print(data_2)
        # return render_template('index.html',header= "안녕하세요 김태경입니다.!!!")

    return render_template('index.html')

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method =="GET":
        return render_template('hello.html')
    
    elif request.method =="POST":
        name = request.form['name']
        hello = request.form['hello']
        return render_template('index.html', name=name , hello = hello)

@app.route('/list', methods=['GET' , 'POST'])
def list():
    data = Articles()
    return render_template('list.html' , data=data)


if __name__ == '__main__':
    app.run(debug=True)