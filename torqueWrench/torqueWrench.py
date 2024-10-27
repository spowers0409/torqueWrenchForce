import tkinter as tk

def show_input():
    formulaTorque = float(torque.get())
    formulaDistance = float(distance.get())
    distanceInches = formulaDistance / 12
    force = formulaTorque / distanceInches
    
    #userT_input = torque.get()
    #userD_input = distance.get()
    
    forceResults.insert(tk.END, F"{force}")
    


    #print(f"Enter Torque (ftLb):     {userT_input}")
    #print(f"Enter Distance (inches): {userD_input}")
    #print(f"Force required(in lbs):  {force}")

root = tk.Tk()
root.title("Torque Wrench Formula")
root.geometry("800x400")

label = tk.Label(root, text="Torque Wrench Formula")
label.pack()

torque = tk.Entry(root, width=30)
torque.pack(side=tk.LEFT, padx=5)

dividedBy = tk.Label(root, text='/')
dividedBy.pack(side=tk.LEFT, padx=5)

distance = tk.Entry(root, width=30)
distance.pack(side=tk.LEFT, padx=5)

def clear_results(event):
    forceResults.delete("1.0", tk.END)
    
torque.bind("<FocusIn>", clear_results)
distance.bind("<FocusIn>", clear_results)

button = tk.Button(root, text="Submit", command=show_input)
button.pack(side=tk.LEFT, padx=5)

forceResults = tk.Text(root, width=10, height=1)
forceResults.pack(side=tk.LEFT, padx=5)


    

root.mainloop()

