from flask import flask


app=Flask(__name__)

@app.route('/',method=['GET', 'POST'])
def index():
    return "Staring Credit Risk Modeling Project"

if __name__ == '__main__':
    app.run(debug=True)