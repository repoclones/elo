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

def normalization_function_entropy(entropy_value: float) -> float:
    """
    in the grade_entropy result and map it to follow human text values, return the multiplier between 0 and 1
    """
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

