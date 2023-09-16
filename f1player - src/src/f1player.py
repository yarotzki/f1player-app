from webbrowser import open as webbrowser_open
import os
import tkinter as tk
from time import sleep as time_sleep
from time import strftime as time_strftime
from time import gmtime as time_gmtime
from subprocess import CREATE_NO_WINDOW
try: 
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
except ModuleNotFoundError:
    os.system("pip install selenium")
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"]) 
chrome_service = Service(service_args = ["--disable-build-check", "--silent"])
chrome_service.creation_flags = CREATE_NO_WINDOW


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

def Get_Next_Session_Time():
    driver = webdriver.Chrome(service = chrome_service, options = chrome_options)
    driver.get("https://f1-countdown.com/")
    days = driver.find_element(By.XPATH, "/html/body/div/main/div[4]/div/div[1]/span[1]").text
    hours = driver.find_element(By.XPATH, "/html/body/div/main/div[4]/div/div[2]/span[1]").text
    mins = driver.find_element(By.XPATH, "/html/body/div/main/div[4]/div/div[3]/span[1]").text
    seconds = driver.find_element(By.XPATH, "/html/body/div/main/div[4]/div/div[4]/span[1]").text
    return [days, hours, mins, seconds]                     

def Install_AceStream(): 
    webbrowser_open("https://download.acestream.media/products/acestream-full/win/latest")
    downloads_path = os.path.join(os.path.expanduser('~'), 'downloads') #if install doesnt work, enter your downloads path here if you changed it from default
    setup_path = os.path.join(downloads_path, "Ace_Stream_Media_3.1.74.exe")#if install doesnt work, version number needs to be updated
    download_complete = os.path.exists(setup_path)
    while download_complete == False:
        download_complete = os.path.exists(setup_path)
        time_sleep(0.5) 
    os.startfile(setup_path)

def Play_SkySportsMainEvent():
    webbrowser_open("acestream://eab7aeef0218ce8b0752e596e4792b69eda4df5e")

def Play_SkySportsF1_Web():
    os.startfile("f1_stream_web.html")

def Play_SkySportsF1():
    driver = webdriver.Chrome(service = chrome_service, options = chrome_options)
    driver.get("https://acestreamid.com/channel/sky-sports-f1-uk")
    streamids = driver.find_elements(By.TAG_NAME, "li")
    idlist = []
    for s in streamids:
        idlist.append(s.text)
    idlist = "".join(idlist)
    idlist = idlist.split("\n")
    idlist = " ".join(idlist)
    idlist = idlist.split(" ")
    idlist.sort(key = len)
    templist = []
    for i in range(len(idlist) - 1):
        if len(idlist[i]) == 40:
            templist.append(idlist[i])
    idlist = templist       
    webbrowser_open("acestream://" + idlist[0])

def Play_SkySportsF1_ALT1():
    driver = webdriver.Chrome(service = chrome_service, options = chrome_options)
    driver.get("https://acestreamid.com/channel/sky-sports-f1")
    streamids = driver.find_elements(By.TAG_NAME, "li")
    idlist = []
    for s in streamids:
        idlist.append(s.text)
    idlist = "".join(idlist)
    idlist = idlist.split("\n")
    idlist = " ".join(idlist)
    idlist = idlist.split(" ")
    idlist.sort(key = len)
    templist = []
    for i in range(len(idlist) - 1):
        if len(idlist[i]) == 40:
            templist.append(idlist[i])
    idlist = templist       
    webbrowser_open("acestream://" + idlist[0])

def Play_SkySportsF1_ALT2():
    driver = webdriver.Chrome(service = chrome_service, options = chrome_options)
    driver.get("https://overtakefans.com/f1-live-stream/sky-sport-f1-live-stream-via-ace-player/")
    streamids = driver.find_elements(By.TAG_NAME, "input")
    idlist = []
    for s in streamids:
        idlist.append(s.get_attribute("value"))
    webbrowser_open("acestream://" + idlist[1])

