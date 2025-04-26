def count_sentence(sentence):
    words = accumulate(lambda x, y: 1+y, 0, sentence)
    letters = accumulate(lambda x, y: len(x)+1+y, -1, sentence)
    return [words, letters]

# Order of growth?: Time: O(n), where n = number of words in the sentences (ie length of the sentence)
# Space: O(n), due to n recursive calls

#### DO NOT EDIT ANYTHING BEYOND THIS LINE. IT IS FOR YOUR REFERENCE ONLY!

def accumulate(op, init, seq):
    if not seq:
        return init
    else:
        return op(seq[0], accumulate(op, init, seq[1:]))

def accumulate_n(op, init, sequences):
    if (not sequences) or (not sequences[0]):
        return type(sequences)()
    else:
        return ( [accumulate(op, init, list((map(lambda x: x[0], sequences))))]
               + accumulate_n(op, init, list((map(lambda x: x[1:], sequences)))))
    

print(count_sentence([['C', 'S', '1', '0', '1', '0', 'S'], ['R', 'o', 'c', 'k', 's']])) # [2, 13]
print(count_sentence([['P', 'y', 't', 'h', 'o', 'n'], ['i', 's'], ['c', 'o', 'o', 'l']])) # [3, 14]