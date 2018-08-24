import app
from flask import Flask, render_template, request, flash, make_response, redirect, url_for
import requests
#import json

app = Flask(__name__)
WTF_CSRF_ENABLED = True

@app.route('/')
def home():
    y = 0
    title = ""
    return render_template('home.html')

@app.route('/animal',methods=['POST'])
def animals():
    name = request.form['species']
    url = 'https://api.jsonbin.io/b/5b794f7a6376d24455a89004/7'
    headers = {
        'secret-key': '$2a$10$dKH7Mf31dIBNqbaH4Pcw4ucLNGMgr5ggMdBTBczssMZBsvNUyQePS'
    }

    r = requests.get(url, headers=headers)
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
        pic_1 = data[y]['pic_1']
        pic_2 = data[y]['pic_2']
        pic_3 = data[y]['pic_3']
        
        return render_template('index.html',title=title,facts=facts,iframe=iframe,status=status,scientific_name=scientific_name,habitat=habitat,places=places,matter=matter,pic_1=pic_1,pic_2=pic_2,pic_3=pic_3)
    else:
        #print("Error..")
        return render_template('home.html')

 

if __name__ == "__main__":
    app.run(debug=True)