### Given a large chunk of text, identify the most frequently occurring trigram in it.
# If there are multiple trigrams with the same frequency, then print the one which occurred first.
# Trigrams are groups of three consecutive words in the same sentence which are separated by a single space and are case insensitive.

import re
import collections
import operator

class OrderedCounter(collections.Counter, collections.OrderedDict):
    'Counter that remembers the order elements are first encountered'

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, collections.OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (collections.OrderedDict(self),)

def parseToSentences(text):
    return re.split('\.\s*', text)[:-1]

trigrams = lambda a: zip(a, a[1:], a[2:])

def countTrigrams(sentences):
    trigrams = OrderedCounter()
    queue = collections.deque(maxlen=3)

    for sentence in sentences:
        queue.clear()
        for word in sentence.split():
            queue.append(word)
            if(len(queue) == 3):
                current = tuple(queue)
                trigrams[current[:3]] += 1

    while len(queue) > 3:
        queue.popleft()
        current = tuple(queue)
        trigrams[current[:3]] += 1

    return trigrams



def mostCommonTrigram(trigrams):
    return ' '.join(max(trigrams.items(), key=operator.itemgetter(1))[0]).lower()

text = "I promised to look after a friends cat for the week. My place has a glass atrium that goes through two levels I have put the cat in there with enough food and water to last the week. I am looking forward to the end of the week. It is just sitting there glaring at me it doesnt do anything else. I can tell it would like to kill me. If I knew I could get a perfect replacement cat I would kill this one now and replace it Friday afternoon. As we sit here glaring at each other I have already worked out several ways to kill it.\n"+"The simplest would be to drop heavy items on it from the upstairs bedroom though I have enough basic engineering knowledge to assume that I could build some form of spear like projectile device from parts in the downstairs shed. If the atrium was waterproof the most entertaining would be to flood it with water. It wouldnt have to be that deep just deeper than the cat.\n"+"I dont know how long cats can swim but I doubt it would be for a whole week. If it kept the swimming up for too long I could always try dropping things on it as well. I have read that drowning is one of the most peaceful ways to die so really it would be a win win situation for me and the cat I think.\n"+"My offsprings birthday is next week. Last birthday I told him to draw pictures of what he wanted as a visual list. When I inquired as to one image which I first took to be a box of coloured crayons I deciphered his explanations as it being tampons. In particular the multicoloured brand. His only references to the product were the adverts featuring a girl jumping out of a window onto a tree which lowered her into a bmw convertible full of friends an electric green street racing car with black flames and the ability to do a single handed handstand starjump on a dance machine to crowd applause.\n"+"I bought him a box and figured he would work it out. Yesterday I asked him what he wants for his birthday and he replied not tampons.\n"+"My offsprings birthday is next week. Last birthday I told him to draw pictures of what he wanted as a visual list. When I inquired as to one image which I first took to be a box of coloured crayons I deciphered his explanations as it being tampons. In particular the multicoloured brand. His only references to the product were the adverts featuring a girl jumping out of a window onto a tree which lowered her into a bmw convertible full of friends an electric green street racing car with black flames and the ability to do a single handed handstand starjump on a dance machine to crowd applause.\n"+"I bought him a box and figured he would work it out. Yesterday I asked him what he wants for his birthday and he replied not tampons.\n"+"At the local swimming pool canteen not realising until afterwards that my cat was caught in the elastic of my swimming shorts with the tip sticking out I purchased a packet of twisties and a can of coke before asking out the cat who served me but she said no.\n"+"I love you I. love you. I love. you."


sentences = parseToSentences(text)

print(mostCommonTrigram(countTrigrams(sentences)))