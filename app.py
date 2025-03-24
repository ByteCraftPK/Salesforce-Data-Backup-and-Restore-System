from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Salesforce Backup & Restore System</h1> <a href='/backup'>Run Backup</a> | <a href='/restore'>Restore Data</a>"

@app.route("/backup")
def backup():
    os.system("python salesforce_backup.py")
    return "Backup process started!"

@app.route("/restore")
def restore():
    return "Restore function not implemented yet!"

if __name__ == "__main__":
    app.run(debug=True)
