import csv
import os

def populate_csv():
    """
    Skeleton script to populate a CSV file with data.
    """
    
    # =================================
    # COLUMN HEADINGS CONFIGURATION
    # =================================
    # Define your column headers here
    column_headers = [
        "id",
        "name", 
        "price",
        "category",
        "description"
    ]
    
    # CSV file configuration
    csv_filename = "data.csv"
    csv_filepath = os.path.join(os.getcwd(), csv_filename)
    
    # Sample data (replace with your actual data source)
    sample_data = [
        [1, "Product A", 9.99, "Electronics", "Sample product description"],
        [2, "Product B", 15.50, "Clothing", "Another sample product"],
        [3, "Product C", 7.25, "Food", "Food item description"]
    ]
    
    try:
        # Create/open CSV file for writing
        with open(csv_filepath, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write column headers
            writer.writerow(column_headers)
            
            # Write data rows
            for row in sample_data:
                writer.writerow(row)
            
            print(f"CSV file '{csv_filename}' has been created successfully!")
            print(f"File location: {csv_filepath}")
            print(f"Total rows written: {len(sample_data) + 1} (including header)")
    
    except Exception as e:
        print(f"Error writing to CSV file: {e}")

def read_csv():
    """
    Optional function to read and display the CSV contents.
    """
    csv_filename = "data.csv"
    
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            
            print(f"\nContents of {csv_filename}:")
            print("-" * 50)
            
            for row_num, row in enumerate(reader, 1):
                print(f"Row {row_num}: {row}")
                
    except FileNotFoundError:
        print(f"File '{csv_filename}' not found. Run populate_csv() first.")
    except Exception as e:
        print(f"Error reading CSV file: {e}")

if __name__ == "__main__":
    # Run the CSV population function
    populate_csv()
    
    # Optionally read and display the contents
    read_csv()
