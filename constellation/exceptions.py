class WrongVectorSizeValue(Exception):

    def __init__(self):
        self.msg = "Vectors have different sizes and cannot be stacked"

    def __str__(self):
        return self.msg


class TypeVectorError(Exception):

    actions = {'div': "/", 'mul': "*", 'sum': "+", 'sub': "-"}

    def __init__(self, action, other_type):
        self.msg = f"unsupported operand type(s) for {self.actions[action]}: 'cords' and '{other_type}'"

    def __str__(self):
        return self.msg
