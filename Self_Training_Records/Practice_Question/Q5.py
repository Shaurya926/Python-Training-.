# Write a program to construct the algo for AI.
def ai_algorithm(data):
    # Example: A simple AI algorithm that classifies data based on a threshold
    threshold = sum(data) / len(data)
    classified_data = {'above_threshold': [], 'below_threshold': []}

    for item in data:
        if item >= threshold:
            classified_data['above_threshold'].append(item)
        else:
            classified_data['below_threshold'].append(item)

    return classified_data
# Sample data
data = [10, 20, 30, 40, 50, 60]
result = ai_algorithm(data)
print("Classified Data:", result)
# Output: Classified Data: {'above_threshold': [40, 50, 60],
