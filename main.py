from flask import Flask,request,render_template,send_file
import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
from urllib.parse import  unquote
import zipfile
import shutil
import pathlib
from pathlib import Path

import datetime




app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def ftn():
    if request.method =='POST':
       if 'fdate' in request.form:
          fdate=request.form['fdate']
       if 'todate' in request.form:
              todate = request.form['todate']
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

       pdf_urls = []



       start = datetime.datetime.strptime(fdate, "%d-%m-%Y")
       end = datetime.datetime.strptime(todate, "%d-%m-%Y")
       date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days)]

       for single_date in date_generated:
           d=single_date.strftime("%d-%m-%Y")
           print(d)
           r = extraction(d)
           all_urls = r.find_all('a')






       path = "D:/pdf"

       try:
           pathlib.Path(path).mkdir(parents=True, exist_ok=True)

           print("folder created")
       except FileExistsError:
           print("file already exists")



       for url in all_urls:

            if 'pdf' in url['href']:
               p_url = str(url['href'])
               print('HTTP GET: %s', p_url)
               pdf_urls.append(p_url)

               pdf_response = requests.get(p_url)
               filename = unquote(pdf_response.url).split('/')[-1].replace(' ', '_')


               with open("D:/pdf/"+ filename, 'wb') as pdf:
                    pdf.write(pdf_response.content)


       return render_template('home.html', content=pdf_urls)
    else:
       return render_template('home.html')






@app.route('/download/',methods=['POST'])
def downloadFile():
    dir = Path(r"D:/pdf")

    with zipfile.ZipFile('judpdf.zip', "w", zipfile.ZIP_DEFLATED) as zip_file:
        for entry in dir.rglob("*"):
            zip_file.write(entry, entry.relative_to(dir))

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
