def initialize_page_ranks(n):
    return {chr(97 + i): 1 / n for i in range(n)}

def get_matrix(n):
    return [list(map(int, input(f"Enter row {i + 1}: ").split())) for i in range(n)]

def display_matrix(matrix):
    print("\nThe entered matrix is:")
    for row in matrix:
        print(row)

def display_page_ranks(page_ranks, message="Page ranks"):
    print(f"\n{message}:")
    for key, value in page_ranks.items():
        print(f"{key}: {value:.4f}")

def update_page_ranks(page_ranks, matrix, factor, n):
    for i in range(n):
        inbound_sum = 0
        for j in range(n):
            if matrix[j][i] == 1 and sum(matrix[j]) > 0:
                inbound_sum += page_ranks[chr(97 + j)] / sum(matrix[j])
        new_rank = (1 - factor) + factor * inbound_sum
        page_ranks[chr(97 + i)] = new_rank

        print(f"\nCalculation for {chr(97 + i)}:")
        print(f"PR({chr(97 + i)}) = (1 - {factor}) + {factor} * ({inbound_sum:.4f})")
        print(f"PR({chr(97 + i)}) = {1 - factor:.4f} + {factor} * {inbound_sum:.4f} = {new_rank:.4f}")

def find_highest_rank(page_ranks):
    highest_node = max(page_ranks, key=page_ranks.get)
    highest_value = page_ranks[highest_node]
    print(f"\nThe node with the highest PageRank is '{highest_node}' with a value of {highest_value:.4f}.")

def main():
    it = int(input("Enter number of iterations: "))
    factor = float(input("Enter teleportation factor (between 0 and 1): "))
    n = int(input("Enter number of pages: "))

    page_ranks = initialize_page_ranks(n)
    matrix = get_matrix(n)

    display_matrix(matrix)
    display_page_ranks(page_ranks, "Initial page ranks")
    for x in range(1, it + 1):
        print(f"\nIteration {x}:")
        update_page_ranks(page_ranks, matrix, factor, n)
        display_page_ranks(page_ranks, "Updated page ranks")
    find_highest_rank(page_ranks)

if __name__ == '__main__':
    main()
