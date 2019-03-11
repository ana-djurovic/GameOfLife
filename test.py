import copy
import unittest

from logicalgrid import LogicalGrid


class LogicalGridTest(unittest.TestCase):

    def test_no_living_neighbourg(self):
        self.assertEqual(logicalgrid_t.count_neighbours(1, 1), 0)

    def test_one_living_neighbourg(self):
        self.assertEqual(logicalgrid_t.count_neighbours(2, 4), 1)

    def test_two_living_neighbourgs(self):
        self.assertEqual(logicalgrid_t.count_neighbours(3, 4), 2)

    def test_three_living_neighbourgs(self):
        self.assertEqual(logicalgrid_t.count_neighbours(4, 3), 3)

    def test_four_living_neighbourgs(self):
        self.assertEqual(logicalgrid_t.count_neighbours(3, 2), 4)

    def test_five_living_neighbourgs(self):
        self.assertEqual(logicalgrid_t.count_neighbours(4, 2), 5)

    def test_six_living_neighbourgs(self):
        self.assertEqual(logicalgrid_t.count_neighbours(5, 1), 6)

    def test_seven_living_neighbourgs(self):
        self.assertEqual(logicalgrid_t.count_neighbours(9, 3), 7)

    def test_six_living_neighbourgs(self):
        self.assertEqual(logicalgrid_t.count_neighbours(9, 2), 8)

    def test_update_alive_cell_with_one_neighbourg(self):
        update_data = copy.deepcopy(logicalgrid_t.datas)
        logicalgrid_t.update_alive_cell(1, 1, update_data)
        self.assertEqual(update_data[1][1], '.')

    def test_update_alive_cell_with_four_neighbourgs(self):
        update_data = copy.deepcopy(logicalgrid_t.datas)
        logicalgrid_t.update_alive_cell(1, 2, update_data)
        self.assertEqual(update_data[1][2], '.')

    def test_update_alive_cell_with_two_neighbourgs(self):
        update_data = copy.deepcopy(logicalgrid_t.datas)
        logicalgrid_t.update_alive_cell(3, 4, update_data)
        self.assertNotEqual(update_data[3][4], '.')

    def test_update_alive_cell_with_three_neighbourgs(self):
        update_data = copy.deepcopy(logicalgrid_t.datas)
        logicalgrid_t.update_alive_cell(4, 3, update_data)
        self.assertNotEqual(update_data[4][3], '.')

    def test_update_dead_cell_with_three_neighbourgs(self):
        update_data = copy.deepcopy(logicalgrid_t.datas)
        logicalgrid_t.update_dead_cell(2, 2, update_data)
        self.assertEqual(update_data[2][2], '*')

    def test_update_dead_cell_with_no_neighbourg(self):
        update_data = copy.deepcopy(logicalgrid_t.datas)
        logicalgrid_t.update_dead_cell(0, 6, update_data)
        self.assertNotEqual(update_data[0][6], '*')

    def test_update_dead_cell_with_one_neighbourg(self):
        update_data = copy.deepcopy(logicalgrid_t.datas)
        logicalgrid_t.update_dead_cell(0, 0, update_data)
        self.assertNotEqual(update_data[0][0], '*')

    def test_update_dead_cell_with_two_neighbourgs(self):
        update_data = copy.deepcopy(logicalgrid_t.datas)
        logicalgrid_t.update_dead_cell(2, 5, update_data)
        self.assertNotEqual(update_data[5][2], '*')

    def test_update_dead_cell_with_four_neighbourgs(self):
        update_data = copy.deepcopy(logicalgrid_t.datas)
        logicalgrid_t.update_dead_cell(2, 5, update_data)
        self.assertNotEqual(update_data[2][5], '*')

if __name__ == "__main__":
    logicalgrid_t = LogicalGrid()
    logicalgrid_t.enter_json_file ='test.json'
    logicalgrid_t.read_file_case()
    unittest.main()
