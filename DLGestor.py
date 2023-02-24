from datetime import date
from getpass import getpass
import time

#(usuario, senha)
users = [("admin", "admin"),]

#(codigo, marca, time, temporada, tamanho, modelo/corte, skull, quantidade, valorCusto)
dataInv = [(1, "Adidas", "Flamengo", "22/23", "G", "Masculino" ,"ADI FLA 1 TD 23 G MAS", 1, 90),
             (2, "Nike", "Barcelona", "22/23", "GG", "Feminino" ,"NIK BAR 1 TD 23 GG FEM", 2, 90),
             (3, "Adidas", "Real Madrid", "21/22", "M", "Masculino" ,"ADI MAD 2 JG 22 M MAS", 5, 90),
             (4, "Puma", "Manchester City", "21/22", "P", "Feminino", "PUM MCI 3 TD 22 P FEM", 3, 90),
             (5, "Nike", "Liverpool", "22/23", "G", "Masculino" ,"NIK LIV 1 JG 23 G MAS", 1, 90)]

#(codigo, vendedor, cod_produtoVendido, unidades_vendidas, valor, data_daVenda)
dataSale = [(1, "Delandilucas", 2, 1, 130, date.today().isoformat()),
              (2, "Delandi", 3, 2, 260, date.today().isoformat()),
              (3, "Mateus", 1, 2, 260, date.today().isoformat()),
              (4, "Lucas", 4, 4, 520, date.today().isoformat()),
              (5, "Mateus", 2, 1, 130, date.today().isoformat())]

#(codigo, fornecedor, cod_produtoComprado, unidades_compradas, valor_custo, data_daCompra)
dataPurchase = [(1, "Fabrica 1", 1, 1, 90, date.today().isoformat()),
                (2, "Fabrica 12", 2, 2, 90, date.today().isoformat()),
                (3, "Fabrica 10", 3, 5, 90, date.today().isoformat()),
                (4, "Fabrica 3", 4, 3, 90, date.today().isoformat()),
                (5, "Fabrica 5", 5, 1, 90, date.today().isoformat())]


#----------------------------------------------------------------------- Inicio - Funçoes Utilitarias ---------------------------------------------------------------------
def setCodeProduct(data: list):
    (code, _, _, _, _, _, _, _, _) = data[len(data) - 1]
    return code + 1

def setCode(data: list):
    (code, _, _, _, _, _) = data[len(data) - 1]
    return code + 1

def slowPrint(text, delay):
    for i in text:
        print(i, end='', flush=True)
        time.sleep(delay)
#----------------------------------------------------------------------- Fim - Funçoes Utilitarias ------------------------------------------------------------------------

#----------------------------------------------------------------------- Inicio - Funçoes Estoque -------------------------------------------------------------------------
def listProducts(data: list):
    print()
    print()
    print("| Cód.. | Marca    | Time                 | Temporada | Tamanho | Corte     | Skull                  | Qnt. | Preço     |")
    print("-------- ---------- ---------------------- ----------- --------- ----------- ------------------------ ------ ------------")
    for i in range(len(data)):
        (code, brand, club, season, size, model, skull, quant, price) = data[i]
        # código
        print("| {:05d} |".format(code), end="")
        # marca
        if len(brand) > 8:
            brand = brand[:5] + "..."
        else:
            brand = brand.ljust(8)
        print(" " + brand, end=" |")
        # time
        if len(club) > 20:
            club = club[:17] + "..."
        else:
            club = club.ljust(20)
        print(" " + club, end=" |")
        # temporada
        if len(season) > 9:
            season = season[:6] + "..."
        else:
            season = season.ljust(9)
        print(" " + season, end=" |")

        # tamanho
        if len(size) > 7:
            size = size[:4] + "..."
        else:
            size = size.ljust(7)
        print(" " + size, end=" |")
        # corte
        if len(model) > 9:
            model = model[:7] + "..."
        else:
            model = model.ljust(9)
        print(" " + model, end=" |")
        # skull
        if len(skull) > 22:
            skull = skull[:19] + "..."
        else:
            skull = skull.ljust(22)
        print(" " + skull, end=" |")
        # qnt_estoque
        print(" {:4d}".format(quant), end=" |")
        # preço
        print(" R${:4d},00 |".format(price))
        print("-------- ---------- ---------------------- ----------- --------- ----------- ------------------------ ------ ------------")
    print()

