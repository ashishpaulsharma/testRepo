from app import app

from flask import render_template

@app.route("/")
def index():
    return render_template("index.htm")
    
    

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run()