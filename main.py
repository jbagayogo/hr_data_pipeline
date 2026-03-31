def clean_heartrate_data(data: list) -> tuple:
    """
    Clean raw heart-rate data by removing malformed or impossible values.
    """
    cleaned_list = []
    removed_values = 0

    for value in data:
        stripped = value.strip("\n")
        if stripped.isdigit():
            cleaned_list.append(int(stripped))
        else:
            removed_values += 1

    return cleaned_list, removed_values



def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    total = 0
    for num in data:
        total += num
    
    average = total / len(data)

    return average


def median(data: list) -> float:
    """
    Calculate median of a list of integers, assuming the data is cleaned
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        median = ( sorted_data[n // 2 - 1] + sorted_data[n // 2] ) / 2
    else:
        median = sorted_data[n // 2]
    
    return median
    


def range(data: list) -> float:
    """
    Calculate the range of the heartrate data
    """
    sorted_data = sorted(data)
    heart_range = sorted_data[-1] - sorted_data[0]

    return heart_range


def rolling_avg(data: list, k: int) -> float:
    """
    CHALLENGE FUNCTION (Optional)
    """
    pass


def run(file: str):
    """
    Process heart rate data from the a file by cleaning and
    calculating summary statistics. Print out final values.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, median, and range.
    """
    data = []

    # open file using file I/O and read it into the `data` list
    file_obj = open(file)

    data = file_obj.readlines()


    # Use `clean_heartrate_data` to clean the data and remove invalid entries
    cleaned_list, removed_values = clean_heartrate_data(data)
    #i keep getting a type error that reads "cannot unpack non-iterable object"

    # calculate the average, median, and range of this file using the functions you've wrote
    average_heartrate_data = average(cleaned_list)
    median_heartrate_data = median(cleaned_list)
    heartrate_range = range(cleaned_list)
    
    # print out your data quality measure to the console
    print(cleaned_list)

    # print out your descriptive statistics to the console
    print(average_heartrate_data)
    print(median_heartrate_data)
    print(heartrate_range)


if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")
