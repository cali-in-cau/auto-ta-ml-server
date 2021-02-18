from keras.layers import Dense, Activation, Dropout
from keras.layers import LSTM
from keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler

from io import StringIO
import pandas as pd
import numpy as np
import time

def predict_with_lstm(data):
    #close값으로만 예측을 한다.
    data = StringIO(data)
    df = pd.read_csv(data)
    
    df_close = df['Close']
    tmp_close = df_close
    df_close = df_close.values.reshape(df_close.shape[0], 1)
    scaler = MinMaxScaler(feature_range=(0, 1))
    df_close = scaler.fit_transform(df_close)


    train_size = int(len(df_close) * 0.90)
    #train_size = int(len(df_close) -1)
    test_size = len(df_close) - train_size
    train, test = df_close[0:train_size,:], df_close[train_size:len(df_close),:]

        # convert an array of values into a dataset matrix
    def create_dataset(dataset, look_back=1): #keep only similar value data if a data point is too far of the last one jump to the next value
        dataX, dataY = [], []       #put this in data x
        for i in range(len(dataset)-look_back-1): #let dataY have only output values
            a = dataset[i:(i+look_back), 0]
            dataX.append(a)
            dataY.append(dataset[i + look_back, 0])
        return np.array(dataX), np.array(dataY)

    # reshape into X=t and Y=t+1
    look_back = 1
    trainX, trainY = create_dataset(train, look_back)
    testX, testY = create_dataset(test, look_back)

    trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
    testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))

    # Build Model
    model = Sequential()

    model.add(LSTM(
        input_dim=1,
        units=50,
        return_sequences=True))
    model.add(Dropout(0.2))

    model.add(LSTM(
        100,
        return_sequences=False))
    model.add(Dropout(0.2))

    model.add(Dense(
        units=1))
    model.add(Activation('relu'))

    start = time.time()
    model.compile(loss='mse', optimizer='rmsprop', metrics=['mae'])
    print ('compilation time : ', time.time() - start)

    model.fit(
        trainX,
        trainY,
        batch_size=128,
        epochs=40,
        validation_split=0.05)
    predicted_stateful = model.predict(testX)
    real_predicted_stateful = scaler.inverse_transform(predicted_stateful)
    # print(real_predicted_stateful[-5:])
    # print("-------")
    # print(tmp_close[-5:])
    # print(real_predicted_stateful[-1])\
    predict_value = float(real_predicted_stateful[-1][0])
    print(predict_value)
    return predict_value