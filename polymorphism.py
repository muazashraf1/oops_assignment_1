# Problem Set 5: Polymorphism (2 Problems)
# Problem 5.1: Media Player System
# Scenario:
# Create a media player that can play different types of media files using polymorphism.
# Requirements:
# Create a base class MediaFile with abstract method play()
# Create classes: AudioFile , VideoFile , and ImageFile that inherit from MediaFile
# Each class should implement play() differently:
# AudioFile : Print "Playing audio: [filename]"
# VideoFile : Print "Playing video: [filename]"
# ImageFile : Print "Displaying image: [filename]"
# Create a MediaPlayer class with a method play_media(media_file) that accepts any MediaFile object
# Create a list containing different media types and play them all using a loop
# Demonstrate that the same play() method call produces different behaviors



from abc import ABC, abstractmethod


class MediaFile(ABC):
    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def play(self):
        pass


class AudioFile(MediaFile):
    def play(self):
        print(f"Playing audio: {self.filename}")


class VideoFile(MediaFile):
    def play(self):
        print(f"Playing video: {self.filename}")


class ImageFile(MediaFile):
    def play(self):
        print(f"Displaying image: {self.filename}")


class MediaPlayer:
    def play_media(self, media_file):
        media_file.play()



media_list = [
    AudioFile("song.mp3"),
    VideoFile("movie.mp4"),
    ImageFile("photo.jpg")
]

player = MediaPlayer()

for media in media_list:
    player.play_media(media)




# Problem 5.2: Animal Sound System
# Scenario:
# Create an animal system where different animals make different sounds, demonstrating polymorphism.
# Requirements:
# Create a base class Animal with method make_sound() that prints "Some generic animal sound"
# Create classes: Dog , Cat , Cow , and Duck that inherit from Animal
# Override make_sound() in each class:
# Dog : "Woof!"
# Cat : "Meow!"
# Cow : "Moo!"
# Duck : "Quack!"
# Create a function animal_concert(animals) that takes a list of animals and makes each one produce its sound
# Create a list with one of each animal type and call animal_concert()
# Demonstrate that the same method call ( make_sound() ) produces different outputs based on the object type


class Animal:
    def make_sound(self):
        print("Some generic animal sound")


class Dog(Animal):
    def make_sound(self):
        print("Woof!")


class Cat(Animal):
    def make_sound(self):
        print("Meow!")


class Cow(Animal):
    def make_sound(self):
        print("Moo!")


class Duck(Animal):
    def make_sound(self):
        print("Quack!")


def animal_concert(animals):
    for animal in animals:
        animal.make_sound()



animals = [
    Dog(),
    Cat(),
    Cow(),
    Duck()
]

animal_concert(animals)
