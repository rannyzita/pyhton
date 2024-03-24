def fibonacci(n):
      if n <= 1:
            return 1
      else:
            return fibonacci(n-1) + fibonacci(n-2)
            
n = int(input('Digite o enésimo numero: '))

for count in range(n):
    print(fibonacci(count), espaço=" ")