import pandas as pd

from pymeos import DeserializerFloat
from pymeos import TFloatInst, TFloatSeq
from sqlalchemy.types import UserDefinedType
from pandas.api.types import is_numeric_dtype

from .TBaseType import TBaseType


class TFloat(TBaseType):
    pymeos_sequence_type = TFloatSeq
    pymeos_instant_type = TFloatInst
    pymeos_deserializer_type = DeserializerFloat

    def get_col_spec(self):
        return "TFLOAT"

    @staticmethod
    def validate_type(value):
        dtypes = value["value"].dtypes
        if not is_numeric_dtype(dtypes):
            raise TypeError(
                "TInt needs int values. Got: {} Expected {}".format(dtypes.kind, "f")
            )
