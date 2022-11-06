from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
    <html>
        <body>
            <center>
                <h1>Team 9</h1>
                <h3>Mike Medved, Benny Chen</h3>
            </center>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run()