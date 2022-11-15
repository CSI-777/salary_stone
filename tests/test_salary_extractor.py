import pytest
from salary_stone.salary_extractor import Salary_Extractor

@pytest.fixture
def prepare():
    SalaryE = Salary_Extractor()
    jobdesc = """
    python is a great skill as is azure and it's also great that we can use data modeling to answer some questions.
    """
    yield SalaryE, jobdesc
    
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')

class TestSalary:
    def test_default(self, prepare):
        SalaryE = prepare[0]
        jobdesc = prepare[1]
        result = SalaryE.extract_salary(jobdesc)
        assert type(result) == list
        assert len(result) == 2
        assert type(result[0]) == float
        assert result[0] < result[1]
    
    def test_empty(self, prepare):
        SalaryE = prepare[0]
        result = SalaryE.extract_salary('')
        assert result == None

    def test_no_skill(self, prepare):
        SalaryE = prepare[0]
        result = SalaryE.extract_salary('There are no skills here to extract.')
        assert result == None
    
    def test_error(self, prepare):
        SalaryE = prepare[0]
        with pytest.raises(Exception):
            SalaryE.extract_salary(1)