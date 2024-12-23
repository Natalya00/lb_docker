#!/bin/sh
sleep 5 

flask db init || true  
flask db migrate -m "Initial migration" || true 
flask db upgrade 

exec python app.py 
