import pandas as pd
from sqlalchemy import create_engine

# Create a SQLite engine
engine = create_engine('sqlite:///assignment.db')


def load_data(file_path, table_name):
    try:
        # Read the CSV file with the correct encoding
        data = pd.read_csv(file_path, encoding='UTF-16LE')

        # Write the DataFrame to a SQL table
        data.to_sql(table_name, con=engine, if_exists='replace', index=False)

        print(f"Data from {file_path} has been loaded into the table {table_name}.")

    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file {file_path} is empty.")
    except pd.errors.ParserError:
        print(f"Error: The file {file_path} could not be parsed.")
    except UnicodeDecodeError as e:
        print(f"Encoding error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    load_data('../data/training_data.csv', 'training_data')
    load_data('../data/ideal_functions.csv', 'ideal_functions')
