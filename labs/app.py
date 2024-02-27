import os

from flask import Flask

app = Flask(__name__)

host = os.environ.get("HOSTNAME", "Unknown")
environment = os.environ.get("ENVIRONMENT", "Unknown")
user_name = os.environ.get("NAME", "Unknown")


@app.route("/", methods=["GET"])
def index():
    html = f"""
    <html>
        <head>
            <title>Flask app on {host}</title>
        </head>
        <body>
            <h2>Flask is up and running!</h2>
            <p>Welcome, {user_name}, your application is now up and running in
            the {environment} environment!  You can deploy this same image to
            different environments just by changing parameters for "docker run"
            </p>
            <p>Container hostname: {host}</p>
        </body>
    </html>"""

    return html


if __name__ == "__main__":
    print("Flask app is starting up!")
    print("Configuration:")
    print(f"  HOSTNAME={host}")
    print(f"  ENVIRONMENT={environment}")
    print(f"  NAME={user_name}")
    app.run(host="0.0.0.0", port=8888)
