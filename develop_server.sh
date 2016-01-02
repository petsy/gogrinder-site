#!/usr/bin/env bash
##
# This section should match your Makefile
##
PY=${PY:-python}
PELICAN=${PELICAN:-buccaneer}
PELICANOPTS=

BASEDIR=$(pwd)
INPUTDIR=$BASEDIR/content
#OUTPUTDIR=$BASEDIR/output
CONFFILE=$BASEDIR/pelicanconf.py

###
# Don't change stuff below here unless you are sure
###

SRV_PID=$BASEDIR/srv.pid
PELICAN_PID=$BASEDIR/buccaneer.pid

function usage(){
  echo "usage: $0 (stop) (start) (restart)"
  echo "This starts Buccaneer in debug and reload mode and then launches"
  echo "an HTTP server to help site development. It doesn't read"
  echo "your Buccaneer settings, so if you edit any paths in your Makefile"
  echo "you will need to edit your settings as well."
  exit 3
}

function alive() {
  kill -0 $1 >/dev/null 2>&1
}

function shut_down(){
  PID=$(cat $SRV_PID)
  if [[ $? -eq 0 ]]; then
    if alive $PID; then
      echo "Stopping HTTP server"
      kill $PID
    else
      echo "Stale PID, deleting"
    fi
    rm $SRV_PID
  else
    echo "HTTP server PIDFile not found"
  fi

  PID=$(cat $PELICAN_PID)
  if [[ $? -eq 0 ]]; then
    if alive $PID; then
      echo "Killing Buccaneer"
      kill $PID
    else
      echo "Stale PID, deleting"
    fi
    rm $PELICAN_PID
  else
    echo "Buccaneer PIDFile not found"
  fi
}

function start_up(){
  echo "Starting up Buccaneer and HTTP server"
  shift
  $PELICAN --debug --autoreload -r $INPUTDIR -s $CONFFILE $PELICANOPTS &
  buccaneer_pid=$!
  echo $buccaneer_pid > $PELICAN_PID
  #cd $OUTPUTDIR
  $PY -m buccaneer.server $CONFFILE &
  srv_pid=$!
  echo $srv_pid > $SRV_PID
  #cd $BASEDIR
  sleep 1
  if ! alive $buccaneer_pid ; then
    echo "Buccaneer didn't start. Is the Buccaneer package installed?"
    return 1
  elif ! alive $srv_pid ; then
    echo "The HTTP server didn't start. Is there another service using the ports?"
    return 1
  fi
  echo 'Buccaneer and HTTP server processes now running in background.'
}

###
#  MAIN
###
[[ ($# -eq 0) || ($# -gt 1) ]] && usage

if [[ $1 == "stop" ]]; then
  shut_down
elif [[ $1 == "restart" ]]; then
  shut_down
  start_up
elif [[ $1 == "start" ]]; then
  if ! start_up; then
    shut_down
  fi
else
  usage
fi
