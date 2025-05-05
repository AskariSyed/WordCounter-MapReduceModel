from collections import Counter

def reduce_counts(mapper_results):
    final_counter = Counter()
    for mapper_id in mapper_results:
        final_counter += mapper_results[mapper_id]
    return final_counter
