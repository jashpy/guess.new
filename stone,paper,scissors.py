a=input("first turn:")
b=input("second turn:")


def  match(name1,name2):
    if name1=="stone" and name2=="stone":
        return(print("drawn"))

    elif name1=="stone" and name2=="paper":
        return(print("user2 wins"))

    elif name1=="stone" and  name2=="scissor":
        return(print("user1 wins"))

    elif name1=="paper" and name2=="stone":
        return(print("user1 wins"))

    elif name1=="paper"  and name2=="paper":
        return(print("drawn"))

    elif name1=="paper" and name2=="scissor":
        return(print("user2 wins"))

    elif name1=="scissor" and name2=="stone":
        return(print("user2 wins"))

    elif name1=="scissor"  and name2=="paper":
        return(print("user1 wins"))

    elif name1=="scissor" and name2=="scissor":
        return(print("drawn"))

print(match(a,b))

print("Thank you for playing the game,Made by JASHBANT DASH")                           