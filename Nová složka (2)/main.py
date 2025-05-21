from funkce import vypis,prvniPismeno

def main():
    text=input("jaky text chcete napsat")
    num=int(input("kolikrat to chcete"))
    vypis(text,num)
    prvniPismeno(text)
if __name__=="__main__":
    main()