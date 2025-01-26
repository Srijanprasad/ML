import json
import pickle

from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)
## Load the model
regmodel=pickle.load(open('regmodel.pkl','rb'))
scalar=pickle.load(open('scaling.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data=scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output=regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input=scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=regmodel.predict(final_input)[0]
    return render_template("home.html",prediction_text="The House price prediction is {}".format(output))



if __name__=="__main__":
    app.run(debug=True)








































































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
#     import pickle
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

# import pickle
# from flask import Flask, request, jsonify, render_template
# import numpy as np
# import pandas as pd

# app = Flask(__name__)

# # Load the model and scaler
# model = pickle.load(open('model.pkl', 'rb'))
# scalar = pickle.load(open('scalar.pkl', 'rb'))

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict_api', methods=['POST'])
# def predict_api():
#     data = request.json['data']
#     print(data)
#     new_data = scalar.transform(np.array(list(data.values())).reshape(1, -1))
#     output = model.predict(new_data)
#     print(output[0])
#     return jsonify({'prediction': output[0]})

# @app.route('/predict', methods=['POST'])
# def predict():
#     data=[float(x)for x in  request.form.values()]
#     final_intput=scalar.trsansform(np.array(data).reshape(1,-1))
#     print(final_intput)
#     output=regmodel.predict(final_intput)[0]
#     return render_template("home.html",prediction_text="The predicted value is {}".format(output))

# if __name__ == '__main__':
#     app.run(debug=True)



# import pickle
# from sklearn.preprocessing import StandardScaler
# from sklearn.datasets import load_diabetes
# import pandas as pd

# # Load the diabetes dataset
# diabetes = load_diabetes()

# # Convert to pandas DataFrame
# diabetes_df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)

# # Initialize the scaler and fit it to the data
# scaler = StandardScaler()
# scaler.fit(diabetes_df)

# # Save the scaler
# pickle.dump(scaler, open('scalar.pkl', 'wb'))

# from flask import Flask, request, jsonify, render_template


# # import numpy as np
# # import pandas as pd
# # import pickle

# # app = Flask(__name__)

# # # Load the model and scaler
# # model = pickle.load(open('model.pkl', 'rb'))
# # scalar = pickle.load(open('scalar.pkl', 'rb'))

# # @app.route('/')
# # def home():
# #     return render_template('index.html')

# # @app.route('/predict_api', methods=['POST'])
# # def predict_api():
# #     data = request.json['data']
# #     print(data)
# #     new_data = scalar.transform(np.array(list(data.values())).reshape(1, -1))
# #     output = model.predict(new_data)
# #     print(output[0])
# #     return jsonify({'prediction': output[0]})

# # if __name__ == '__main__':
# #     app.run(debug=True)


# import json
# import pickle

# from flask import Flask,request,app,jsonify,url_for,render_template
# import numpy as np
# import pandas as pd

# app=Flask(__name__)
# ## Load the model
# regmodel=pickle.load(open('regmodel.pkl','rb'))
# scalar=pickle.load(open('scaling.pkl','rb'))
# @app.route('/')
# def home():
#     return render_template('home.html')

# # @app.route('/predict_api',methods=['POST'])
# # def predict_api():
# #     data=request.json['data']
# #     print(data)
# #     print(np.array(list(data.values())).reshape(1,-1))
# #     new_data=scalar.transform(np.array(list(data.values())).reshape(1,-1))
# #     output=regmodel.predict(new_data)
# #     print(output[0])
# #     return jsonify(output[0])

# # @app.route('/predict',methods=['POST'])
# # def predict():
# #     data=[float(x) for x in request.form.values()]
# #     final_input=scalar.transform(np.array(data).reshape(1,-1))
# #     print(final_input)
# #     output=regmodel.predict(final_input)[0]
# #     return render_template("home.html",prediction_text="The House price prediction is {}".format(output))



# # if __name__=="__main__":
# #     app.run(debug=True)


# import pickle
# from flask import Flask, request, jsonify, render_template
# import numpy as np
# import pandas as pd

# app = Flask(__name__)

# # Load the model and scaler
# model = pickle.load(open('model.pkl', 'rb'))
# scalar = pickle.load(open('scalar.pkl', 'rb'))

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict_api', methods=['POST'])
# def predict_api():
#     data = request.json['data']
#     print(data)
#     new_data = scalar.transform(np.array(list(data.values())).reshape(1, -1))
#     output = model.predict(new_data)
#     print(output[0])
#     return jsonify({'prediction': output[0]})

# if __name__ == '__main__':
#     app.run(debug=True)