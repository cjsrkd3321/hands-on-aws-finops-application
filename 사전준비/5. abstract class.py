from abc import ABCMeta, abstractmethod


class Test:
    def __init__(self):
        pass

    def test(self):
        raise NotImplementedError


class ResourceBase(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def delete(self) -> str:
        NotImplementedError()
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class Rex(Test):
    def __init__(self):
        pass

    # def delete(self):
    #     pass

    def __str__(self):
        pass


Rex()
