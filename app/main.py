from typing import Optional

from fastapi import FastAPI, Request
from pydantic import BaseModel

from ml_model.preprocessing import parse_data, ohlc_to_ta_lib

app = FastAPI()


class MLData(BaseModel):
    info: dict
    data: dict

@app.get("/")
def read_root():
    return {"message": "auto-ta-ml-server"}


@app.post("/ml/graph")
def read_item(data: MLData):
    res = {}
    convert_csv_data = parse_data(data)
    res['talib'] = ohlc_to_ta_lib(convert_csv_data)


    return res


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8878)
