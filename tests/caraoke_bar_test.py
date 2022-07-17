import unittest
from classes.caraoke_bar import CaraokeBar
from classes.guest import Guest
from classes.room   import Room
from classes.song import Song

class TestCaraokebarTest(unittest.TestCase):
    def setUp(self):
        self.careoke_bar_1=CaraokeBar('CCCB',100)
        self.room_1=Room('room1',2,10)
        self.room_2=Room('room2',3,15)
        self.guest_1=Guest('Joe',10,'song_name_1')
        self.guest_2=Guest('Jane',20,'song_name_2')
        self.guest_3=Guest('Jill',30,'song_name_3')
        self.song_1=Song('song_name_1')
        self.guest_list2=[self.guest_1,self.guest_2]
        self.guest_list3=[self.guest_1,self.guest_2,self.guest_3]
        self.room_list2=[self.room_1,self.room_2]


# instance attributes test
    def test_bar_has_name(self):
        self.assertEqual('CCCB',self.careoke_bar_1.name)
    def test_bar_has_till(self):
        self.assertEqual(100,self.careoke_bar_1.till)
    def test_guest_has_name(self):
        self.assertEqual('Joe',self.guest_1.name)
    def test_guest_has_money(self):
        self.assertEqual(10,self.guest_1.wallet)
    def test_guest_has_fav_song(self):
        self.assertEqual('song_name_1',self.guest_1.favorite_song)
# functionality tests
    def test_add__song_in_room_list(self):
        self.room_1.add_song(self.song_1)
        self.assertEqual(1,len(self.room_1.song_list))

    def test_guest_happy_about_song(self):
        self.room_1.add_song(self.song_1)
        self.assertEqual('Woohoo',self.guest_1.happy_guest(self.room_1,self.guest_1,))
    
    def test_add_guest_to_room(self):
        self.room_1.add_guest(self.guest_1)
        self.assertEqual('Joe',self.room_1.guest_list[0])

    def test_add_multiple_guests_to_room(self):
        self.room_1.add_multiple_guests(self.guest_list2)
        self.assertEqual(['Joe','Jane'],self.room_1.guest_list)

    def test_remove_guests_from_room(self):
        
        self.room_1.remove_guests_from_room(self.guest_list2)
        self.assertEqual(0,len(self.room_1.guest_list))
    
    def test_room_capacity_can_fit(self):
        room=self.room_1
        self.assertEqual('Can fit',self.careoke_bar_1.room_capacity_check(self.guest_list2,room))

    def test_room_capacity_cant_fit(self):
        self.careoke_bar_1.room_capacity_check(self.guest_list3,self.room_1)
        self.assertEqual('Cant fit',self.careoke_bar_1.room_capacity_check(self.guest_list3,self.room_1))

    def test_move_guests_to_appropriate_room(self):
        self.careoke_bar_1.move_guests_to_appropriate_room(self.room_list2,self.guest_list3)
        self.assertEqual(3, len(self.room_2.guest_list))

    def test_put_song_in_room_if_guest_has_fav_song(self):
        self.get_fav_song=(self,self.guest_list3,self.room_1,self.song_1)
        self.assertEqual('song_name_1',self.careoke_bar_1.get_fav_song(self.guest_list3,self.room_1,self.song_1))
    
    def test_guests_pay_for_room(self):
        self.careoke_bar_1.guests_split_bill(self.guest_list3,self.room_2)
        self.assertEqual(5,self.guest_1.wallet)
        self.assertEqual(15,self.guest_2.wallet)
        self.assertEqual(25,self.guest_3.wallet)
        self.assertEqual(115,self.careoke_bar_1.till)

