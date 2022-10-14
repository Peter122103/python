if __name__ == "__main__":
    # user input
    user_input = input

    # specify an answer
    answer = "apple"

    #compare user input and answer
    for i in range(len(user_input)):
        if user_input[i] == answer[i]:
            print("A")
        elif user_input[i] in answer:
            print("B")
        else:
            print("X")