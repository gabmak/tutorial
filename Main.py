class Calculator:

    def findClass(income):
        if income == 0:
            return 'no'
        elif income <= 45000:
            return 'first'
        elif income <= 90000:
            return 'second'
        elif income <= 135000:
            return 'third'
        elif income > 135000:
            return 'forth'
        else:
            return

    def calculateSingle(income, taxClass):
        if taxClass == 'no':
            return 0
        elif taxClass == 'first':
            subTotal = Calculator.multipleCal(income, 0.02)
            return subTotal
        elif taxClass == 'second':
            remainder = Calculator.checkRemainder(income, 45000)
            subTotal = 900 + Calculator.multipleCal(remainder, 0.07)
            return subTotal
        elif taxClass == 'third':
            remainder = Calculator.checkRemainder(income, 90000)
            subTotal = 900 + 3150 + Calculator.multipleCal(remainder, 0.12)
            return subTotal
        elif taxClass == 'forth':
            remainder = Calculator.checkRemainder(income, 135000)
            subTotal = 900 + 3150 + 5400 + Calculator.multipleCal(remainder, 0.17)
            return subTotal

    def taxReduction (subtotal):
        subtotal = float(subtotal)
        if subtotal * 0.75 >= 20000:
            return 20000
        else:
            return subtotal * 0.75

    def checkRemainder(value, ceiling):
        if value == ceiling:
            return ceiling
        else:
            return value - ceiling

    def multipleCal(amount, percentage):
        returnValue = amount * percentage
        return returnValue

    def findCharageableIncome(income, MPF, allowance):
        if float(income) * float(MPF) > 15000:
            lessMPF = 15000
        else:
            lessMPF = float(income) * float(MPF)

        netTotalIncome = float(income) - float(lessMPF)
        if netTotalIncome-allowance <= 0:
            return 0
        else:
            return netTotalIncome-allowance

    def processTax(income):
        classValue = Calculator.findClass(income)
        subTotal = Calculator.calculateSingle(income, classValue)
        taxReductionValue = Calculator.taxReduction(subTotal)
        taxPayable = subTotal - taxReductionValue
        print(classValue)
        print(taxPayable)
        return taxPayable

    #Main
    def mainProgram(firstPerson, secondPerson):

        combineIncome = firstPerson + secondPerson
        firstCharageable = Calculator.findCharageableIncome(firstPerson, 0.05, 132000)
        secondCharageable = Calculator.findCharageableIncome(secondPerson, 0.05, 132000)

        combineCharageable = Calculator.findCharageableIncome(combineIncome, 0.05, 132000+132000)
        print(combineCharageable)

        if (firstPerson >= 0) and (secondPerson >= 0):
            firstPersonTotalTax = Calculator.processTax(firstCharageable)
            print(firstPersonTotalTax)
            secondPersonTotalTax = Calculator.processTax(secondCharageable)
            print(secondPersonTotalTax)
            individualTotal = firstPersonTotalTax + secondPersonTotalTax
            print(combineCharageable)
            combineTotalTax = Calculator.processTax(combineCharageable)

            print("individual: ",  individualTotal)
            print("combine: ", combineTotalTax)
            if combineTotalTax < individualTotal:
                print("Joint")
                return "Use joint"
            elif combineTotalTax == individualTotal:
                print("Same")
                return 'Same!'
            else:
                print("Use individual")
                return 'Use individual'
        else:
            print('Error')
            return 'Error'
