with open('site/src/pages/ItauPreparationCase.tsx', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'title:' in line:
        # print 5 lines before and after
        start = max(0, i-4)
        end = min(len(lines), i+3)
        print(f"--- Line {i+1} ---")
        for j in range(start, end):
            print(f"{j+1}: {lines[j]}", end='')
