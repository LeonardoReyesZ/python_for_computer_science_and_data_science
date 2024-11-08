# ex_9.9: Telephone-number word generator -> file

def telephoneNumber(digits):
    if digits == "":
        return []
    d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    result = [""]
    for digit in digits:
        temp = []
        for letter in d[digit]:
            for r in result:
                temp.append(r + letter)
        result = temp
    result.sort()
    for i in range(len(result)):
        print(i+1, result[i])
    return result
# end telephoneNumber


result = telephoneNumber("25495")

with open('telephoneNumber.txt', 'w') as file:
    for telephone in result:
        file.write(telephone+'\t')