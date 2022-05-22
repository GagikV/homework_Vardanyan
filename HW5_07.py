import json

with open("text7.txt", encoding="utf-8") as obj, open("text7.json", "w", encoding="utf-8") as write_new:
    profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in obj}
    profit_h = [i for i in profit.values() if i > 0]
    result = [profit, {"средняя выручка": round(sum(profit_h)) / len(profit_h)}]

    json.dump(result, write_new, ensure_ascii=False, indent=4)
