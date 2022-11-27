#!/usr/bin/env python

"""Tests for `salary_stone` package."""

import pytest
import pandas as pd

from salary_stone.metrics import similarity_measure, skill_freq, skill_salary_dist

@pytest.fixture
def prepare():
    dat = pd.DataFrame({'job_title': ['Data Scientist', 'Software Developer', 'Software Developer', 'Manager'], 'salary_bin': ['40k-50k', '40k-50k', '50-70k', '180k+'], 'skills':[['python', 'keras', 'tensorflow'], ['python', 'tensorflow', 'ai'], ['gitlab', 'python', 'tensorflow', 'keras'], ['excel', 'business', 'managing']]})
    yield dat

class TestMetrics:

    def test_skill_freq_default(self, prepare):
        dat = prepare
        skills, freqs = skill_freq(skill_vec=['python'], data=dat, extracted_scol='skills')
        assert len(skills) == 1
        assert len(freqs) == 1
    
    def test_skill_freq_multi(self, prepare):
        dat = prepare
        skills, freqs = skill_freq(skill_vec=['python', 'keras'], data=dat, extracted_scol='skills')
        assert len(skills) == 2
        assert len(freqs) == 2
        assert set(freqs) == set([0.75, 0.5])
    
    def test_skill_salary_dist_default(self, prepare):
        dat = prepare
        bins = skill_salary_dist(skill_vec = ['python', 'keras'], data=dat, extracted_salcol='salary_bin', extracted_scol='skills')
        assert len(bins.items()) == 2
    
    def test_similarity_default(self, prepare):
        dat = prepare
        ans = similarity_measure(skill_vec=['python'], data=dat, topn=3, jobtitle_col='job_title', extracted_scol='skills')
        assert len(ans[1]) == 3