def listProductForCod(data: list, cod: int):
    print()
    print()
    print("| Cód.. | Marca    | Time                 | Temporada | Tamanho | Corte     | Skull                  | Qnt. | Preço     |")
    print("-------- ---------- ---------------------- ----------- --------- ----------- ------------------------ ------ ------------")

    (code, brand, club, season, size, model, skull, quant, price) = data[cod]
    # código
    print("| {:05d} |".format(code), end="")
    # marca
    if len(brand) > 8:
        brand = brand[:5] + "..."
    else:
        brand = brand.ljust(8)
    print(" " + brand, end=" |")
    # time
    if len(club) > 20:
        club = club[:17] + "..."
    else:
        club = club.ljust(20)
    print(" " + club, end=" |")
    # temporada
    if len(season) > 9:
        season = season[:6] + "..."
    else:
        season = season.ljust(9)
    print(" " + season, end=" |")

    # tamanho
    if len(size) > 7:
        size = size[:4] + "..."
    else:
        size = size.ljust(7)
    print(" " + size, end=" |")
    # corte
    if len(model) > 9:
        model = model[:7] + "..."
    else:
        model = model.ljust(9)
    print(" " + model, end=" |")
    # skull
    if len(skull) > 22:
        skull = skull[:19] + "..."
    else:
        skull = skull.ljust(22)
    print(" " + skull, end=" |")
    # qnt_estoque
    print(" {:4d}".format(quant), end=" |")
    # preço
    print(" R${:4d},00 |".format(price))
    print("-------- ---------- ---------------------- ----------- --------- ----------- ------------------------ ------ ------------")
    print()

def findProductForCod(data: list, cod: int):
    for i in range(len(data)):
        (code, _, _, _, _, _, _, _, _) = data[i]
        if cod == code:
            return True, i
    return False, 0

def listProductsForBrand(data: list, string: str):
    listProductsFinded = []
    for i in range(len(data)):
        product = (_, brand, _, _, _, _, _, _, _) = data[i]
        if type(brand) == type(string) and brand == string:
            listProductsFinded.append(product)
    if listProductsFinded != []:
        listProducts(listProductsFinded)
    else:
        print("\n Produto não encontrado!! \n")

def listProductsForClub(data: list, string: str):
    listProductsFinded = []
    for i in range(len(data)):
        product = (_, _, club, _, _, _, _, _, _) = data[i]
        if type(club) == type(string) and club == string:
            listProductsFinded.append(product)
    if listProductsFinded != []:
        listProducts(listProductsFinded)
    else:
        print("\n Produto não encontrado!! \n")

def listProductsForSeason(data: list, string: str):
    listProductsFinded = []
    for i in range(len(data)):
        product = (_, _, _, season, _, _, _, _, _) = data[i]
        if type(season) == type(string) and season == string:
            listProductsFinded.append(product)
    if listProductsFinded != []:
        listProducts(listProductsFinded)
    else:
        print("\n Produto não encontrado!! \n")

def listProductsForSize(data: list, string: str):
    listProductsFinded = []
    for i in range(len(data)):
        product = (_, _, _, _, size, _, _, _, _) = data[i]
        if type(size) == type(string) and size == string:
            listProductsFinded.append(product)
    if listProductsFinded != []:
        listProducts(listProductsFinded)
    else:
        print("\n Produto não encontrado!! \n")

def listProductsForModel(data: list, string: str):
    listProductsFinded = []
    for i in range(len(data)):
        product = (_, _, _, _, _, model, _, _, _) = data[i]
        if type(model) == type(string) and model == string:
            listProductsFinded.append(product)
    if listProductsFinded != []:
        listProducts(listProductsFinded)
    else:
        print("\n Produto não encontrado!! \n")

def listProductsForQuant(data: list, var: int):
    listProductsFinded = []
    for i in range(len(data)):
        product = (_, _, _, _, _, _, _, quant, _) = data[i]
        if type(quant) == type(var) and quant == var:
            listProductsFinded.append(product)
    if listProductsFinded != []:
        listProducts(listProductsFinded)
    else:
        print("\n Produto não encontrado!! \n")

def listProductsForPrice(data: list, var: int):
    listProductsFinded = []
    for i in range(len(data)):
        product = (_, _, _, _, _, _, _, _, price) = data[i]
        if type(price) == type(var) and price == var:
            listProductsFinded.append(product)
    if listProductsFinded != []:
        listProducts(listProductsFinded)
    else:
        print("\n Produto não encontrado!! \n")

def listProductsInInv(data: list):
    inventory = []
    for i in range(len(data)):
        product = (_, _, _, _, _, _, _, quant, _) = data[i]
        if quant > 0:
            inventory.append(product)
    if inventory != []:
        listProducts(inventory)
    else:
        print("\n Nenhum produto em estoque!! \n")

def filterProductByUniform(data: list, var: str):
    listProductsFinded = []
    if var == "1" or var == "2" or var == "3":
        for i in range(len(data)):
            product = (_, _, _, _, _, _, skull, _, _) = data[i]
            listSkull = skull.split()
            
            if type(listSkull[2]) == type(var) and listSkull[2] == var:
                listProductsFinded.append(product)
            
        if listProducts != []:
            listProducts(listProductsFinded)
        else:
            print("\n Não encontrado nenhum produto!! \n")
    else:
            print(" \nUniforme inválido. Digite 1, 2, ou 3... \n")

