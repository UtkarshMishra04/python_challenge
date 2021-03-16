import unittest
from game_class import Game

class TestGameOfLife(unittest.TestCase):

    def setUp(self):

        print("################ Testing Class Initialization ###################")
        
        self.env = Game()
        
        print("################             Passed           ###################")

    def test_default_board_dimensions(self):

        print("################   Testing Board Dimensions   ###################")

        self.assertEqual(self.env.width, 40)
        self.assertEqual(self.env.height, 30)

        print("################             Passed           ###################")

    def test_get_neighbours(self):

        print("############### Testing Neighbour Call Function ###################")

        self.assertEqual(self.env.get_neighbours(2,2), [[1, 1], [1, 2], [1, 3], 
                                        [2, 1], [2, 3], [3, 1], [3, 2], [3, 3]])
        self.assertEqual(self.env.get_neighbours(0,0), [[0, 1], [1, 0], [1, 1]])
        self.assertEqual(self.env.get_neighbours(44,0), [])

        print("###############             Passed           ###################")

    def test_update_board(self):

        print("############### Testing Update Board Function ###################")

        for i in range(3):
            for j in range(3):
                self.env.board[i][j] = self.env.patterns["LWSpaceship"][i][j]
        self.env.update_board()
        self.assertEqual(self.env.board[0][1], 1)
        self.assertEqual(self.env.board[2][1], 0)
        self.assertEqual(self.env.board[2][0], 1)

        print("###############             Passed           ###################")
            
    def test_key_pressed(self):

        print("############### Testing Key Presses ###################")

        self.assertEqual(self.env.patterns[self.env.menu[ord('2')]], [[1, 1, 1], [1, 0, 1], 
                            [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1]])

        print("###############             Passed           ###################")
    

if __name__ == '__main__':
    unittest.main()