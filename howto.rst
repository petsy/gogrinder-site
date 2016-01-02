
developserver
=============

$ ./develop_server.sh start

browse http://localhost:8000

$ ./develop_server.sh stop


build
=====

$ buccaneer -D -s pelicanconf.py


uploading to s3
===============

$ buccaneer-upload -s pelicanconf.py gogrinder --s3host s3.eu-central-1.amazonaws.com -v
