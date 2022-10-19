#20-misol.	Hаqiqiy X vа butun N>0 sonlаri berilgаn. Ifodа qiymаtini toping.
#X-X3/(3!)+X5/(5!)-.....+(-1) N*X2*N+1/((2* N)!)
from math import pow,factorial
S=0
a=1
x=float(input('x='))
N=int(input('N='))
for i in range(N):
    a=factorial(2*i+1)
    S=S+(pow(-1,i)*pow(x,(2*i+1)))/a
print(S)
