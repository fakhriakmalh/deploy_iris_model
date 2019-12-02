
# A very simple Flask Hello World app for you to get started with...

# Import libraries
#import numpy as np
from flask import Flask, request, jsonify
from sklearn.externals import joblib
#import pickle
import pandas as pd


# load model
model = joblib.load(open('/home/fakhriakmalh/mysite/iris_model.pkl','rb'))

# app
app = Flask(__name__)

# routes
@app.route('/api', methods=['POST'])

def predict():
    # get data
    data = request.get_json(force=True)

    # convert data into dataframe
    data.update((x, [y]) for x, y in data.items())
    data_df = pd.DataFrame.from_dict(data)

    # predictions
    result = model.predict(data_df)

    # send back to browser
    output = {'results': str(result)}

    # return data
    return jsonify(results=output)

if __name__ == '__main__':
    app.run(port = 5000, debug=True)

# if __name__ == '__main__':
#     try:
#         app.run(port=5000, debug=True)
#     except:
#         print("Server is exited unexpectedly. Please contact server admin.")


