from flask import Flask
from flask import render_template, request, redirect
import speech_recognition as spr
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")
        
        if "file" not in request.files:
            return redirect(request.url)
        ##if file exists
        file = request.files["file"]
        ##failsafe
        if file.filename=="":
            return redirect(request.url)
        if file:
            recognizer = spr.Recognizer()
            audioFile = spr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)
    return render_template('index.html', transcript=transcript)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)