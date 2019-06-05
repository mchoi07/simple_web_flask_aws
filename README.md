# simple_web_flask_aws


Building a basic web (html) form using flask. </br>
Database is AWS RDS

1. Creating DB instance in AWS RDS.
- Has to open the trafic through security group conf. 

2. To run the flask server in your local, you have to use virtual env of python.
- `virtualenv flask-aws`
- `source flask-aws/bin/activate`

3. Before you run the flask application, you have to export requried instances.
- `export FLASK_APP=flaskr` (flaskr is directory of the application)
- `export FLASK_ENV=development`

4. `flask run`

REFERANCES: </br>
https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80 </br>
http://flask.pocoo.org/docs/1.0/patterns/sqlalchemy/





