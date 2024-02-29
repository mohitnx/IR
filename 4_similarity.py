import string
def preprocess_text(text):
 text = text.lower()
 text = text.translate(str.maketrans('', '', string.punctuation))
 return text
def create_bow(text):
 words = text.split()
 word_count = {}
 for word in words:
    if word in word_count:
         word_count[word] += 1
    else:
        word_count[word] = 1
 return word_count
def calculate_similarity(bow1, bow2):
 all_words = set(bow1.keys()).union(set(bow2.keys()))
 dot_product = sum(bow1.get(word, 0) * bow2.get(word, 0) for word in all_words)
 magnitude1 = sum(val ** 2 for val in bow1.values()) ** 0.5
 magnitude2 = sum(val ** 2 for val in bow2.values()) ** 0.5
 # Calculate cosine similarity
 if magnitude1 == 0 or magnitude2 == 0:
     return 0
 else:
        return dot_product / (magnitude1 * magnitude2)
def main():
    doc1 = "my name is mohit neupane."
    doc2 = "mohit neupane loves football."

    doc1 = preprocess_text(doc1)
    doc2 = preprocess_text(doc2)
    bow1 = create_bow(doc1)
    bow2 = create_bow(doc2)

    # Calculate similarity
    similarity = calculate_similarity(bow1, bow2)

    print("Document 1:", doc1)
    print("Document 2:", doc2)
    print("Similarity:", similarity)

if __name__ == "__main__":
    main()