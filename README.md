# auto-ta-ml-server
## Authors
## Summary
* 2021 people space group c, auto-ta-ml model server to back-end server.
* we use fastAPI
## Prerequisites
    * python3 (3.8>=, tested on 3.8.5)
## Module Install
```sh
#make virtual env
pip install -r requirements.txt
```
* look at `requirements.txt`
## Execute
```sh
cp app
#dev
uvicorn main:app --reload --host=0.0.0.0 --port=8888
#see http://your-ip:8888
#Swagger UI is on the http://your-ip:8888/docs
```
## How TO

## TODO
https://fastapi.tiangolo.com/tutorial/bigger-applications/
이거 보고 구조화, 및 모델 서빙 준비
## License
