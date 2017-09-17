## Do not change import statements.
import unittest
from SI507F17_project1_cards import *

## Write your unit tests to test the cards code here.
## You should test to ensure that everything explained in the code description file works as that file says.
## If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code.
## You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
## You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########

class ClassTests(unittest.TestCase):
    def setUp(self):
        self.card = Card()

    #These are the test for the Suit Names
    def test_Suit_Type(self):
        self.assertEqual(type(self.card.suit_names), type([]))
        

    #These are the test for the Rank
    def test_Rank_Type(self):
        self.assertEqual(type(self.card.rank_levels), type([]))
        
    def test_vRank_Integer(self):
        for item in self.card.rank_levels:
            self.assertEqual(type(item), type(1))
            
    def test_RankEqualsThirtheen(self):
        self.assertTrue(len(self.card.rank_levels), 13)
        
    def test_variable_count(self):
        i = 0
        for item in self.card.rank_levels:
            print(item)
            self.assertEqual(item, i+1)
            i += 1

    #These are the test for the Faces
    def test_faces(self):
        self.assertEqual(type(self.card.faces), type({}))
        
    def test_FacesKey(self):
        self.assertTrue(type(self.card.faces.keys()), int)
        
    def test_FacesValue(self):
        self.assertTrue(type(self.card.faces.values()), str)

    def test_FaceAceOnePair(self):
        self.assertTrue(self.card.faces[1], "Ace")
        
    def test_FaceJackEleven(self):
        self.assertTrue(self.card.faces[11], "Jack")
        
    def test_FaceQueenTweleve(self):
        self.assertTrue(self.card.faces[12], "Queen")
        
    def test_FaceKingThirteen(self):
        self.assertTrue(self.card.faces[13], "King")


    #Testing the class Card's constructor
    def testConstructorInput(self):
        list=["Diamonds", "Clubs", "Hearts", "Spades"]
        for n in range(4):
            for i in range(13):
                card = Card(n, i)

    def test_SelfSuitisStrinandSuit(self):
        self.assertEqual(self.card.suit, "Diamonds" or "Clubs" or "Hearts" or "Spades")

    def test_SelfRank(self):
        if self.card.rank == 11:
            self.assertEqual(self.card.rank, "Jack")
        elif self.card == 12:
            self.assertEqual(self.card.rank, "Queen")
        elif self.card.rank == 13:
            self.assertEqual(self.card.rank, "King")
        elif self.card.rank == 1:
            self.assertEqual(self.card.rank, "Ace")
        else:
            pass

    def test_SelfRanNum(self):
        self.assertTrue(type(self.card.rank_num), int)
        
    def test_SelfTanNumRange(self):
        self.assertTrue(self.card.rank_num, range(1,14))
        
    def testSDefaultConstructor(self):
        card2 = str(self.card.rank_num)
        print(card2)

    #def test_strClass(self):
       # for n in range(4):
       #     for k in range(1,14):
       #        self.card = Card(n, k) #Bug here, does list out Ace BUG BUG BUG BUG
       #        print(str(self.card))

                
class DeckTest(unittest.TestCase):
    
    def setUp(self):
            self.deck = Deck()


    def test_Consructor_Test(self):
        self.deck = Deck(0)
        self.assertRaises()

    def test_DeckCreatsList(self):
        self.assertEqual(type(self.deck.cards), type([]))

    def test_DeckSize(self):
        self.assertEqual(len(self.deck.cards), 52)

    def test_DeckRanks(self):
        self.assertEqual(len(self.deck.cards), 52)

    def test_DeckHasAll(self):
        self.assertEqual(self.deck.cards.rank, range(1,14))
            
        

    
                  
        # any setup code for this test method

        #def test_constructor_defaults(self):

        #def teatDown(self):
        
if __name__ == "__main__":
    unittest.main(verbosity=2)
