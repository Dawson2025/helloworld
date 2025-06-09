import yaml

SYLLABLE_YAML = """
syllable_making_dataset:
  CVC:
    onset:
      single_consonants:
        Stops:
          frequency: 0
          phonemes:
            - p: 0
            - t: 0
            - k: 1
            - b: 0
            - d: 0
            - g: 0
        Fricatives:
          frequency: 0
          phonemes:
            - f: 0
            - v: 0
            - s: 0
            - z: 1
            - ʃ: 0
            - ʒ: 0
            - θ: 0
            - ð: 0
            - h: 0
        Affricates:
          frequency: 0
          phonemes:
            - tʃ: 0
            - dʒ: 0
        Nasals:
          frequency: 0
          phonemes:
            - m: 0
            - n: 0
            - ŋ: 0
        Liquids:
          frequency: 0
          phonemes:
            - l: 0
            - ɹ: 0
        Glides:
          frequency: 0
          phonemes:
            - j: 0
            - w: 1
      cluster2:
        Stop+:
          frequency: 0
          Stop+Liquid:
            frequency: 0
            phonemes:
              - pl: 0
              - bl: 0
              - kl: 0
              - gl: 0
          Stop+Glide:
            frequency: 0
            phonemes:
              - pj: 0
              - kj: 0
        Fricative+:
          frequency: 0
          Fricative+Liquid:
            frequency: 0
            phonemes:
              - fl: 0
        S+:
          frequency: 0
          S+Stop:
            frequency: 0
            phonemes:
              - st: 0
              - sp: 0
              - sk: 0
          S+Nasal:
            frequency: 0
            phonemes:
              - sn: 0
              - sm: 0
          S+Liquid:
            frequency: 0
            phonemes:
              - sl: 0
          S+Glide:
            frequency: 0
            phonemes:
              - sw: 0
      cluster3:
        S+Stop+:
          frequency: 0
          S+Stop+Liquid:
            frequency: 0
            phonemes:
              - spl: 0
              - str: 0
              - skr: 0

    nucleus:
      vowels:
        monophthongs:
          High:
            frequency: 0
            phonemes:
              - i: 1
              - ɪ: 0
              - u: 0
              - ʊ: 0
          Mid:
            frequency: 0
            phonemes:
              - e: 0
              - ɛ: 0
              - ə: 0
              - o: 0
              - ɔ: 0
          Low:
            frequency: 0
            phonemes:
              - æ: 0
              - a: 1
              - ɑ: 0
        diphthongs:
          Closing:
            frequency: 0
            Fronting:
              frequency: 0
              phonemes:
                - aɪ: 0
                - eɪ: 0
                - ɔɪ: 0
            Backing:
              frequency: 0
              phonemes:
                - aʊ: 0
                - oʊ: 0
          # No centering diphthongs in CVC

    coda:
      single_consonants:
        Stops:
          frequency: 0
          phonemes:
            - p: 1
            - t: 0
            - k: 0
            - b: 1
            - d: 0
            - g: 0
        Fricatives:
          frequency: 0
          phonemes:
            - f: 0
            - v: 0
            - s: 0
            - z: 0
            - ʃ: 0
            - ʒ: 0
            - θ: 0
            - ð: 0
            - h: 0
        Affricates:
          frequency: 0
          phonemes:
            - tʃ: 0
            - dʒ: 0
        Nasals:
          frequency: 0
          phonemes:
            - m: 0
            - n: 0
            - ŋ: 0
        Liquids:
          frequency: 0
          phonemes:
            - l: 0
            - ɹ: 0
        Glides:
          frequency: 0
          phonemes:
            - j: 0
            - w: 0
      cluster2:
        Nasal+:
          frequency: 0
          Nasal+Stop:
            frequency: 0
            phonemes:
              - nt: 0
              - mp: 0
              - nk: 0
        Stop+:
          frequency: 0
          Stop+Liquid:
            frequency: 0
            phonemes:
              - dl: 0
        Liquid+:
          frequency: 0
          Liquid+Stop:
            frequency: 0
            phonemes:
              - lt: 0
              - rd: 0
        Frictative+:
          frequency: 0
          Fricative+Stop:
            frequency: 0
            phonemes:
              - ft: 0
              - sp: 0

  CV:
    onset:
      single_consonants:
        Stops:
          frequency: 0
          phonemes:
            - p: 0
            - t: 0
            - k: 1
            - b: 0
            - d: 0
            - g: 0
        Fricatives:
          frequency: 0
          phonemes:
            - f: 0
            - v: 0
            - s: 0
            - z: 1
            - ʃ: 0
            - ʒ: 0
            - θ: 0
            - ð: 0
            - h: 0
        Affricates:
          frequency: 0
          phonemes:
            - tʃ: 0
            - dʒ: 0
        Nasals:
          frequency: 0
          phonemes:
            - m: 0
            - n: 0
            - ŋ: 0
        Liquids:
          frequency: 0
          phonemes:
            - l: 0
            - ɹ: 0
        Glides:
          frequency: 0
          phonemes:
            - j: 0
            - w: 1
      cluster2:
        Stop+:
          frequency: 0
          Stop+Liquid:
            frequency: 0
            phonemes:
              - pl: 0
              - bl: 0
              - kl: 0
              - gl: 0
          Stop+Glide:
            frequency: 0
            phonemes:
              - pj: 0
              - kj: 0
        Fricative+:
          frequency: 0
          Fricative+Liquid:
            frequency: 0
            phonemes:
              - fl: 0
              - sl: 0
        S+:
          frequency: 0
          S+Stop:
            frequency: 0
            phonemes:
              - st: 0
              - sp: 0
              - sk: 0
          S+Nasal:
            frequency: 0
            phonemes:
              - sn: 0
              - sm: 0
          S+Liquid:
            frequency: 0
            phonemes:
              - sl: 0
          S+Glide:
            frequency: 0
            phonemes:
              - sw: 0
      cluster3:
        S+Stop+:
          frequency: 0
          S+Stop+Liquid:
            frequency: 0
            phonemes:
              - spl: 0
              - str: 0
              - skr: 0

    nucleus:
      vowels:
        monophthongs:
          High:
            frequency: 0
            phonemes:
              - i: 0
              - ɪ: 0
              - u: 0
              - ʊ: 0
          Mid:
            frequency: 0
            phonemes:
              - e: 0
              - ɛ: 0
              - ə: 0
              - o: 0
              - ɔ: 0
          Low:
            frequency: 0
            phonemes:
              - æ: 0
              - a: 0
              - ɑ: 0
        diphthongs:
          Closing:
            frequency: 0
            Fronting:
              frequency: 0
              phonemes:
                - aɪ: 0
                - eɪ: 0
                - ɔɪ: 0
            Backing:
              frequency: 0
              phonemes:
                - aʊ: 0
                - oʊ: 0
          Centering:
            frequency: 0
            phonemes:
              - ɪə: 0
    # No coda in CV
"""


def load_dataset():
    """Load the syllable dataset YAML into a Python object."""
    return yaml.safe_load(SYLLABLE_YAML)



def gather_frequencies(node, path=None):
    """Recursively collect (path, frequency) pairs from the dataset."""
    if path is None:
        path = []
    entries = []
    if isinstance(node, dict):
        for key, value in node.items():
            new_path = path + [key]
            if isinstance(value, int):
                entries.append(("/".join(new_path), value))
            else:
                entries.extend(gather_frequencies(value, new_path))
    elif isinstance(node, list):
        for item in node:
            entries.extend(gather_frequencies(item, path))
    return entries


if __name__ == "__main__":
    data = load_dataset()
    # Print a portion of the data structure for demonstration
    from pprint import pprint
    pprint(data)
