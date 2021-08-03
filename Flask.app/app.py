
from flask import Flask,render_template,request
import pickle
#intialise the app
app =Flask(__name__)

#load the model
model=pickle.load(open('dib_79.pkl','rb'))

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/contacts')
def contact():
    return 'Contact Page'

@app.route('/submit',methods=['POST'])
def form_data():
    # fname = request.form.get('fname')
    # sname=request.form.get('sname')
    # phone_number = request.form.get('phone')
    # mail= request.form.get('email')
    # print(fname,sname,phone_number,mail)
    
    # fname = request.form.get('fname')
    # sname=request.form.get('sname')
    # phone_number = request.form.get('phone')
    # mail= request.form.get('email')
    preg = request.form.get('preg')
    plas=request.form.get('plas')
    pres = request.form.get('pres')
    skin= request.form.get('skin')
    test = request.form.get('test')
    mass=request.form.get('mass')
    pedi = request.form.get('pedi')
    age= request.form.get('age')

    output=model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])
    print(output)
    if output[0]==1:
        out='diabetic'
    else:
        out="Not Diabetic"
    return render_template('form.html' , data = f'person is {out}')

    
if __name__=='__main__':
    app.run(debug=True)

