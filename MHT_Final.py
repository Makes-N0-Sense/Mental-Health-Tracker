import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime
from datetime import date
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

#read from dict

global data
data = {}

with open("data.txt", "r") as f:
    for line in f:
        line_dict = eval(line)
        data.update(line_dict)

def button_click(button,feel):
    data[today] = feel
    for b in buttons:
        if b != button:
            b.pack_forget()
    heading.config(text="How are you feeling today?")

def already_defined(feel):
    if feel==0:
        very_sad_button = ttk.Button(root, text="Very Sad")
        very_sad_button.pack(pady=5)
    elif feel==1:
        sad_button = ttk.Button(root, text="Sad")
        sad_button.pack(pady=5)
    elif feel==2:
        neutral_button = ttk.Button(root, text="Neutral")
        neutral_button.pack(pady=5)
    elif feel==3:
        happy_button = ttk.Button(root, text="Happy")
        happy_button.pack(pady=5)
    elif feel==4:
        very_happy_button = ttk.Button(root, text="Very Happy")
        very_happy_button.pack(pady=5)
    heading.config(text="How are you feeling today?")
  
root = tk.Tk()
root.geometry("800x600")
root.configure(bg='white')
root.title("Mental Health Tracker")

style = ttk.Style()
style.configure('TLabel', background='white')
style.configure('TButton', background='white')

# Header
heading = ttk.Label(root, text="Mental Health Tracker", font=("TkDefaultFont", 18, "bold"))
heading.pack(pady=10)
subheading = ttk.Label(root, text=datetime.now().strftime("%A, %d %B %Y"), font=("TkDefaultFont", 12))
subheading.pack()

# Display today's date
today = str(date.today())

if(today in data.keys()):
    feel = data[str(today)]
    already_defined(feel)
else:
    # Buttons
    very_sad_button = ttk.Button(root, text="Very Sad", command=lambda: button_click(very_sad_button,0))
    very_sad_button.pack(pady=5)

    sad_button = ttk.Button(root, text="Sad", command=lambda: button_click(sad_button,1))
    sad_button.pack(pady=5)

    neutral_button = ttk.Button(root, text="Neutral", command=lambda: button_click(neutral_button,2))
    neutral_button.pack(pady=5)

    happy_button = ttk.Button(root, text="Happy", command=lambda: button_click(happy_button,3))
    happy_button.pack(pady=5)

    very_happy_button = ttk.Button(root, text="Very Happy", command=lambda: button_click(very_happy_button,4))
    very_happy_button.pack(pady=5)

    buttons = [very_sad_button, sad_button, neutral_button, happy_button, very_happy_button]

# create data for line graph
x = list(data.keys())
y = list(data.values())

# create a figure object and add a subplot
fig = plt.Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)

# plot the line graph
ax.plot(x, y, marker='o')
ax.set_ylim([0, 5])
yticklabels = ['Very Sad', 'Sad', 'Neutral', 'Happy', 'Very Happy']
ax.set_yticklabels(yticklabels)
ax.tick_params(axis='x', labelsize=7)

# add the plot to a Tkinter canvas
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# create a navigation toolbar object
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# function to enable zoom
def zoom():
    toolbar.zoom()

# Start the main event loop
root.mainloop()

#write to file

with open("data.txt", "w") as f:
    f.write(str(data))