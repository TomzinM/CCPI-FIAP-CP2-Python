def triangulo(cat_a,cat_b,cat_c):

   if cat_a >= cat_b + cat_c:
       print("Não forma triangulo.")
   elif cat_a == cat_b == cat_c:
       print("Triangulo Equilatero.")
   elif cat_a == cat_b or cat_a == cat_c or cat_b == cat_c:
       print("Triangulo Isosceles")
   elif cat_a ** 2 < cat_b ** 2 + cat_c ** 2:
       print("Triangulo Acutangulo.")
   elif cat_a ** 2 == cat_b ** 2 + cat_c ** 2:
       print("Triangulo Retangulo.")
   elif cat_a ** 2 > cat_b ** 2 + cat_c ** 2:
       print("Triangulo Obsutangulo.")