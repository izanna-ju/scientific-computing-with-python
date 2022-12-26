def arithmetic_arranger(problems, *args):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = []

    for problem in problems:
        # parse string of problem into its individual element
        ops = problem.split(" ")
        num_1 = ops[0]
        num_2 = ops[2]
        operation = ops[1]

        if ops[1] not in "+-":
            return "Error: Operator must be '+' or '-'."
        if len(ops[0]) > 4 or len(ops[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        if ops[0].isdigit() and ops[2].isdigit(): pass
        else:
            return "Error: Numbers must only contain digits."
        num_1 = ops[0]
        num_2 = ops[2]
        operation = ops[1]

        longest_num = max(len(num_1), len(num_2))
        max_len = longest_num + 2
        dash_length = "-" * (max_len)

        jxt_num_1 = num_1.rjust(max_len)
        jxt_num_2 = num_2.rjust(max_len - 2)

        comb_bot = f"{operation} {jxt_num_2}"

        # print(answer)

        try:
            arranged_problems[0] += (" " * 4)  + jxt_num_1
        except IndexError:
            arranged_problems.append(jxt_num_1)

        try:
            arranged_problems[1] += (" " * 4) + comb_bot
        except IndexError:
            arranged_problems.append(comb_bot)

        try:
            arranged_problems[2] += (" " * 4) + dash_length
        except IndexError:
            arranged_problems.append(dash_length)


        if args:
            if operation == "+" :
                ans = int(num_1) + int(num_2)
            else:
                ans = int(num_1) - int(num_2)

            answer = str(ans).rjust(max_len)

            try:
                arranged_problems[3] += (" " * 4) + answer
            except IndexError:
                arranged_problems.append(answer)



    output =  f"{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}"

    output = output + f"\n{arranged_problems[3]}" if args else output

    return output
