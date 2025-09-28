from flask import Flask

app = Flask(__name__)

# Homepage
@app.route('/')
def home():
    return '''
        <h1>Welcome!</h1>
        <p>
            <a href="/about">About</a> | 
            <a href="/contact">Contact</a>
        </p>
    '''

# About page
@app.route('/about')
def about():
    return '''
        <h1>About</h1>
        <p>This is the about page of my Flask project.</p>
        <p><a href="/">Back to Home</a></p>
    '''

# Contact page
@app.route('/contact')
def contact():
    return '''
        <h1>Contact</h1>
        <p>You can reach me at: <strong>kessienaunuakpor@gmail.com</strong></p>
        <p><a href="/">Back to Home</a></p>
    '''

if __name__ == '__main__':
    app.run(debug=True)
