#%%
import itertools
import numpy as np



# %%
def generate_sentences(num_of_all_holes, count):
    with open('testfile.txt', 'w+') as file:
        for i in range(1,7):
            indexes = list(range(1,8))
            permutations = set(itertools.product(indexes, repeat=i))
            for p in permutations:
                for _ in range(3):
                    if count <= 0: 
                        break
                    line_arr = np.random.permutation([0] * (num_of_all_holes - i) + list(p))
                    line = ' '.join([str(v) for v in line_arr])
                    file.writelines(line + '\n')
                    count -= 1

#%%
def get_sentences():
    base = 'A királynét megölni nem kell félnetek jó lesz ha mindenki egyetért én nem ellenzem.'
    parts = base.split()

    ending_punctuation = ['. ', '? ', '! ', '... ']
    between_punctuation = [', ', '; ', ': ']
    add_punct = ' '

    permutations_from_file = []
    with open('testfile.txt', 'r') as file:
        lines = [line.rstrip() for line in file]

    for line in lines:
        permutations_from_file.append([int(e) for e in line.split()])

    while(len(permutations_from_file)):
        random_index = np.random.randint(0, len(permutations_from_file))
        random_sequence = permutations_from_file.pop(random_index)
        all_punctuations = [add_punct] + between_punctuation + ending_punctuation
        generated_punctuations = []
        for punctuation_idx in random_sequence:
            char = all_punctuations[punctuation_idx]
            generated_punctuations.append(char)

        tmp = parts.copy()
        sentence = tmp.pop(0)
        for part, punctuation in zip(tmp, generated_punctuations):
            sentence += punctuation + (part.capitalize() if punctuation in ending_punctuation else part)
            
        yield sentence

# %%
generate_sentences(num_of_all_holes=13, count=40000)

# %%
def get_all():
    while True:
        try:
            yield get_sentences()
        except:
            print('No more sentences left')
            break
    
# %%
with open('generated_sentences.txt', 'w+') as f:
    f.writelines() 


#%%
get_all()
# %%
queens = []
for e in get_sentences():
    queens.append(e + '\n')

with open('generated_sentences.txt', 'w+', encoding='utf-8') as f:
    f.writelines(queens) 
# %%
