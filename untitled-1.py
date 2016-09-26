def decode_letters(L):
    message = []
    for item in L:
        word = ''
        for code in item:
            word += chr(code)
        message.append(word)
    return message

def decode_letters_mutate(L):
    message = []
    for item in L:
        word = ''
        for code in item:
            word += chr(code)
        message.append(word)
    for index in range(len(L)):
        L[index] = message[index]
        
def count_even_numbers(num1,num2):
    count = 0
    L = list(range(num1,num2))
    for item in L:
        if item % 2 == 0:
            count += 1
    return count


def numeric_report(report_name, month_to_quarter):
    month = report_name[-1]
    report = 0
    for quarter in month_to_quarter:
        if month in quarter:
            report += 1
            lst = list(report_name)
            lst[-1] = str(report)    
            return ''.join(lst)
        else:
            report += 1


