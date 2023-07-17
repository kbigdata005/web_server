from flask import Flask , render_template ,request

app = Flask(__name__)

@app.route('/' , methods=['GET','POST'])
def index():
    if request.method == "GET":
        os_info = dict(request.headers)
        print(os_info) 
        return render_template('index.html',header=os_info )
    
    elif request.method == "POST":
        return render_template('index.html',header= "안녕하세요 김태경입니다.!!!")


if __name__ == '__main__':
    app.run(debug=True)