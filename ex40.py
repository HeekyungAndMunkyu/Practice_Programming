# -*- coding: utf-8 -*-

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
        print type(self)

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

    def sing_me_twice(self):
        for line in self.lyrics:
            print line
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday",
    "Since I don\'t want to be sued",
    "I'll stop here."])

bulls_on_parade = Song(["With bags full of shells",
    "they gathered around the family."])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

oh_happy_day = Song(["Oh!",
    "Happy",
    "day!"])

oh_happy_day.sing_me_a_song()
print type(oh_happy_day)

oh_happy_day.sing_me_twice()

newLyrics = ["1", "2", "3"]

number_song = Song(newLyrics)

number_song.sing_me_a_song()
