#Week-2
#Activity-2

#Wb Application to have Hyper link and load an image (from end user input) using Flask.

from flask import Flask
app = Flask(__name__)
@app.route('/upload/<name>')
def upload_image(name):
    return f'''
    <html>
    <head>
        <title>Upload Image</title>
    </head>
    <body>
        <h1>Hello, {name}!</h1>
        <form action="/display_image" method="post" enctype="multipart/form-data">
            <label for="image">Select image to upload:</label>
            <input type="file" name="image" id="image" accept="image/*" required>
            <input type="submit" value="Upload Image">
        </form>
    </body>
    </html>

'''
    