#!/bin/bash

# Exit on error
set -e

echo "🚀 Starting setup..."
# run docker compose up -d --build
docker compose up -d --build
echo "🔧 Waiting for the backend to be ready..."

# Wait for the backend to be ready
while ! curl -s http://localhost:8000/health; do
    sleep 1
done

echo "✅ Backend is ready!"