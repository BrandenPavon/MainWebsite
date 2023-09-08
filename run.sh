#!/bin/bash
. venv/bin/activate
gunicorn -w 2 -b 127.0.0.1:5000 'main:app'
