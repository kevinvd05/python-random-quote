import random

def primary():

  numberOfLines = 14
  r = random.randint(0, numberOfLines-1)

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[r])

if __name__== "__main__":
  primary()