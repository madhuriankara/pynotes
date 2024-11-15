import jellyfish

def levenshtein_distance(str1, str2):
    if not str1: return len(str2)
    if not str2: return len(str1)

    if str1[0] == str2[0]:
        return levenshtein_distance(str1[1:], str2[1:])

    return 1 + min(
        levenshtein_distance(str1[1:], str2),   # Deletion
        levenshtein_distance(str1, str2[1:]),   # Insertion
        levenshtein_distance(str1[1:], str2[1:])  # Substitution
    )

# Example usage:
str1 = "kitten"
str2 = "sitting"
print("Levenshtein Distance:", levenshtein_distance(str1, str2))

# Calculate similarity using Jellyfish's Jaro-Winkler similarity
similarity = jellyfish.jaro_winkler_similarity(str1, str2)
print("Jaro-Winkler similarity:", similarity)
