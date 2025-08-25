# Deployment Guide – Secure OCR On-Prem

## 1. Prerequisites
- Docker & Docker Compose installed
- Azure OCR Container image downloaded
- Air-gapped Linux server (Ubuntu recommended)

## 2. Steps
1. Clone this repository
2. Build and run using Docker Compose:
   ```bash
   docker-compose up -d
   ```
3. Access web UI at: `http://localhost:8000`
4. Upload documents → OCR results are displayed.
