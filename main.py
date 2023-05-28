"""Module with functions."""


def largest_sum(numbers: list[int]) -> tuple[int, int]:
    """Encontra e retorna os dois números que somados dão o maior valor."""
    if len(numbers) < 2:
        return None
    numbers.sort(reverse=True)
    primeiro = numbers[1]  # o primeiro número da soma
    segundo = numbers[0]  # o segundo número da soma
    return primeiro, segundo