def filterProductByVersion(data: list, var: str):
    listProductsFinded = []
    if var == "TD" or var == "JG":
        for i in range(len(data)):
            product = (_, _, _, _, _, _, skull, _, _) = data[i]
            listSkull = skull.split()
            
            if type(listSkull[3]) == type(var) and listSkull[3] == var:
                listProductsFinded.append(product)

        if listProductsFinded != []:
            listProducts(listProductsFinded)
        else:
            print("\n Não encontrado nenhum produto!! \n")
    else:
            print(" \n Versão Inválida. Digite TD ou JG... \n")

def filterProducts(data: list):
    option = options("filters")
    while option != 12:
        match(option):
            case 1:
                print(" \nCódigo do produto: ", end="")
                code = int(input())
                finded, ind = findProductForCod(data, code)
                if finded:
                    listProductForCod(data, ind)
                else:
                    print("\n Produto não encontrado!! \n")
            case 2:
                print(" \nDigite a Marca do produto: ", end="")
                brand = input().rstrip(" ").lstrip(" ").capitalize()
                listProductsForBrand(data, brand)
            case 3:
                print(" \nDigite o Time: ", end="")
                club = input().rstrip(" ").lstrip(" ").capitalize()
                listProductsForClub(data, club)
            case 4:
                print(" \nDigite a Temporada: ", end="")
                season = input().upper().rstrip(" ").lstrip(" ")
                listProductsForSeason(data, season)
            case 5:
                print(" \nDigite o Tamanho: ", end="")
                size = input().upper().rstrip(" ").lstrip(" ")
                listProductsForSize(data, size)
            case 6:
                print(" \nDigite o Corte: ", end="")
                model = input().rstrip(" ").lstrip(" ").capitalize()
                listProductsForModel(data, model)
            case 7:
                print(" \nDigite a Quantidade: ", end="")
                quant = int(input())
                listProductsForQuant(data, quant)
            case 8:
                print(" \nDigite o Preço: ", end="")
                price = int(input())
                listProductsForPrice(data, price)
            case 9:
                print(" \n Produtos em Estoque: \n")
                listProductsInInv(data)
            case 10:
                print(" \nDigite o Uniforme: ", end="")
                uniform = input().rstrip(" ").lstrip(" ")
                filterProductByUniform(data, uniform)
            case 11:
                print(" \nDigite a Versão(TD ou JG): ", end="")
                version = input().upper().rstrip(" ").lstrip(" ")
                filterProductByVersion(data, version)
        option = options("filters")

def editProduct(data: list):
    cod = int(input(" Código do Produto: "))
    finded, ind = findProductForCod(data, cod)
    
    if finded:
        (_, brand, club, season, size, model, skull, quant, price) = data[ind]
        print("\n Produto Encontrado: \n")
        listProductForCod(data, ind)

        option = options("editProduct")
        while option != 10:
            match(option):
                case 1:
                    print("\n Digite a nova Marca: ", end="")
                    brand = input().rstrip(" ").lstrip(" ").capitalize()
                    print("\n Nova Marca: " + str(brand))
                case 2:
                    club = print("Digite o novo Time: ", end="")
                    club = input().rstrip(" ").lstrip(" ").capitalize()
                    print("\n Novo Time: " + str(club))
                case 3:
                    season = print("Digite a nova Tempoarada: ", end="")
                    season = input().upper().rstrip(" ").lstrip(" ")
                    print("\n Nova Temporada: " + str(season))
                case 4:
                    size = print("Digite o novo Tamanho: ", end="")
                    size = input().upper().rstrip(" ").lstrip(" ")
                    print("\n Novo Tamanho: " + str(size))
                case 5:
                    model = print("Digite o novo Corte: ", end="")
                    model = input().rstrip(" ").lstrip(" ").capitalize()
                    print("\n Novo Corte: " + str(model))
                case 6:
                    skull = print("Digite o novo Skull: ", end="")
                    skull = input().upper().rstrip(" ").lstrip(" ")
                    print("\n Novo Skull: " + str(skull))
                case 7:
                    quant = print("Digite a nova Quantidade: ", end="")
                    quant = input().rstrip(" ").lstrip(" ")
                    print("\n Nova Quantidade: " + str(quant))
                case 8:
                    price = print("Digite o novo Preço: ", end="")
                    price = input().rstrip(" ").lstrip(" ")
                    print("\n Novo Preço: " + str(price))
                case 9:
                    # registrar nova tupla com alteração
                    product = (cod, brand, club, season, size, model, skull, quant, price)
                    data[ind] = product
                    print("\n Informações de Produto editados com sucesso!!\n")
            option = options("editProduct")
        else:
            print(" \n Alterações Descartadas!! \n")
    else:
        print("\n Erro: Produto não encontrado!!\n")

def deleteProduct(data: list):
    cod = int(input(" Código: "))
    finded, ind = findProductForCod(data, cod)
    verification = True
    if finded:
        print(" \nRegistro Encontrado: ")
        listProductForCod(data, ind)
        while verification:
            print(" Tem certeza que deseja excluir este registro? (s|n): ", end="")
            option = input().lower()
            if option == "s":
                del(data[ind])
                print("\n Registro Excluído!! \n")
                verification = False
            elif option == "n":
                verification = False
            else:
                print("\n Erro: Digite 's' ou 'n' \n")
    else:
        print("\n Erro: código inválido!!\n")

