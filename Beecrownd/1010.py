cod1, n1, vu1 = input().split()
cod2, n2, vu2 = input().split()

total = (float(n1)*float(vu1))+(float(n2)*float(vu2))

print("VALOR A PAGAR: R$ {:.2f}".format(total))