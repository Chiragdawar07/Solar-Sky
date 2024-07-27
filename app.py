from flask import Flask, render_template, request
import pickle
import numpy as np
import os  
model = pickle.load(open('iri.pkl','rb'))
app = Flask(__name__)

picfolder=os.path.join('static','img')
app.config['UPLOAD_FOLDER']=picfolder

@app.route('/')
def home():
    pic1=os.path.join(app.config['UPLOAD_FOLDER'],'gallery-6.jpg')
    pic2=os.path.join(app.config['UPLOAD_FOLDER'],'gallery-2.jpg')
    pic3=os.path.join(app.config['UPLOAD_FOLDER'],'gallery-1.jpg')
    pic4=os.path.join(app.config['UPLOAD_FOLDER'],'carousel-1.jpg')
    return render_template('index.html', user_image=pic1, user_image1=pic2, user_image2=pic3, user_image3=pic4)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data1 = float(request.form['a'])
        data2 = float(request.form['b'])
        data3 = float(request.form['c'])
        data4 = float(request.form['d'])
        data5 = float(request.form['e'])
        data6 = float(request.form['f'])
        data7 = float(request.form['g'])
        data8 = float(request.form['h'])

        arr = np.array([[data1, data2, data3, data4, data5, data6]])
        pred = model.predict(arr)
        if pred[0] != 0:
            Ideal_efficiency = (pred[0] / data7) * 100
        else:
            Ideal_efficiency = 0 

        Ideal_efficiency = round(Ideal_efficiency,0)

        efficiency=Ideal_efficiency - data8*0.5

        
        


        
        return render_template('after.html', data=pred, max=data7, Ideal_Efficiency=Ideal_efficiency, Present_Efficiency=efficiency)

    except Exception as e:
        return render_template('error.html', error_message=str(e))


if __name__ == "__main__":
    app.run(debug=True)
    