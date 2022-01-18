import re                                              

def tokenize(text):                                    
  return re.findall(r'\w+', text.lower())

profane_tokens = {"a", "b"}                        

insta_comment = "Why you stuck-up, half-witted, scruffy-looking a !"             

tokens = tokenize(insta_comment)                      

                                                      
degree_of_profanity = sum(1 for t in tokens if t in profane_tokens) / len(tokens)
print(degree_of_profanity)
