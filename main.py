from app.email_tracker import log_email, track_job_application
from app.db import create_tables

if __name__ == "__main__":
    # Initialize database tables
    create_tables()

    # Log a sample email
    log_email("recruiter@example.com", "Application for Data Scientist",
              "Body of the email")

    # Track a job application
    track_job_application("PrizePicks", "Data Scientist", "applied")
