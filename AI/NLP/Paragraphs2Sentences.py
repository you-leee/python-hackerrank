### Break up given paragraphs into text into individual sentences
# Abbreviations: Dr. W. Watson is amazing. In this case, the first and second "." occurs after Dr (Doctor) and W (initial in the person's name) and should not be confused as the end of the sentence.
# Sentences enclosed in quotes: "What good are they? They're led about just for show!" remarked another. All of this, should be identified as just one sentence.
# Questions and exclamations: Who is it? This is a question. This should be identified as a sentence. I am tired! Something which has been exclaimed. This should also be identified as a sentence.

import re


def parseToSentences(text):
    splittedText = re.split("(?<![a-z]\.[a-z]\.)(?<![0-9]\.[0-9])(?<![A-Z][a-z]\.)(?<=\.|\?|\!)(\s|[A-Z])", text)
    splittedText = list(filter(str.strip, splittedText))
    return splittedText


def printLines(sentences):
    i = 0
    while i < len(sentences):
        s = sentences[i].strip()
        if (len(s) == 1):
            s += sentences[i + 1]
            i += 1

        i += 1
        print(s)


# text = input()
text = 'In the third category he included those Brothers (the majority) who saw nothing in Freemasonry but the external forms and ceremonies, and prized the strict performance of these forms without troubling about their purport or significance. Such were Willarski and even the Grand Master of the principal lodge. Finally, to the fourth category also a great many Brothers belonged, particularly those who had lately joined. These according to Pierre\'s observations were men who had no belief in anything, nor desire for anything, but joined the Freemasons merely to associate with the wealthy young Brothers who were influential through their connections or rank, and of whom there were very many in the lodge.Pierre began to feel dissatisfied with what he was doing. Freemasonry, at any rate as he saw it here, sometimes seemed to him based merely on externals. He did not think of doubting Freemasonry itself, but suspected that Russian Masonry had taken a wrong path and deviated from its original principles. And so toward the end of the year he went abroad to be initiated into the higher secrets of the order.What is to be done in these circumstances? To favor revolutions, overthrow everything, repel force by force?No! We are very far from that. Every violent reform deserves censure, for it quite fails to remedy evil while men remain what they are, and also because wisdom needs no violence. "But what is there in running across it like that?" said Ilagin\'s groom. "Once she had missed it and turned it away, any mongrel could take it," Dr. Ilagin was saying at the same time, breathless from his gallop and his excitement. About 1.9999 million people e.g. asd!'

printLines(parseToSentences(text))
