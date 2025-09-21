import unittest

from file_entry_list import file_entry_list

class TestMultipliedFileEntryByParentPath(unittest.TestCase):
    def test_root_level_single_file(self):
        line = '\t'.join([ 'A', str(0), '/a' ])
        actual_result = file_entry_list(line)
        expected_result = [
            ('/', ('A', 0, 'a')),
        ]
        self.assertEqual(actual_result, expected_result)

    def test_one_level_nested_single_file(self):
        line = '\t'.join([ 'A', str(0), '/0/a' ])
        actual_result = file_entry_list(line)
        expected_result = [
            ('/0', ('A', 0, 'a')),
            ('/', ('A', 0, '0/a')),
        ]
        self.assertEqual(actual_result, expected_result)

    def test_two_level_nested_single_file(self):
        line = '\t'.join([ 'A', str(0), '/0/0/a' ])
        actual_result = file_entry_list(line)
        expected_result = [
            ('/0/0', ('A', 0, 'a')),
            ('/0', ('A', 0, '0/a')),
            ('/', ('A', 0, '0/0/a')),
        ]
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()