def addProduct(data: list):

    print(" Marca: ", end="")
    brand = input().rstrip(" ").lstrip(" ").capitalize()
    print(" Time: ", end="")
    club = input().rstrip(" ").lstrip(" ").capitalize()
    print(" Temporada: ", end="")
    season = input().upper().rstrip(" ").lstrip(" ")
    print(" Tamanho: ", end="")
    size = input().upper().rstrip(" ").lstrip(" ")
    print(" Corte: ", end="")
    model = input().rstrip(" ").lstrip(" ").capitalize()
    print(" Skull: ", end="")
    skull = input().upper().rstrip(" ").lstrip(" ")
    print(" Quantidade: ", end="")
    quant = int(input())
    print(" Preço: R$", end="")
    price = int(input())
    product = (setCodeProduct(data), brand, club, season, size, model, skull, quant, price)
    data.append(product)
    print(" \nProduto incluso no estoque!\n")
#----------------------------------------------------------------------- Fim - Funçoes Estoque ----------------------------------------------------------------------

#----------------------------------------------------------------------- Inicio - Funçoes Venda --------------------------------------------------------------------
def listSales(data: list):
    print()
    print()
    print("| Cód.. | Vendedor      | Produto                     | Cód. Produto | Quantidade | Valor da Venda | Data da Venda |")
    print("-------- --------------- ----------------------------- -------------- ------------ ---------------- ----------------")
    count = 0
    for i in range(len(data)):
        (code, seller, codProduct, quant, value, date) = data[i]
        _, indProduct = findProductForCod(dataInv, codProduct)
        count += 1

        productName = dataInv[indProduct][2]
        productSeason = dataInv[indProduct][3]
        productSize = dataInv[indProduct][4]
        productModel = dataInv[indProduct][5]
        productType = productSeason + " " + productName + " " + productSize + " " + productModel

        # código
        print("| {:05d} |".format(code), end="")

        # vendedor
        if len(seller) > 13:
            seller = seller[:10] + "..."
        else:
            seller = seller.ljust(13)
        print(" " + seller, end=" |")

        # nome do Produto
        if len(productType) > 27:
            productType = productType[:24] + "..."
        else:
            productType = productType.ljust(27)
        print(" " + productType, end=" |")

        #Código do Produto
        print(" {:05d}        |".format(codProduct), end="")

        # unidades
        print(" {:03d}        |".format(quant), end="")

        # preço
        print(" R${:4d},00      |".format(value), end="")

        #data
        if len(date) > 13:
            date = date[:10] + "..."
        else:
            date = date.ljust(13)
        print(" " + date, end=" |")
        print("\n-------- --------------- ----------------------------- -------------- ------------ ---------------- ----------------")
        
    print("\nTotal de {:03d} Vendas Listadas!".format(count))
    print()

def listSaleForCod(data: list, var: int):
    print()
    print()
    print("| Cód.. | Vendedor      | Produto                     | Cód. Produto | Quantidade | Valor da Venda | Data da Venda |")
    print("-------- --------------- ----------------------------- -------------- ------------ ---------------- ----------------")
    (code, seller, codProduct, quant, value, date) = data[var]
    _, indProduct = findProductForCod(dataInv, codProduct)

    productName = dataInv[indProduct][2]
    productSeason = dataInv[indProduct][3]
    productSize = dataInv[indProduct][4]
    productModel = dataInv[indProduct][5]
    productType = productSeason + " " + productName + " " + productSize + " " + productModel

    # código
    print("| {:05d} |".format(code), end="")

    # vendedor
    if len(seller) > 13:
        seller = seller[:10] + "..."
    else:
        seller = seller.ljust(13)
    print(" " + seller, end=" |")

    # nome do Produto
    if len(productType) > 27:
        productType = productType[:24] + "..."
    else:
        productType = productType.ljust(27)
    print(" " + productType, end=" |")

    #Código do Produto
    print(" {:05d}        |".format(codProduct), end="")

    # unidades
    print(" {:03d}        |".format(quant), end="")

    # preço
    print(" R${:4d},00      |".format(value), end="")

    #data
    if len(date) > 13:
        date = date[:10] + "..."
    else:
        date = date.ljust(13)
    print(" " + date, end=" |")
    print("\n-------- --------------- ----------------------------- -------------- ------------ ---------------- ----------------")
    print()

