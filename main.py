from flask import Flask,request,render_template
import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
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

         data = "juddt=date&Submit=Submit"
         response= requests.post(url, headers=headers, data=data)
         content = BeautifulSoup(response.text, 'lxml')
         return content

       r= extraction(jdate)

       all_urls = r.find_all('a')
       pdf_urls=[]
       for url in all_urls:

               if 'pdf' in url['href']:
                   p_url=url['href']
               pdf_urls.append(p_url)


       return render_template('home.html',content=pdf_urls)



    else:
        return render_template('home.html')

if __name__=='__main__':
    app.run(debug=True)

