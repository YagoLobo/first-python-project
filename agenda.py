def adicionar_contato(lista_contatos, nome_contato= "Contato 1", telefone_contato= 0,email_contato= "email@gmail.com"):
    contatos = {"nome": nome_contato, "Telefone": telefone_contato, "Email": email_contato, "Favorito": False}
    lista_contatos.append(contatos)
    print(f"O contato {nome_contato} foi adicionado com sucesso")
    return

def ver_contatos(lista_contatos):
    print("\nLista de contatos cadastrados: ")
    for indice, contatos in enumerate(lista_contatos, start=1):
        status = "✓" if contatos["Favorito"] else " "
        nome_contato = contatos["nome"]
        telefone_contato = contatos["Telefone"]
        email_contato = contatos["Email"]
        print(f"\n{indice}. [{status}] {nome_contato}\nTelefone: {telefone_contato}\nEmail: {email_contato}")
    return

def editar_contato(lista_contatos, indice_contatos, novo_nome_contato, novo_telefone, novo_email):
    indice_contato_ajudstado = int(indice_contatos) - 1
    if indice_contato_ajudstado >=0 and indice_contato_ajudstado < len(lista_contatos):
        lista_contatos[indice_contato_ajudstado]["nome"] = novo_nome_contato
        lista_contatos[indice_contato_ajudstado]["Telefone"] = novo_telefone
        lista_contatos[indice_contato_ajudstado]["Email"] = novo_email
        print(f"Contato {indice_contatos} editado para {novo_nome_contato}")
    else:
        print("Contato nao cadastrado")
    return

def favoritar_contato(lista_contatos, indice_contatos):
    indice_contato_ajudstado = int(indice_contatos) - 1
    if indice_contato_ajudstado >=0 and indice_contato_ajudstado < len(lista_contatos):
        lista_contatos[indice_contato_ajudstado]["Favorito"] = True
        contatos_favoritos = {"nome": nome_contato, "Telefone": telefone_contato, "Email": email_contato, "Favorito": False}
        lista_contatos_favoritos.append(lista_contatos[indice_contato_ajudstado])
        print(f"Contato {indice_contatos} marcado como favorito")
    else:
        print("Contato nao encontrado")
    return

def desfavoritar_contato(lista_contatos, indice_contatos):
    indice_contato_ajudstado = int(indice_contatos) - 1
    if indice_contato_ajudstado >=0 and indice_contato_ajudstado < len(lista_contatos):
        lista_contatos[indice_contato_ajudstado]["Favorito"] = False
        lista_contatos_favoritos.pop(indice_contato_ajudstado)
        print(f"Contato {indice_contatos} desmarcado como favorito")
    else:
        print("Contato nao encontrado")
    return

def ver_contatos_favoritos(lista_contatos_favoritos):
    if len(lista_contatos_favoritos) == 0:
        print("\nNao ha contatos favoritados")
        return
    print("\nLista de contatos favoritados: ")
    for indice, contatos_favoritos in enumerate(lista_contatos_favoritos, start=1):
        status = "✓" if contatos_favoritos["Favorito"] else " "
        nome_contato = contatos_favoritos["nome"]
        telefone_contato = contatos_favoritos["Telefone"]
        email_contato = contatos_favoritos["Email"]
        print(f"\n{indice}. [{status}] {nome_contato}\nTelefone: {telefone_contato}\nEmail: {email_contato}") 
    return

#contato removido da lista contatos mas nao da lista contatos favoritos 
def remover_contatos(lista_contatos, nome_contatos_remover):
    for contato in lista_contatos:
        if contato["nome"] == nome_contatos_remover:
            lista_contatos.remove(contato)
            print(f"Contato {nome_contatos_remover} removido com sucesso")
            try:
                lista_contatos_favoritos.remove(contato)
            finally:
                return
            return
    print("Contato nao cadastrado")
    
        

lista_contatos_favoritos = []
lista_contatos = []

while True:
    print("\nMenu da agenda:")
    print("1. Adicionar um contato")
    print("2. Visualizar contatos")
    print("3. Editar contato")
    print("4. Marcar contato como favorito")
    print("5. Desmarcar contato como favorito")
    print("6. Visualizar contatos favoritos")
    print("7. Apagar um contato")
    print("8. Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
            nome_contato = input("Digite o nome do contato: ")
            telefone_contato = input("Telefone: ")
            email_contato = input("Email: ")
            adicionar_contato(lista_contatos, nome_contato, telefone_contato, email_contato)

    elif escolha == "2":
        ver_contatos(lista_contatos)
    
    elif escolha == "3":
        ver_contatos(lista_contatos)
        indice_contatos = input("Digite a posicao do contato que deseja atualizar: ")
        novo_nome_contato = input("Novo nome do contato: ")
        novo_telefone = input("Novo telefone de contato: ")
        novo_email = input("Novo email do contato: ")
        editar_contato(lista_contatos, indice_contatos, novo_nome_contato, novo_telefone, novo_email)

    elif escolha == "4":
        ver_contatos(lista_contatos)
        indice_contatos = input("Digite o contato que deseja favoritar: ")
        favoritar_contato(lista_contatos, indice_contatos)

    elif escolha == "5":
        ver_contatos_favoritos(lista_contatos_favoritos)
        indice_contatos = input("Digite o contato que deseja desfavoritar: ")
        desfavoritar_contato(lista_contatos,indice_contatos)

    elif escolha == "6":
        ver_contatos_favoritos(lista_contatos_favoritos)

    elif escolha == "7":
        ver_contatos(lista_contatos)
        nome_contatos_remover = input("Digite o NOME do contato que deseja remover: ")
        remover_contatos(lista_contatos, nome_contatos_remover)

    elif escolha == "8":
        break

    else: 
        print("\nEscolha nao valida")


