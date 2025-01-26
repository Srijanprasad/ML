# import pickle
# from flask import Flask, request, jsonify, url_for, render_template
# import numpy as np
# import pandas as pd

# app = Flask(__name__)
# # load the model
# model = pickle.load(open('model.pkl', 'rb')) 
# scalar = pickle.load(open('scalar.pkl', 'rb'))

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict_api', methods=['POST'])

# def predict_api():
#     data = request.json['data']
#     print(data)
#     print(np.array(list(data.values())).reshape(1, -1))
#     new_data = scalar.transform(np.array(list(data.values())).reshape(1, -1))
#     output = regmodel    import pickle
#     from flask import Flask, request, jsonify, render_template
#     import numpy as np
#     import pandas as pd
    
#     app = Flask(__name__)
#         import pickle
#     from flask import Flask, request, jsonify, render_template
#     import numpy as np
#     import pandas as pd
    
#     app = Flask(__name__)
    
#     # Load the model and scaler
#     model = pickle.load(open('model.pkl', 'rb'))
#     scalar = pickle.load(open('scalar.pkl', 'rb'))
    
#     @app.route('/')
#     def home():
#         return render_template('index.html')
    
#     @app.route('/predict_api', methods=['POST'])
#     def predict_api():
#         data = request.json['data']
#         print(data)
#         new_data = scalar.transform(np.array(list(data.values())).reshape(1, -1))
#         output = model.predict(new_data)
#         print(output[0])
#         return jsonify({'prediction': output[0]})
    
#     if __name__ == '__main__':
#         app.run(debug=True)
#     # Load the model and scaler
#     model = pickle.load(open('model.pkl', 'rb'))
#     scalar = pickle.load(open('scalar.pkl', 'rb'))
    
#     @app.route('/')
#     def home():
#         return render_template('index.html')
    
#     @app.route('/predict_api', methods=['POST'])
#     def predict_api():
#         data = request.json['data']
#         print(data)
#         new_data = scalar.transform(np.array(list(data.values())).reshape(1, -1))
#         output = model.predict(new_data)
#         print(output[0])
#         return jsonify({'prediction': output[0]})
    
#     if __name__ == '__main__':
#         app.run(debug=True).predict(new_data)
#     print(output[0])
#     return jsonify({'prediction': output[0]})

# if __name__ == '__main__':
#     app.run(debug=True)


    # new_data = np.array(list(data.values())).reshape(1, -1)
    # data_unseen = pd.DataFrame(data)
    # prediction = model.predict(data_unseen)
    # prediction = prediction.to_json(orient='records')
    # return jsonify(prediction)

import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scalar = pickle.load(open('scalar.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    new_data = scalar.transform(np.array(list(data.values())).reshape(1, -1))
    output = model.predict(new_data)
    print(output[0])
    return jsonify({'prediction': output[0]})

if __name__ == '__main__':
    app.run(debug=True)