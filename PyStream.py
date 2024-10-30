from vidstream import *
import tkinter as tk
import socket
import threading
import requests
local_ip_address=socket.gethostbyname(socket.gethostname())
server= StreamingServer(local_ip_address, 9999)
receiver=AudioReceiver(local_ip_address, 8888)
def start_listening():
    t1=threading.Thread(target=server.start_server)
    t2=threading.Thread(target=receiver.start_server)
    t1.start()
    t2.start()
def start_camera():
    cam_client=CameraClient(text_target_ip.get(1.0,'end-1c'), 7777)
    t3=threading.Thread(target=cam_client.start_stream)
    t3.start()
def start_screen():
    screen_client=ScreenShareClient(text_target_ip.get(1.0,'end-1c'), 7777)
    t4=threading.Thread(target=screen_client.start_stream)
    t4.start()
def start_audio():
    audio_sender=AudioSender(text_target_ip.get(1.0,'end-1c'), 6666)
    t5=threading.Thread(target=audio_sender.start_stream)
    t5.start()

#print(local_ip_address)
#GUI
window=tk.Tk()
window.title("PyStream Trial")
window.geometry('400x300')
label_target_ip=tk.Label(window, text="Target IP")
label_target_ip.pack()
text_target_ip=tk.Text(window, height=1)
text_target_ip.pack()
btn_listen=tk.Button(window, text="Start Listening", width=50, command=start_listening)
btn_listen.pack(anchor=tk.CENTER, expand=True)
btn_vid=tk.Button(window, text="Start Video", width=50, command=start_camera)
btn_vid.pack(anchor=tk.CENTER, expand=True)
btn_share=tk.Button(window, text="Start Screen Share", width=50, command=start_screen)
btn_share.pack(anchor=tk.CENTER, expand=True)
btn_audio=tk.Button(window, text="Start Audio", width=50, command=start_audio)
btn_audio.pack(anchor=tk.CENTER, expand=True)
window.mainloop()
