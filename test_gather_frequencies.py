from syllable_dataset import gather_frequencies


def main():
    sample_data = {
        "alpha": 2,
        "beta": 5,
        "gamma": {
            "delta": 0,
            "epsilon": 3,
        },
        "items": [
            {"zeta": 4},
            {"eta": 1},
            {"theta": 2},
        ],
    }

    pairs = gather_frequencies(sample_data)
    for path, freq in sorted(pairs, key=lambda x: x[1]):
        print(f"{freq:2} - {path}")


if __name__ == "__main__":
    main()
