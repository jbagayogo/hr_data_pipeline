def average(data: list) -> float:
    total = 0
    for num in data:
        total += num
    return round(total / len(data), 2)


def median(data: list) -> float:
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        med = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        med = sorted_data[n // 2]
    return round(med, 2)


def heartrate_range(data: list) -> float:
    sorted_data = sorted(data)
    return sorted_data[-1] - sorted_data[0]


def rolling_avg(data: list, k: int) -> list:
    """
    CHALLENGE: Returns a list of rolling averages with window size k.
    """
    result = []
    for i in range(len(data) - k + 1):
        window = data[i:i + k]
        total = 0
        for val in window:
            total += val
        result.append(round(total / k, 2))
    return result