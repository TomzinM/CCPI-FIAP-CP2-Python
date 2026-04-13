def calculador_media(cp1, cp2, cp3, sp1, sp2, gs):

   total = cp1 + cp2 + cp3

   if cp1 <= cp2 and cp1 <= cp3:
       total -= cp1
   elif cp2 <= cp1 and cp2 <= cp3:
       total -= cp2
   else:
       total -= cp3

   primeira_metade = (total + sp1 + sp2)/4
   primeira_metade *= 0.4
   segunda_metade = gs * 0.6

   media = primeira_metade + segunda_metade
   media_peso = media * 0.4

   print(f"Sua media no primeiro bimestre foi de {media:.1f}, e sua media anual agora é de {media_peso:.1f}.")

calculador_media(5, 4, 3, 10, 7, 10)
