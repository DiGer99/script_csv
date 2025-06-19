from utils import where_parse, aggregate_condition, file_open


def main():
    import argparse
    from tabulate import tabulate

    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    parser.add_argument("--where")
    parser.add_argument("--aggregate")

    args = parser.parse_args()

    if args.file:
        rows = file_open(args)
    else:
        raise FileNotFoundError("Файловый параметр не передан (--file 'products.csv')")

    if args.where and args.aggregate:
        res = where_parse(args.where, rows)
        data = aggregate_condition(args.aggregate, res)
        return tabulate(data, headers="keys", tablefmt="github")

    elif args.where:
        data = where_parse(args.where, rows)
        return tabulate(data, headers="keys", tablefmt="github")

    elif args.aggregate:
        data = aggregate_condition(args.aggregate, rows)
        return tabulate(data, headers="keys", tablefmt="github")

    return tabulate(rows, headers="keys", tablefmt="github")


if __name__ == "__main__":
    print(main())
