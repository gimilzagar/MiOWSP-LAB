while(1):
    #wejścia
    M = int(input("Podaj ilość strumieni ruchu M: "))
    a = []
    t = []
    for i in range(1, M+1): 
        a.append(float(input("podaj ruch oferowany - a"+format(i)+": ")))
        t.append(int(input("podaj ruch oferowany - t"+format(i)+": ")))
    V = int(input("Podaj pojemność wiązki V: "))
    x = [1]*(V+1) #tablica x 
    P =[1] * (V+1) #tablica P 
    
    def calc_x(V, M, a ,t): #wyliczanie x-ow
        for n in range(1, V+1):
            summaryX = 0
            for i in range(0, M):
                if n >= t[i]:
                    summaryX += a[i]*t[i]*x[n-t[i]]
            x[n] = summaryX/n 
        return x
    calc_x(V, M, a, t)
    for i in range(0, V+1):
        print("x"+format(i)+": "+format(x[i]), end = ' ')
    print("\n")
    def calc_P0(x): #wyliczanie P0
        summaryX = 0 
        for i in x:
            summaryX += i
        return 1/summaryX
    
    def calc_Pn(x, V, M, a, t) : #wyliczanie kolejnych prawdopodobieństw znalezienia się wiązki doskonałej w stanie zajętości n kanałów - P(n), poza P0
        P[0] = calc_P0(x)
        for n  in range(1, V+1 ):
            P[n] = (P[0] * x[n])
        return P
    calc_Pn(x, V, M, a, t)
    for i in range(0, V+1):
        print("P"+format(i)+": "+format(P[i]), end = ' ')
    print("\n")
    
    def calc_bi(P, V, t, i): #wyliczenie prawdopodobieństwa blokady strumnienia zgłoszeń klasy i
        summary = 0 
        for n in range( V-t[i-1]+1, V+1):
            summary += P[n]
        return summary
    for b in range(1, M+1):
        print("b"+format(b)+": "+format(calc_bi(P,V, t, b)), end = ' ')
    print("\n")
