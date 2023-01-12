from Day11_The_Blackjack.logo import logo
import os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, text, shift):
    '''
    direction : 決定要編碼還是解碼
    text : 輸入的文字
    shift : 平移的數量
    '''
    #根據輸入的平移數量，平移原始的單字庫
    alphabet_re = alphabet[shift:] + alphabet[:shift]

    #創建一個空的list來儲存輸入字串的index
    text_index = []
    text_re = []
    text_re_str = ''

    if direction == 'encode':
        #對於輸入的字串的每個字查詢其index，並且添加到text_index當中
        for i in text:
            text_index.append(alphabet.index(i))

        #透過原始的index到平移後的單字庫找出對應的字
        for i in text_index:
            text_re.append(alphabet_re[i])
        text_re_str += ''.join(text_re)
        return text_re_str

    else:
        #對於輸入的字串的每個字查詢其index，並且添加到text_index當中
        for i in text:
            text_index.append(alphabet_re.index(i))
        
        #透過原始的index到平移後的單字庫找出對應的字
        for i in text_index:
            text_re.append(alphabet[i])
        text_re_str += ''.join(text_re)
        return text_re_str

again = True


while again:
    print(logo)
    text_re_list = []
    result = ''
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    text_list = text.split(' ')
    shift = int(input("Type the shift number:\n"))
    for word in text_list:
        text_re_str = caesar(direction, word, shift)
        text_re_list.append(text_re_str)
    result += ' '.join(text_re_list)
    print(f"Here is the answer {result}")
    user = input("Try again?  Y/N").lower()
    os.system('cls')
    if user == 'n':
        again = False