"""Main module."""
import spacy
import os
#Data loading/ Data manipulation

#nltk
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
    
nltk.download(['stopwords','wordnet', 'omw-1.4'])

fp = str(os.path.dirname(__file__))
class Skill_Extractor:
    """
    This class contains the methods related to extracting the skills from text. The class takes in a .jsonl file which has
    all of the skills available for extraction and a model that is a spacy model which has also been installed.
    """
    def __init__(self, model:str ='en_core_web_sm', skill_dict:str =fp+'/data/jz_skill_patterns.jsonl'):
        self.nlp = spacy.load(model)
        ruler = self.nlp.add_pipe("entity_ruler")
        ruler.from_disk(skill_dict)
    
    def extract_skills(self, text: str):
        """
        The purpose of this method is to clean the text data being input and return the unique
        set of skills found within the string.
        
        :param: text is the text where the skills are being extracted from.
        
        :returns: the unique list of skills
        """
        review = re.sub(
            '(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?"',
            " ",
            text,
        )
        review = review.lower()
        review = review.split()
        lm = WordNetLemmatizer()
        review = [
            lm.lemmatize(word)
            for word in review
            if not word in set(stopwords.words("english"))
        ]
        review = " ".join(review)
        skills = self.get_skills(review.lower())
        skills_set = list(set(skills))
        return(skills_set)
    
    def get_skills(self, text:str):
        """
        The purpose of this method is to extract all the skills from the text.
        """
        doc = self.nlp(text)
        myset = []
        subset = []
        for ent in doc.ents:
            if ent.label_ == "SKILL":
                subset.append(ent.text)
        myset.append(subset)
        return subset