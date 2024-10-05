

def symbol_statistics(text):
    stat ={}
    for letter in text:
        letter = letter.lower()
        stat[letter] = stat.get(letter, 0) + 1
    return stat
text = input('Input text ->') 
stat = symbol_statistics(text) 
for symbol in sorted(stat):
    print(symbol, '=', stat[symbol])