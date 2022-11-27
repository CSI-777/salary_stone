from salary_stone.salary_extractor import Salary_Extractor

def recommend(skill_vec, data, model: Salary_Extractor, extracted_scol:str):
    """
    The purpose of this method is to provide the recommended skills and predicted percentage increase in salary
    that could be expected if that skill were to be included.

    :param skill_vec: is the vector of skills that a person currently has.
    :param data: is the pandas dataframe of the data that we are using to make the comparison.
    :param model: is a salary extractor model that we will be using to make the recommendations.
    :param extracted_scol: is a column consisting of a list of skills for the row in the dataframe.

    :returns: a list of the skill names and a list of the expected return percentages.
    """
    salarye = model

    # make a list of the unique extracted skills
    list_extracted_skills = []
    for skill in data[extracted_scol]:
        for i in skill:
            list_extracted_skills.append(i)
    unique_list_extracted_skills = list(set(list_extracted_skills))
    #len(unique_list_extracted_skills)
    # find skills and percentage of how much they will help

    skill_list = []
    percentage_prediction = []
    for index in range(len(unique_list_extracted_skills)):
        if index == 0:
            prediction = salarye.extract_salary(' '.join(skill_vec))
    #        print(prediction)
            if prediction[1] == 'inf':
                base_mean = prediction[0]
            else:
                base_mean = (prediction[0] + prediction[1]) / 2

        if unique_list_extracted_skills[index] not in skill_vec:
            skill_vec.extend([unique_list_extracted_skills[index]])
            # find the prediction from random forest model
            prediction = salarye.extract_salary(' '.join(skill_vec))
    #         print(unique_list_extracted_skills[index])
    #         print(prediction)
            try:
                if prediction[1] == 'inf':
                    mean = prediction[0]
                else:
                    mean = (prediction[0] + prediction[1]) / 2

                percentage_prediction.append((mean - base_mean)/ base_mean)
                skill_list.append(unique_list_extracted_skills[index])
            except:
                continue
            skill_vec = skill_vec[:-1]


    percentage_prediction, skill_name = zip(*sorted(zip(percentage_prediction, skill_list), reverse = True))
    
    return skill_name, percentage_prediction