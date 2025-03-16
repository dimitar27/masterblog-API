from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


@app.route('/api/posts', methods=['GET'])
def get_posts():
    return jsonify(POSTS)

@app.route('/api/posts', methods=['POST'])
def add_post():
    """
    Adds a new blog post.

    Expects a JSON request with "title" and "content".
    Returns 201 on success, or 400 if validation fails.
    """
    new_post = request.get_json()

    if "title" not in new_post or not new_post['title'].strip():
        return jsonify({"error": "Title is required and cannot be empty."}), 400

    elif "content" not in new_post or not new_post['content'].strip():
        return jsonify({"error": "Content is required and cannot be empty."}), 400

    new_id = max(post['id'] for post in POSTS) + 1
    new_post['id'] = new_id

    POSTS.append(new_post)
    return jsonify(new_post), 201

@app.route('/api/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    """
    Deletes a blog post by its ID.

    Returns 200 OK if deleted successfully.
    Returns 404 Not Found if the post does not exist.
    """
    post_index = None

    for i, post in enumerate(POSTS):
        if post['id'] == id:
            post_index = i
            break

    if post_index is None:
        return jsonify({"error": f"Post with id {id} not found."}), 404

    POSTS.pop(post_index)

    return jsonify({"message": f"Post with id {id} has been deleted successfully."}), 200



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
