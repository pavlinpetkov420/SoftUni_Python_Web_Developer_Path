from abc import ABC


class ValidatorBase(ABC):
    def validate_type(self, *args, **kwargs):
        pass


class TypeValidator(ValidatorBase):

    def validate_type(self, value, types):
        if type(value) not in types:
            raise ValueError('"numbers" should be ints or floats')
