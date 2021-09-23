from flask import Flask,request,render_template
import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def ftn():
    if request.method=='POST':
       if 'jdate' in request.form:
          jdate=request.form['jdate']



       def extraction(date):
         url = "http://164.100.69.66/jsearch/juddt1page.php?dc=31&fflag=1"

         headers = CaseInsensitiveDict()
         headers["Content-Type"] = "application/x-www-form-urlencoded"

         data = "jddate=date&Submit=Submit"
         return requests.post(url, headers=headers, data=data)

       r= extraction(jdate)

       content = BeautifulSoup(r.text, 'lxml')
       all_urls = content.find_all('a')
       for url in all_urls:
           try:
               if 'pdf' in url['href']:
                   print(url['href'])
           except:
               pass




    else:
        return render_template('home.html')

if __name__=='__main__':
    app.run(debug=True)
