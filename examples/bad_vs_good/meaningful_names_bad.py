def process(items):
    total = 0

    for x in items:
        if x["t"] == "cc":
            total += 1

    return {
        "n": total,
        "d": "ok" if total > 0 else "none",
    }
