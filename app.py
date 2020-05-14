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
        
        gender = flask.request.form.get('gender')
        
        temprature = flask.request.form['temprature']
        cough = flask.request.form.get('cough')
        throat = flask.request.form.get('throat')
        weak = flask.request.form.get('weak')
        breath = flask.request.form.get('breath')
        drow = flask.request.form.get('drow')
        pain = flask.request.form.get('pain')
        red = flask.request.form.get('red')
        
        input_variables = pd.DataFrame([[age,gender,temprature, cough,throat, weak,breath,drow,pain,red]])
        '''
        pred = model.predict(input_variables)[0]
        
        if int(pred)==0:
          prediction='Low Risk'
        elif int(pred)==1:
          prediction='moderate Risk'
        else:
          prediction='high Risk'
          '''
          
          
        return flask.render_template('main.html',result=red)
    
    if __name__ == '__main__':
        app.debug=True
        app.run()
