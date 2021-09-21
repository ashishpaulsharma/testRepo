from flask import Flask,redirect,render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
    

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run()