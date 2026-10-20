def compute_gate_areas(max_n: int):
    NAND: list[int] = [max_n*8] * (max_n + 1)
    AND: list[int] = [max_n*8] * (max_n + 1)

    NAND[1] = 2  # 1 输入与非门就是非门
    AND[1] = 0  # 1 输入与门就是导线本身

    for n in range(2, max_n + 1):
        for a in range(1, n):
            b = n - a
            # NAND(AND[a], AND[b])
            NAND[n] = min(NAND[n], AND[a] + AND[b] + 6)

            # OR(NAND[a], NAND[b])
            NAND[n] = min(NAND[n], NAND[a] + NAND[b] + 8)

            # NOR(NAND[a], NAND[b])
            AND[n] = min(AND[n], NAND[a] + NAND[b] + 6)

            # AND(AND[a], AND[b])
            AND[n] = min(AND[n], AND[a] + AND[b] + 8)

    return NAND, AND


def formula_NAND(n: int) -> int:
    k, r = divmod(n, 3)
    if r == 0:
        return 18 * k - 4
    elif r == 1:
        return 18 * k + 2
    else:
        return 18 * k + 6


def formula_AND(n: int) -> int:
    k, r = divmod(n, 3)
    if r == 0:
        return 18 * k - 4
    elif r == 1:
        return 18 * k
    else:
        return 18 * k + 8


if __name__ == "__main__":
    N = 30
    F, G = compute_gate_areas(N)

    print(f"{'n':>3} {'NAND':>8} {'AND':>8} {'公式NAND':>10} {'公式AND':>10}")
    print("-" * 50)

    for n in range(1, N + 1):
        ok_NAND = F[n] == formula_NAND(n)
        ok_AND = G[n] == formula_AND(n)
        mark = "OK" if ok_NAND and ok_AND else "MISMATCH"
        print(f"{n:>3} {F[n]:>8} {G[n]:>8} {formula_NAND(n):>10} {formula_AND(n):>10}  {mark}")