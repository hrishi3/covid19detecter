
import flask
import pickle
import pandas as pd

# Use pickle to load in the pre-trained model
with open(f'model/covid19detector.pkl', 'rb') as f:
    model = pickle.load(f)

# Initialise the Flask app
app = flask.Flask(__name__, template_folder='templates')
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
        age = flask.request.form['age']
        gender = flask.request.form['gender']
        temperature = flask.request.form['temperature']
        cough = flask.request.form['cough']
        throat = flask.request.form['throat']
        weak = flask.request.form['weak']
        breath = flask.request.form['breath']
        drow = flask.request.form['drow']
        pain = flask.request.form['pain']
        red = flask.request.form['red']
       # input_variables = pd.DataFrame([[age,gender,temperature, cough,throat, weak,breath,drow,pain,red]])
        pred = model.predict([[int(age),int(gender),int(temperature), int(cough),int(throat),int( weak),int(breath),int(drow),int(pain),int(red)]])[0]
        if int(pred)==0:
          prediction='Low Risk'
        elif int(pred)==1:
          prediction='moderate Risk'
        else:
          prediction='high Risk'

       return flask.render_template('main.html',
                                     result='YESSS',
                                    )
    
    if __name__ == '__main__':
        app.run()
