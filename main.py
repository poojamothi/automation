from flask import Flask,request,render_template,send_file
import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
from urllib.parse import  unquote
import zipfile
import shutil
from datetime import datetime

import os
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def ftn():
    if request.method =='POST':
       if 'jdate' in request.form:
          jdate=request.form['jdate']
          #date_obj=datetime.strptime(jdate,'%d-%m-%y')



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

       all_urls = r.find_all('a')

         #path="D:/pdf"

         #try:
           #os.mkdir(path)
           #print("folder created")
            # except FileExistsError:
             #print("file already exists")
       pdf_urls=[]
       path = "D:/pdf"

       try:
           os.mkdir(path)
           print("folder created")
       except FileExistsError:
           print("file already exists")

       for url in all_urls:
           #try:
            if 'pdf' in url['href'] and jdate in url['href']:
               p_url=str(url['href'])
               pdf_urls.append(p_url)
               print('HTTP GET: %s', p_url)
               pdf_response = requests.get(p_url)
               filename = unquote(pdf_response.url).split('/')[-1].replace(' ', '_')


               with open("D:/pdf/"+ filename, 'wb') as pdf:
                   pdf.write(pdf_response.content)


       return render_template('home.html', content=pdf_urls)
    else:
       return render_template('home.html')






@app.route('/download/',methods=['POST'])
def downloadFile():
    zipf = zipfile.ZipFile('judpdf.zip', 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(r"D:/pdf"):
        for file in files:
            if file.endswith('.pdf'):
                print(file)
                zipf.write("D:/pdf/"+ file)
    zipf.close()
    try:
        shutil.rmtree("D:/pdf/")
        print("folder is deleted")
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
    return send_file('judpdf.zip', mimetype='zip',attachment_filename='judpdf.zip',as_attachment=True)


           #except:
               #pass









if __name__=='__main__':
    app.run(debug=True)
