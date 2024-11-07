def get_frequent_itemsets(transactions, min_support):
    item_count = {}
    for transaction in transactions:
        for item in transaction:
            item_count[item] = item_count.get(item, 0) + 1

    frequent_itemsets = {frozenset([item]): count for item, count in item_count.items() if count >= min_support}
    all_frequent_itemsets = dict(frequent_itemsets)
    k = 2
    iteration = 1

    while frequent_itemsets:
        candidate_sets = {}
        itemsets = list(frequent_itemsets.keys())
        print(f"\nIteration {iteration}: Generating Candidates of size {k}")

        # Generate candidate itemsets of size k
        for i in range(len(itemsets)):
            for j in range(i + 1, len(itemsets)):
                union_set = itemsets[i] | itemsets[j]
                if len(union_set) == k:
                    candidate_sets[union_set] = 0

        print("Candidates generated:")
        for candidate in candidate_sets:
            print(f"Candidate: {set(candidate)}")

        # Count support for candidate sets
        for transaction in transactions:
            transaction_set = set(transaction)
            for candidate in candidate_sets:
                if candidate.issubset(transaction_set):
                    candidate_sets[candidate] += 1

        print("\nSupport values for candidates:")
        for itemset, count in candidate_sets.items():
            print(f"Candidate: {set(itemset)}, Support: {count}")

        # Filter candidates to find frequent itemsets
        frequent_itemsets = {itemset: count for itemset, count in candidate_sets.items() if count >= min_support}
        all_frequent_itemsets.update(frequent_itemsets)

        print("\nFrequent itemsets after filtering:")
        for itemset, count in frequent_itemsets.items():
            print(f"Frequent Itemset: {set(itemset)}, Support: {count}")

        if not frequent_itemsets:
            print(f"\nIteration {iteration}: No more frequent itemsets found.")
            break

        k += 1
        iteration += 1

    return all_frequent_itemsets

def get_association_rules(frequent_itemsets, min_confidence):
    rules = []
    for itemset, itemset_support in frequent_itemsets.items():
        if len(itemset) > 1:
            itemset_list = list(itemset)
            for i in range(len(itemset_list)):
                subset = frozenset([itemset_list[i]])
                if subset in frequent_itemsets:
                    confidence = itemset_support / frequent_itemsets[subset]
                    if confidence >= min_confidence:
                        rules.append((subset, itemset - subset, confidence))
    return rules

transactions = [
    ['11', '12', '15'],
    ['12', '14'],
    ['12', '13'],
    ['11', '12', '14'],
    ['11', '13'],
    ['12', '13'],
    ['11', '13'],
    ['11', '12', '13', '15'],
    ['11', '12', '13'],
]

min_support = 2
min_confidence = 0.6 

print(f"Number of transactions: {len(transactions)}")
print(f"Number of items in transactions: {sum(len(t) for t in transactions)}")

frequent_itemsets = get_frequent_itemsets(transactions, min_support)
print("\nFinal Frequent Item Sets:")
for itemset, count in frequent_itemsets.items():
    print(f"{set(itemset)}: {count}")

association_rules = get_association_rules(frequent_itemsets, min_confidence)
print("\nAssociation Rules:")
for antecedent, consequent, confidence in association_rules:
    print(f"{set(antecedent)} -> {set(consequent)}, confidence: {confidence:.2f}")
