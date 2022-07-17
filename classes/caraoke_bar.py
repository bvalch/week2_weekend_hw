from classes.guest import Guest
from classes.room import Room
class CaraokeBar:
    def __init__(self,name,till):
        self.name=name
        self.till=till


    def room_capacity_check(self,guest_list,room):
        if len(guest_list)<=room.capacity:
            return 'Can fit'
        else:
            return "Cant fit"
        
    def move_guests_to_appropriate_room(self,room_list,guest_list):
        for room in room_list:
            if len(guest_list) == room.capacity:
                room.add_multiple_guests(guest_list)


    def get_fav_song(self,guest_list,room,song):
        guest_fav_song_list=[]
        for guest in guest_list:
             guest_fav_song_list.append(guest.favorite_song)
        for item in guest_fav_song_list:
            if item==song.name:
                room.song_list.append(item)
        return room.song_list[-1]
        
    def guests_split_bill(self,guest_list,room):
        for guest in guest_list:
            guest.wallet-=(room.fee/3)
        self.till+=room.fee
