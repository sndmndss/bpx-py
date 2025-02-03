from typing import Optional, Literal, TypedDict


class RequestConfiguration:
    def __init__(
        self,
        url: str,
        headers: Optional[dict] = None,
        params: Optional[dict] = None,
        data: Optional[dict] = None,
    ):
        self.url = url
        self.headers = headers
        self.params = params
        self.data = data

    def __repr__(self):
        return (
            f"RequestConfiguration("
            f"url={self.url!r}, "
            f"headers={self.headers!r}, "
            f"params={self.params!r}, "
            f"data={self.data!r})"
        )


class MMFFunction(TypedDict):
    type: Literal["sqrt"]
    base: str
    factor: str


class IMFFunction(TypedDict):
    type: Literal["sqrt"]
    base: str
    factor: str


class CollateralFunctionKind(TypedDict):
    type: Literal["identity", "inverseSqrt"]


class HaircutFunction(TypedDict):
    weight: str
    kind: CollateralFunctionKind
