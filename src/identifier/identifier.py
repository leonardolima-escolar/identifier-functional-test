def validate_identifier(identifier: str):
    length = len(identifier)
    if length < 1 or length > 6 or identifier[0].isdigit() or not identifier.isalnum():
        return "Inválido"
    else:
        return "Válido"
