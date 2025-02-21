word = 'Python'
word = 'Ali Raza'
if(len(word)>3):
    newword = word[0]
    word1 = []
    for createlist in word[1:]:
        word1.append(createlist)
    word1.append(newword)
    string_list = [str(element) for element in word1]
    delimiter = ""
    result_string = delimiter.join(string_list)
    endodedword = f'rio{result_string}rio'
    print('The Encoded word is',endodedword)
    re_write = endodedword.replace('rio','')
    rewrite = re_write[len(re_write)-1]
    rewrite1 = re_write[:-1]
    decodedworld = f'{rewrite}{rewrite1}'
    print('The Decoded word is',decodedworld)

