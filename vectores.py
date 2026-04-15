"""
Marcel Botines Ramallo









class Vector:
    vector = []

    def __init__(self, numeros):
        self.vector = list(numeros)

    def __repr__(self):
        return f"Vector({self.vector})"

    def __str__(self):
        return "[" + " ".join(str(c) for c in self.vector) + " ]"

    def __mul__(self, other):
        resultado = []

        if isinstance(other, (int, float)):
            resultado = [x * other for x in self.vector]

        elif isinstance(other, Vector):
            if len(self.vector) != len(other.vector):
                raise ValueError("Dimensiones incompatibles")
            resultado = [
                a * b for a, b in zip(self.vector, other.vector)
            ]

        return Vector(resultado)

    def __rmul__(self, other):
        return self * other

    def __matmul__(self, v2):
        return sum(a * b for a, b in zip(self.vector, v2.vector))

    def __rmatmul__(self, v2):
        return self @ v2

    def __floordiv__(self, v2):
        factor = (self @ v2) / (v2 @ v2)
        return v2 * factor

    def __rfloordiv__(self, v2):
        factor = (self @ v2) / (self @ self)
        return self * factor

    def __mod__(self, v2):
        v1_paralelo = self // v2
        resultado = [
            a - b for a, b in zip(self.vector, v1_paralelo.vector)
        ]
        return Vector(resultado)

    def __rmod__(self, v2):
        v1_paralelo = v2 // self
        resultado = [
            a - b for a, b in zip(v1_paralelo.vector, self.vector)
        ]
        return Vector(resultado)
        
        
    
