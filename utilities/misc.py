from datetime import datetime


class Misc:

    @staticmethod
    def getrandomdate():
        current_date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        str1 = current_date.replace('/', '_').replace(',', '_').replace(' ', '_').replace(':', '_')
        return str1
