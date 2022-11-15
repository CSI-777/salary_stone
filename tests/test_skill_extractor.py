#!/usr/bin/env python

"""Tests for `salary_stone` package."""

import pytest

from salary_stone.skill_extractor import Skill_Extractor

@pytest.fixture
def prepare():
    SkillE = Skill_Extractor()
    jobdesc = """
    python is a great skill as is azure and it's also great that we can use data modeling to answer some questions.
    """
    yield SkillE, jobdesc
    
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


class TestSkill:

    def test_default(self, prepare):
        SkillE = prepare[0]
        jobdesc = prepare[1]
        result = SkillE.extract_skills(jobdesc)
        assert len(result) == 3
        assert set(result) == set(['python', 'azure', 'data modeling'])
    
    def test_empty(self, prepare):
        SkillE = prepare[0]
        result = SkillE.extract_skills('')
        assert len(result) == 0

    def test_error(self, prepare):
        SkillE = prepare[0]
        with pytest.raises(Exception):
            SkillE.extract_skills(123)
    
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
