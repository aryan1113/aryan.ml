'''
had a bunch of .txt files with items without any numbering
and wished to have a numerical order to things for media/watchlist
simple python scripts that numbers lines
'''

def number_lines(input_text):
    # split the input text into lines
    lines = input_text.split('\n')
    
    # number the lines, removing any empty lines
    numbered_lines = [f"{i+1}. {line.strip()}" for i, line in enumerate(lines) if line.strip()]
    
    # join the numbered lines back together
    return '\n'.join(numbered_lines)

# check for fragment of list 'web-series'
input_text = """Sense8
Maniac Emma Stone
Alice In Borderland 2020	
Itaewon class (korean) 
Law School (netflix korea)
Silicon valley
Dial 100
Everybody Hates Chris
Squid game
Parks and Recreation
Beyond evil (korean)
Lost in spaceS
"""

print(number_lines(input_text))