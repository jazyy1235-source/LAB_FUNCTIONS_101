def printPattren(n: int) -> str:
    result = ""
    """Prints a descending pyramid pattern of numbers starting from n down to 1."""
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            result += str(j) + " "
        result += "\n"
    return result

pattrenOutput = printPattren(5)
print(pattrenOutput)
print(printPattren.__doc__)
