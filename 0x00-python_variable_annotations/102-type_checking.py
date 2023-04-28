#!/usr/bin/env python3

from typing import List, Tuple


def zoom_array(lst: Tuple[int], factor: int = 2) -> List[int]:
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


if __name__ == "__main__":
    array = (12, 72, 91)

    zoom_2x = zoom_array(array)

    zoom_3x = zoom_array(array, 3)

    print(zoom_2x)
    print(zoom_3x)
