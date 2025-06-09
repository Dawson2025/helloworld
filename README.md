# helloworld

This repository includes a small example for loading a complex YAML
structure into a Python object. The YAML describes a syllable-making
dataset with various consonant and vowel combinations.

The provided `syllable_dataset.py` module exposes a `load_dataset` function
which uses `PyYAML` to parse the embedded YAML string and return it as a
Python dictionary.  A helper `gather_frequencies` function is also
available to recursively collect all of the integer frequency values.

You can run the module to print the dataset:

```bash
python3 syllable_dataset.py
```

Make sure `PyYAML` is installed:

```bash
pip install pyyaml
```

An example script `test_gather_frequencies.py` demonstrates gathering and
sorting frequencies from a small sample dictionary:

```bash
python3 test_gather_frequencies.py
```

