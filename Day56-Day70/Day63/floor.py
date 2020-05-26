for i in range(1,6):
    print("-------{i}层------")
    if i== 3:
        print("-3层不走...")
        continue
    for j in range(1,9):
        if i == 4and j==4:
            print("有鬼404...")
            break
    print(f"L{i}-{i}8{j}室")
