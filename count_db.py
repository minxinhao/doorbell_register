import re

filename = "out.txt"  # 替换为你的文件名

unique_pairs = {}
unique_qp = set()
unique_db = set()
unique_bf = set()
unique_bf_offset = set()

with open(filename, "r") as file:
    for line in file:
        match = re.search(r'qp:(\w+) db:(\w+) bf:(\w+) bf.offset:(\w+)', line)
        if match:
            qp = match.group(1)
            db = match.group(2)
            bf = match.group(3)
            bf_offset = match.group(3)
            unique_pairs[(qp, db,bf,bf_offset)] = unique_pairs.get((qp, db,bf,bf_offset), 0) + 1
            unique_qp.add(qp)
            unique_db.add(db)
            unique_bf.add(bf)
            unique_bf_offset.add(bf_offset)

print("Unique qp",len(unique_qp))
for qp in unique_qp:
    print(qp)

print("Unique db",len(unique_db))
for db in unique_db:
    print(db)

print("Unique bf",len(unique_bf))
for bf in unique_bf:
    print(bf)

print("Unique bf_offset",len(unique_bf_offset))
for bf_offset in unique_bf_offset:
    print(bf_offset)

print("Unique <qp, db> pairs: total",len(unique_pairs))
for pair, count in unique_pairs.items():
    print(pair[0], pair[1], count)