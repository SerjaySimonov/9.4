m = int(input("Ievadi no kuras pakāpes jāaprēķina: "))
N = int(input("Ievadi līdz kurai pakāpei jāaprēķina: "))
for i in range(m,N+1):
  n = pow(2,i)
  print(n)