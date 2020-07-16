from decimal import Decimal

from flask import jsonify, json, Flask

class DecimalJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            # Convert decimal instances to strings.
            return float(obj)
        return super(DecimalJSONEncoder, self).default(obj)

Flask.json_encoder =  DecimalJSONEncoder

