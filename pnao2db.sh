#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

cd /home/llepontois/python/pnao2db/
source venv/bin/activate
python pnao2db.py
deactivate
