# 0304 buildup one job search and hunting dictionary data
# from typing import Dict, List, Union
#
# 第一步
# 寫出一個class 可以記錄公司名稱 位置 薪水 需要技能
# 存成dictionary in text file.

import pandas as pd
import numpy as np

dict_sample = {
    "Company": "Toyota",
    "position": "data scientist",
    "salary": 120000,
    "skill": ["Python", "R", "AI"]
}


class job_search:

    def __init__(self, company, position, salary, skill):
        self.company = company
        self.position = position
        self.salary = salary
        self.skill = skill
        self.dicc = {'company': company, 'position': position, 'salary': salary, 'skill': skill}

    def save_dic(self):
        for key in self.dicc:
            print(key)
        for item in self.dicc.items():
            print(item)
        return self.dicc

    # dic_db(self) -> object:
    #
    # filename = 'jobsearch.txt'
    #     with open(filename. 'w') as file_object:
    #         note_content = file_object.write({'company': self.company,'position': self.position,'salary': self.salary,'skill': self.skill,})


if __name__ == '__main__':
    test_1 = job_search('tes', 'www', 2222, 'test')

tessss = job_search.save_dic(test_1)
print(tessss)
