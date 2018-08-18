import app
from flask import Flask, render_template, request, flash, make_response, redirect, url_for
import requests
import json

app = Flask(__name__)
WTF_CSRF_ENABLED = True

@app.route('/')
def home():
    return render_template('final_plot.html')

@app.route('/animal',methods=['POST'])
def animals():
    name = request.form['species']
    url = 'https://api.myjson.com/bins/ylvyc' #test link

    r = requests.get(url)
    if r.status_code == 200:
        resp = r.json()
        data = resp['features']
        
        x = len(data)
        y = 0
        for i in range(0,x):
            if name == data[i]['name']:
                y = i
                break
        
        title = data[y]['name']
        facts = data[y]['facts']
        iframe = data[y]['iframe']
        status = data[y]['status']
        scientific_name = data[y]['scientific name']
        habitat = data[y]['habitat']
        places = data[y]['places']
        matter = data[y]['matter']
        print(name,status,places)
        return render_template('index.html',title=title,facts=facts,iframe=iframe,status=status,scientific_name=scientific_name,habitat=habitat,places=places,matter=matter)
    else:
        print("Error..")
        return render_template('final_plot.html')

    

if __name__ == "__main__":
    app.run(debug=True)