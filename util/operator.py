def apply_operator(operator, value: str, other):
    if operator == "contains":
        return other in value
    if operator == "not contains":
        return other not in value
    if operator == "equals":
        return eq(value, other)
    if operator == "starts with":
        return value.startswith(other)
    if operator == "ends with":
        return value.endswith(other)
    if operator == "is empty":
        return len(value) == 0
    if operator == "is not empty":
        return len(value) > 0
