from flask import Flask
import urllib.request
helloworld = Flask(__name__)
@helloworld.route("/")
def run():
    #status_code = urllib.request.urlopen("https://google.com").getcode()
    url = input("Enter your URL: ")
    return str(urllib.request.urlopen(url).getcode())
    #print(status_code)
    #return "{\"message\":\"Hello World Python v2\"}"
if __name__ == "__main__":
    helloworld.run(host="0.0.0.0", port=int("5000"), debug=True)
    
    
#url = input("Enter your URL: ")
#status_code = urllib.request.urlopen("https://google.com").getcode()
#print(status_code)