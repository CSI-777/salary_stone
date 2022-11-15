import pickle
import pandas as pd
import os
from .skill_extractor import Skill_Extractor

fp = str(os.path.dirname(__file__))
class Salary_Extractor:
    """
    The purpose of this class is to extract out salary based on skills.
    """
    def __init__(self, model=fp+'/data/model.pkl', skill_extractor=Skill_Extractor(), sp=['ai',
 'algorithm',
 'analytics',
 'artificial intelligence',
 'azure',
 'big data',
 'business',
 'business intelligence',
 'collaboration',
 'computer science',
 'data analysis',
 'data management',
 'data mining',
 'data model',
 'data modeling',
 'data quality',
 'data science',
 'data visualization',
 'data warehouse',
 'database',
 'deep learning',
 'deployment',
 'design',
 'documentation',
 'engineering',
 'finance',
 'framework',
 'hadoop',
 'library',
 'machine learning',
 'marketing',
 'ml',
 'monitoring',
 'play',
 'programming language',
 'project management',
 'python',
 'relational database',
 'scala',
 'security',
 'server',
 'software',
 'support',
 'tableau',
 'tensorflow',
 'testing',
 'visualization',
 'workflow']):
        self.skill_extractor = skill_extractor
        self.sp = sp
        with open(model, 'rb') as f:
            self.mlb, self.clf = pickle.load(f)
            
    
    def extract_salary(self, text: str):
        skill_vec = self.skill_extractor.extract_skills(text)
        if len(skill_vec) == 0:
            return None
        tmp = pd.DataFrame({'skills': [skill_vec]})

        tmp = tmp.join(
                    pd.DataFrame.sparse.from_spmatrix(
                        self.mlb.transform(tmp.pop('skills')),
                        index=tmp.index,
                        columns=self.mlb.classes_))
        res = str(self.clf.predict(tmp[self.sp].to_numpy())[0])
        res = res.split('-')
        res = [float(x) for x in res] 
        return res