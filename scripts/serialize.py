import pandas as pd
from pyexcelp import file_input, file_output
from collections import OrderedDict, defaultdict

# records = pe.iget_records(file_name=file_input)
# fi = pd.read_excel(file_input)


class Cchecks:

    def __init__(self, file_name=file_input, *args, **kwargs):
        self.book = pd.read_excel(
            file_input, sheet_name=None)  # returns an ordered dict

        self.ccheck_sheet = self.book['C_Initial']

    #     self.aircraft_info = self._serialize_to_aircraft()

    # def _serialize_to_aircraft(self):
    #     """ returns a dict of aircraft_id:info """
    #     aircraft_info = OrderedDict()
    #     keys = self.ccheck_sheet.keys()
    #     for _ in self.ccheck_sheet['Aircraft_ID']:
    #         aircraft_info[_] = OrderedDict()

    #     return aircraft_info
