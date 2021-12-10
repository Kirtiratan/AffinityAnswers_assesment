import re                                              #importing useful Python library

def tokenize(text):                                    #text here is the Instagram comment for which we want to check degree
  return re.findall(r'\w+', text.lower())

profane_tokens = {"nerfherder", "shit"}                        #we have to provide few words which can be profane in this list

insta_comment = "Why you stuck-up, half-witted, scruffy-looking nerfherder!"                #let's say this is one of comment

tokens = tokenize(insta_comment)                       #comment is converted into list of words

                                                       # Rate: number of occurrences normalized by total number
degree_of_profanity = sum(1 for t in tokens if t in profane_tokens) / len(tokens)
print(degree_of_profanity)
