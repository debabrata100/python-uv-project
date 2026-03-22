import os
import json
import pandas as pd


def json_to_csv_excel(json_file):
    json_file_name = os.path.join("data", json_file)
    output_file = os.path.join("data", "commit_count.csv")
    excel_path = output_file[:-3] + "xlsx"
    # read json
    data = None
    with open(json_file_name, "r", encoding="utf-8") as f:
        data = json.load(f)
    df = pd.DataFrame(data.items(), columns=["Year", "Commit Count"])
    df.to_csv(output_file, index=False, encoding="utf-8")
    df.to_excel(excel_path, index=False)


def main():
    json_to_csv_excel("commit_count.json")


if __name__ == "__main__":
    main()
