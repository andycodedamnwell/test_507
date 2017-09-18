
# Do not change import statements.
import unittest
from SI507F17_project1_cards import *

# Write your unit tests to test the cards code here.
# You should test to ensure that everything explained in
# the code description file works as that file says.
# If you have correctly written the tests, at least 3 tests should fail.
# If more than 3 tests fail, it should be because multiple of the test
# methods address the same problem in the code.
# You may write as many TestSuite subclasses as you like, but you should try
# to make these tests well-organized and easy to read the output.
# You should invoke the tests with verbosity=2 (make sure you invoke them!)

class ClassTests(unittest.TestCase):   
    def setUp(self):
        self.card = Card()

    def test_Suit_Type(self):
        self.assertEqual(type(self.card.suit_names), type([]))       

    def test_SuitContains(self):
        lists = ["Diamonds", "Clubs", "Hearts", "Spades"]
        self.assertListEqual(lists, self.card.suit_names)       

    def test_len(self):
        self.assertTrue(self.card.suit_names)
        self.assertTrue(self.card.rank_levels)
        self.assertTrue(self.card.faces)

#   Rank tests        
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
#            print(item)
            self.assertEqual(item, i+1)
            i += 1

#   These are the test for the Faces

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

    def test_RankTotal(self):
        total = 6227020800
        factorial = 1
        for item in self.card.rank_levels:
            factorial = factorial * item           
        self.assertEqual(total, factorial)

    def test_SelfSuitisStrinandSuit(self):
        if self.card.suit == "Diamond":
            pass
        elif self.card.suit == "Clubs":
            pass
        elif self.card.suit == "Hearts":
            pass
        elif self.card.suit == "Spades":
            pass
        else:
            self.assertRaises(ValueError)               

    def test_SelfRank(self):
        if self.card.rank_levels == 11:
            self.assertEqual(self.card.rank, "Jack")
        elif self.card.rank_levels == 12:
            self.assertEqual(self.card.rank, "Queen")
        elif self.card.rank_levels == 13:
            self.assertEqual(self.card.rank, "King")
        elif self.card.rank_levels == 1:
            self.assertEqual(self.card.rank, "Ace")
        else:
            pass       

    def test_SelfRanNum(self):
        self.assertEqual(type(self.card.rank_num), int)       

    def test_SelfTanNumRange(self):
        self.assertIn(self.card.rank_num, range(1,14))

    def testSDefaultConstructor(self):
        card2 = str(self.card.rank_num)
#       print(card2)
        self.assertEqual(type(str(self.card)), str)

    def test_strClass(self): # BUG1
        for n in range(4):
            for k in range(1,14):
                self.card = Card(n, k) 
#               print(str(self.card))
        Test = Card(3, 13)
        self.assertEqual(str(Test), "Ace of Spades")


class DeckTest(unittest.TestCase):

    def setUp(self):
            self.deck = Deck()
            self.card = Card()

    def test_Consructor_Test(self):
        self.assertRaises(TypeError, Deck(0))

    def test_DeckCreatsList(self):
        self.assertEqual(type(self.deck.cards), type([]))     

    def test_cardsInstanceinDeck(self):
        for item in self.deck.cards:
            self.assertIsInstance(item, Card)

    def test_DeckSize(self):
        self.assertEqual(len(self.deck.cards), 52)

    def test_DeckRanks(self):
        self.assertEqual(len(self.deck.cards), 52)

    def test_CardInstance(self):
#        print(type(Deck))
#        print(type(Card))
#        print(type(self.deck.cards))
        self.assertIsInstance(self.deck, Deck)       

    def test_DeckHasAll(self):
        for i in range(13):           
            if self.deck.cards[i].rank == "Ace":
                self.assertIn(self.deck.cards[i].rank_num, range(1,14))               
            elif self.deck.cards[i].rank == "Jack":
                self.assertIn(self.deck.cards[i].rank_num, range(1,14))
            elif self.deck.cards[i].rank == "Queen":
                self.assertIn(self.deck.cards[i].rank_num, range(1,14))
            elif self.deck.cards[i].rank == "King":
                self.assertIn(self.deck.cards[i].rank_num, range(1,14))               
            else:
                self.assertIn(self.deck.cards[i].rank, range(1,14))

    def test_instanceoeach(self):
        for i in range(52):
            if self.deck.cards[i].suit == "Ace":
                i = 0
                for i in range(13):
                    self.assertTrue(self.deck.cards[i].rank, i)

    def test_something(self):
        deck = str(self.deck)
        split = deck.split("\n")
        self.assertEqual(52, len(split))
