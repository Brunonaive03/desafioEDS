prescricao = ""
estoque = ""

for c in prescricao:
    if c in estoque:
        prescricao = prescricao.replace(c,"",1)
        estoque = estoque.replace(c,"",1)

if prescricao == "":
    print("true")
else:
    print("false")