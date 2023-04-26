class Round:
    def __init__(self, round_num, name, start_date_time, end_date_time):
        self._round_num = round_num
        self._name = name
        self._start_date_time = start_date_time
        self._end_date_time = end_date_time

    # Getters
    def get_round_num(self):
        return self._round_num

    def get_name(self):
        return self._name

    def get_start_date_time(self):
        return self._start_date_time

    def get_end_date_time(self):
        return self._end_date_time

    # Setters
    def set_round_num(self, round_num):
        self._round_num = round_num

    def set_name(self, name):
        self._name = name

    def set_start_date_time(self, start_date_time):
        self._start_date_time = start_date_time

    def set_end_date_time(self, end_date_time):
        self._end_date_time = end_date_time
