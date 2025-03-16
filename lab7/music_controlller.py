from tkinter import Tk, Button
import os
import pygame
from pygame import mixer

mixer.init()

MUSIC_FOLDER = "music"  
music_files = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]

current_track = 0 

def play_music():
    global current_track
    track_path = os.path.join(MUSIC_FOLDER, music_files[current_track])
    mixer.music.load(track_path)
    mixer.music.play()
    print(f"Playing now: {music_files[current_track]}")

def play_song():
    if not mixer.music.get_busy(): 
        play_music()

def stop_song():
    mixer.music.stop()

def next_song():
    global current_track
    current_track = (current_track + 1) % len(music_files) 
    play_music()

def previous_song():
    global current_track
    current_track = (current_track - 1) % len(music_files) 
    play_music()

def key_press(event):
    if event.keysym == "space":
        play_song()
    elif event.keysym == "s":
        stop_song()
    elif event.keysym == "Right":
        next_song()
    elif event.keysym == "Left":
        previous_song()

window = Tk()
window.bind("<KeyPress>", key_press) 
window.withdraw()
window.mainloop()
