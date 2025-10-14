# app/functions/feedback/main.py
import os
import functions_framework
from flask import Request, jsonify
# In a real project, you would use the Google Cloud client library
# from google.cloud import bigquery

# Mock BigQuery client for demonstration
class MockBigQuery:
    def insert_rows_json(self, table, rows):
        print(f"--- MOCK BIGQUERY ---")
        print(f"Inserting into table: {table}")
        print(f"Rows: {rows}")
        print(f"---------------------")
        return [] # Return an empty list for no errors

@functions_framework.http
def ingest_feedback(request: Request):
    """
    HTTP Cloud Function to ingest user feedback and save it to BigQuery.
    
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    if request.method != 'POST':
        return 'Only POST requests are accepted', 405

    request_json = request.get_json(silent=True)
    if not request_json:
        return 'Invalid JSON', 400

    # --- Data Validation ---
    required_fields = ['user_id', 'request_id', 'rating', 'agent_name']
    if not all(field in request_json for field in required_fields):
        return f"Missing one or more required fields: {required_fields}", 400
    
    if not isinstance(request_json['rating'], int) or not (1 <= request_json['rating'] <= 5):
        return "Field 'rating' must be an integer between 1 and 5.", 400

    # --- Data Processing ---
    table_id = os.environ.get("BIGQUERY_TABLE")
    if not table_id:
        print("ERROR: BIGQUERY_TABLE environment variable not set.")
        return "Internal server error: BigQuery table not configured.", 500

    # In a real application, you would initialize the actual client
    # bq_client = bigquery.Client()
    bq_client = MockBigQuery()

    rows_to_insert = [
        {
            "user_id": request_json["user_id"],
            "request_id": request_json["request_id"],
            "rating": request_json["rating"],
            "agent_name": request_json["agent_name"],
            "feedback_text": request_json.get("feedback_text", None), # Optional field
            "timestamp": "AUTO", # BigQuery can auto-populate this
        }
    ]

    errors = bq_client.insert_rows_json(table_id, rows_to_insert)
    if errors:
        print(f"Encountered errors while inserting rows: {errors}")
        return "Failed to save feedback.", 500

    return jsonify({"status": "success"}), 200
