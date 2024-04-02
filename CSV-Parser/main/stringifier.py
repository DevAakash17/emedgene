
from typing import List


class Strigifier:

    def __init__(self, val = None):
        self.data = val

    def convert_to_write_format(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                if '"' in self.data[i][j]:
                    self.data[i][j] = self.data[i][j].replace('"', '""')

                if "," in self.data[i][j] or '"' in self.data[i][j]:
                    self.data[i][j] = '"' + self.data[i][j] + '"'

    def write_data_to_csv(self, path):
        with open(path, "w") as file:
            for line in self.data:
                temp = ",".join(line)
                file.write(f"{temp}\n")


def testcase_1():
    data = [['Name', 'Email', 'Phone Number', 'Address'],
            ['Bob Smith', 'bob@example.com', '123-456-7890', '123 Fake Street'],
            ['Mike Jones', 'mike@example.com', '098-765-4321', '321, Fake B Avenue']]
    obj = Strigifier(data)
    obj.convert_to_write_format()
    obj.write_data_to_csv("stringifier_write_1")
    print("testcase 1 passed")


def testcase_2():
    data = [['Name', 'Email', 'Phone Number', 'Address'], ['Bob Smith', 'bob@example.com', '123-456-7890', '123 Fake Street'], ['Jack "B" Jones', 'mike@example.com', '098-765-4321', '321, Fake "B" Avenue']]
    obj = Strigifier(data)
    obj.convert_to_write_format()
    obj.write_data_to_csv("stringifier_write_2")
    print("testcase 2 passed")


if __name__ == "__main__":
    testcase_1()
    testcase_2()