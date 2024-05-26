import pandas as pd
import os

conditions = [
    lambda param: param['max_continuous_inview_0_pct_time_ms'] >= param['max_continuous_inview_50_pct_time_ms'],
    lambda param: param['max_continuous_inview_50_pct_time_ms'] >= param['max_continuous_inview_100_pct_time_ms'],
    lambda param: param['cumulative_inview_0_pct_time_ms'] >= param['cumulative_inview_50_pct_time_ms'],
    lambda param: param['cumulative_inview_50_pct_time_ms'] >= param['cumulative_inview_100_pct_time_ms'],
    lambda param: param['cumulative_inview_0_pct_time_ms'] >= param['max_continuous_inview_0_pct_time_ms'],
    lambda param: param['cumulative_inview_50_pct_time_ms'] >= param['max_continuous_inview_50_pct_time_ms'],
    lambda param: param['cumulative_inview_100_pct_time_ms'] >= param['max_continuous_inview_100_pct_time_ms'],
    lambda param: param['max_continuous_inview_0_pct_time_ms'] > 0,
    lambda param: param['cumulative_inview_0_pct_time_ms'] > 0,
    lambda param: param['cumulative_inview_50_pct_time_ms'] <= param['video_duration'],
    lambda param: param['cumulative_inview_100_pct_time_ms'] <= param['video_duration'],
    lambda param: param['max_continuous_inview_50_pct_time_ms'] <= param['video_duration'],
    lambda param: param['max_continuous_inview_100_pct_time_ms'] <= param['video_duration'],
    lambda param: param['cumulative_inview_100_pct_time_audible_ms'] <= param['video_duration'],
]


def check_conditions(metrics):
    return all(condition(metrics) for condition in conditions)


def read_from_excel(filepath):
    scenarios_df = pd.read_excel(filepath)
    print(scenarios_df)


script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'test_data/scenarios.xlsx')
read_from_excel(file_path)

