wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-213.0.0-linux-x86_64.tar.gz
tar -zxvf google-cloud-sdk-213.0.0-linux-x86_64.tar.gz
./google-cloud-sdk/install.sh --quiet

export PATH="~/google-cloud-sdk/bin:$PATH"
gcloud auth activate-service-account --key-file "$PWD/config/credential.json"

# test
python3 emotion_estimator_test.py
