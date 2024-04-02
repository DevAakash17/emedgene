

from typing import List


class Parser:

    def __init__(self):
        self.data = None

    def read_csv(self, path):
        data = []
        with open(path) as f:
            data = f.readlines()
        for i, val in enumerate(data):
            data[i] = val.rstrip('\n')
        return data

    def parse_data(self, data: str) -> List[str]:
        l, r = 0, 0
        result = []
        keep_reading = False
        while r < len(data):
            if data[r] == '"' and r+1 < len(data) and data[r+1] == '"':
                r += 2
                continue
            elif keep_reading and data[r] == '"':
                result.append(data[l:r].replace('""', '"'))
                l = r + 1
                keep_reading = False
            elif data[r] == '"' and not keep_reading:
                keep_reading = True
                l += 1
                r = l
            elif data[r] == "," and not keep_reading:
                if l != r:
                    result.append(data[l:r].replace('""', '"'))
                l = r+1

            r += 1
        if l < len(data):
            result.append(data[l:])
        return result

    def main(self, path: str) -> List[List[str]]:
        result = []
        data_lines = self.read_csv(path)
        for data in data_lines:
            temp = self.parse_data(data)
            result.append(temp)
        return result


def testcase_1():
    obj = Parser()
    assert obj.main("1.csv") == [['Name', 'Email', 'Phone Number', 'Address'], ['Bob Smith', 'bob@example.com', '123-456-7890', '123 Fake Street'], ['Mike Jones', 'mike@example.com', '098-765-4321', '321 Fake Avenue']]
    print("testcase 1 passed")


def testcase_2():
    obj = Parser()
    assert obj.main("2.csv") == [['Name', 'Email', 'Phone Number', 'Address'], ['Bob Smith', 'bob@example.com', '123-456-7890', '123 Fake Street'], ['Mike Jones', 'mike@example.com', '098-765-4321', '321 Fake Avenue']]
    print("testcase 2 passed")


def testcase_3():
    obj = Parser()
    assert obj.main("3.csv") == [['Name', 'Email', 'Phone Number', 'Address'], ['Bob Smith', 'bob@example.com', '123-456-7890', '123 Fake Street'], ['Mike Jones', 'mike@example.com', '098-765-4321', '321, Fake "B" Avenue']]
    print("testcase 3 passed")


def testcase_4():
    obj = Parser()
    assert obj.main("4.csv") == [['Name', 'Email', 'Phone Number', 'Address'], ['Bob Smith', 'bob@example.com', '123-456-7890', '123 Fake Street'], ['Jack "B" Jones', 'mike@example.com', '098-765-4321', '321, Fake "B" Avenue']]
    print("testcase 4 passed")


def testcase_5():
    obj = Parser()
    assert obj.main("5.csv") == [['Name', 'Email', 'Phone Number', 'Address'], ['Bob Smith', 'bob@example.com', '123-456-7890', '123 Fake Street'], ['Mike Jones', 'mike@example.com', '098-765-4321', '321, Fake B Avenue']]
    print("testcase 5 passed")


if __name__ == "__main__":
    testcase_1()
    testcase_2()
    testcase_3()
    testcase_4()
    testcase_5()
