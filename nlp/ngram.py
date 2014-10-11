def ngram(terms, n=2):
    ret = []
    for i in range(0, len(terms)-n+1):
        ret.append(terms[i:i+n])
    return ret