def addSale(data: list):
    
    print(" Código do Produto: ", end="")
    codProduct = int(input())
    finded, indProduct = findProductForCod(dataInv, codProduct)
    if finded:
        print(" Vendedor: ", end="")
        seller = input().rstrip(" ").lstrip(" ").capitalize()

        print(" Unidades Vendidas: ", end="")
        quant = int(input())

        if 0 < quant <= dataInv[indProduct][7]:
            print(" Valor varejo de cada peça: R$", end="")
            price = int(input())

            sale = (setCode(data), seller, codProduct, quant, price * quant, date.today().isoformat())
            data.append(sale)
            removeQuantProduct(dataInv, indProduct, quant)

            print(" \nVenda Registrada com Sucesso!!\n")
        else:
            print("\n Erro: Não há essa quantidade de peça em estoque!! \n")
    else:
        print("\n Erro: Produto não encontrado no estoque!!\n")

def findSaleForCod(data: list, cod: int):
    for i in range(len(data)):
        (code, _, _, _, _, _) = data[i]
        if cod == code:
            return True, i
    return False, 0

def deleteSale(data: list):
    cod = int(input(" Código: "))
    finded, ind = findSaleForCod(data, cod)
    (_, _, b, a, _, _) = data[ind] #tupla da venda
    _, indProduct = findProductForCod(dataInv, b) # b = codigo do produto
    verification = True
    if finded:
        print(" \nRegistro Encontrado: ")
        listSaleForCod(data, ind)
        while verification:
            print(" Tem certeza que deseja excluir este registro? (s|n): ", end="")
            option = input().lower()
            if option == "s":
                del(data[ind])
                addQuantProduct(dataInv, indProduct, a)
                print("\n Registro Excluído!! \n")
                verification = False
            elif option == "n":
                verification = False
            else:
                print("\n Erro: Digite 's' ou 'n' \n")
    else:
        print("\n Erro: código inválido!!\n")

def filterSale(data: list):
    option = options("filterSale")
    while option != 5:
        match(option):
            case 1:
                print(" \nCódigo da venda: ", end="")
                code = int(input())
                finded, ind = findSaleForCod(data, code)
                if finded:
                    listSaleForCod(data, ind)
                else:
                    print("\n Venda não encontrada!! \n")
            case 2:
                print(" \nDigite o código do produto: ", end="")
                codProduct = int(input())
                listForCodProduct(data, codProduct)
            case 3:
                print(" \nDigite a Data (2022-06-29): ", end="")
                date = input().rstrip(" ").lstrip(" ")
                listForDate(data, date)
            case 4:
                print(" \nDigite o vendedor: ", end="")
                seller = input().upper().rstrip(" ").lstrip(" ").capitalize()
                listForSeller(data, seller)
        option = options("filterSale")

#----------------------------------------------------------------------- Fim - Funçoes Venda -----------------------------------------------------------------------

#----------------------------------------------------------------------- Inicio - Funçoes Compra -------------------------------------------------------------------
def addPurchase(data: list):
    
    print(" Código do Produto: ", end="")
    codProduct = int(input())
    finded, indProduct = findProductForCod(dataInv, codProduct)
    if finded:
        print(" Fornecedor: ", end="")
        provider = input().rstrip(" ").lstrip(" ").capitalize()

        print(" Unidades Compradas: ", end="")
        quant = int(input())

        print(" Valor custo de cada peça: R$", end="")
        price = int(input())

        product = (setCode(data), provider, codProduct, quant, price, date.today().isoformat())
        data.append(product)
        addQuantProduct(dataInv, indProduct, quant)

        print(" \nCompra Registrada com Sucesso!!\n")
    else:
        print("\n Erro: Produto não encontrado no estoque!!\n")

def deletePurchase(data: list):
    cod = int(input(" Código: "))
    finded, ind = findSaleForCod(data, cod)
    (_, _, b, a, _, _) = data[ind] #tupla da compra
    _, indProduct = findProductForCod(dataInv, b) # b = codigo do produto
    verification = True
    if finded:
        
        print(" \nCompra Encontrada: ")
        listPurchaseForCod(data, ind)
        while verification:
            print(" Tem certeza que deseja excluir esta compra? (s|n): ", end="")
            option = input().lower()
            if option == "s":
                del(data[ind])
                removeQuantProduct(dataInv, indProduct, a)
                print("\n Compra Excluída!! \n")
                verification = False
            elif option == "n":
                verification = False
            else:
                print("\n Erro: Digite 's' ou 'n' \n")
    else:
        print("\n Erro: código inválido!!\n")

def listPurchaseForCod(data: list, cod: int):
    print()
    print()
    print("| Cód.. | Fornecedor    | Cód. Produto | Quantidade | Valor da Compra | Data da Venda |")
    print("-------- --------------- -------------- ------------ ----------------- ----------------")
    (code, provider, codProduct, quant, value, date) = data[cod]
    valueTotaly = value * quant

    # código
    print("| {:05d} |".format(code), end="")

    # fornecedor
    if len(provider) > 13:
        provider = provider[:10] + "..."
    else:
        provider = provider.ljust(13)
    print(" " + provider, end=" |")

    #Código do Produto
    print(" {:05d}        |".format(codProduct), end="")

    # unidades
    print(" {:03d}        |".format(quant), end="")

    # preço
    print(" R${:6d},00      |".format(valueTotaly), end="")

    #data
    if len(date) > 13:
        date = date[:10] + "..."
    else:
        date = date.ljust(13)
    print(" " + date, end=" |")
    print("\n-------- --------------- -------------- ------------ ----------------- ----------------")
    print()

