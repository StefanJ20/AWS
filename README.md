# AWS

This service places a Django Web Server into an EC2 instance on AWS, running directly from this GitHub repository.

The instance is configured to serve a Django application using Gunicorn as the WSGI server and Nginx as the reverse proxy for production-grade performance. The deployment leverages AWS’s free-tier resources (t2.micro or t3.micro instance) to provide a cost-effective environment for testing, staging, or lightweight production workloads.

Key Features:

Automated deployment: Source code is pulled directly from this GitHub repository onto the EC2 instance.
Virtual environment: Python dependencies are isolated using a virtual environment (venv).
Static file management: Django static files are collected and served through Nginx for improved efficiency.

Security best practices:

Secrets are never committed to Git. (.gitignore)
HTTPS configuration is supported via Let’s Encrypt.
SSH key-based authentication is used for EC2 access.

Scalability: The setup can easily be extended with AWS services like RDS for databases, S3 for media storage, and CloudFront for CDN caching.

Typical Workflow:

Launch an EC2 instance (Amazon Linux or Ubuntu).
Clone this repository onto the instance.
Create a virtual environment and install dependencies.
Configure environment variables and database settings.
Collect static files and start the Django server with Gunicorn.
Set up Nginx as a reverse proxy to route incoming HTTP traffic.
This configuration provides a complete end-to-end deployment path for Django applications hosted on AWS, emphasizing simplicity, reliability, and adherence to best practices.