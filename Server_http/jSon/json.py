schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"},
        "scores": {
            "type": "array",
            "items": {"type": "number"},
        }
    },
    "required": ["name"],
    "additionalProperties": False
}
instance =  {
try:
    validate(instance, schema)
    print("L'istanza è coerente con lo schema")
except jsonschema.exceptions.ValidationError:
    print("L'istanza non è valida")
