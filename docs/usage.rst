=====
Usage
=====


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

