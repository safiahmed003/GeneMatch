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
def csv_input():
    try:
        file1 = input("\nEnter CSV file path 1: ")
        file2 = input("Enter CSV file path 2: ")

        df1 = pd.read_csv(file1)
        df2 = pd.read_csv(file2)

        print("\nFile 1 columns:", list(df1.columns))
        col1 = input("Select sequence column from file 1: ")

        print("\nFile 2 columns:", list(df2.columns))
        col2 = input("Select sequence column from file 2: ")

        if col1 not in df1.columns or col2 not in df2.columns:
            print("Invalid column name!")
            return

        seq1 = validate_sequence(
            "".join(df1[col1].dropna().astype(str))
        )
        seq2 = validate_sequence(
            "".join(df2[col2].dropna().astype(str))
        )

        compare_sequences(seq1, seq2)

    except FileNotFoundError:
        print("Error: CSV file not found!")
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Error:", e)

def main():
    while True:
        print("\n========== LCS DNA ANALYZER ==========")
        print("1. Manual DNA Sequence Comparison")
        print("2. DNA Sequence Comparison Using CSV")
        print("3. Exit")
        print("======================================")

        choice = input("Select an option: ")

        if choice == "1":
            manual_input()
        elif choice == "2":
            csv_input()
        elif choice == "3":
            print("Program terminated.")
            break
        else:
            print("Invalid option! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()