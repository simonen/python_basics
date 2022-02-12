men = int(input())
women = int(input())
tables = int(input())
free_tables = tables
is_free_tables = True
for man in range(1, men + 1):
    for woman in range(1, women + 1):
        free_tables -= 1
        if free_tables >= 0:
            print(f"({man} <-> {woman})", end=" ")
        else:
            is_free_tables = False
    if not free_tables:
        break
