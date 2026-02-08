#!/usr/bin/env bash
# Render Build Script

set -o errexit  # Exit on error

echo "🔄 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Dependencies installed!"

echo "🔄 Initializing database..."
python migrate_render.py

echo "✅ Build completed successfully!"
