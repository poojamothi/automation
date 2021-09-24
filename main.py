from flask import Flask,request,render_template
import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
import re
from urllib.parse import  unquote
from datetime import datetime

import os
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def ftn():
    if request.method =='POST':
       if 'jdate' in request.form:
          jdate=request.form['jdate']



       def extraction(date):
         url = "http://164.100.69.66/jsearch/juddt1page.php?dc=31&fflag=1"

         headers = CaseInsensitiveDict()
         headers["Content-Type"] = "application/x-www-form-urlencoded"

         # data = "juddt=date&Submit=Submit"
         data = dict()
         data["juddt"] = date
         data["Submit"] = "Submit"
         response= requests.post(url, headers=headers, data=data)
         content = BeautifulSoup(response.text, 'lxml')

         return content

       r = extraction(jdate)
       pdf_urls=[]
       all_urls = r.find_all('a')
       if 'download' in request.form:
         path="D:/pdf"

         try:
             os.mkdir(path)
             print("folder created")
         except FileExistsError:
             print("file already exists")
         for url in all_urls:
           try:
               if 'pdf' in url['href']:
                   pdf_url=''
                   pdf_url=url['href']
                   print('HTTP GET: %s',pdf_url)
                   pdf_response=requests.get(pdf_url)
                   filename=unquote(pdf_response.url).split('/')[-1].replace(' ','_')
                   with open('./pdf/'+filename,'wb') as f:
                       f.write(pdf_response.content)

               pdf_urls= pdf_urls.append(pdf_url)


           except:
               pass




       return render_template('home.html',content=pdf_urls)



    else:
        return render_template('home.html')

if __name__=='__main__':
    app.run(debug=True)
