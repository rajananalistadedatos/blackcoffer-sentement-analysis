import nltk
from nltk.corpus import stopwords
import re
from collections import Counter

# Download the stopwords from NLTK
nltk.download('stopwords')

# Sample positive and negative word dictionaries (you can replace these with your own dictionaries)
positive_words = set(['good', 'happy', 'positive', 'fortunate', 'correct', 'superior'])
negative_words = set(['bad', 'sad', 'negative', 'unfortunate', 'wrong', 'inferior','challenging'])

# Text for analysis
text = """Title: Amazon Buy Bot, an Automation AI tool to Auto-Checkouts

Paragraph:

Client Background
Client: A leading consulting firm in the USA
Industry Type: Consulting
Services: Management consultant
Organization Size: 100+
Project Objective
The main objective of this project is to build the automation tool to buy product on amazon.
Project Description
This project is basically completed using selenium and Python. All we have done is write a python script for automation using Selenium.
Make some clicks use logics to check item is in stock or not. If the item is in stock then it buys the product otherwise repeat the process again.
Our Solution
A simple python code which uses selenium web driver to do all work.
Project Deliverables
Python Code
Tools used
Selenium Webdriver
Language/techniques used
Python
Skills used
Web Scraping
Selenium
Project Snapshots









"""

# Preprocessing text
def preprocess_text(text):
    # Remove punctuations
    text = re.sub(r'[^\w\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    # Tokenize text
    words = nltk.word_tokenize(text)
    return words

# Sentiment analysis
def sentiment_analysis(words):
    positive_score = sum(1 for word in words if word in positive_words)
    negative_score = sum(1 for word in words if word in negative_words) * -1
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
    subjectivity_score = (positive_score + negative_score) / (len(words) + 0.000001)
    return positive_score, negative_score, polarity_score, subjectivity_score

# Readability analysis
def readability_analysis(text):
    sentences = nltk.sent_tokenize(text)
    words = preprocess_text(text)
    total_words = len(words)
    total_sentences = len(sentences)
    complex_words = sum(1 for word in words if len(re.findall(r'[aeiou]', word)) > 2)
    
    avg_sentence_length = total_words / total_sentences if total_sentences != 0 else 0
    percentage_complex_words = complex_words / total_words if total_words != 0 else 0
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
    
    return avg_sentence_length, percentage_complex_words, fog_index

# Average words per sentence
def average_words_per_sentence(total_words, total_sentences):
    return total_words / total_sentences if total_sentences != 0 else 0

# Complex word count
def complex_word_count(words):
    return sum(1 for word in words if len(re.findall(r'[aeiou]', word)) > 2)

# Word count (after cleaning)
def word_count(words):
    cleaned_words = [word for word in words if word not in stopwords.words('english')]
    return len(cleaned_words)

# Syllable count per word
def syllable_count(word):
    word = word.lower()
    syllable_count = len(re.findall(r'[aeiou]', word))
    if word.endswith('es') or word.endswith('ed'):
        syllable_count -= 1
    return max(1, syllable_count)

# Personal pronouns count
def personal_pronouns_count(text):
    pronouns = re.findall(r'\b(I|we|my|ours|us)\b', text, re.I)
    return len(pronouns)

# Average word length
def average_word_length(words):
    total_characters = sum(len(word) for word in words)
    return total_characters / len(words) if words else 0

# Main function to run all analyses
def main(text):
    words = preprocess_text(text)
    positive_score, negative_score, polarity_score, subjectivity_score = sentiment_analysis(words)
    avg_sentence_length, percentage_complex_words, fog_index = readability_analysis(text)
    avg_words_per_sentence = average_words_per_sentence(len(words), len(nltk.sent_tokenize(text)))
    complex_words = complex_word_count(words)
    total_word_count = word_count(words)
    syllable_counts = [syllable_count(word) for word in words]
    personal_pronouns = personal_pronouns_count(text)
    avg_word_length = average_word_length(words)
    
    results = {
        'Positive Score': positive_score,
        'Negative Score': negative_score,
        'Polarity Score': polarity_score,
        'Subjectivity Score': subjectivity_score,
        'Average Sentence Length': avg_sentence_length,
        'Percentage of Complex Words': percentage_complex_words,
        'Fog Index': fog_index,
        'Average Words Per Sentence': avg_words_per_sentence,
        'Complex Words Count': complex_words,
        'Total Word Count': total_word_count,
        'Syllable Count Per Word': syllable_counts,
        'Personal Pronouns Count': personal_pronouns,
        'Average Word Length': avg_word_length
    }
    
    return results

# Running the analysis
analysis_results = main(text)
print(analysis_results)
