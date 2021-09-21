from flask import Flask, request, jsonify
from flask import render_template

app = Flask(__name__,template_folder='templates')



@app.route("/")
def index():
    return render_template("index.html")
    
    

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run()