def listPurchase(data: list):
    print()
    print()
    print("| Cód.. | Fornecedor    | Cód. Produto | Quantidade | Valor da Compra | Data da Venda |")
    print("-------- --------------- -------------- ------------ ----------------- ----------------")
    count = 0
    for i in range(len(data)):
        (code, provider, codProduct, quant, value, date) = data[i]
        count += 1
        valueTotaly = value * quant

        # código
        print("| {:05d} |".format(code), end="")

        # fornecedor
        if len(provider) > 13:
            provider = provider[:10] + "..."
        else:
            provider = provider.ljust(13)
        print(" " + provider, end=" |")

        #Código do Produto
        print(" {:05d}        |".format(codProduct), end="")

        # unidades
        print(" {:03d}        |".format(quant), end="")

        # preço
        print(" R${:6d},00      |".format(valueTotaly), end="")

        #data
        if len(date) > 13:
            date = date[:10] + "..."
        else:
            date = date.ljust(13)
        print(" " + date, end=" |")
        print("\n-------- --------------- -------------- ------------ ----------------- ----------------")
        
    print("\nTotal de {:03d} Vendas Listadas!".format(count))
    print()

def filterPurchase(data: list):
    option = options("filterSale")
    while option != 5:
        match(option):
            case 1:
                print(" \nCódigo da compra: ", end="")
                code = int(input())
                finded, ind = findSaleForCod(data, code)
                if finded:
                    listPurchaseForCod(data, ind)
                else:
                    print("\n Venda não encontrada!! \n")
            case 2:
                print(" \nDigite o código do produto: ", end="")
                codProduct = int(input())
                listForCodProduct(data, codProduct)
            case 3:
                print(" \nDigite a Data (2022-06-29): ", end="")
                date = input().rstrip(" ").lstrip(" ")
                listForDate(data, date)
            case 4:
                print(" \nDigite o fornecedor: ", end="")
                seller = input().upper().rstrip(" ").lstrip(" ").capitalize()
                listForSeller(data, seller)
        option = options("filterSale")
#----------------------------------------------------------------------- Fim - Funçoes Relatório -------------------------------------------------------------------

#----------------------------------------------------------------------- Inicio - Funçoes Relatório -------------------------------------------------------------------
def listRelatorySale():
    totalySale = len(dataSale) #Total de Vendas cadastradas no sistema
    totalyValue = 0
    totalyUni = 0
    for i in range(len(dataSale)):
        (_, _, _, d, e, _) = dataSale[i] # d = Quantidade de camisas vendidas por venda \\\\ e = valor total da venda
        totalyValue += e
        totalyUni += d
    return totalySale, totalyValue, totalyUni

def listRelatoryPurchase():
    totalySale = len(dataPurchase) #Total de Compras cadastradas no sistema
    totalyValue = 0
    totalyUni = 0
    for i in range(len(dataPurchase)):
        (_, _, _, d, e, _) = dataPurchase[i] # d = Quantidade de camisas compradas por compra \\\\ e = valor total da compra
        v = e * d
        totalyValue += v
        totalyUni += d
    return totalySale, totalyValue, totalyUni

def printRelatory(string: str):
    a, b, c = listRelatorySale()
    d, e, f = listRelatoryPurchase()
    while True:
        match(string):
            case "sale":
                slowPrint("\n#####################################", 0.01)
                slowPrint("\n##                                 ##", 0.01)
                slowPrint("\n##         -- DLGestor --          ##", 0.01)
                slowPrint("\n##   Relatório Básico de Vendas    ##", 0.01)
                slowPrint("\n##                                 ##", 0.01)
                slowPrint("\n#####################################", 0.01)
                print()
                slowPrint("\n Total de Vendas no Sistema: {:3d}".format(a), 0.03)
                slowPrint("\n Total de Produtos Vendidos: {:3d}".format(c), 0.03)
                slowPrint("\n Valor Total em Vendas: R${:5d},00".format(b), 0.03)
                print()
                print()
            case "purchase":
                slowPrint("\n#####################################", 0.01)
                slowPrint("\n##                                 ##", 0.01)
                slowPrint("\n##         -- DLGestor --          ##", 0.01)
                slowPrint("\n##   Relatório Básico de Compras   ##", 0.01)
                slowPrint("\n##                                 ##", 0.01)
                slowPrint("\n#####################################", 0.01)
                print()
                slowPrint("\n Total de Compras no Sistema: {:3d}".format(d), 0.03)
                slowPrint("\n Total de Produtos Comprados: {:3d}".format(f), 0.03)
                slowPrint("\n Valor Total em Compras: R${:5d},00".format(e), 0.03)
                print()
                print()
            case "all":
                slowPrint("\n################################", 0.01)
                slowPrint("\n##                            ##", 0.01)
                slowPrint("\n##       -- DLGestor --       ##", 0.01)
                slowPrint("\n##   Relatório Básico Geral   ##", 0.01)
                slowPrint("\n##                            ##", 0.01)
                slowPrint("\n################################", 0.01)
                print()
                slowPrint("\n Total de Registros no sistema(Compras/Vendas): {:3d}".format(d + a), 0.03)
                slowPrint("\n Total de Produtos em Estoque: {:3d}".format(f - c), 0.03)
                slowPrint("\n Valor Total Gasto: R${:5d},00".format(e), 0.03)
                slowPrint("\n Valor Total Ganho: R${:5d},00".format(b), 0.03)
                slowPrint("\n Lucro Total: R${:5d},00".format(b - e), 0.03)
                print()
                print()
        return string
