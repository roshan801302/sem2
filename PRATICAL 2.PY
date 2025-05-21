class RELATION:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)

    def is_reflexive(self):
        return all(self.matrix[i][i] == 1 for i in range(self.n))

    def is_symmetric(self):
        return all(self.matrix[i][j] == self.matrix[j][i] for i in range(self.n) for j in range(self.n))

    def is_antisymmetric(self):
        return all(self.matrix[i][j] == 0 or self.matrix[j][i] == 0 for i in range(self.n) for j in range(self.n) if i != j)

    def is_transitive(self):
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    if self.matrix[i][j] and self.matrix[j][k] and not self.matrix[i][k]:
                        return False
        return True

    def relation_type(self):
        ref = self.is_reflexive()
        sym = self.is_symmetric()
        anti = self.is_antisymmetric()
        trans = self.is_transitive()

        print("Reflexive:", ref)
        print("Symmetric:", sym)
        print("Anti-symmetric:", anti)
        print("Transitive:", trans)

        if ref and sym and trans:
            return "Equivalence Relation"
        elif ref and anti and trans:
            return "Partial Order Relation"
        else:
            return "None"

# User interaction
n = int(input("Enter the size of the matrix: "))
print("Enter the relation matrix row by row (space-separated):")
matrix = [list(map(int, input().split())) for _ in range(n)]

R = RELATION(matrix)
print("Relation Type:", R.relation_type())
