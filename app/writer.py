def write_report(path, summary):
    with open(path, "w", encoding="utf-8") as file:
        for level, count in summary.items():
            file.write(f"{level}: {count}\n")