#----------------------------------------------------------------------- Fim - Funçoes Relatório -------------------------------------------------------------------

#----------------------------------------------------------------------- Inicio - Funçoes Login -----------------------------------------------------------------------
def autenticate(data: list, log, pas):
    for i in range(len(data)):
        (login, passw) = data[i]
        if type(login) == type(log) and login == log:
            if type(pas) == type(passw) and pas == passw:
                return True
    return False
#----------------------------------------------------------------------- Fim - Funçoes Login --------------------------------------------------------------------------

#----------------------------------------------------------------------- Inicio - Funçoes Globais ---------------------------------------------------------------------
def listForCodProduct(data: list, codProduct: int):
    listSecondary = []
    for i in range(len(data)):
        sale = (_, _, c, _, _, _) = data[i]
        if c == codProduct:
            listSecondary.append(sale)
    if listSecondary != []:
        listSales(listSecondary)
    else:
        print("\n Nenhuma Venda Encontrada!! \n")

def listForDate(data: list, string: str):
    listSecondary = []
    for i in range(len(data)):
        sale = (_, _, _, _, _, f) = data[i]
        if f == string:
            listSecondary.append(sale)
    if listSecondary != []:
        listSales(listSecondary)
    else:
        print("\n Nenhuma Venda Encontrada!! \n")

def listForSeller(data: list, string: str):
    listSecondary = []
    for i in range(len(data)):
        sale = (_, b, _, _, _, _) = data[i]
        if b == string:
            listSecondary.append(sale)
    if listSecondary != []:
        listSales(listSecondary)
    else:
        print("\n Nenhuma Venda Encontrada!! \n")

def removeQuantProduct(data: list, ind: int, quant: int):
    (code, brand, club, season, size, model, skull, qtd, price) = data[ind]
    newQuant = qtd - quant
    product = (code, brand, club, season, size, model, skull, newQuant, price)
    data[ind] = product

def addQuantProduct(data: list, ind: int, quant: int):
    (code, brand, club, season, size, model, skull, qtd, price) = data[ind]
    newQuant = qtd + quant
    product = (code, brand, club, season, size, model, skull, newQuant, price)
    data[ind] = product

