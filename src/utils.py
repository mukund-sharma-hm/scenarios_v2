import pandas as pd


def read_data_from_excel_and_convert_to_dict(filepath):
    scenarios_df_dict = pd.read_excel(filepath).to_dict()
    return scenarios_df_dict


def transform_into_list_of_dict(filepath):
    df_dict = read_data_from_excel_and_convert_to_dict(filepath)
    metrics = []
    for i in range(len(df_dict["max_continuous_inview_0_pct_time_ms"])):
        temp_dict = {key: value[i] for key, value in df_dict.items()}
        metrics.append(temp_dict)
    return metrics
