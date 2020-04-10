MOON_MULTIPLE=0.165

def main():
    earth_weight_str=input("Enter a weight on earth:")
    earth_weigh=float(earth_weight_str)
    moon_weight=earth_weight*MOON_MULTIPLE
    print("Equivalent weight on the moon: "+str(moon_weight))


if __name__=='main':
    main()