def options(menu: str):
    while True:
        match(menu):
            case "inventory":
                print("\nGerenciamento de Estoque")
                print(" Opções:")
                print("  1) Listar Todos os Produtos")
                print("  2) Adicionar Produto")
                print("  3) Buscar Produto")
                print("  4) Excluir Produto")
                print("  5) Editar Produto")
                print("  6) Voltar ao Menu")
                print("\n Digite o número da opção desejada: ", end="")
                option = int(input())
                if 1 <= option <= 6:
                    return option
                else:
                    print("\n Erro: opção inválida!\n")

            case "editProduct":
                print("\n Opções:")
                print("  1) Marca")
                print("  2) Time")
                print("  3) Temporada")
                print("  4) Tamanho")
                print("  5) Corte")
                print("  6) Skull ")
                print("  7) Quantidade")
                print("  8) Preço")
                print("  9) Confirmar")
                print(" 10) Voltar(Descartar Alterações)")
                print("\n Digite o número da opção que deseja editar: ", end="")
                option = int(input())
                if 1 <= option <= 10:
                    return option
                else:
                    print("\n Erro: opção inválida!\n")

            case "filters":
                print("\n Filtros:")
                print("  1) Código")
                print("  2) Marca")
                print("  3) Time")
                print("  4) Temporada")
                print("  5) Tamanho")
                print("  6) Corte ")
                print("  7) Quantidade")
                print("  8) Preço")
                print("  9) Em estoque")
                print(" 10) Uniforme (1, 2, 3)")
                print(" 11) Versão (Torcedor, Jogador)")
                print(" 12) Voltar")
                print("\n Digite o número da opção que deseja filtrar: ", end="")
                option = int(input())
                if 1 <= option <= 12:
                    return option
                else:
                    print("\n Erro: opção inválida!\n")
            case "menu":
                print("\nOpções:")
                print("  1) Vendas")
                print("  2) Estoque")
                print("  3) Compras")
                print("  4) Relatórios")
                print("  5) Sair")
                print("\n Digite o número da opção que deseja: ", end="")
                option = int(input())
                if 1 <= option <= 5:
                    return option
                else:
                    print("\nErro: Opção Inválida!\n")
            case "sales":
                print("\nOpções:")
                print("  1) Listar Vendas")
                print("  2) Nova Venda")
                print("  3) Excluir Venda")
                print("  4) Filtrar Vendas")
                print("  5) Voltar")
                print("\n Digite o número da opção que deseja: ", end="")
                option = int(input())
                if 1 <= option <= 5:
                    return option
                else:
                    print("\nErro: Opção Inválida!\n")
            case "purchase":
                print("\nOpções:")
                print("  1) Listar Compras")
                print("  2) Registrar Compra")
                print("  3) Excluir Compra")
                print("  4) Filtrar Compras")
                print("  5) Voltar")
                print("\n Digite o número da opção que deseja: ", end="")
                option = int(input())
                if 1 <= option <= 5:
                    return option
                else:
                    print("\nErro: Opção Inválida!\n")
            case "relatory":
                print("\nOpções:")
                print("  1) Relatório de Vendas")
                print("  2) Relatório de Compras")
                print("  3) Relatório Total")
                print("  4) Voltar")
                print("\n Digite o número da opção que deseja: ", end="")
                option = int(input())
                if 1 <= option <= 4:
                    return option
                else:
                    print("\nErro: Opção Inválida!\n")
            case "filterSale":
                print("\nFiltros:")
                print("  1) Código")
                print("  2) Produto")
                print("  3) Data")
                print("  4) Vendedor")
                print("  5) Voltar")
                print("\n Digite o número da opção que deseja: ", end="")
                option = int(input())
                if 1 <= option <= 5:
                    return option
                else:
                    print("\nErro: Opção Inválida!\n")
            case "filterPurchase":
                print("\nFiltros:")
                print("  1) Código")
                print("  2) Produto")
                print("  3) Data")
                print("  4) Fornecedor")
                print("  5) Voltar")
                print("\n Digite o número da opção que deseja: ", end="")
                option = int(input())
                if 1 <= option <= 5:
                    return option
                else:
                    print("\nErro: Opção Inválida!\n")
        return menu

def inventory():
    
    op = options("inventory")
    while op != 6:
        match op:
            case 1:
                listProducts(dataInv)
            case 2:
                addProduct(dataInv)
            case 3:
                filterProducts(dataInv)
            case 4:
                deleteProduct(dataInv)
            case 5:
                editProduct(dataInv)
        op = options("inventory")

def purchase():
    op = options("purchase")
    while op != 5:
        match op:
            case 1:
                listPurchase(dataPurchase)
            case 2:
                addPurchase(dataPurchase)
            case 3:
                deletePurchase(dataPurchase)
            case 4:
                filterPurchase(dataPurchase)
        op = options("purchase")

def relatory():
    op = options("relatory")
    while op != 4:
        match op:
            case 1:
                printRelatory("sale")
            case 2:
                printRelatory("purchase")
            case 3:
                printRelatory("all")
        op = options("relatory")

def sale():
    op = options("sales")
    while op != 5:
        match op:
            case 1:
                listSales(dataSale)
            case 2:
                addSale(dataSale)
            case 3:
                deleteSale(dataSale)
            case 4:
                filterSale(dataSale)
        op = options("sales")

def menu():
    op = options("menu")
    while op != 5:
        match op:
            case 1:
                sale()
            case 2:
                inventory()
            case 3:
                purchase()
            case 4:
                relatory()
        op = options("menu")
    print("\n\nAté logo!\n\n")

def login():
    
    slowPrint("\n#####################################", 0.01)
    slowPrint("\n##                                 ##", 0.01)
    slowPrint("\n##          -- DLGestor --         ##", 0.05)
    slowPrint("\n##   Sistema de Gestão Comercial   ##", 0.05)
    slowPrint("\n##     Feito para sua empresa      ##", 0.05)
    slowPrint("\n##         By Delandi Lucas        ##", 0.05)
    slowPrint("\n##           BETA 1.0.10           ##", 0.01)
    slowPrint("\n##                                 ##", 0.01)
    slowPrint("\n#####################################", 0.01)
    while True: 
        slowPrint("\n\nLogin: ", 0.1)
        login = input().lstrip(" ").rstrip(" ").lower()
        
        
        password = getpass("\nSenha: ")

        autenticated = autenticate(users, login, password)
        if autenticated:
            print("\nLogin Efetuado com Sucesso!!\n")
            print("Bem Vindo " + login)
            menu()
        else:
            print("\nErro: Login ou Senha Incorretos...\n")
            print("Tente Novamente..")
#----------------------------------------------------------------------- Fim - Funçoes Globais ------------------------------------------------------------------------

if __name__ == "__main__":
    login()
