#!/bin/bash

# Deploys the feedback ingestor Cloud Function

# Exit immediately if a command exits with a non-zero status.
set -e

# --- Configuration ---
PROJECT_ID="${1:-manufacturing-copilot-dev}"
REGION="${2:-us-central1}"
FUNCTION_NAME="feedback-ingestor"
ENTRY_POINT="ingest_feedback"
RUNTIME="python311"
TRIGGER="--trigger-http"
SOURCE_DIR="./app/functions/feedback" # Assuming function code is in app/
BIGQUERY_TABLE="feedback.user_ratings"
MEMORY="256Mi"

# --- Validation ---
if [ ! -d "$SOURCE_DIR" ]; then
  echo "Error: Source directory '$SOURCE_DIR' not found."
  echo "Please ensure your Cloud Function code is located in the correct directory."
  exit 1
fi

echo "--- Deploying Cloud Function ---"
echo "Project:       ${PROJECT_ID}"
echo "Region:        ${REGION}"
echo "Function Name: ${FUNCTION_NAME}"
echo "Source:        ${SOURCE_DIR}"
echo "--------------------------------"

gcloud functions deploy "${FUNCTION_NAME}" \
  --project="${PROJECT_ID}" \
  --region="${REGION}" \
  --runtime="${RUNTIME}" \
  --entry-point="${ENTRY_POINT}" \
  ${TRIGGER} \
  --source="${SOURCE_DIR}" \
  --allow-unauthenticated \
  --memory="${MEMORY}" \
  --set-env-vars="BIGQUERY_TABLE=${BIGQUERY_TABLE}"

echo "✅ Deployment complete."
