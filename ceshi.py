import tkinter as tk
import pygame

def play_music():
    pygame.mixer.music.load("D:/ai/9.wav")
    pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def resume_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

# 创建GUI窗口
window = tk.Tk()
window.title("音乐播放器")

# 创建进度条
progress_bar = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, length=200)
progress_bar.pack()

# 创建播放按钮
play_button = tk.Button(window, text="播放", command=play_music)
play_button.pack()

# 创建暂停按钮
pause_button = tk.Button(window, text="暂停", command=pause_music)
pause_button.pack()

# 创建继续按钮
resume_button = tk.Button(window, text="继续", command=resume_music)
resume_button.pack()

# 创建停止按钮
stop_button = tk.Button(window, text="停止", command=stop_music)
stop_button.pack()

# 初始化pygame
pygame.mixer.init()

# 启动GUI事件循环
window.mainloop()
