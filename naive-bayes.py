import csv

# 1: Define the dataset by reading from 'data.csv'
data = []
with open('data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# 2: Print the dataset
print("Training Data Table:")
for i, entry in enumerate(data):
    print(f"{i}: {entry}")
print("\n")

# 3: Print number of rows and columns in the dataset
num_rows = len(data)
num_columns = len(data[0]) if data else 0
print(f"Number of Rows: {num_rows}")
print(f"Number of Columns: {num_columns}")
print("\n")

# 4: Calculate and print individual class probabilities
stolen_yes_count = sum(1 for x in data if x['Stolen?'] == 'Yes')
stolen_no_count = sum(1 for x in data if x['Stolen?'] == 'No')
p_stolen_yes = stolen_yes_count / num_rows
p_stolen_no = stolen_no_count / num_rows
print(f"Probability of 'Stolen? = Yes': {p_stolen_yes}")
print(f"Probability of 'Stolen? = No': {p_stolen_no}")
print("\n")

# 5: Calculate and print probability of individual values of attributes
def calculate_likelihood(attribute, value, stolen_status):
    subset = [x for x in data if x['Stolen?'] == stolen_status] 
    count = sum(1 for x in subset if x[attribute] == value)
    likelihood = count / len(subset) if subset else 0
    print(f"P({attribute}={value} | Stolen?={stolen_status}): {likelihood}")
    return likelihood

print("Probability of Individual Values of Attributes Given 'Stolen? = Yes':")
likelihood_stolen_yes_color = calculate_likelihood('Color', 'Red', 'Yes')
likelihood_stolen_yes_type = calculate_likelihood('Type', 'SUV', 'Yes')
likelihood_stolen_yes_origin = calculate_likelihood('Origin', 'Domestic', 'Yes')

print("\nProbability of Individual Values of Attributes Given 'Stolen? = No':")
likelihood_stolen_no_color = calculate_likelihood('Color', 'Red', 'No')
likelihood_stolen_no_type = calculate_likelihood('Type', 'SUV', 'No')
likelihood_stolen_no_origin = calculate_likelihood('Origin', 'Domestic', 'No')
print("\n")

# 6: Print new tuple for classification
new_tuple = {'Color': 'Red', 'Type': 'SUV', 'Origin': 'Domestic'}
print("New Tuple for Classification:")
print(new_tuple)
print("\n")

# 7: Print class probabilities
posterior_stolen_yes = likelihood_stolen_yes_color * likelihood_stolen_yes_type * likelihood_stolen_yes_origin * p_stolen_yes
posterior_stolen_no = likelihood_stolen_no_color * likelihood_stolen_no_type * likelihood_stolen_no_origin * p_stolen_no
print("Posterior Probabilities:")
print(f"P(Stolen? = Yes | New Tuple): {posterior_stolen_yes}")
print(f"P(Stolen? = No | New Tuple): {posterior_stolen_no}")

# 8: Classify the new tuple
if posterior_stolen_yes > posterior_stolen_no:
    print("The new tuple is classified as stolen: Yes")
else:
    print("The new tuple is classified as stolen: No")
