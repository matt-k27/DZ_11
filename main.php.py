print('DZ11')

iterator = 0
inputtedActionContinue = ''

while True:
    if iterator != 0:
        inputtedActionContinue = str(input('Do you want to perform another calculation? '))

    if iterator == 0 or (inputtedActionContinue == 'y' or inputtedActionContinue == 'yes'):
        inputtedNumber1 = float(input('Please enter first number : '))
        inputtedNumber2 = float(input('Please enter second number : '))
        inputtedAction = str(input('Please enter action : '))

        if inputtedAction == '+':
            print(inputtedNumber1 + inputtedNumber2)
        elif inputtedAction == '-':
            print(inputtedNumber1 - inputtedNumber2)
        elif inputtedAction == '*':
            print(inputtedNumber1 * inputtedNumber2)
        elif inputtedAction == '/':
            if inputtedNumber2 == 0:
                print('You can\'t divide by 0')
            else:
                print(inputtedNumber1 / inputtedNumber2)
        else:
            print('Invalid')

        iterator += 1
    else:
        print('Thank you for using')
        break


###############################################################

# while True:
#     inputtedActionContinue = str(input('Do you want to perform another calculation? '))
#
#     if inputtedActionContinue == 'y' or inputtedActionContinue == 'yes':
#         inputtedNumber1 = float(input('Please enter first number : '))
#         inputtedNumber2 = float(input('Please enter second number : '))
#         inputtedAction = str(input('Please enter action : '))
#
#         if inputtedAction == '+':
#             print(inputtedNumber1 + inputtedNumber2)
#         elif inputtedAction == '-':
#             print(inputtedNumber1 - inputtedNumber2)
#         elif inputtedAction == '*':
#             print(inputtedNumber1 * inputtedNumber2)
#         elif inputtedAction == '/':
#             if inputtedNumber2 == 0:
#                 print('You can\'t divide by 0')
#             else:
#                 print(inputtedNumber1 / inputtedNumber2)
#         else:
#             print('Invalid')
#     else:
#         print('Thank you for using')
#         break
