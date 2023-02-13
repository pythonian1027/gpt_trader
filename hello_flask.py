from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_flask():
    return 'Hello, World!'

# from flask import Flask, jsonify, Response
# import gdown
# import subprocess
# app = Flask(__name__)

# @app.route('/')
# def hello_flask():    
#     url = 'https://drive.google.com/file/d/1ODbfWm7SaV-r5r9clcUdQdmcDBx0NJSy/view?usp=sharing'
#     output="colab.ipynb"
#     gdown.download(url, output,  fuzzy = True, quiet=False)
    
#     # execute the results
#     print ('running colab notebook')
#     result = subprocess.run(["jupyter", "nbconvert", "--execute", "colab.ipynb"], capture_output=True, text=True)
#     print (result.stdout)
#     # return jsonify(message='colab notebook ran successfully')
#     return Response(result.stdout, content_type='text/plain')