def fibonacciRec(n):
    
    if n == 1 or n == 2:
        res = 1   
    else: 
        res = fibonacciRec(n - 2) + fibonacciRec(n - 1)  
    
    print(res)        
        
    return res



fibonacciRec(10)