cp1 = float(input("Digite sua nota do Checkpoint 1 (0-10): "))
while cp1 < 0 or cp1 > 10:
    print("Nota do Checkpoint 1 inválida, digite uma nota de zero a dez.")
    cp1 = float(input("Digite sua nota do Checkpoint 1 (0-10): "))

cp2 = float(input("Digite sua nota do Checkpoint 2 (0-10): "))
while cp2 < 0 or cp2 > 10:
    print("Nota do Checkpoint 2 inválida, digite uma nota de zero a dez.")
    cp2 = float(input("Digite sua nota do Checkpoint 2 (0-10): "))

cp3 = float(input("Digite sua nota do Checkpoint 3 (0-10): "))
while cp3 < 0 or cp3 > 10:
    print("Nota do Checkpoint 3 inválida, digite uma nota de zero a dez.")
    cp3 = float(input("Digite sua nota do Checkpoint 3 (0-10): "))

sp1 = float(input("Digite sua nota da Sprint 1 (0-10): "))
while sp1 < 0 or sp1 > 10:
    print("Nota do Sprint 1 inválida, digite uma nota de zero a dez.")
    sp1 = float(input("Digite sua nota da Sprint 1 (0-10): "))

sp2 = float(input("Digite sua nota da Sprint 2 (0-10): "))
while sp2 < 0 or sp2 > 10:
    print("Nota do Sprint 2 inválida, digite uma nota de zero a dez.")
    sp2 = float(input("Digite sua nota da Sprint 2 (0-10): "))

gs = float(input("Digite sua nota da Global Solution (0-10): "))
while gs < 0 or gs > 10:
    print("Nota do Global Solution inválida, digite uma nota de zero a dez.")
    gs = float(input("Digite sua nota da Global Solution (0-10): "))

if cp1 <= cp2 and cp1 <= cp3:
    menor_nota = cp1
    checkpoints = cp2 + cp3
    print(f"Sua menor nota entre os checkpoints foi a da cp1. ({cp1})")

elif cp2 <= cp1 and cp2 <= cp3:
    menor_nota = cp2
    checkpoints = cp1 + cp3
    print(f"Sua menor nota entre os checkpoints foi a da cp2. ({cp2})")

else:
    menor_nota = cp3
    checkpoints = cp1 + cp2
    print(f"Sua menor nota entre os checkpoints foi a da cp3. ({cp3})")

cp_final = (checkpoints)
sp_final = sp1 + sp2

media_final = (cp_final + sp_final)/4 * 0.4 + gs * 0.6
media_sem_peso = (cp_final + sp_final)/4

print(f"\n" + "="*30)
print("RESULTADO FINAL")
print("="*30)

print(f"Menor checkpoint removido: {menor_nota}")
print(f"Nota final dos Checkpoints: {checkpoints}")
print(f"Nota final das Sprints: {sp_final}")
print(f"Nota final da Global Solution: {gs}")

print(f"-"*30)
print(f"Média final: {media_final:.1f}")
print(f"Média final sem peso: {media_sem_peso:.1f}")
print(f"="*30)


















