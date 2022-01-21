def sumOfElements(firstTerm, *otherTerms):
    s = firstTerm + sum(otherTerms)
    print(s)

sumOfElements(10, 10, 10, 10, 10)
sumOfElements(10, 10)
sumOfElements(10, 10, 10)
