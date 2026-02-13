from flask import Flask
app = Flask(__namw__)

@app.route("/")
def hello():
	return "Hello from Flask inside Docker!"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
