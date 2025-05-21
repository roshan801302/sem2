class SET:
    def __init__(self, elements):
        self.elements = set(elements)

    def ismember(self, elem):
        return elem in self.elements

    def powerset(self):
        from itertools import chain, combinations
        return list(chain.from_iterable(combinations(self.elements, r) for r in range(len(self.elements)+1)))

    def subset(self, other):
        return self.elements.issubset(other.elements)

    def union(self, other):
        return self.elements.union(other.elements)

    def intersection(self, other):
        return self.elements.intersection(other.elements)

    def complement(self, universal):
        return set(universal) - self.elements

    def difference(self, other):
        return self.elements.difference(other.elements)

    def symmetric_difference(self, other):
        return self.elements.symmetric_difference(other.elements)

    def cartesian_product(self, other):
        return [(a, b) for a in self.elements for b in other.elements]


def menu():
    U = list(map(int, input("Enter elements of Universal Set: ").split()))
    A = SET(list(map(int, input("Enter elements of Set A: ").split())))
    B = SET(list(map(int, input("Enter elements of Set B: ").split())))

    while True:
        print("\nMenu:")
        print("1. isMember")
        print("2. Power Set")
        print("3. Subset Check")
        print("4. Union")
        print("5. Intersection")
        print("6. Complement (of A)")
        print("7. Set Difference (A - B)")
        print("8. Symmetric Difference")
        print("9. Cartesian Product (A x B)")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            x = int(input("Enter element to check in A: "))
            print("Yes" if A.ismember(x) else "No")

        elif choice == "2":
            print("Power set of A:", A.powerset())

        elif choice == "3":
            print("A is subset of B:", A.subset(B))

        elif choice == "4":
            print("Union:", A.union(B))

        elif choice == "5":
            print("Intersection:", A.intersection(B))

        elif choice == "6":
            print("Complement of A:", A.complement(U))

        elif choice == "7":
            print("A - B:", A.difference(B))

        elif choice == "8":
            print("Symmetric Difference:", A.symmetric_difference(B))

        elif choice == "9":
            print("Cartesian Product A x B:", A.cartesian_product(B))

        elif choice == "0":
            break

        else:
            print("Invalid choice!")

menu()
