def avg_aggregate(
    name: str, rows: list[dict[str, str | int]]
) -> dict[str, list[float | str]]:
    res = 0
    for num in rows:
        res += float(num[name])
    return {"avg": [round(res / len(rows), 2)]}


def min_aggregate(
    name: str, rows: list[dict[str, str | int]]
) -> dict[str, list[float | str]]:
    min_obj = None, float("inf")
    for row in rows:
        if float(row[name]) < min_obj[1]:
            min_obj = row, float(row[name])
    return {"min": [min_obj[1]]}


def max_aggregate(
    name: str, rows: list[dict[str, str | int]]
) -> dict[str, list[float | str]]:
    max_obj = None, float("-inf")
    for row in rows:
        if float(row[name]) > max_obj[1]:
            max_obj = row, float(row[name])
    return {"max": [max_obj[1]]}
