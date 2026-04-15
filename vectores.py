"""
Marcel Botines Ramallo


"""






class Vector:
    def __init__(self, numeros, verbose=False):
        self.vector = list(numeros)
        self.verbose = verbose

    def _log(self, mensaje):
        if self.verbose:
            print(mensaje)

    def __repr__(self):
        return f"Vector({self.vector})"

    def __str__(self):
        return "[" + " ".join(str(c) for c in self.vector) + " ]"

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            self._log(f"Multiplicación escalar: {self.vector} * {other}")
            resultado = [x * other for x in self.vector]
            return Vector(resultado, self.verbose)

        elif isinstance(other, Vector):
            self._log(f"Multiplicación elemento a elemento: {self.vector} * {other.vector}")

            if len(self.vector) != len(other.vector):
                raise ValueError("Dimensiones incompatibles")

            resultado = [a * b for a, b in zip(self.vector, other.vector)]
            return Vector(resultado, self.verbose)

        return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __matmul__(self, v2):
        self._log(f"Producto escalar: {self.vector} @ {v2.vector}")
        return sum(a * b for a, b in zip(self.vector, v2.vector))

    def __rmatmul__(self, v2):
        return self @ v2

    def __floordiv__(self, v2):
        self._log(f"Proyección: {self.vector} // {v2.vector}")
        factor = (self @ v2) / (v2 @ v2)
        resultado = [x * factor for x in v2.vector]
        return Vector(resultado, self.verbose)

    def __rfloordiv__(self, v2):
        self._log(f"Proyección (reverse): {v2.vector} // {self.vector}")
        factor = (v2 @ self) / (self @ self)
        resultado = [x * factor for x in self.vector]
        return Vector(resultado, self.verbose)

    def __mod__(self, v2):
        self._log(f"Componente perpendicular: {self.vector} % {v2.vector}")
        v_paralela = self // v2
        resultado = [a - b for a, b in zip(self.vector, v_paralela.vector)]
        return Vector(resultado, self.verbose)

    def __rmod__(self, v2):
        self._log(f"Componente perpendicular (reverse): {v2.vector} % {self.vector}")
        v_paralela = v2 // self
        resultado = [a - b for a, b in zip(v_paralela.vector, self.vector)]
        return Vector(resultado, self.verbose)
        
    
