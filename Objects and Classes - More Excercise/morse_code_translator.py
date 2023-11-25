morse_code_msg = input().split(" | ")

morse_code_dic = {'-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
                  '.....': '5', '-....': '6', '--...': '7', '---..': '8','----.': '9',
                  '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
                  '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K',
                  '.-..': 'L', '--': 'M',  '-.': 'N', '---': 'O', '.--.': 'P',
                  '--.-': 'Q', '.-.': 'R',  '...': 'S', '-': 'T', '..-': 'U',
                  '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z'}

result = ""
for word in morse_code_msg:
    for letter in word.split():
        if letter in morse_code_dic.keys():
            result += morse_code_dic[letter]
    result += " "

print(result[0:-1])