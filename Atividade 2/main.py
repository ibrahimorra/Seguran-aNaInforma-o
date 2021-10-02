from collections import Counter


def runsTest(key):
    count = 1
    repeticoes = []
    firstCounter = [0, 0, 0, 0, 0, 0]
    secondCounter = [0, 0, 0, 0, 0, 0]
    if len(key) > 1:
        for i in range(1, len(key)):
            if key[i - 1] == key[i]:
                count += 1
            else:
                repeticoes.append([key[i - 1], count])
                count = 1
        repeticoes.append([key[i], count])

    for repet in repeticoes:
        if repet[0] == "0":
            if repet[1] >= 6:
                firstCounter[5] += 1
            else:
                firstCounter[repet[1] - 1] += 1
        if repet[0] == "1":
            if repet[1] >= 6:
                secondCounter[5] += 1
            else:
                secondCounter[repet[1] - 1] += 1

    is_0_true = False
    is_1_true = False
    if (
        (firstCounter[0] > 2267)
        and (firstCounter[0] < 2733)
        and (firstCounter[1] > 1079)
        and (firstCounter[1] < 1421)
        and (firstCounter[2] > 502)
        and (firstCounter[2] < 748)
        and (firstCounter[3] > 223)
        and (firstCounter[3] < 402)
        and (firstCounter[4] > 90)
        and (firstCounter[4] < 223)
        and (firstCounter[5] > 90)
        and (firstCounter[5] < 223)
    ):
        is_0_true = True

    if (
        (secondCounter[0] > 2267)
        and (secondCounter[0] < 2733)
        and (secondCounter[1] > 1079)
        and (secondCounter[1] < 1421)
        and (secondCounter[2] > 502)
        and (secondCounter[2] < 748)
        and (secondCounter[3] > 223)
        and (secondCounter[3] < 402)
        and (secondCounter[4] > 90)
        and (secondCounter[4] < 223)
        and (secondCounter[5] > 90)
        and (secondCounter[5] < 223)
    ):
        is_1_true = True

    return is_0_true and is_1_true


def monobitQuantityt(key):
    return key.count("1")


def poker(key):
    segmentos = [key[i : i + 4] for i in range(0, len(key), 4)]
    count = Counter(segmentos)
    f_i = sum(quant * quant for string, quant in count.items())
    x = ((16 / 5000) * f_i) - 5000

    return (x > 1.03) and (x < 57.4)


def pokerQuantity(key):
    segmentos = [key[i : i + 4] for i in range(0, len(key), 4)]
    return Counter(segmentos)


def runsQuantityTest(key):
    count = 1
    repeticoes = []
    firstCounter = [0, 0, 0, 0, 0, 0]
    secondCounter = [0, 0, 0, 0, 0, 0]
    if len(key) > 1:
        for i in range(1, len(key)):
            if key[i - 1] == key[i]:
                count += 1
            else:
                repeticoes.append([key[i - 1], count])
                count = 1
        repeticoes.append([key[i], count])

    for repet in repeticoes:
        if repet[0] == "0":
            if repet[1] >= 6:
                firstCounter[5] += 1
            else:
                firstCounter[repet[1] - 1] += 1
        if repet[0] == "1":
            if repet[1] >= 6:
                secondCounter[5] += 1
            else:
                secondCounter[repet[1] - 1] += 1
    print("- Quantidade de cada sequencia do Run test para zeros: " + str(firstCounter))
    print("- Quantidade de cada sequencia do Run test para uns: " + str(secondCounter))


def longRun(key):
    count = 1

    if len(key) > 1:
        for i in range(1, len(key)):
            if key[i - 1] == key[i]:
                count += 1
            elif count >= 34:
                return False
            else:
                count = 1
    return True


def convertHexBinary(t):
    return "".join("{0:04b}".format(int(char, 16)) for char in t)


def monobit(key):
    number = key.count("1")
    return (number > 9654) and (number < 10346)


def main():
    filtered_binaries = []
    binary_fileKeys = []

    fileKeys = open("chaves.txt", "r")

    for item in fileKeys:
        temp = item[1:]
        temp = temp[:-2]
        a = len(temp)
        filtered_binaries.append(temp)
        binary_fileKeys.append(convertHexBinary(temp))

    for itemOnFile, binaryKey in enumerate(binary_fileKeys, start=1):
        monobitTest = monobit(binaryKey)
        quantityMonobit = monobitQuantityt(binaryKey)
        quantityPoker = pokerQuantity(binaryKey)
        pokerTest = poker(binaryKey)
        runs = runsTest(binaryKey)
        long = longRun(binaryKey)

        if monobitTest and pokerTest and runs and long:
            print("\n")
            print("Chave Numero: " + str(itemOnFile) + " -> APROVADA")
        else:
            print("\n")
            print("Chave Numero: " + str(itemOnFile) + " -> REPROVADA")
            print(
                "- Monobit: "
                + str(monobitTest)
                + " | Poker: "
                + str(pokerTest)
                + " | Runs: "
                + str(runs)
                + " | Long: "
                + str(long)
            )
        print("- quantidade Monobit: " + str(quantityMonobit))
        print(
            "- valor calculado no pokerTest e quantidade de cada nible "
            + str(quantityPoker)
        )
        runsQuantityTest(binaryKey)


main()
