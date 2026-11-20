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