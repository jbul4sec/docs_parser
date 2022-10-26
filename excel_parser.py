"""
https://www.tutorialspoint.com/python_data_science/python_processing_xls_data.htm
https://pandas.pydata.org/docs/user_guide/io.html#io-excel


testing path
../../Documents/ОУД_СБПэй/20220830_ОУД4_СБПэй/eKassir-NSPK-SBPay-Monitoring.xlsx
../../Documents/ОУД_СБПэй/20220830_ОУД4_СБПэй/SBPay Android_version 1_0_14.xlsx
"""

import pandas as pd

data = pd.read_excel('../../Documents/ОУД_СБПэй/20220830_ОУД4_СБПэй/SBPay Android_version 1_0_14.xlsx',
                     usecols="A:E")
print(type(data.columns.values))
print(data.columns.values)
print(data)
print(', '.join(data.columns.values))


# print(type(data))


def return_dataframe(file_name: str):
    return pd.read_excel(file_name, usecols="A:I")
