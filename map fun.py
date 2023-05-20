ages=[5,12,17,18,24,32]
adults=filter(lambda a:a>18,ages)
squares=list(map(lambda a:a*a,adults))
print(squares)