def Play_ESPNHD():
    webbrowser_open("acestream://4b4907de51ec11087d4bed5876f2a0c68264f442")

def Play_ESPN2():
    webbrowser_open("acestream://664eb5fe460b96941aed633959a845b185cd8394")

def Play_F1TV():
    driver = webdriver.Chrome(service = chrome_service, options = chrome_options)
    driver.get("https://overtakefans.com/f1-live-stream/sky-sport-f1-live-stream-via-ace-player/")
    streamids = driver.find_elements(By.TAG_NAME, "input")
    idlist = []
    for s in streamids:
        idlist.append(s.get_attribute("value"))
    webbrowser_open("acestream://" + idlist[0])

def Play_F1TVHD():
    driver = webdriver.Chrome(service = chrome_service, options = chrome_options)
    driver.get("https://overtakefans.com/f1-live-stream/sky-sport-f1-live-stream-via-ace-player/")
    streamids = driver.find_elements(By.TAG_NAME, "input")
    idlist = []
    for s in streamids:
        idlist.append(s.get_attribute("value"))
    webbrowser_open("acestream://" + idlist[2])

def Play_ElevenSports1():
    webbrowser_open("acestream://14407b00d454cb7dc0d70aa26e8bbc554f457f00")

def Frame1():
    if frame2_created == False:
        frame2.destroy
    frame1 = tk.Frame(root, bg = "grey", borderwidth = 0)
    frame1.place(x = 20, y = 300, width = 560, height = 80)
    
    left_button = tk.Button(frame1, text = "<" , bg = "grey", command = Frame2, borderwidth = 0, activebackground = "black", activeforeground= "grey")
    left_button.place(x = 0, y = 0, width = 20, height = 80)

    right_button = tk.Button(frame1, text = ">" , bg = "grey", command = Frame2, borderwidth = 0, activebackground = "black", activeforeground= "grey")
    right_button.place(x = 540, y = 0, width = 20, height = 80)

    menu_button = tk.Button(frame1, bg = "grey", image = skysportsmainevent_logo, command = Play_SkySportsMainEvent, borderwidth = 0, activebackground = "grey")
    menu_button.place(x = 20, y = 0, width = 104, height = 80)

    menu1_button = tk.Button(frame1, bg = "grey", image = skysportsf1_logo, command = Play_SkySportsF1_Web, borderwidth = 0, activebackground = "grey")
    menu1_button.place(x = 124, y = 0, width = 104, height = 80)

    menu1_label = tk.Label(frame1, bg = "grey", image = web_icon)
    menu1_label.place(x = 124, y = 7, width = 104, height = 20)

    menu2_button = tk.Button(frame1, bg = "grey", image = skysportsf1_logo, command = Play_SkySportsF1, borderwidth = 0, activebackground = "grey")
    menu2_button.place(x = 228, y = 0, width = 104, height = 80)

    menu3_button = tk.Button(frame1, bg = "grey", image = skysportsf1_logo, command = Play_SkySportsF1_ALT1, borderwidth = 0, activebackground = "grey")
    menu3_button.place(x = 332, y = 0, width = 104, height = 80)

    menu4_button = tk.Button(frame1, bg = "grey", image = skysportsf1_logo, command = Play_SkySportsF1_ALT2, borderwidth = 0, activebackground = "grey")
    menu4_button.place(x = 436, y = 0, width = 104, height = 80)


