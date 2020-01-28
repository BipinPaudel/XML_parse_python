import pandas as pd


def hello():
    print("Hello world")


def prepare_csv(csv_type,columns, data):
    print("starting to prepare")
    df = pd.read_csv(csv_type)
    df2 = pd.DataFrame(data, columns=columns)
    df = df.append(df2)
    df.to_csv(csv_type, index=False)


