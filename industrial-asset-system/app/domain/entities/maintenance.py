from datetime import date
from uuid import uuid4


class Maintenance:
    def __init__(self, asset_id: str, description: str, scheduled_date: date):
        if scheduled_date < date.today():
            raise ValueError("Scheduled date cannot be in the past")

        self.id = str(uuid4())
        self.asset_id = asset_id
        self.description = description
        self.scheduled_date = scheduled_date
        self.completed = False

    def complete(self):
        if self.completed:
            raise ValueError("Already completed")
        self.completed = True