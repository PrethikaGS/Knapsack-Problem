from tkinter import *
import tkinter as tk
import tkinter.messagebox
import heapq

color1 = "#202020"
color2 = "#E2DBDB"



def validation(n, value, weight, maxcapacity):
    condition = True

    if n != len(value) or n!= len(weight):
        condition = False
    elif n <=0:
        condition = False
    elif maxcapacity < 0:
        condition = False
    return condition
   
def greedymethod():

    n, value, weight, maxcapacity = getinput()
    condition = validation(n, value, weight, maxcapacity)
    if condition == False:
        print("Error! Please check your input.")
        tkinter.messagebox.showinfo('Warning!','Error! Please check your input.')
    else:
        fractional_knapsack(value, weight, maxcapacity)

def bbmethod():

    n, value, weight, maxcapacity = getinput()
    condition = validation(n, value, weight, maxcapacity)
    if condition == False:
        print("Error! Please check your input.")
        tkinter.messagebox.showinfo('Warning!','Error! Please check your input.')
    else:
        zeroone_knapsack(maxcapacity, weight, value)

def fractional_knapsack(value, weight, capacity):

    """Return maximum value of items and their fractional amounts.
 
    (max_value, fractions) is returned where max_value is the maximum value of
    items with total weight not more than capacity.
    fractions is a list where fractions[i] is the fraction that should be taken
    of item i, where 0 <= i < total number of items.
 
    value[i] is the value of item i and weight[i] is the weight of item i
    for 0 <= i < n where n is the number of items.
 
    capacity is the maximum weight.
    """
    # index = [0, 1, 2, ..., n - 1] for n items
    index = list(range(len(value)))
    # contains ratios of values to weight
    ratio = [v/w for v, w in zip(value, weight)]
     
    # index is sorted according to value-to-weight ratio in decreasing order
    index.sort(key=lambda i: ratio[i], reverse=True)
 
    max_value = 0
    max_value_cumulative = [0]*len(value)
    weight_cumulative = [0]*len(value)
    weight_before = 0
    fractions = [0]*len(value)
    
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            weight_cumulative[i] =+ fractions[i]*weight[i]+weight_before
            weight_before =+weight_cumulative[i]
            max_value += value[i]
            max_value_cumulative[i]+=(max_value)
            capacity -= weight[i]
        else:
            fractions[i] = capacity/weight[i]
            weight_cumulative[i] =+ fractions[i]*weight[i]+weight_before
            weight_before =+weight_cumulative[i]
            max_value += value[i]*capacity/weight[i]
            max_value_cumulative[i]+=(max_value)
            break


    print("*Fractional Knapsack (Greedy Method) *")
    print("The weight of items are ", weight)
    print("The value of items are ", value)
    print('The number in which the items should be taken:', fractions)
    print('The maximum Benefit(value) of items that can be carried:', max_value)
    

    text1="The weight of items are: "
    text2="The value of items are: "
    text3='The number in which the items should be taken:'
    text4='The maximum Benefit(value) of items that can be carried:'
    
    display = Tk()
    display.title("*Fractional Knapsack (Greedy Method) OUTPUT")
    Label1 = Label(display, text=text1)
    Labela = Label(display, text=weight)
    Label2 = Label(display, text=text2)
    Labelb = Label(display, text=value)
    Label3 = Label(display, text=text3)
    Labelc = Label(display, text=fractions)
    Label4 = Label(display, text=text4)
    Labeld = Label(display, text=max_value)
    #Label5 = Label(display, text=x)
    Label1.pack()
    Labela.pack()
    Label2.pack()
    Labelb.pack()
    Label3.pack()
    Labelc.pack()
    Label4.pack()
    Labeld.pack()
    #Label5.pack()
        
