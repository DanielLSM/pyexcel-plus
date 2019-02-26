import pandas as pd
from pyexcelp import file_input, file_output

fi = pd.read_excel(open(file_input, 'rb'))