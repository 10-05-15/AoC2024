def is_safe_sequence(levels):
    """Check if a sequence of levels is safe according to the rules."""
    if len(levels) < 2:
        return True
        
    # Check first difference to determine direction
    dir_up = levels[1] > levels[0]
    
    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]
        
        # Must maintain same direction
        if dir_up and diff <= 0:
            return False
        if not dir_up and diff >= 0:
            return False
            
        # Must differ by 1-3
        if abs(diff) < 1 or abs(diff) > 3:
            return False
            
    return True

def check_dampened_safety(levels):
    """Check if sequence is safe with Problem Dampener (can remove one number)."""
    # First check if already safe
    if is_safe_sequence(levels):
        return True
        
    # Try removing each number one at a time
    for i in range(len(levels)):
        test_sequence = levels[:i] + levels[i+1:]
        if is_safe_sequence(test_sequence):
            return True
            
    return False

def process_file(filename):
    """Process input file and count safe reports with Problem Dampener."""
    safe_count = 0
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.strip():  # Skip empty lines
                    # Convert line to list of integers
                    levels = [int(x) for x in line.strip().split()]
                    if check_dampened_safety(levels):
                        safe_count += 1
                        
        return safe_count
    except FileNotFoundError:
        print(f"Error: Could not find file '{filename}'")
        return None
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        return None

# Main execution
if __name__ == "__main__":
    filename = "/Users/j03/Desktop/Coding/GitHub/AoC/AoC2024/puzzle2Levels.txt"  # Change this to your input file name
    result = process_file(filename)
    
    if result is not None:
        print(f"Number of safe reports with Problem Dampener: {result}")