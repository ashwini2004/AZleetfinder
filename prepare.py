# read the index.txt and prepare documents, vocab , idf

import chardet

def find_encoding(fname):
    r_file = open(fname, 'rb').read()
    result = chardet.detect(r_file)
    charenc = result['encoding']
    return charenc

filename = 'Leetcode/Qdata/index.txt'
my_encoding = find_encoding(filename)

with open(filename, 'r', encoding=my_encoding, errors='ignore') as f:  # add the 'errors' parameter to ignore any characters that cannot be encoded
    lines = f.readlines()

def preprocess(document_text):
    # remove the leading numbers from the string, make everything lowercase
    terms = [term.lower() for term in document_text.strip().split()[1:]]
    return terms

sus_words = ['n','return','given','you','if','number','example','a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'was', 'were', 'will', 'with']
def bodyprocess(data_list):
    text = []
    for data in data_list:
        data.strip()
        data = data.lower()
        if data == 'Example 1:':
            break
        else:
            data = data.replace('\u2192', '->')  # replace the character with an alternative character
            words = data.split()  # split the line into words
            for word in words:
                if word.isalpha() and word not in sus_words:
                    text.append(word)
    return text


vocab = {}
headings = []
documents = []

for index, line in enumerate(lines):
    # read statement and add it to the line and then preprocess and then adding it to headings
    tokens = preprocess(line)
    headings.append(tokens)
    # reading the body, preprocessing
    filepath = 'Leetcode/Qdata/'+ str(index+1) + '/' + str(index+1) + '.txt'
    with open(filepath, 'r',encoding='utf-8') as f:
        datas = f.readlines()
    body = bodyprocess(datas)
    tokens = tokens + body
    # appending in the documents which is a list of lists
    documents.append(tokens)
    tokens = set(tokens)
    for token in tokens:
        if token not in vocab:
            vocab[token] = 1
        else:
            vocab[token] += 1

# reverse sort the vocab by the values
vocab = dict(sorted(vocab.items(), key=lambda item: item[1], reverse=True))

print('Number of documents: ', len(documents))
print('Size of vocab: ', len(vocab))
print('Sample document: ', documents[0])

# save the vocab in a text file
with open('tf-idf/vocab.txt', 'w') as f:
    for key in vocab.keys():
        f.write("%s\n" % key)

# save the idf values in a text file
with open('tf-idf/idf-values.txt', 'w') as f:
    for key in vocab.keys():
        f.write("%s\n" % vocab[key])

# save the documents in a text file
with open('tf-idf/documents.txt', 'w') as f:
    for document in documents:
        f.write("%s\n" % ' '.join(document))

with open('tf-idf/headings.txt', 'w') as f:
    for heading in headings:
        f.write("%s\n" % ' '.join(heading))


inverted_index = {}
for index, document in enumerate(documents):
    for token in document:
        if token not in inverted_index:
            inverted_index[token] = [index]
        else:
            inverted_index[token].append(index)

# save the inverted index in a text file
with open('tf-idf/inverted-index.txt', 'w') as f:
    for key in inverted_index.keys():
        f.write("%s\n" % key)
        f.write("%s\n" % ' '.join([str(doc_id) for doc_id in inverted_index[key]]))