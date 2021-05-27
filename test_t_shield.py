import SHIELD
import unittest
from unittest.mock import patch
from unittest import TestCase

class Test_SHIELD(unittest.TestCase):        
        
    @patch('builtins.input', side_effect=[1, 2, 'Black Widow, Hawkeye',' Get the Hulk back','Hulk has gone underground again, find him and bring him back.',
                                             2,'Thor, Hawkeye','Find the Space Infinity Stone','Loki has stolen the Space Infinity Stone which needs to be captured',
                                             2,'Hawkeye, Iron Man','Save New York','The Chitauri Army has taken over the city',
                                             1,
                                             3,'Get the Hulk back',
                                             4,'Iron Man',
                                             5,'Get the Hulk back','Completed',
                                             1,
                                             6,
                                             7,'Iron Man','Find the Space Infinity Stone'])


    def test_for_misson_set(self,mock_input):
        Captain=SHIELD.Avenger('Captain Fury') 

        self.assertEqual(Captain.initialize(), 'No mission has been assigned yet.')
        
        self.assertEqual(Captain.initialize(), 'Mission has been assigned to Black Widow and Hawkeye \n Email or SMS notification has been sent')

        self.assertEqual(Captain.initialize(), 'Mission has been assigned to Thor and Hawkeye \n Email or SMS notification has been sent')

        self.assertEqual(Captain.initialize(), 'Sorry,Hawkeye has already working on two missions')

        self.assertEqual(Captain.initialize(),  ['Get the Hulk back', 'Assigned', ['Black Widow', 'Hawkeye'],'Find the Space Infinity Stone', 'Assigned',['Thor','Hawkeye']])

        self.assertEqual(Captain.initialize(), "Mission: details:['Hulk has gone underground again, find him and bring him back.']\n Mission status: Assigned\n Avengers:['Black Widow', 'Hawkeye']")

        self.assertEqual(Captain.initialize(), 'Person Name:Tony Stark \n Abilities:Highly intelligent suit of armour \n Missions Assigned:0 \n Missions Completed:0')

        self.assertEqual(Captain.initialize(), 'Email and SMS are sent to Black Widow and Hawkeye')

        self.assertEqual(Captain.initialize(), ['Get the Hulk back', 'Completed', ['Black Widow', 'Hawkeye'],'Find the Space Infinity Stone', 'Assigned',['Thor','Hawkeye']])

        self.assertEqual(Captain.initialize(), ['Captain America', 'Available', 
                                                'Black Widow','On Mission',['Get the Hulk back'],
                                                'Hawkeye','On Mission',['Get the Hulk back', 'Find the Space Infinity Stone'],
                                                'Thor','On Mission',['Find the Space Infinity Stone'],
                                                'Hulk','Available',
                                                'Iron Man','Available'])

        self.assertEqual(Captain.initialize(), 'Thor and Hawkeye are already working on this mission')




if __name__=='__main__':
    pass