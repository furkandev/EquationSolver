#
# equation solver - v1
#
# coded by furkan akal
#
# 23.01.18 tue
#

import math

equation = input("Çözmek istediğiniz ikinci dereceden denklemi girin: ")

split1 = equation.split("--")

der2_terim = split1[0]
der1_terim = split1[1]
sabit_terim = split1[2]

split2 = der2_terim.split("-")
split3 = der1_terim.split("-")

a = split2[0]
b = split3[0]
c = sabit_terim

delta = float(b)*float(b) - 4*float(a)*float(c)

if(delta > 0):
	x1 = (- float(b) + float(math.sqrt(delta)))/(2*float(a))
	x2 = (- float(b) - float(math.sqrt(delta)))/(2*float(a))

	print(x1)
	print(x2)