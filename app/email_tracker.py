

def log_email(recipient, subject, body):
    email = Email(recipient, subject, body, datetime.now())
    # Save email to database
    save_email_to_db(email)


def log_follow_up_email(recipient, subject, body, follow_up_date):
    follow_up = FollowUpEmail(recipient, subject, body, datetime.now(), follow_up_date)
    # Save follow-up email to database
    save_follow_up_to_db(follow_up)


def track_job_application(company, position, status):
    job = JobApplication(company, position, status, datetime.now())
    # Save job application details
    save_job_to_db(job)