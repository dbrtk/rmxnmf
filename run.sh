#!/bin/sh

export FLASK_ENV=development
export FLASK_APP=rmxnmf/app.py

flask run -p 8007 --host=0.0.0.0

