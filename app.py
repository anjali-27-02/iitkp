
from flask import Flask,render_template,request

from icrawler.builtin import GoogleImageCrawler
import os
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def getvalue():
    value=request.form['q']
    google_crawler = GoogleImageCrawler(storage={'root_dir': 'static/images/'+value})
    google_crawler.crawl(keyword=value, max_num=20)
    image_files = os.listdir('static/images/'+value)
    return render_template('pass.html',image_files=image_files,value=value)


if __name__=='__main__':
    app.run(debug=True)