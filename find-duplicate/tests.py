from option1 import findDuplicate1, findDuplicate2
import random
import unittest

class TestFindDuplicates(unittest.TestCase):
    def test_small_list1(self):
        list = [6, 3, 5, 4, 3, 2, 1]
        assert findDuplicate1(list) == 3 and findDuplicate2(list) == 3

    def test_small_list2(self):
        list = [6, 3, 5, 4, 7, 2, 1, 9, 10, 8, 10]
        assert findDuplicate1(list) == 10 and findDuplicate2(list) == 10

    def test_small_list3(self):
        list = [1, 7, 6, 3, 8, 9, 10, 11, 5, 4, 16, 12, 2, 1, 14, 13, 17, 15]
        assert findDuplicate1(list) == 1 and findDuplicate2(list) == 1

    def test_large_list1(self):
        list = [i for i in range(10000)]
        list.append(1234)
        random.shuffle(list)
        assert findDuplicate1(list) == 1234 and findDuplicate2(list) == 1234

    def test_large_list2(self):
        list = [i for i in range(100000)]
        list.append(98765)
        random.shuffle(list)
        assert findDuplicate1(list) == 98765 and findDuplicate2(list) == 98765

    def test_large_list3(self):
        list = [i for i in range(5000000)]
        list.append(555555)
        random.shuffle(list)
        assert findDuplicate1(list) == 555555 and findDuplicate2(list) == 555555

    def test_only_duplicates(self):
        list = [1, 1]
        assert findDuplicate1(list) == 1 and findDuplicate2(list) == 1

    def test_small_duplicates_at_start(self):
        list = [3, 3, 2, 1, 4]
        assert findDuplicate1(list) == 3 and findDuplicate2(list) == 3

    def test_small_duplicates_at_end(self):
        list = [1, 2, 4, 3, 5, 6, 6]
        assert findDuplicate1(list) == 6 and findDuplicate2(list) == 6

    def test_small_duplicates_start_and_end(self):
        list = [2, 1, 3, 4, 7, 6, 8, 2]
        assert findDuplicate1(list) == 2 and findDuplicate2(list) == 2

    def test_small_duplicates_in_middle(self):
        list = [1, 2, 6, 8, 9, 5, 6, 7, 3, 4]
        assert findDuplicate1(list) == 6 and findDuplicate2(list) == 6

    def test_large_duplicates_at_start(self):
        list = [i for i in range(100000)]
        random.shuffle(list)
        duplicate_value = list[0]
        list.insert(0, duplicate_value)
        assert findDuplicate1(list) == duplicate_value and findDuplicate2(list) == duplicate_value

    def test_large_duplicates_at_end(self):
        list = [i for i in range(100000)]
        random.shuffle(list)
        duplicate_value = list[-1]
        list.append(duplicate_value)
        assert findDuplicate1(list) == duplicate_value and findDuplicate2(list) == duplicate_value

    def test_large_duplicates_start_and_end(self):
        list = [i for i in range(100000)]
        random.shuffle(list)
        duplicate_value = list[0]
        list.append(duplicate_value)
        assert findDuplicate1(list) == duplicate_value and findDuplicate2(list) == duplicate_value

    def test_large_duplicates_in_middle(self):
        list = [i for i in range(100000)]
        random.shuffle(list)
        duplicate_value = list[87654]
        list.insert(54321, duplicate_value)
        assert findDuplicate1(list) == duplicate_value and findDuplicate2(list) == duplicate_value

if __name__ == '__main__':
    unittest.main()
