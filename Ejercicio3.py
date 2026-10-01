def total_interrupciones(a: int, b: int) -> int:
    if b <= 0:
        return 0
    return a + total_interrupciones(a, b - 1)