def Frame2():
    frame1.destroy
    frame2 = tk.Frame(root, bg = "grey", borderwidth = 0)
    frame2.place(x = 20, y = 300, width = 560, height = 80)

    left_button = tk.Button(frame2, text = "<" , bg = "grey", command = Frame1, borderwidth = 0, activebackground = "black", activeforeground= "grey")
    left_button.place(x = 0, y = 0, width = 20, height = 80)

    right_button = tk.Button(frame2, text = ">" , bg = "grey", command = Frame1, borderwidth = 0, activebackground = "black", activeforeground= "grey")
    right_button.place(x = 540, y = 0, width = 20, height = 80)

    menu5_button = tk.Button(frame2, bg = "grey", image = espnhd_logo, command = Play_ESPNHD, borderwidth = 0, activebackground = "grey")
    menu5_button.place(x = 20, y = 0, width = 104, height = 80)

    menu6_button = tk.Button(frame2, bg = "grey", image = espn2_logo, command = Play_ESPN2, borderwidth = 0, activebackground = "grey")
    menu6_button.place(x = 124, y = 0, width = 104, height = 80)

    menu7_button = tk.Button(frame2, bg = "grey", image = f1tv_logo, command = Play_F1TV, borderwidth = 0, activebackground = "grey")
    menu7_button.place(x = 228, y = 0, width = 104, height = 80)

    menu8_button = tk.Button(frame2, bg = "grey", image = f1tvpro_logo, command = Play_F1TVHD, borderwidth = 0, activebackground = "grey")
    menu8_button.place(x = 332, y = 0, width = 104, height = 80)

    menu9_button = tk.Button(frame2, bg = "grey", image = elevensports1_logo, command = Play_ElevenSports1, borderwidth = 0, activebackground = "grey")
    menu9_button.place(x = 436, y = 0, width = 104, height = 80)

sessiontime = Get_Next_Session_Time()
frame2_created = False
runtimer = True
root = tk.Tk()
root.resizable(0, 0)
root.title("F1 Streams")
root.geometry("600x400")
root.overrideredirect(1)
center(root)
frame1_created = True
frame2_created = False

bg1 = tk.PhotoImage(file = "icons/rsz_1f1-background-image.png")
exit_icon = tk.PhotoImage(file = "icons/close.png")
skysportsmainevent_logo = tk.PhotoImage(file = "icons/skysportsmainevent_logo.png")
skysportsf1_logo = tk.PhotoImage(file = "icons/skysportsf1_logo.png")
web_icon = tk.PhotoImage(file = "icons/web_icon.png")
espnhd_logo = tk.PhotoImage(file = "icons/espnhd_logo.png")
espn2_logo = tk.PhotoImage(file = "icons/espn2_logo.png")
f1tv_logo = tk.PhotoImage(file = "icons/f1tv_logo.png")
f1tvpro_logo = tk.PhotoImage(file = "icons/f1tvpro_logo.png")
elevensports1_logo = tk.PhotoImage(file = "icons/elevensports1_logo.png")
download_icon = tk.PhotoImage(file = "icons/download_icon.png")

label1 = tk.Label(root, image = bg1)
label1.place(x = -2,y = -2)

frame1 = tk.Frame(root, bg = "grey", borderwidth = 0)
frame1.place(x = 20, y = 300, width = 560, height = 80)
    
left_button = tk.Button(frame1, text = "<" , bg = "grey", command = Frame2, borderwidth = 0, activebackground = "black", activeforeground= "grey")
left_button.place(x = 0, y = 0, width = 20, height = 80)

right_button = tk.Button(frame1, text = ">" , bg = "grey", command = Frame2, borderwidth = 0, activebackground = "black", activeforeground= "grey")
right_button.place(x = 540, y = 0, width = 20, height = 80)

menu_button = tk.Button(frame1, bg = "grey", image = skysportsmainevent_logo, command = Play_SkySportsMainEvent, borderwidth = 0, activebackground = "grey")
menu_button.place(x = 20, y = 0, width = 104, height = 80)

menu1_button = tk.Button(frame1, bg = "grey", image = skysportsf1_logo, command = Play_SkySportsF1_Web, borderwidth = 0, activebackground = "grey")
menu1_button.place(x = 124, y = 0, width = 104, height = 80)

menu1_label = tk.Label(frame1, bg = "grey", image = web_icon)
menu1_label.place(x = 124, y = 7, width = 104, height = 20)

