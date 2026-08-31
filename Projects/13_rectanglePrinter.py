print("="*10 + " Rectangle Printer " + "="*10)

rows = int(input("enter the number of rows: "))
cols = int(input("enter the number of columns: "))
symbol = input("enter the symbol to print the ractangle: ")

for x in range(rows):
    for y in range(cols):
        print(symbol, end=" ")
    print()