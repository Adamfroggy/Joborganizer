from datetime import datetime


class Email:
    def __init__(self, recipient, subject, body, date_sent):
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.date_sent = date_sent


class FollowUpEmail(Email):
    def __init__(self, recipient, subject, body, date_sent, follow_up_date):
        super().__init__(recipient, subject, body, date_sent)
        self.follow_up_date = follow_up_date


class JobApplication:
    def __init__(self, company, position, status, applied_date):
        self.company = company
        self.position = position
        self.status = status  # e.g., 'applied', 'interviewed', 'offer'
        self.applied_date = applied_date
