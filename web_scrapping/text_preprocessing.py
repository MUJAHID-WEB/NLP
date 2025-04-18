### Segmentation

import nltk
from nltk.tokenize import sent_tokenize
nltk.download('punkt_tab')

text="The weather is nice today. I feel like enjoying it with a cup of tea. It's a pleasant morning."

sentences=sent_tokenize(text)
print(sentences)

for i, sentence in enumerate(sentences):
    print(f"Sentence {i+1}: {sentence}")




# punctuation and special characters

import re
import nltk
from nltk.tokenize import word_tokenize

text = "Hello! Check out my website: http://example.com. It's awesome! #excited @user $100."

url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
punctuation_pattern = r'[^\w\s]'

text = re.sub(url_pattern, '', text)
text = re.sub(punctuation_pattern, '', text)

tokens = word_tokenize(text)

print(tokens)
print(text)


#lowercasing

import re
import nltk
from nltk.tokenize import word_tokenize

text = "Hello! Check out my website: http://example.com. It's awesome! #excited @user $100."

url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
punctuation_pattern = r'[^\w\s]'

text = re.sub(url_pattern, '', text)
text = re.sub(punctuation_pattern, '', text)

lowercase_text=text.lower()

tokens = word_tokenize(text)

print("Lowercasing results:", lowercase_text)

#tokenization

import nltk
from nltk.tokenize import word_tokenize

text = "Hello! Check out my website: http://example.com. It's awesome! #excited @user $100."

tokens = word_tokenize(text)

print(tokens)


## pos tagging

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

nltk.download('averaged_perceptron_tagger_eng')

text = "The brown quick fox jumped over the lazy dog."

tokens = word_tokenize(text)

print(tokens)

pos_tags = pos_tag(tokens)

print(pos_tags)

#stopwords removal

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('stopwords')

sentence="The weather is very nice."

tokens=word_tokenize(sentence)

stop_words=set(stopwords.words('english'))

filtered_tokens=[word for word in tokens if word.lower() not in stop_words]

filtered_sentence=' '.join(filtered_tokens)
print("Sentence original:",sentence)
print(filtered_sentence)



# text norm

import re
from nltk.tokenize import word_tokenize

text="I loveeeeee this! Do you luv it too?"

def normalize(text):
  text=text.lower()
  text=re.sub(r'(.)\1+',r'\1',text) # loveeeeee 1+5 e's => e word: love instead of loveeeeee
  text=re.sub(r'\bluv\b','love',text) ### luv => love
  return text


normalized_text=normalize(text)
print("Text normalized text:",normalized_text)


#lemma and stem

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

text="I am running in the park and feeling troubled."

tokens=word_tokenize(text)

print("Tokens:", tokens)

stemmer=PorterStemmer()

stemmed_tokens=[stemmer.stem(token) for token in tokens]

stemmed_text=' '.join(stemmed_tokens)

print("Stemmed text:", stemmed_text)


import spacy

nlp=spacy.load('en_core_web_sm')

text="I am running in the park and feeling troubled."

doc=nlp(text)

lemmatized_tokens=[token.lemma_ for token in doc]

lemmatized_text=' '.join(lemmatized_tokens)

print("Lemmatized text:",lemmatized_text)

