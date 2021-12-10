from flask import Flask, jsonify, render_template, request
import requests
import time
app = Flask(__name__)


@app.route('/urlapi',methods=['GET','POST'])
def url_rep():
      value = request.args.get('dmk')
      api_secret = 'c654b02b275e45e0333b40b76286a91a'
      api_key = 'acc_7b4791ea506b6bf'
      response = requests.get('https://api.imagga.com/v2/tags?image_url=%s' % value,auth=(api_key, api_secret))
      data=response.json()
      pfruit = data["result"]["tags"][0]["tag"]["en"]
      pconfi =data["result"]["tags"][0]["confidence"]
      pfruit=str(pfruit)
      pconfi=str(pconfi)
      url="https://www.fruityvice.com/api/fruit/"+pfruit
      r = requests.get(url)
      if r.status_code == 200:
         data = r.json()
         quote = f'<br><b>Sugar :</b> {data["nutritions"]["sugar"]} <br> <b>Calories :</b> {data["nutritions"]["calories"]}<br><b> Protein :</b> {data["nutritions"]["protein"]}<br><b> Carbs :</b> {data["nutritions"]["carbohydrates"]} <br><b> Fat : </b>{data["nutritions"]["fat"]} '
      else:
         quote = 'try later'
      print(pfruit+" "+pconfi)
      return {"fruit":pfruit,"details":quote}
   
 
@app.route('/')
def homescan():
   return render_template('index.html')

@app.route('/knowyourfruit')
def urlscaning():
   return render_template('index.html')

@app.route('/facts')
def deepscaning():
   return render_template('facts.html')

@app.route('/dietplan')
def dnsipscaning():
   return render_template('dietplan.html')

if __name__ == '__main__':
   app.run()