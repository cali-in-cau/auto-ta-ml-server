
import mplfinance as mpf
import pandas as pd
import io
import talib

def parse_data(data):

    data = data.data
    #데이터를 파싱해서 한열에 각각 Date, Open, High, Low, Close,Volume 형태로 나타낸다.
    date = data['date']
    value = data['value']

    csv_string="Date,Open,High,Low,Close,Volume\n"
    for i, v in enumerate(date):
        open = value[i]['Open']
        high = value[i]['High']
        low = value[i]['Low']
        close = value[i]['Close']
        volume = value[i]['Volume']

        csv_string += f'{v},{open},{high},{low},{close},{volume}\n'
    
    return csv_string

def ohlc_to_ta_lib(data):
    ta_lib_dict = {'bull':[],'bear':[]}

    csv_string = data
    csv_data = pd.read_csv(io.StringIO(csv_string), index_col=0, parse_dates=True)
    
    patterns_names = talib.get_function_groups()['Pattern Recognition']
    #ta-lib pattern recognition list print(patterns_names)
    for pattern in patterns_names:
        csv_data[pattern] = getattr(talib, pattern)(csv_data['Open'], csv_data['High'], csv_data['Low'], csv_data['Close'])
        tmp_data = csv_data
    
    #pattern이 없는 0칼럼들 다 제외
    zero_column = list(csv_data.columns[(csv_data == 0).all()])
    not_zero_column = list(set(patterns_names) - set(zero_column))
    #print(not_zero_column)
    #csv_data.to_csv('./sample.csv', sep=',', na_rep='NaN')

    for pattern in not_zero_column:
        #print(pattern)
        csv_data_bull = tmp_data[tmp_data[pattern] > 0]
        csv_data_bear = tmp_data[tmp_data[pattern] < 0]
        #각 csv_data에서 양수 인거(보통 100)은 bullish를 나타내고 음수 인거(보통 -100)은 bearish를 나타낸다.
        # 각 패턴이 bull version도 있고 bear 버전도 있다. 따라서 나눠야 한다.
        date_bull = list(map(lambda x : x.strftime("%Y-%m-%d"), csv_data_bull.index))
        date_bear = list(map(lambda x : x.strftime("%Y-%m-%d"), csv_data_bear.index))

        #print(date_bull)
        for date in date_bull:
            ta_lib_dict['bull'].append((f'{pattern[3:]}_BULL', date))
            data_to_image

        for date in date_bear:
            ta_lib_dict['bear'].append((f'{pattern[3:]}_BEAR', date))
    
    return ta_lib_dict


def data_to_image():
    #talib에서 걸러진것을 image processing project로 가져간다.
    pass

