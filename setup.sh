#!/bin/bash
flask db init
flask db migrate
flask db upgrade
python populate_fake_db.py