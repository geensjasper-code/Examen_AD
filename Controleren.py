numlist = [100, 101, 0, "103", 104]

try:
    i1 = int(input("Give an index: "))
    print("100 /", numlist[i1], "=", 100 / numlist[i1])
except ZeroDivisionError:
    print("Error: it looks like the list contains a zero")
except TypeError:
    print("Error: it looks like the list contains a string")
except IndexError:
    print("Error: you gave too large of an index")
except ValueError:
    print("Error: please enter an integer as the index")
