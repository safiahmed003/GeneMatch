import pandas as pd


def lcs(seq1, seq2):
    m, n = len(seq1), len(seq2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct LCS
    i, j = m, n
    result = []

    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            result.append(seq1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(result[::-1])

def validate_sequence(seq):
    seq = "".join(seq.split()).upper()

    if not seq:
        raise ValueError("DNA sequence cannot be empty.")

    if any(char not in "ACGTN" for char in seq):
        raise ValueError("Invalid DNA sequence! Use only A, C, G, T, N.")

    return seq
def compare_sequences(seq1, seq2):
    common = lcs(seq1, seq2)
    percentage = (len(common) / max(len(seq1), len(seq2))) * 100

    print("\n========== DNA COMPARISON ==========")
    print("Sequence 1 :", seq1)
    print("Sequence 2 :", seq2)
    print("LCS         :", common)
    print("LCS Length  :", len(common))
    print(f"Match       : {percentage:.2f}%")
    print("===================================")

def manual_input():
    try:
        seq1 = validate_sequence(input("\nEnter DNA sequence 1: "))
        seq2 = validate_sequence(input("Enter DNA sequence 2: "))
        compare_sequences(seq1, seq2)
    except ValueError as e:
        print("Error:", e)