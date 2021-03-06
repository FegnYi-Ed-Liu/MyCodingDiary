# 0304 buildup one job search and hunting dictionary data
from typing import Dict, List, Union

import pandas as pd
import numpy as np


class job_search:

    def __init__(self, company, position, salary, skill):
        self.company = company
        self.position = position
        self.salary = salary
        self.skill = skill

    def dic_db(self) -> object:
        for k, v in self.items():
            print(k, v)


def main():
    dict_sample = {
        "Company": "Toyota",
        "position": "data scientist",
        "salary": 120000,
        "skill": ["Python", "R", "AI"]
    }
