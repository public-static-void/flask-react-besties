from flask import jsonify, request

from models import Friend, db


def init_routes(app):

    # Get all friends
    @app.route("/api/friends", methods=["GET"])
    def get_friends():
        friends = Friend.query.all()
        result = [friend.to_json() for friend in friends]
        return jsonify(result)

    # Create a friend
    @app.route("/api/friends", methods=["POST"])
    def create_friend():
        try:
            friend = request.json

            required_field = ["name", "role", "description", "gender"]
            missing_fields = []
            for field in required_field:
                if field not in friend:
                    missing_fields.append(field)
            if len(missing_fields) != 0:
                return (
                    jsonify(
                        {
                            "error": (
                                f"Missing required field(s): {missing_fields}"
                            )
                        }
                    ),
                    400,
                )

            name = friend.get("name")
            role = friend.get("role")
            description = friend.get("description")
            gender = friend.get("gender")

            avnm = name.replace(" ", "_")
            # Fetch avatar image based on gender
            if gender == "male":
                img_url = (
                    f"http://avatar.iran.liara.run/public/boy?username={avnm}"
                )
            elif gender == "female":
                img_url = (
                    f"http://avatar.iran.liara.run/public/boy?username={avnm}"
                )
            else:
                img_url = None

            new_friend = Friend(
                name=name,
                role=role,
                description=description,
                gender=gender,
                img_url=img_url,
            )

            db.session.add(new_friend)
            db.session.commit()
            return (
                jsonify(
                    new_friend.to_json(),
                ),
                201,
            )
        except Exception as e:
            return (
                jsonify({"message": "Error creating friend. " + str(e)}),
                500,
            )

    # Delete a friend
    @app.route("/api/friends/<int:id>", methods=["DELETE"])
    def delete_friend(id):
        try:
            friend = Friend.query.get(id)
            if friend is None:
                return jsonify({"message": "Friend not found"}), 404
            db.session.delete(friend)
            db.session.commit()
            return jsonify({"message": "Friend deleted successfully"}), 200
        except Exception as e:
            db.session.rollback()
            return (
                jsonify({"message": "Error deleting friend. " + str(e)}),
                500,
            )

    # Update a friend
    @app.route("/api/friends/<int:id>", methods=["PATCH"])
    def update_friend(id):
        try:
            friend = Friend.query.get(id)
            if friend is None:
                return jsonify({"message": "Friend not found"}), 404
            friend_data = request.json

            friend.name = friend_data.get("name", friend.name)
            friend.role = friend_data.get("role", friend.role)
            friend.description = friend_data.get(
                "description", friend.description
            )
            friend.gender = friend_data.get("gender", friend.gender)

            db.session.commit()
            return jsonify(friend.to_json()), 200
        except Exception as e:
            db.session.rollback()
            return (
                jsonify({"message": "Error updating friend. " + str(e)}),
                500,
            )
