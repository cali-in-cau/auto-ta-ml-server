from typing import Optional

from fastapi import FastAPI, Request
from pydantic import BaseModel

from ml_model.preprocessing import parse_data, ohlc_to_ta_lib
#from ml_model.predict_lstm import predict_with_lstm
from ml_model.predict_image import predict_model_image_deep
from ml_model.afterprocessing import calculate_bull_bear
class RGB2GreyTransform:
    order = 15 # run after IntToFloatTransform
    def encodes(self, o):
        c = o.shape[1]
        return rgb_to_grayscale(o).expand(-1,c,-1,-1)

app = FastAPI()


class MLData(BaseModel):
    info: dict
    data: dict

@app.get("/")
def read_root():
    return {"message": "auto-ta-ml-server"}


@app.post("/ml/predict")
def read_item(data: MLData):
    res = {}
    convert_csv_data = parse_data(data)
    res['talib'], res['talibv2'], talib_csv_data  = ohlc_to_ta_lib(convert_csv_data)
    #numpy issue occured so temporatily deleted
    #res['value_prediction'] = predict_with_lstm(convert_csv_data)
    res['image_prediction'] = predict_model_image_deep(res['talib'], talib_csv_data)
    res['price_prediction'] = calculate_bull_bear(res['image_prediction'])
    
    
    return res


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8878)