from datetime import datetime
def is_valid(record):
    start_date = record["start_date"]
    status = record["status"]
    exit_date = record["exit_date"]
    if not start_date or not status:
        return False
    start = datetime.strptime(start_date, "%Y-%m-%d")

    if exit_date:
        exit = datetime.strptime(exit_date, "%Y-%m-%d")
        if exit < start:
            return False
    return True

   