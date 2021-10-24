import random

legend = ["R", "B", "Y", "G", "W", "O"]
scode_length = 4
attemps = 10


def create_secret_code(choice_list, len):
    rand_list = []
    for _ in range(len):
        rand_list.append(random.choice(choice_list))
    return rand_list


def Check_code(secret_code, input_code):
    print("Checking the input secret code with the correct one...")
    solution = []
    if secret_code == input_code:
        return solution

    for idx, c in enumerate(input_code):
        if c in secret_code:
            if secret_code[idx] == c:
                solution.append("B")
                continue
            solution.append("W")

    return randomize_solution(solution)


def randomize_solution(solution):
    rand_solution = []
    for _ in range(len(solution)):
        itm = random.choice(solution)
        rand_solution.append(itm)
        solution.remove(itm)
    return rand_solution


if __name__ == "__main__":

    print("Welocme to MasterMind game!")
    secret_code = create_secret_code(legend, scode_length)

    print("New secret code is created, please start writing some codes to check the result.")
    print("Legend: (R)ed, (B)lue, (Y)ellow, (G)reen, (W)hite, (O)range")

    for i in range(1, attemps+1):
        print("Attemps: %d/%d" % (i, attemps))
        code = input()

        while len(code) > scode_length or len(code) == 0:
            print("Input charecters should be 4!")
            code = input()

        input_code = [c.upper() for c in code]
        solution = Check_code(secret_code, input_code)

        if len(solution) == 0:
            print("You win!")
            break
        print("The feedback solution is: ", solution)
