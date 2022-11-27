=====
Usage
=====


Extractors
----------


How to use the Skill Extractor::

    from salary_stone.skill_extractor import Skill_Extractor
    # By default the en_core_web_sm model is used for extraction, but this can be updated by passing the model parameter.
    skille = Skill_Extractor()
    jobdesc = "My skills include things like python and also data analytics. I also have a great abilities to do business."
    skills = skille.extract_skills(jobdesc)
    print(skills)
    ['python', 'data analytics', 'business']

How to use the Salary Extractor::

    from salary_stone.salary_extractor import Salary_Extractor
    salarye = Salary_Extractor()
    jobdesc = "For this position we will require someone to use python. Additionally we will require a working knowledge of data analytics"
    salary = salarye.extract_salary(jobdesc)
    print(salary)
    "40k-50k"

Recommender
-------------------

How to use the skill recommender:: 

    from salary_stone.salary_extractor import Salary_Extractor
    from salary_stone.skill_extractor import Skill_Extractor
    from salary_stone.skill_recommender import recommend

    skille = Skill_Extractor()
    se = Salary_Extractor()
    # dat = dataframe of kaggle data.
    dat['skills'] = dat['job_desc_col'].apply(lambda r: skille.extract_skills(r))
    skills, vals = recommend(['python'], data=dat, model=se, extracted_scol='skills')

Generating Metrics
-------------------

Calculating Skill Frequency::

    import pandas as pd
    from salary_stone.metrics import skill_freq
    from salary_stone.skill_extractor import Skill_Extractor
    se = Skill_Extractor()
    # Or can read the data from elastic just as long as it has a job title, salary bin, and skill column.
    data = pd.read_csv('/path/to/kaggle/data')
    data['skills'] = data['job_desc'].apply(lambda r: se.extract_skills(r))
    skills, freqs = skill_freq(skill_vec=['python'], data=dat, extracted_scol='skills')
    print(skills)
    ['python']
    print(freq)
    [0.8]

Calculating Skill Salary Distribution::
    
    import pandas as pd
    from salary_stone.metrics import skill_salary_dist
    from salary_stone.skill_extractor import Skill_Extractor
    from salary_stone.salary_extractor import Salary_Extractor
    se = Skill_Extractor()
    salarye = Salary_Extractor()
    # Or can read the data from elastic just as long as it has a job title, salary bin, and skill column.
    data = pd.read_csv('/path/to/kaggle/data')
    data['skills'] = data['job_desc'].apply(lambda r: se.extract_skills(r))
    data['salary_bin'] = data['job_desc'].apply(lambda r: se.extract_salary(r))
    bins = skill_salary_dist(skill_vec = ['python'], data=dat, extracted_salcol='salary_bin', extracted_scol='skills')
    print(bins)
    [0.2, 0.4, 0.1, 0.2, 0.1]

Calculating Job Similarity By Skills::

    import pandas as pd
    from salary_stone.metrics import skill_freq
    from salary_stone.skill_extractor import Skill_Extractor
    se = Skill_Extractor()
    # Or can read the data from elastic just as long as it has a job title, salary bin, and skill column.
    data = pd.read_csv('/path/to/kaggle/data')
    data['skills'] = data['job_desc'].apply(lambda r: se.extract_skills(r))
    
    res = similarity_measure(skill_vec=['python'], data=dat, topn=3, jobtitle_col='job_title', extracted_scol='skills')
    print(res)
    ((0.4, 0.3, 0)('Software Developer', 'Data Scientist', 'Manager'))

