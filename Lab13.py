print ("Michael Mordec, 7/19/22, Lab 13, CSC 242:")

myDict = {
        "Clarence Carson":[250,1000,3.2],
        "Daphne Danvers":[100,6000,6.5],
        "Julia Jefferson":[100,4000,3.2],
        "Randolph Reeds":[250,2000,6.5],
        "Sabrina Sanders":[250,3000,3.2]
}
print("\nCommission: ")
for name in myDict:
    comm = myDict[name][1] * myDict[name][2] * .01
    print(name + ":",comm)

print("\nGross Income: ")
for name in myDict:
    comm = myDict[name][0] + myDict[name][1] * myDict[name][2] * .01
    print(name + ":",comm)

print("\nTotal Commission: ")
commTotal = 0
for name in myDict:
    commTotal = commTotal + myDict[name][1] * myDict[name][2] * .01
print("Total:",commTotal)

# test for inclusion of a key
print ("please enter a key to search")
theKey = input() 
if (theKey in myDict) :
    print ("the key exists in the dictionary")
else :
    print ("the key does not exist in the dictionary")
    # accessing dictionary values
print (myDict[theKey])



