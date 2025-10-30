from flask import Blueprint, request, jsonify
from bson import ObjectId
from config.db import mongo
from models.user_model import UserModel, UserUpdateModel
from pydantic import ValidationError

user_bp = Blueprint('user_bp', __name__)

# CREATE
@user_bp.route('/users', methods=['POST'])
def create_user():
    try:
        db = mongo.db.users  # Access db inside the route function
        data = request.get_json()
        user = UserModel(**data)
        user_id = db.insert_one(user.model_dump()).inserted_id
        return jsonify({"id": str(user_id)}), 201
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#READ
@user_bp.route('/get_users', methods=['GET'])
def get_users():
    try:
        db = mongo.db.users
        users = db.find()
        return jsonify({"data": users})
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#UPDATE
@user_bp.route('/update_user/<id>', methods=['PUT'])
def update_users(id):
    try:
        db = mongo.db.users
        data = request.get_json()
        user = UserUpdateModel(**data)
        result = db.update_one({"_id": ObjectId(id)}, {"$set": user.model_dump(exclude_none=True)})
        if result.modified_count == 0:
            return jsonify({"error": "user not found"}), 404
        return jsonify({"message": "user updated successfully"}), 200
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#DELETE
@user_bp.route('/delete_user/<id>', methods=['DELETE'])
def detele_users(id):
    try:
        db = mongo.db.users
        result = db.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 0:
            return jsonify({"error": "user not found"}), 404
        return jsonify({"message": "user deleted successfully"}), 200

    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500









