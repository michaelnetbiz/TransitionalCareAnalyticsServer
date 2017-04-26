# import csv
# from unittest.mock import MagicMock, patch
# from io import StringIO
#
#
# def get_csv_stub(*args, **kwargs):
#     with patch('StringIO.readlines') as m:
#         csvfile = m.return_value
#         with open('data/closeouts.csv', 'r') as f:
#             csvfile = f.read()
#             f.close()
#             return csvfile
#
#
# StringIO.readlines = MagicMock(side_effect=get_csv_stub)
