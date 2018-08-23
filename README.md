# MotherWeatherNewsServer
MotherWeatherNews server

## Environments
- Python3.6

## How to set up
- Google CloudのCloud Natural Language APIに登録し、サービスアカウントキー(json)を`/config/credential.json`に置く
- サービスアカウントキーが置いてある場所のpathを`GOOGLE_APPLICATION_CREDENTIALS`に入れる
- Azureに登録し、Azure Face APIのAPIキーを`AZURE_FACE_API_SUBSCRIPTION_KEY`に入れる
- ```pip3 install -r requirements.txt```
- `./init.sh`

## How to set up for IBM Cloud
- 環境変数`MOTHER_WEATHER_NEWS_SERVER_BLUEMIX_APP_NAME`にアプリの名前を入れる
- `bluemix cf set-env $MOTHER_WEATHER_NEWS_SERVER_BLUEMIX_APP_NAME AZURE_FACE_API_SUBSCRIPTION_KEY $AZURE_FACE_API_SUBSCRIPTION_KEY`
- `bluemix cf set-env $MOTHER_WEATHER_NEWS_SERVER_BLUEMIX_APP_NAME GOOGLE_APPLICATION_CREDENTIALS "/home/vcap/app/config/credential.json"`

## How to up server in local
- ```python3 app.py```

## How to deploy
- `./deploy.sh`
