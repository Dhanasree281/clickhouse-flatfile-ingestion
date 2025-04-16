from flask import Flask, request, jsonify
app = Flask(__name__)

# @app.route('/health', methods=['GET'])
# def health():
#     return jsonify({"status": "Backend is running!"})

# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask, request, jsonify
# from clickhouse_connect import get_client
# import pandas as pd  # Will be used later for CSV upload

# app = Flask(__name__)

# # ✅ Test route to check if backend is running
# @app.route('/')
# def home():
#     return jsonify({"message": "Backend is working!"})

# # ✅ STEP 6: ClickHouse Connection Endpoint
# @app.route('/connect_clickhouse', methods=['POST'])
# def connect_clickhouse():
#     data = request.json  # This reads the JSON payload from frontend

#     # Read data sent by the user
#     host = data.get('host')
#     port = int(data.get('port'))
#     user = data.get('user')
#     jwt_token = data.get('jwt')  # JWT is passed as password

#     try:
#         # Connect to ClickHouse server
#         client = get_client(
#             host=host,
#             port=port,
#             username=user,
#             password=jwt_token
#         )

#         # Fetch list of tables
#         result = client.query("SHOW TABLES").result_rows
#         tables = [row[0] for row in result]

#         # Return the table names
#         return jsonify({"tables": tables})

#     except Exception as e:
#         return jsonify({"error": str(e)}), 400

# # 👇 In future, we will add other routes below this
# # /upload_flatfile
# # /flatfile_to_clickhouse
# # etc.

# if __name__ == '__main__':
#     app.run(debug=True)

@app.route('/connect_clickhouse', methods=['POST'])
def connect_clickhouse():
    data = request.json
    print("Received connection data:", data)  # ✅ Debug print

    host = data.get('host')
    port = int(data.get('port'))
    user = data.get('user')
    jwt_token = data.get('jwt')

    try:
        client = get_client(
            host=host,
            port=port,
            username=user,
            password=jwt_token
        )
        print("Connected to ClickHouse!")  # ✅ Debug print

        result = client.query("SHOW TABLES").result_rows
        tables = [row[0] for row in result]
        print("Fetched tables:", tables)  # ✅ Debug print

        return jsonify({"tables": tables})

    except Exception as e:
        print("Error:", str(e))  # ✅ Print error if occurs
        return jsonify({"error": str(e)}), 400
