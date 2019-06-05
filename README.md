# simple_web_flask_aws
simple_web_flask_aws

Building a basic web (HTML) applicaiton using Flask.

1) Create DB in AWS RDS
- Instanciate mySql Database in AWS
- Open the network (inbound and outbound)

2) Set up Python environment
- To run Flask application, you have to use virtual python environment 

- `pip install -r requirment.txt`
- `virtualenv flask-aws`
- `source flask-aws/bin/activate`
- `export FLASK_APP=flaskr` - Name of directory 
- `export FLASK_ENV=development`
- `flask run`


References: </br>
https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80 </br>
http://flask.pocoo.org/docs/1.0/tutorial/factory/ </br>
http://flask.pocoo.org/docs/1.0/patterns/sqlalchemy/ </br>
