from typing import (
    TypedDict,
    List,
    Tuple,
    Dict,
    Literal,
    LiteralString,
    Union,
    Optional,
    Any,
    Generator,
    Callable,
)

# 타입 기본
a = int
type a = int
b: int = 1
c: Literal["rex", "rex1"] = "rex"
d: LiteralString = "asdf"
e: Dict | dict[str, Any] = {1: 1}
f: Optional[int] | int | None = 1
g: tuple | Tuple = (1,)
h: list | List[str | None] = []
i: Union[str, int] | str | int = 1
j: Generator[int, None, None] = (
    x for x in [1, 2, 3]
)  # YieldType, SendType, ReturnType
k: Callable[[int], int] = lambda x: x + 1
l: Callable[[int, int], int] = lambda x, y: x + y


class DICT(TypedDict):
    a: str
    b: int


rex: DICT = {
    "a": "1",
    "b": 2,
}
