import numpy as np
from flask import Flask,request,render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('fraud.pkl','rb'))

@app.route('/')
def home():
    return render_template('fra-ud.html')
@app.route('/detect',methods=["GET","POST"])
def detect():
    data1 = request.form['Step']
    data2 = request.form['Type']
    data3 = float(request.form['Amount'])
    data4 = float(request.form['Oldbalorg'])
    data5 = float(request.form['newbalorg'])
    data6 = float(request.form['oldbaldes'])
    data7 = float(request.form['newbaldes'])
    
    if data2 == 'Cash Out':
        data2 = 4
    if data2 == 'Payment':
        data2 = 3
    if data2 == 'Cash In':
        data2 = 2
    if data2 == 'Transfer':
        data2 = 1
    if data2 == 'Debit':
        data2 = 0
    
    arr = np.array([[data1,data2,data3,data4,data5,data6,data7]])
    prediction = model.predict(arr)
    if prediction == 1:
        text = 'ThIS IS A FRAUDLENT TRANSACTION!!'
    else:
        text = 'THIS IS NOT A FRAUDLENT TRANSACTION'
        
    return render_template('fra-ud.html',pred_text = text)

if __name__=='__main__':
    app.run(debug=True)