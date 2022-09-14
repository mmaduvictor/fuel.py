def main():
        while True:
                while True:
                        #getting user input
                        fuel = input("Fraction: ")
                        #perform the spilt and assign them to 2 variable
                        x , y = fuel.split("/")
                        #break
                else:
                        pass
                try:
                        #converting x and y variable into an integer
                        x, y = int(input(""))
                        if (x < y and y != 0) or x == y:
                                #calculate the percentage of fuel left
                                fuel = round(x/y * 100)
                                if fuel <= 99:
                                        print("f")
                                        break
                                elif fuel < 1:
                                        print(f"(round (x/y) * 100)%")
                                        break
                                elif fuel <= 1:
                                        print("E")
                                        break
                except:
                        pass






main()















