import pandas as pd
from src.reported_is_viewability_eleigible import check_conditions
from src.utils import transform_into_list_of_dict


def test_viewability():
    case_dict = transform_into_list_of_dict("test_data/scenarios.xlsx")
    for idx, metrics in enumerate(case_dict, start=1):
        if check_conditions(metrics):
            print(f"Test case number {idx} passed")
        else:
            print(f"Test case number {idx} failed")

    # for idx, metrics in enumerate(case_dict, start=1):
    #     assert check_conditions(metrics), f"Test case number {idx} failed"
