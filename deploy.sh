#!/bin/sh

bluemix target --cf
cf push MotherWeatherNews -b https://github.com/cloudfoundry/python-buildpack