menu2_button = tk.Button(frame1, bg = "grey", image = skysportsf1_logo, command = Play_SkySportsF1, borderwidth = 0, activebackground = "grey")
menu2_button.place(x = 228, y = 0, width = 104, height = 80)

menu3_button = tk.Button(frame1, bg = "grey", image = skysportsf1_logo, command = Play_SkySportsF1_ALT1, borderwidth = 0, activebackground = "grey")
menu3_button.place(x = 332, y = 0, width = 104, height = 80)

menu4_button = tk.Button(frame1, bg = "grey", image = skysportsf1_logo, command = Play_SkySportsF1_ALT2, borderwidth = 0, activebackground = "grey")
menu4_button.place(x = 436, y = 0, width = 104, height = 80)

frame2 = tk.Frame(root, bg = "grey", borderwidth = 0) #so bad but whatever
frame2.destroy

exit_button = tk.Button(root, image = exit_icon, command = root.destroy, borderwidth = 0, activebackground = "black", activeforeground= "grey")
exit_button.place(x = 570, y = 10, width = 20, height = 20)

install_button = tk.Button(root, bg = "grey", image = download_icon, text = "     Install AceStream", command = Install_AceStream, borderwidth = 0, activebackground = "black", activeforeground= "grey", compound = "left") 
install_button.place(x = 20, y = 10, width = 245, height = 20)

days = tk.StringVar()
hours = tk.StringVar()
mins = tk.StringVar()
seconds = tk.StringVar()

days.set(str(sessiontime[0]))
hours.set(str(sessiontime[1]))
mins.set(str(sessiontime[2]))
seconds.set(str(sessiontime[3]))

countdown = tk.Frame(root, bg = "grey", borderwidth = 0)
countdown.place(x = 275, y = 10, width = 285, height = 20)
text_label = tk.Label(countdown, text = "Time remaining until next session: ", borderwidth = 0, bg = "grey")
text_label.place(x = 0, y = 0, width = 200, height = 20)
day_label = tk.Label(countdown, textvariable = days, borderwidth = 0, bg = "grey", fg = "red")
day_label.place(x = 200, y = 0, width = 15, height = 20)
comma_label = tk.Label(countdown, text = ":", borderwidth = 0, bg = "grey")
comma_label.place(x = 215, y = 0, width = 6, height = 20)
hour_label = tk.Label(countdown, textvariable = hours, borderwidth = 0, bg = "grey", fg = "yellow")
hour_label.place(x = 221, y = 0, width = 15, height = 20)
comma_label = tk.Label(countdown, text = ":", borderwidth = 0, bg = "grey")
comma_label.place(x = 236, y = 0, width = 6, height = 20)
mins_label = tk.Label(countdown, textvariable = mins, borderwidth = 0, bg = "grey", fg = "white")
mins_label.place(x = 242, y = 0, width = 15, height = 20)
comma_label = tk.Label(countdown, text = ":", borderwidth = 0, bg = "grey")
comma_label.place(x = 257, y = 0, width = 6, height = 20)
seconds_label = tk.Label(countdown, textvariable = seconds, borderwidth = 0, bg = "grey", fg = "blue")
seconds_label.place(x = 263, y = 0, width = 15, height = 20)

def runTimer():
    clockTime = int(days.get())*86400 + int(hours.get())*3600 + int(mins.get())*60 + int(seconds.get())
    while(clockTime > -1):
        d, hms_time = divmod(clockTime, 86400)
        d = round(d)
        hms_time= time_strftime("%H:%M:%S", time_gmtime(hms_time))
        hms_time = hms_time.split(":")
        h = hms_time[0]
        m = hms_time[1]
        s = hms_time[2]
        days.set(d)
        hours.set(h)
        mins.set(m)
        seconds.set(s)
        root.update()
        time_sleep(0.1)
        clockTime -= 0.1

if runtimer == True:
    runTimer()
    runtimer = False

root.mainloop()