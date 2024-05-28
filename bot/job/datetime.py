from jdatetime import datetime


class DateAndTime:
    def _get_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        return current_time

    def _get_date(self):
        current_date = datetime.now().date().strftime("%Y/%M/%d")
        return current_date
