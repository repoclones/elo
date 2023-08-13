import os
import sys

# not being in the root dir thing
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

if not os.path.exists(os.path.join(current_dir, "test_artifacts")):
    os.mkdir(os.path.join(current_dir, "test_artifacts"))

import grading_functions

def test_message_rating_system():
    with open(os.path.join(current_dir, "./chat_examples/chat_logs.txt")) as f:
        testlist = f.readlines()
    for line in testlist:
        line = line.strip()
        print(f"{grading_functions.normalization_function_entropy(grading_functions.grade_entropy(line)):<22}{line}")

def test_normalization_function_entropy():
    import matplotlib.pyplot as plt
    list_of_values = []
    for i in range(0,100, 1):
        j = i / 100
        value = grading_functions.normalization_function_entropy(j)
        list_of_values.append([j,value])
    plt.plot([point[0] for point in list_of_values], [point[1] for point in list_of_values])
    plt.xlabel('Input')
    plt.ylabel('Output')
    plt.title('Normalization Mapping')
    plt.grid(True)
    
    # Save the image to disk (in PNG format)
    plt.savefig(os.path.join(current_dir, "test_artifacts", "Entropy normalization mapping.png"))
    for value in list_of_values:
        print(value)
        assert value[1] <= 1
        assert value[1] >= 0


if __name__ == "__main__":
    test_message_rating_system()
    # test_normalization_function_entropy()
