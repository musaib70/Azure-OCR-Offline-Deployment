#!/bin/bash
if curl -s http://localhost:8000 > /dev/null; then
  echo "OCR Web App is running ✅"
else
  echo "OCR Web App is DOWN ❌"
fi
