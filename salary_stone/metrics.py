from collections import Counter
import pandas as pd


def skill_freq(skill_vec: list, data: pd.DataFrame, extracted_scol: str='extracted_skills'):
    """
    The purpose of this method is to get the distribution of skills within a dataframe of 
    glassdoor job salary data.

    :param skill_vec: is the vector of skills that we are calculating the frequency of.
    :param data: is the dataframe that we are using for our frequency calculation.
    :param extracted_scol: is the name of the column with the extracted skill from the skill extractor.

    :returns: a vector of the skills and the skill percentage found within the dataframe.
    """
    extracted_skills = [item for sub_list in list(data[extracted_scol]) for item in sub_list]
    counts = Counter(extracted_skills)
    skill_percentages = []
    for i in skill_vec:
        skill_percentages.append(counts[i]/len(data))
    return skill_vec, skill_percentages

def skill_salary_dist(skill_vec: list, data: pd.DataFrame, extracted_salcol:str='salary_bin', extracted_scol:str='extracted_skills'): # list of the skills ['python', 'java']
    """
    The purpose of this method is to get the salary distribution of jobs that include a skill.

    :param skill_vec: is the vector of skills that we are calculating the frequency of.
    :param data: is the dataframe that we are using for our frequency calculation.
    :param extracted_salcol: is the name of the extracted salary column from the salary extractor.
    :param extracted_scol: is the name of the extracted skill column from the skill extractor.

    :returns: a dictionary with the skill as key and the counts of which salary bins it appears in.
    """
    sorted_data = data.sort_values(by=[extracted_salcol]).reset_index(drop=True)
    dictionary = {}
    for i in skill_vec:
        salarybin_count = [0] * len(sorted_data[extracted_salcol].unique())
        index = 0
        salary_bin = sorted_data[extracted_salcol][0]
        for j in range(len(sorted_data)):
            count = sorted_data[extracted_scol][j].count(i)
            if count > 0:
                if salary_bin == sorted_data[extracted_salcol][j]:
                    salarybin_count[index] += 1
                else:
                    index += 1
                    salarybin_count[index] += 1
                salary_bin = sorted_data[extracted_salcol][j]
        dictionary[i] = salarybin_count
    # dict with skill as key and vector with the value for each salary bin. {'python': [1,2,3,4,5], 'java': [6,7,8,9,10]}
    return dictionary

def similarity_measure(skill_vec: list, data: pd.DataFrame, topn:int=5, jobtitle_col='job_title_sim', extracted_scol='extracted_skills'):
    '''
    The purpose of this method is to return the most similar job titles based on a lis tof skills passed in.

    :param skill_vec: a vector of skills.
    :param data: a dataframe of the job description data.
    :param topn: a value for the number of similar job titles to return.

    :return: two lists where one is the similarity score and the other is the job title.
    '''
    # caculate the skill vec similarity score for each job title
    extracted_skills_list_by_title = []
    tmp = []
    job_titles = []
    for i in data[jobtitle_col].unique():
        extracted_skills_by_title = [item for sub_list in list(data[data[jobtitle_col]==i][extracted_scol]) for item in sub_list]
        counts = Counter(extracted_skills_by_title)
        skill_similarity_count = 0
        for j in skill_vec:
            skill_similarity_count += counts[j]
        extracted_skills_list_by_title.append(skill_similarity_count/len(extracted_skills_by_title))
        tmp.append(skill_similarity_count/len(extracted_skills_by_title)) 
        job_titles.append(i)

    final_list = []

    for i in range(0, topn):
        max1 = 0

        for j in range(len(extracted_skills_list_by_title)):    
            if extracted_skills_list_by_title[j] > max1:
                max1 = extracted_skills_list_by_title[j];

        extracted_skills_list_by_title.remove(max1);
        final_list.append(max1)

    s = set(final_list)

    nums = [num for num, letter in zip(tmp, job_titles) if num in s ]
    letters = [letter for num, letter in zip(tmp, job_titles) if num in s ]
    
    percentages, titles = zip(*sorted(zip(nums, letters), reverse=True))

    # return the topn job titles most similar.
    return percentages, titles