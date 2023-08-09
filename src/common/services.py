from typing import List
from src.common.exceptions import ObjectNotFoundException


class Service:
    model = None

    @classmethod
    def get(cls, *args, **kwargs) -> model:
        try:
            return cls.model.objects.get(**kwargs)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException(f'{cls.model.__name__} not found')

    @classmethod
    def filter(cls, *args, **kwargs) -> List[model]:
        return cls.model.objects.filter(*args, **kwargs)
