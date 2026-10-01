def ordenar_eventos(eventos: list, descendente: bool = False) -> list:
    return sorted(eventos, reverse=bool(descendente))