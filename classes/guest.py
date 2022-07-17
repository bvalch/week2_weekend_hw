from classes.room import Room
class Guest:
    def __init__(self,name,wallet,favorite_song):
        self.name=name
        self.wallet=wallet
        self.favorite_song=favorite_song
    
    def happy_guest(self,room,song):
        # self.room_1.add_song(self.song_1)
        if self.favorite_song in room.song_list:
            return 'Woohoo'
        