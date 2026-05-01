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