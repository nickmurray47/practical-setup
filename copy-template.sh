#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: ./copy-template.sh <new-project-name>"
    echo "Example: ./copy-template.sh my-interview-project"
    exit 1
fi

NEW_NAME=$1
TEMPLATE_DIR="$(pwd)"
PARENT_DIR="$(dirname "$TEMPLATE_DIR")"
NEW_DIR="$PARENT_DIR/$NEW_NAME"

echo "Copying template to: $NEW_DIR"

# Copy the entire directory
cp -r "$TEMPLATE_DIR" "$NEW_DIR"

# Remove git history, node modules, cache files, and database
cd "$NEW_DIR"
rm -rf .git
rm -rf node_modules
rm -rf backend/__pycache__
rm -rf backend/app/__pycache__
rm -f backend/dev.db
rm -f dev.db

# Initialize fresh git
git init
git add .
git commit -m "Initial commit from template"

echo "✅ Template copied to: $NEW_DIR"
echo "📁 cd $NEW_DIR"
echo "🚀 Ready for your interview!" 