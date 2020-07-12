import numpy as np
from flask import Flask, request, render_template
import pickle
from forms import MyForm
import numpy as np
app = Flask(__name__) #Initialize the flask App

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

model = pickle.load(open('model3.pkl', 'rb'))

@app.route('/')
def home():
    form = MyForm()
    return render_template('submit.html', title='predict', form=form)

    return render_template('layout.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    form=MyForm()

    features=request.form.values()


    final_features=[]
    for val in features:

        final_features.append(val)
    final_features.remove(final_features[-1])
    final_features.remove(final_features[0])
    final_list=[]
    for num in final_features:
        final_list.append(int(num))
    final=[final_list]
    final_arr=np.asarray(final)
    final_arr.reshape(-1, 1)
    prediction = model.predict(final_arr)

    output = prediction
    if(output==0):
        predicted_value="Rejected"
    elif(output==1):
        predicted_value = "Accepted"

    #output=features
    return render_template('about.html', prediction_text=f"Your Loan Application is likely to be : {predicted_value}")



if __name__ == "__main__":
    app.run(debug=True)