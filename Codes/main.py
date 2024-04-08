import pandas as pd
import os

def view(data_frame):
	# Get the first 5 rows of the spreadsheet
	print(data_frame.head())
	print("=====================================================================================================================================")
	# Get the shape of the spreadsheet
	print(data_frame.shape)
	print("=====================================================================================================================================")
	# Get the column names of the spreadsheet
	print(data_frame.columns)
	print("=====================================================================================================================================")
	# Get summary statistics for each column
	print(data_frame.describe())
	print("=====================================================================================================================================")

def clean_data_frame(data_frame):
	data_frame.drop_duplicates(inplace=True)
	data_frame.rename(
	columns=
	{
		"Name": "Title",
		"Year" : "Publication Year",
		"User Rating" : "Rating"
	}
	, inplace=True)
	data_frame["Price"] = data_frame["Price"].astype(float)
	return data_frame

def get_author_counts(data_frame):
    return data_frame["Author"].value_counts()

def get_avg_rating_by_genre(data_frame):
    return data_frame.groupby("Genre")["Rating"].mean()

def analysis(data_frame):
    print(get_author_counts(data_frame))
    print(get_avg_rating_by_genre(data_frame))

def write_analysis_to_csv(data_frame, script_directory):
    top_10_authors_file_path = os.path.join(script_directory,'top_10_authors.csv')
    get_author_counts(data_frame).head(10).to_csv(top_10_authors_file_path)
    avg_rating_by_genre_file_path = os.path.join(script_directory,'avg_rating_by_genre.csv')
    get_avg_rating_by_genre(data_frame).to_csv(avg_rating_by_genre_file_path)

if __name__ == '__main__':
	script_directory = os.path.dirname(os.path.abspath(__file__))
	best_sellers_file_path = os.path.join(script_directory,'bestsellers.csv')
	data_frame = pd.read_csv(best_sellers_file_path)
	# view(data_frame)
	cleaned_data_frame = clean_data_frame(data_frame)
	# view(cleaned_data_frame)
	# print(type(cleaned_data_frame["Price"][0]))
	analysis(cleaned_data_frame)
	write_analysis_to_csv(cleaned_data_frame,script_directory)