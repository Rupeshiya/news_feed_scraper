import decimal
from typing import Any
from jsonpickle.handlers import BaseHandler
import jsonpickle


class JsonPickleDecimal:
    @staticmethod
    # convert complex objects to json format
    def encode(values: Any):
        jsonpickle.set_preferred_backend('simplejson')
        jsonpickle.set_encoder_options('simplejson', use_decimal=True, sort_keys=True)

        SimpleDecimalHandler.handles(decimal.Decimal)
        return jsonpickle.encode(values, unpicklable=False)

    @staticmethod
    # convert json string to python objects
    def decode(json: str) -> Any:
        jsonpickle.set_preferred_backend('simplejson')
        jsonpickle.set_decoder_options('simplejson', use_decimal=True)
        return jsonpickle.decode(json)


class SimpleDecimalHandler(BaseHandler):
    # Flatten obj into a json-friendly form and write result to data.
    def flatten(self, obj, data):
        return obj

    # Restore an object from the json-friendly representation obj and return it.
    def restore(self, obj):
        return obj
