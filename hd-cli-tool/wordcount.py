import sys
from collections import Counter
import re

def main():
    input_path = "/data/input.txt"
    output_path = "/data/output.txt"

    print(f"Reading from {input_path}...")

    try:
        with open(input_path, 'r') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"ERROR: {input_path} not found. Make sure to mount a volume to /data.")
        sys.exit(1)

    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    counts = Counter(words)

    print(f"Processed {len(words)} words, {len(counts)} unique.")

    with open(output_path, 'w') as f:
        f.write("Word Frequency Report\n")
        f.write("======================\n\n")
        for word, count in counts.most_common(20):
            f.write(f"{word}: {count}\n")

    print(f"Results written to {output_path}")
    print("Top 5 words:")
    for word, count in counts.most_common(5):
        print(f"  {word}: {count}")

if __name__ == '__main__':
    main()