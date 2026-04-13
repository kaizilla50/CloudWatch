1. User sends request through browser
2. Request hits Elastic Beanstalk environment
3. EC2 instance runs Flask app via Gunicorn
4. App processes input and generates analysis
5. Logs are sent to CloudWatch
6. Static/project assets stored in S3

---

## Features

- Simple web interface for company input
- Generates structured analysis (summary, risk, opportunity)
- Deployed and accessible via public AWS URL
- Logging and monitoring with CloudWatch
