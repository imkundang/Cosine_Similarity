import math
def cos_similarity(a,b):
    ab=0
    suma=0
    sumb=0
    for i in range(len(a)):
        ab+=a[i] * b[i]
        suma+=a[i] * a[i]
        sumb+=b[i] * b[i]
    cosinesi=ab /math.sqrt(suma) * math.sqrt(sumb)
    print('Cosine similarity:', cosinesi)

a=[1,2,5]
b=[2,2,4]
#cos_similarity(a,b)

def counter(m):
    j=dict()
    for word in m:
        if word in j:
            j[word]= j[word] + 1
        else:
            j.update({word:1})
    return j



def take_cosine(vec1, vec2):

    intersection= set(vec1.keys()) & set(vec2.keys())
    n = sum([vec1[x] * vec2[x] for x in intersection])

    sum1= sum([vec1[x]**2 for x in vec1])
    sum2= sum([vec2[x]**2 for x in vec2])
    d= math.sqrt(sum1) * math.sqrt(sum2)
    if not d:
        return 0.0
    else:
        return float(n)/d



def text_to_vetor(text):
    words=text.split()
    return counter(words)



sent1= input("enter the first sentence\n")
sent2= input("enter the second sentence\n")

vector1=text_to_vetor(sent1)
vector2=text_to_vetor(sent2)

cosine=take_cosine(vector1,vector2)
print(cosine)