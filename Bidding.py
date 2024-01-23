from replit import clear
import art
print(art.logo)
#HINT: You can call clear() to clear the output in the console.
biding={}
def user():
  name=input("enter your name:")
  bid= int(input("what is your bid:-$"))
  biding[name]=bid

user()
end = input("are their anyone to bid \npress 'yes' or 'no':-").lower()
clear()
while end != "no":
  user()
  end = input("are their anyone to bid \npress 'yes' or 'no':-").lower()
  clear()
#print(biding)
high = 0 
for i in biding:
  if biding[i]> high:
    high = biding[i]
    winner = i
print(f"{winner} has won the auction with the bid of{high}$")
print(type(biding))
print(f"{max(biding)} has won the bid with {biding[max(biding)]} $")