def zeroone_knapsack(capacity, weights, values):
    """
    Best-First Branch-and-Bound algorithm for the 0-1 Knapsack problem.

    capacity: maximum weight capacity of the knapsack
    weights: list of weights of the items
    values: list of values of the items
    """
    # Calculate the bound for the root node
    bound = bound_value(capacity, weights, values)
    
    # Initialize the priority queue with the root node
    queue = [(-bound, 0, 0, [])]
    
    # Initialize the best solution found so far
    best_value = 0
    best_subset = []
    
    # Explore the search tree using Best-First Branch-and-Bound
    while queue:
        # Get the node with the highest priority (i.e., lowest bound)
        _, weight, value, subset = heapq.heappop(queue)
        
        # Check if this node represents a complete solution
        if weight > capacity:
            continue
        
        # Check if this node represents a new best solution
        if value > best_value:
            best_value = value
            best_subset = subset
        
        # Expand the node by considering the next item
        if len(subset) < len(weights):
            # Include the next item
            include_weight = weight + weights[len(subset)]
            include_value = value + values[len(subset)]
            include_subset = subset + [1]
            include_bound = bound_value(capacity - include_weight, weights[len(subset)+1:], values[len(subset)+1:]) + include_value
            heapq.heappush(queue, (-include_bound, include_weight, include_value, include_subset))
            
            # Exclude the next item
            exclude_weight = weight
            exclude_value = value
            exclude_subset = subset + [0]
            exclude_bound = bound_value(capacity - exclude_weight, weights[len(subset)+1:], values[len(subset)+1:]) + exclude_value
            heapq.heappush(queue, (-exclude_bound, exclude_weight, exclude_value, exclude_subset))
            
    #return (best_value, best_subset)
    print("The value of items are:", values)
    print("The weight of items are:", weight)
    print("The best value:",best_value)
    print("Best subset:", best_subset)

    text5 = "The value of items are:"
    text6 = "The weight of items are:"
    text7 = "The best value:"
    text8 = "Best subset:"

    display = Tk()
    display.title("*0-1 Knapsack (Branch and Bound) *")
    display.geometry("300x200")
    Label5 = Label(display, text=text5)
    Labela = Label(display, text=values)
    Label6 = Label(display, text=text6)
    Labelb = Label(display, text=weight)
    Label7 = Label(display, text=text7)
    Labelc = Label(display, text=best_value)
    Label8 = Label(display, text=text8)
    Labeld = Label(display, text=best_subset)
    
    Label5.pack()
    Labela.pack()
    Label6.pack()
    Labelb.pack()
    Label7.pack()
    Labelc.pack()
    Label8.pack()
    Labeld.pack()
def bound_value(capacity, weights, values):
    """
    Calculate the bound for a node in the search tree.
    """
    bound = 0
    for i in range(len(weights)):
        if weights[i] <= capacity:
            bound += values[i]
            capacity -= weights[i]
        else:
            bound += values[i] * (capacity / weights[i])
            break
    return bound

def getinput():

    print("***NEW INPUT***")
    n = entry_n.get()
    n = int(n)
    print("The number of item is ",n)
    value = entry_value.get().split(" ")
    value = list(map(int, value))
    print("The value of the items are ",value)
    weight = entry_weight.get().split(" ")
    weight = list(map(int, weight))
    print("The weight of the items are ",weight)
    maxcapacity = entry_max.get()
    maxcapacity = int(maxcapacity)
    print("The maximum capacity of knapsack is ",maxcapacity)
    
    return n, value, weight, maxcapacity
    
def main():
    global root
    global display
    global Label
    
    root = Tk()
    root.title("0/1 and Fractional and Fractional Knapsack Solver")
    root.configure(bg=color1)
    root.geometry("750x450")
    
    #start_sound()

    global var
    var= IntVar()

    global entry_n
    global entry_value
    global entry_weight
    global entry_max

    theLabel = Label(root, text="Welcome to 0/1 and Fractional Knapsack Solver",bg=color1,fg=color2,font=(("Garamond", 25, "bold")))
    theLabel.pack(fill=X)

   
    topFrame = Frame(root)
    topFrame.configure(bg=color1)
    #topFrame.place(x=500, y=500)
    topFrame.pack(padx=2,pady=60)

    label_n = Label(topFrame, text="Number of items",bg=color1,fg=color2,font=(("Calibri", 13)))
    label_value = Label(topFrame, text="Value of items [each item seperate by SPACE]",bg=color1,fg=color2,font=(("Calibri", 13)))
    label_weight = Label(topFrame, text="Weight of items [each item seperate by SPACE]",bg=color1,fg=color2,font=(("Calibri", 13)))
    label_max = Label(topFrame, text="Maximum Weight",bg=color1,fg=color2,font=(("Calibri", 13)))
    entry_n = Entry(topFrame)
    entry_value = Entry(topFrame)
    entry_weight = Entry(topFrame)
    entry_max = Entry(topFrame)

    label_n.grid(row=0,column=0,sticky=E)
    label_value.grid(row=1,column=0,sticky=E)
    label_weight.grid(row=2,column=0,sticky=E)
    label_max.grid(row=3,column=0,sticky=E)

    entry_n.grid(row=0,column=1)
    entry_value.grid(row=1,column=1)
    entry_weight.grid(row=2,column=1)
    entry_max.grid(row=3,column=1)


    message2 = Label(root, text="Click the way you want the problem to be solved",bg=color1,fg=color2,font=(("Garamond", 18,"bold")))
    message2.place(x=120,y=250)

    #botFrame = Frame(root)
    #botFrame.pack()

    button1 = Button(root, text="0-1 Problem (Branch& Bound Method)",command = bbmethod, fg="black",bg=color2,font=(("Calibri", 13)))
    button2 = Button(root, text="Fractional Problem (Greedy Method)",command=greedymethod, fg="black",bg=color2,font=(("Calibri", 13)))

    button1.place(x=90,y=310)
    button2.place(x=390,y=310)

    root.mainloop()

main()