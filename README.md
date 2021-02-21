# auto-ta-ml-server
## Summary
* 2021 people space group c, auto-ta-ml model server to back-end server.
* we use fastAPI
## Prerequisites
    * python3 (3.8>=, tested on 3.8.5)
    * tested on linux ubuntu 18.04
## Module Install
* for make install
```sh
sudo apt-get update
sudo apt-get install build-essential
sudo apt upgrade
sudo apt-get install python3-dev
```
* for run the server
```sh
#for linux (for other os see [https://mrjbq7.github.io/ta-lib/install.html])
#make virtual env and then
#install ta-lib
tar -xvf ta-lib-0.4.0-src.tar.gz
cd ta-lib
./configure --prefix=/usr
make
sudo make install

#install python modules
pip install -r requirements.txt
```
* we use git lfs for *.pkl file
```sh
#if your computer doesn't have git lfs
#for linux
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt install git-lfs
sudo git lfs install
sudo git lfs pull
```
## Execute
```sh
cd app
#dev
uvicorn main:app --host=0.0.0.0 --port=8888 &
#see http://your-ip:8888
#Swagger UI is on the http://your-ip:8888/docs
#READ and get the api http://your-ip:8888/<api>
#deployment<TODO>
#see https://www.uvicorn.org/deployment/
#use gunicorn
```
## Issue
* if you have problem of privielge change the privilege of app/ml_model/image_db : `chmod -R 777 image_db`

## TODO

## License
