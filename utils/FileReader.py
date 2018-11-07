"""
File Reader class
Read the <csv> file get the data in the form of rows
"""

import csv


class FileReader(object):
    """ Read the <csv> file get the data in the form of rows """

    def __init__(self, filename):
        self.filename = filename
        self.rows = self.get_rows()

    def get_rows(self):
        """
        return rows of a given csv file
        """
        rows = []
        with open(self.filename, "r") as f:
            csvreader = csv.reader(f)
            # ignore the first naming data
            next(csvreader)
            for row in csvreader:
                rows.append(row)
        return rows

    def __repr__(self):
        return "Returns a list of rows in the given {} name".format(self.filename)

    def __str__(self):
        return "Returns a list of rows in the given {} name".format(self.filename)
