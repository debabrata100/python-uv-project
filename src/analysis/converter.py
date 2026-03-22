import os
import json
import pandas as pd


def json_to_csv_excel(json_file):
    json_file_name = os.path.join("data", "output", json_file)
    output_dir = os.path.join("data", "output")
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, "commit_count.csv")
    excel_path = os.path.join(output_dir, "commit_count.xlsx")

    # read json
    data = None
    with open(json_file_name, "r", encoding="utf-8") as f:
        data = json.load(f)
    df = pd.DataFrame(data.items(), columns=["Year", "Commit Count"])
    df.to_csv(output_file, index=False, encoding="utf-8")
    df.to_excel(excel_path, index=False)
