# from flask import Flask, render_template, request
# import pandas as pd
# from pmdarima import auto_arima
# from statsmodels.tsa.statespace.sarimax import SARIMAX
# import matplotlib.pyplot as plt
# from tqdm import tqdm

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/upload', methods=['POST'])
# def upload():
#     if 'file' not in request.files:
#         return render_template('index.html', error="No file part")
    
#     file = request.files['file']
#     if file.filename == '':
#         return render_template('index.html', error="No selected file")
    
#     if file:
#         df = pd.read_csv(file)
#         # Assuming 'date' column is present and in datetime format
#         df['date'] = pd.to_datetime(df['date'])
#         df = df.set_index('date')
        
#         # Split data into train and test
#         train_size = int(len(df) * 0.8)
#         df_train, df_test = df.iloc[:train_size], df.iloc[train_size:]
        
#         # Build the SARIMAX model using auto_arima
#         autoModel = auto_arima(df_train['Sales'], trace=True, error_action='ignore',
#                                suppress_warnings=True, seasonal=True, m=12, stepwise=True)
#         order = autoModel.order
#         seasonalOrder = autoModel.seasonal_order
        
#         yhat = []
#         for t in tqdm(range(len(df_test['Sales']))):
#             temp_train = df.iloc[:len(df_train)+t]
#             model = SARIMAX(temp_train['Sales'], order=order, seasonal_order=seasonalOrder)
#             model_fit = model.fit(disp=False)
#             predictions = model_fit.predict(start=len(temp_train), end=len(temp_train), dynamic=False)
#             yhat.append(predictions)
        
#         yhat = pd.concat(yhat)
        
#         # Plot the original and forecasted sales data using matplotlib
#         plt.plot(df_test['Sales'], label='Original')
#         plt.plot(yhat, color='red', label='SARIMAX Forecast')
#         plt.xlabel('Date')
#         plt.ylabel('Sales')
#         plt.title('Sales Forecast')
#         plt.xticks(rotation=90)
#         plt.legend()
        
#         # Save the plot as a temporary file
#         plt.tight_layout()
#         plot_path = 'static/forecast_plot.png'
#         plt.savefig(plot_path)
        
#         return render_template('index.html', plot_path=plot_path)

# if __name__ == '__main__':
#     app.run(debug=True)


# --------------------------------------------------------------------------

from flask import Flask, render_template, request, jsonify
import pandas as pd
from pmdarima import auto_arima
from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pyplot as plt
import os
from tqdm import tqdm

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file:
        df = pd.read_csv(file)
        # Assuming 'date' column is present and in datetime format
        df['date'] = pd.to_datetime(df['date'])
        df = df.set_index('date')
        
        # Split data into train and test
        train_size = int(len(df) * 0.8)
        df_train, df_test = df.iloc[:train_size], df.iloc[train_size:]
        
        # Build the SARIMAX model using auto_arima
        autoModel = auto_arima(df_train['Sales'], trace=True, error_action='ignore',
                               suppress_warnings=True, seasonal=True, m=12, stepwise=True)
        order = autoModel.order
        seasonalOrder = autoModel.seasonal_order
        
        yhat = []
        for t in tqdm(range(len(df_test['Sales']))):
            temp_train = df.iloc[:len(df_train)+t]
            model = SARIMAX(temp_train['Sales'], order=order, seasonal_order=seasonalOrder)
            model_fit = model.fit(disp=False)
            predictions = model_fit.predict(start=len(temp_train), end=len(temp_train), dynamic=False)
            yhat.append(predictions)
        
        yhat = pd.concat(yhat)
        
        # Plot the original and forecasted sales data using matplotlib
        plt.figure(figsize=(10, 6))
        plt.plot(df_test.index, df_test['Sales'], 'bo-', label='Original', markersize=6)
        plt.plot(df_test.index, yhat, 'rs--', label='SARIMAX Forecast', markersize=8)
        plt.xlabel('Date')
        plt.ylabel('Sales')
        plt.title('Sales Forecast')
        plt.xticks(rotation=45)
        plt.legend()
        
        # Save the plot as a temporary file
        plot_path = 'static/forecast_plot.png'
        plt.savefig(plot_path)
        plt.close()
        
        best_model_params = {'order': order, 'seasonal_order': seasonalOrder}
        
        return jsonify({'plot_path': plot_path, 'best_model_params': best_model_params})

if __name__ == '__main__':
    app.run(debug=True)
