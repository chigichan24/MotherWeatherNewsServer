#!/bin/sh

bluemix target --cf
bluemix cf push ${MOTHER_WEATHER_NEWS_SERVER_BLUEMIX_APP_NAME}
