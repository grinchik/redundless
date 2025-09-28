import unittest

from high_level_directory_path_group_list import high_level_directory_path_group_list

class TestSubTreeRootList(unittest.TestCase):
    def test_multiple_duplicates_same_level(self):
        directory_path_list_by_file_entry_set_dict = {
            frozenset([
                ('A', 0, '1/2/a'),
                ('A', 0, '1/2/a'),
                ('A', 0, '1/2/a'),
            ]): [
                '/2',
                '/3',
                '/0',
            ],
            frozenset([
                ('A', 0, '2/a'),
                ('A', 0, '2/a'),
                ('A', 0, '2/a'),
            ]): [
                '/2/1',
                '/3/1',
                '/0/1',
            ],
            frozenset([
                ('A', 0, 'a'),
                ('A', 0, 'a'),
                ('A', 0, 'a'),
            ]): [
                '/2/1/2',
                '/3/1/2',
                '/0/1/2',
            ],
        }

        expected_result = [
            [
                '/2',
                '/3',
                '/0',
            ],
        ]

        result = high_level_directory_path_group_list(
            directory_path_list_by_file_entry_set_dict,
            )

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
