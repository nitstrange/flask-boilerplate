from flask import Flask 
import connexion

#create flask application
#app = Flask(__name__)

# Create the application instance
app = connexion.App(__name__, specification_dir='./')
application = app.app
#add swagger yaml from connexion module
app.add_api('swagger.yml')
#home route
@app.route('/')
def home():
    #print("This is just home page")
    return 

#running flask in standalone mode
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)