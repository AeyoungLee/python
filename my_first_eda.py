import sweetviz as sv
import pandas as pd

my_dataframe = pd.read_csv("train.csv");

my_report = sv.analyze(my_dataframe)
my_report.show_html() # Default arguments will generate to "SWEETVIZ_REPORT.html"