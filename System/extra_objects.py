from System.exceptions import WrongVectorSizeValue


class SpaceObject:
    """SpaceObject - object in space, which is necessary
    for modeling the behavior of the interaction
    of the forces of attraction.
    SpaceObject methods:

    """
    def __init__(self, cords: list, speed: list, mass: int, radius: int, color: str, ):
        self.cords: Cords = Cords(*cords)
        self.speed: Cords = Cords(*speed)
        self.mass: int = mass
        self.radius: int = radius
        self.color: str = color
        self.canvas_id: int = None


class Cords:
    """Cords - is a cords position.
    Cords methods:
        add() - mathematical sum of vectors --> Vector()
        sub() - mathematical sub of vectors --> Vector()
        mul() - mathematical mul of vectors --> Vector()
        div() - mathematical div of vectors --> Vector()
    """
    def __init__(self, *nums):
        """
        :param nums: cords in space
        """
        self.numbers = nums

    def __len__(self):
        return len(self.numbers)

    def is_available_type(self, other):
        """If other object type is not available, raise Exception
        :param other: type of other objects
        :return:
        """
        pass

    def __add__(self, other):
        if self.__len__() != len(other):
            raise WrongVectorSizeValue

        result_vector_list = [self.numbers[i] + other.numbers[i] for i in range(self.__len__())]
        return Cords(*result_vector_list)

    def __sub__(self, other):
        if self.__len__() != len(other):
            raise WrongVectorSizeValue

        result_vector_list = [self.numbers[i] - other.numbers[i] for i in range(self.__len__())]
        return Cords(*result_vector_list)

    def __mul__(self, other):
        if self.__len__() != len(other):
            raise WrongVectorSizeValue

        result_vector_list = [self.numbers[i] * other.numbers[i] for i in range(self.__len__())]
        return Cords(*result_vector_list)

    def __div__(self, other):
        if self.__len__() != len(other):
            raise WrongVectorSizeValue

        result_vector_list = [self.numbers[i] / other.numbers[i] for i in range(self.__len__())]
        return Cords(*result_vector_list)

    def __str__(self):
        return f"{self.numbers}"

