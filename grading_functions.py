import gzip
from io import BytesIO

def map_value(value, from_min, from_max, to_min, to_max):
    """
    Map a value from one range to another.
    """
    from_range = from_max - from_min
    to_range = to_max - to_min

    # Avoid division by zero
    if from_range == 0:
        return to_min

    # Calculate the normalized position of the value in the from range
    normalized_value = (value - from_min) / from_range

    # Map the normalized value to the new range
    return to_min + normalized_value * to_range

def calculate_gzip_compression_ratio(string):
    with BytesIO() as buf:
        with gzip.GzipFile(fileobj=buf, mode='wb') as f:
            f.write(string.encode('utf-8'))
        compressed_data = buf.getvalue()

    original_size = len(string.encode('utf-8'))
    compressed_size = len(compressed_data)
    
    # Ensure no division by zero when the string is empty or very short
    if original_size == 0:
        return 0.0
    
    compression_ratio = min(compressed_size / original_size, 2.0)
    return compression_ratio

def grade_entropy(string):
    compression_ratio = calculate_gzip_compression_ratio(string)
    
    # Normalize the compression ratio to a scale from 0 to 1
    normalized_ratio = compression_ratio / 2.0
    
    # Invert the normalized ratio so that high values represent better grades
    #grade = 1.0 - normalized_ratio
    if normalized_ratio == 1.0: # most probably just too short
        return 0.0
    
    return normalized_ratio

def normilization_function_entropy(entropy_value: float) -> float:
    # Take in the grade_entropy result and map it to follow human text values, return the multiplier between 0 and 1
    pass
    if entropy_value < 0.35:
        return 0
    elif entropy_value < 0.6:
        return map_value(entropy_value, 0.35, 0.6, 0.0, 0.9)
    elif entropy_value < 0.8:
        return map_value(entropy_value, 0.6, 0.8, 0.9, 1.0)
    elif entropy_value < 0.95:
        return map_value(entropy_value, 0.8, 0.95, 1.0, 0.3)
    else:
        return 0.3
    

if __name__ == "__main__":
    # Test the function with an example string
    from main import grade_text
    example_string = "the cat in the hat hat hat"
    example_string = input()
    grade = grade_text(example_string, 0)
    print(f"Entropy grade: {grade}")

    example_list = [
        "Thanks for subscibing Coremaster! If you have any questions feel free to ask them in chat.",
        "thanks for subscibing coremaster if you have any questions feel free to ask them in chat",
        "discord",
        "nihmunHypernums nihmunHypernums nihmunHypernums nihmunHypernums nihmunHypernums nihmunHypernums nihmunHypernums nihmunHypernums nihmunHypernums nihmunHypernums nihmunHypernums nihmunHypernums nihmunHypernums nihmunHypernums nihmunHypernums nihmunHypernums nihmunHypernums nihmunHypernums nihmunHypernums nihmunHypernums nihmunHypernums nihmunHypernums nihmunHypernums nihmunHypernums",
        "Sounds painful",
        "Im coming over!",
        "WHY THE DOUBTFUL SATTHE END LMAO",
        "tucker carlson KEKW",
        "4 fingers and one thumb she knows how to count",
        "ICANT wtf ARE THESE LINES",
        "SOUNDS LIKE SHE IS HAVING A STROKE DIESOFCRINGE",
        "Math check ! Is 7+8=15 correct? Is 140/10=14 correct? Is 9*7=103 correct ? Is 11-5=6 correct?",
        "squchaHeart My Fuzzy Baby squchaHeart My Fuzzy Baby squchaHeart My Fuzzy Baby squchaHeart My Fuzzy Baby squchaHeart My Fuzzy Baby",
        "a euro said she hopes Gillian gets kidnapped going to get milk",
        "I wonder if minutes can be divided by 3 ?",
        "gigaevil NeuroGunPull neurolingScared",
        "time loop"
    ]
    for example in example_list:
        print(f"{grade_text(example, 0):<4} string: {example}")

    #import matplotlib.pyplot as plt
    ## Test the function and generate data points
    #inputs = [x / 100 for x in range(101)]  # Generate values from 0 to 1 with a step of 0.01
    #outputs = [normilization_function_entropy(x) for x in inputs]
    ## Plot the data
    #plt.plot(inputs, outputs)
    #plt.xlabel('Input')
    #plt.ylabel('Output')
    #plt.title('Input-Output Mapping')
    #plt.grid(True)
    #plt.savefig('input_output_mapping.png') # Save the image to disk (in PNG format)
    #plt.show()

# sorted_data = sorted(csv_dump, key=lambda x: x[2])
# for index, data in enumerate(sorted_data):
#     sorted_data[index] = data[0] + "\t\t\t" + str(data[1]) + "  " + str(data[2]) + "\n"
# with open("./debug_elolist", "w") as f:
#     f.writelines(sorted_data)
