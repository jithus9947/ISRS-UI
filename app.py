from flask import Flask, request, render_template
import requests
# import json
from bs4 import BeautifulSoup


app = Flask(__name__)


@app.route('/')

@app.route('/',methods=["GET","POST"])
def predict():
    if request.method == "POST":
        keyword = request.form.get("keyword")
        # url='https://www.google.com/search?q='+ keyword
        # response = requests.get(url, timeout=5)
        url='https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword='+keyword
        res = requests.get(url)
        # url='https://www.virustotal.com/gui/search/'+keyword
        # response = requests.get(url)
        print(res.status_code)
        html = res.text
        soup = BeautifulSoup(html, "html.parser")
        div = soup.find('div', {'id':'TableWithRules'})
        td = div.findAll('td')
        print(td[0].a.string)

        
    return render_template('home.html')
if __name__=='__main__':
   app.run()
