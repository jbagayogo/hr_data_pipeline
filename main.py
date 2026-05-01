from cleaning import clean_heartrate_data
from analysis import average, median, heartrate_range


def run(file: str):
    with open(file) as file_obj:
        data = file_obj.readlines()

    cleaned_list, removed_values = clean_heartrate_data(data)

    avg = average(cleaned_list)
    med = median(cleaned_list)
    hr_range = heartrate_range(cleaned_list)

    print(f"\n--- {file} ---")
    print(f"Records kept: {len(cleaned_list)} | Removed: {removed_values}")
    print(f"Average HR:   {avg} bpm")
    print(f"Median HR:    {med} bpm")
    print(f"Range:        {hr_range} bpm")

    return avg, med, hr_range


if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")