def tower_hanoi(n, A, B, C):
    if n == 1:
        print(f"Chuyển đĩa 1 từ {A} sang {B}")
        return
    tower_hanoi(n - 1, A, C, B)
    print(f"Chuyển đĩa {n} từ {A} sang {B}")
    tower_hanoi(n - 1, C, B, A)

n = 3
tower_hanoi(n, "A", "B", "C")