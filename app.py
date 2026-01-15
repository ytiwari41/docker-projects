from flask import Flask, url_for
import socket
import platform

app = Flask(__name__)

OWNER_NAME = "Yogendra Tiwari 🇮🇳"

@app.route("/")
def host_fitness():
    return f"""
    <html>
    <head>
        <title>Host Fitness Test</title>
    </head>
    <body style="font-family: Arial; text-align: center;">

        <h1>🏋️ Host Fitness Test Application</h1>
        <h3 style="color: gray;">By {OWNER_NAME}</h3>

        <img src="{url_for('static', filename='images/fitness.png')}"
             width="400"
             alt="Fitness Image"
             style="border-radius: 10px; margin-bottom: 20px;" />

        <hr style="width:50%">

        <p><b>Hostname:</b> {socket.gethostname()}</p>
        <p><b>Operating System:</b> {platform.system()} {platform.release()}</p>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

