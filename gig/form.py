import urllib.request
import requests
# importing Flask and other modules
from flask import Flask, request, render_template
helloworld = Flask(__name__)
@helloworld.route("/")
# Flask constructor
 
# A decorator used to tell the application
# which URL is associated function
@helloworld.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       url = request.form.get("urlname")
       val = requests.get(url)
       #resp = http.request('GET',url)
       #val = str(resp.status_code)
       #val = str(urllib.request.urlopen(url).getcode())
       return str(val.status_code)
    return render_template("form.html")
 
if __name__ == "__main__":
    helloworld.run(host="0.0.0.0", port=int("5000"), debug=True)