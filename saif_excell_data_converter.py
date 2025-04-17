import pandas as pd

def excel_to_csv(input_path, output_path, sheet_name=0):
   
    df = pd.read_excel(input_path, sheet_name=sheet_name)
    df.to_csv(output_path, index=False)
    print(f"Saved CSV to {output_path}")

if __name__ == "__main__":
    input_path  = r"C:\Users\saify\OneDrive\Desktop\BS\Practice_excell.xlsx"
    output_path = "practice_csv_data.csv"
    excel_to_csv(input_path, output_path)


import pandas as pd

def excel_to_json(input_path, output_path, sheet_name=0, orient='records'):
    df = pd.read_excel(input_path, sheet_name=sheet_name)
    df.to_json(output_path, orient=orient, force_ascii=False, indent=4)
    print(f"Saved JSON to {output_path}")

if __name__ == "__main__":
    input_path  = r"C:\Users\saify\OneDrive\Desktop\BS\Practice_excell.xlsx"
    output_path = "practice_json_data.json"
    excel_to_json(input_path, output_path)


