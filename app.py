from flask import Flask, request, render_template
import requests
# import json
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

@app.route('/')

@app.route('/',methods=["GET","POST"])
def predict():
    if request.method == "POST":
        keyword = request.form.get("keyword")
        # url='https://www.google.com/search?q='+ keyword
        # response = requests.get(url, timeout=5)
        # url='https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword='+keyword
        # response = requests.get(url)
        url='https://www.virustotal.com/gui/search/'+keyword
        response = requests.get(url)
        content = BeautifulSoup(response.content, "html.parser")
        for link in content.find_all('a', attrs={'class':'link secondary','href': re.compile("^https://")}):
            print(link.get('href'))
        # print(data)
        # datajson= r.json()
        # data = {clear


        #     'CVEID' : datajson [''],
        #     'DESC' : datajson [''],
        # }
    return render_template('home.html')
if __name__=='__main__':
   app.run()