#       deck3 = self.deck
#       deck2 = random.shuffle(deck3)
#       deck4 = str(deck2)
#       print(deck)#BUG BUG BUG BUG
#       print(type(self.deck.cards))
#       print(deck4)

    def test_ifitprintsAce(self):
        deck = str(self.deck)
        split = deck.split("\n")
        self.assertEqual(52, len(split))       

    def test_equivalenceinTest(self): # BUG2 (due to the same reason maybe?
        self.assertEqual(str(self.deck.cards[0]),"Ace of Diamonds")                        

    def test_typeofPop_cardDefault(self):
        card = self.deck.pop_card()
#        print(str(card))       

    def test_typeofPop_cardInteger(self):
        card = self.deck.pop_card(2)
#       print(str(card))

    def test_Popall(self):
        for i in range(52):
            self.deck.pop_card()
#            print(len(self.deck.cards))
#       self.assertRaises(IndexError, self.deck.pop_card())

    def test_methodReplace(self):
        deck = self.deck.shuffle()
        listOne = Deck()
        listingOne = str(listOne)
        splitOne = listingOne.split("\n")
        listingTwo = str(self.deck)
        splitTwo = listingTwo.split("\n")
        self.assertNotEqual(splitOne, splitTwo)

    def test_method_replace(self):
#       for i in range(52):
#           self.assertIsInstance(self.card, Card)
        deck = self.deck
        listOne = Deck()
        listingOne = str(listOne)
        splitOne = listingOne.split("\n")
#       print(len(splitOne))
        listingTwo = str(self.deck)
        splitTwo = listingTwo.split("\n")
        self.assertEqual(splitOne, splitTwo)
        self.card = Card(0,4)
        self.deck.replace_card(self.card)
        listingThree = str(self.deck)
        splitThree = listingThree.split("\n")
#       print(len(splitThree))
#       print(len(splitOne))
        self.assertEqual(len(splitThree), len(splitOne))

    def tests_thatEveryCardIsInDeck(self):
        listingTwo = str(self.deck)
        splitTwo = listingTwo.split("\n")
        for i in range(4):
            for n in range(1,14):
                self.card = Card(i,n)
                self.assertIn(str(self.card), splitTwo)

    def test_method_ifCardOut(self):
        self.card = Card(3,13)      
        listingThree = str(self.deck)
        splitThree = listingThree.split("\n")
        popped_card = self.deck.pop_card()
        self.assertEqual(len(splitThree), len(self.deck.cards))

    def test_method_ifCardOut(self):      
        self.card = Card(1,13)      
        listingThree = str(self.deck)
        splitThree = listingThree.split("\n")   
        popped_card = self.deck.pop_card()
        self.deck.replace_card(self.card)
        self.assertNotEqual(len(splitThree), len(self.deck.cards))

    def test_methodJustFail(self):
        self.card = Card(1,13)
        self.deck.replace_card(self.card)
        self.deck.replace_card(self.card)

    def test_sort(self): #Bug3
        self.deck.pop_card()
        lenghtPopped = len(self.deck.cards)
        self.deck.shuffle()
        self.deck.sort_cards()
        lenghtSort = len(self.deck.cards)
        self.assertEqual(lenghtPopped, lenghtSort)       

    def test_deal(self): #BUG4
        for i in range(3):
            self.deck.pop_card()
        self.assertRaises(IndexError, self.deck.deal_hand(52))

    def test_Game(self):
        self.assertEqual(type(play_war_game("TRUE")), type(()))

    def test_GameTwo(self):
        Hand = play_war_game("TRUE")
        first = Hand[0]
        second = Hand[1]
        third = Hand[2]
        self.assertEqual(type(first), str) 
        while True:
            if first == "Player":
                break
            elif first == "Player2":
                break
            elif first == "Tie":
                break
            else:
                self.assertRaises(ValueError)
                break
        self.assertEqual(type(second), int)
        self.assertEqual(type(third), int)

    def test_showSong(self):
        song = show_song()
        self.assertIsInstance(song, helper_functions.Song)
               
if __name__ == "__main__":
    unittest.main(verbosity=2)
