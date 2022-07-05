def generate_solutions(oklepaji: int, zaklepaji: int, s: str, solutions: set) -> set:
    if zaklepaji < oklepaji:
        return solutions

    if oklepaji < 0 or zaklepaji < 0:
        return solutions

    if oklepaji == 0 and zaklepaji == 0:
        solutions.add(s)
        return solutions
    generate_solutions(oklepaji - 1, zaklepaji, s + "(", solutions)
    generate_solutions(oklepaji, zaklepaji - 1, s + ")", solutions)
    return solutions


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return list(generate_solutions(n - 1, n, "(", set()))
