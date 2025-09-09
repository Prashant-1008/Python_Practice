def sum_list_recursive(values: list[int]) -> int:
    if not values:
        return 0
    return values[0] + sum_list_recursive(values[1:])


def count_paths_grid(rows: int, cols: int) -> int:
    if rows == 1 or cols == 1:
        return 1
    return count_paths_grid(rows - 1, cols) + count_paths_grid(rows, cols - 1)


def tail_recursion_style(n: int, acc: int = 1) -> int:
    # Python does not optimize tail recursion, but this shows the style
    if n <= 1:
        return acc
    return tail_recursion_style(n - 1, acc * n)


if __name__ == "__main__":
    print(sum_list_recursive([1, 2, 3, 4, 5]))
    print(count_paths_grid(3, 3))
    print(tail_recursion_style(5)) 