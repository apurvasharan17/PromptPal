import os
from main import create_app

print("Current working directory", os.getcwd())

# Create an instance for the flask application
app=create_app()

if __name__=='__main__':
    print("Flask app is running on http://127.0.0.1:5000/")
    app.run(host='127.0.0.1', port=5000, debug=True)


