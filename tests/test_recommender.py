#!/usr/bin/env python

"""Tests for `salary_stone` package."""

import pytest
import pandas as pd

from salary_stone.salary_extractor import Salary_Extractor
from salary_stone.skill_recommender import recommend

@pytest.fixture
def prepare():
    dat = pd.DataFrame({'job_title': ['Data Scientist', 'Software Developer', 'Software Developer', 'Manager'], 'salary_bin': ['40k-50k', '40k-50k', '50-70k', '180k+'], 'skills':[['python', 'keras', 'tensorflow'], ['python', 'tensorflow', 'ai'], ['gitlab', 'python', 'tensorflow', 'keras'], ['excel', 'business', 'managing']]})
    yield dat

class TestRecommender:

    def test_recommend_default(self, prepare):
        se = Salary_Extractor()
        dat = prepare
        skills, vals = recommend(['python'], data=dat, model=se, extracted_scol='skills')
        assert len(skills) == 7
        assert len(vals) == 7
    
    def test_recommend_multi(self, prepare):
        se = Salary_Extractor()
        dat = prepare
        skills, vals = recommend(['python', 'tensorflow'], data=dat, model=se, extracted_scol='skills')
        assert len(skills) == 6
        assert len(vals) == 6


