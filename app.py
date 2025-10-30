from flask import Flask
from config.db import mongo
from routes.user_routes import user_bp

app = Flask(__name__)

#MongoDB connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/testdb"

# Initialize MongoDB
mongo.init_app(app)

app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True)


