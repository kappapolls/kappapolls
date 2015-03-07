#!/bin/bash

NAME="kappapolls_app"
DJANGODIR=/home/kappapolls/kappa/kappapolls
SOCKFILE=/home/kappapolls/kappa/kappapolls/run/gunicorn.sock
USER=kappapolls
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE=kappapolls.settings
DJANGO_WSGI_MODULE=kappapolls.wsgi
GUNICORN=/home/kappapolls/.virtualenvs/kappapolls/bin/gunicorn

echo "kappapolls starting, no kappa"

cd $DJANGODIR
source /home/kappa/.virtualenvs/kappapolls/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

$GUNICORN  ${DJANGO_WSGI_MODULE}:application \
    --name $NAME \
    --workers $NUM_WORKERS \
    --user=$USER \
    --bind=unix:$SOCKFILE \
    --log-level=debug \

