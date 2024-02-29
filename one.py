# A simple dictionary to represent the documents
documents = {
    1: "Soccer tutorial and training drills",
    2: "Book on soccer tactics and strategies",
    3: "Learning soccer formations and positions",
    4: "Advanced soccer skills and techniques",
    5: "Analysis of soccer matches and player performances"
}

# A dictionary to store the inverted index
inverted_index = {}

# Populate the inverted index
for doc_id, text in documents.items():
    for word in text.split():
        if word not in inverted_index:
            inverted_index[word] = set()
        inverted_index[word].add(doc_id)

# The query
query = "advanced AND skills AND NOT analysis"

# Parse the query
query_terms = query.split()
query_sets = []
current_set = set()

for term in query_terms:
    if term == "and":
        query_sets.append(current_set)
        current_set = set()
    elif term == "or":
        query_sets.append(current_set)
        current_set = set()
    elif term in inverted_index:
        current_set.update(inverted_index[term])
    else:
        query_sets.append(current_set)

# Intersection of query sets
result_set = query_sets[0]
for i in range(1, len(query_sets)):
    result_set = result_set.intersection(query_sets[i])

# Get the document ids from the result set
document_ids = list(result_set)

# Print the result
print("Documents matching the query:")
for doc_id in document_ids:
    print(f"Document {doc_id}: {documents[doc_id]}")
