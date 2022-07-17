class Room:
    def __init__(self,name,capacity,fee):
        self.name=name
        self.capacity=capacity
        self.fee=fee
        self.song_list=[]
        self.guest_list=[]
        
    
    def add_song(self,song):
        self.song_list.append(song.name)

    def add_guest(self,guest):
        self.guest_list.append(guest.name)
    
    def add_multiple_guests(self,guest_list2):
        for guest in guest_list2:
            self.guest_list.append(guest.name)
    
    def remove_guests_from_room(self,guest_list):
        self.add_multiple_guests(guest_list)
        self.guest_list.clear()


    