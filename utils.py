from typing import TYPE_CHECKING
import csv

from aggregate_utils import avg_aggregate, min_aggregate, max_aggregate

if TYPE_CHECKING:
    from argparse import Namespace


def file_open(args: "Namespace") -> list[dict[str, str]]:
    with open(args.file) as fl:
        reader = csv.DictReader(fl)
        rows = list(reader)
    return rows


def where_parse(
    condition: str, rows: list[dict[str, str | int]]
) -> list[dict[str | None, str | int]]:
    res = []

    for i in ("=", "<", ">"):
        if i in condition:
            operator = "==" if i == "=" else i
            parts = condition.split(i)
            name, par = parts[0], parts[1]
            break
    else:
        raise ValueError(
            "Неверный формат - используйте '=' для строк и '=' '>' '<' для числовых значений"
        )

    if par.isdigit():
        for row in rows:
            if eval(f"{float(row[name])}{operator}{float(par)}"):
                res.append(row)
    else:
        for row in rows:
            if eval(f"'{row[name]}'{operator}'{par}'"):
                res.append(row)

    return res


def aggregate_condition(
    condition: str, rows: list[dict[str, str | int]]
) -> dict[str, list[float | str]] | None:
    name, par = condition.split("=")

    match par:
        case "avg":
            return avg_aggregate(name, rows)

        case "min":
            return min_aggregate(name, rows)

        case "max":
            return max_aggregate(name, rows)
