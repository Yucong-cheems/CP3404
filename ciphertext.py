from collections import defaultdict


def find_repeated_sequences(ciphertext, min_sequence_length=3):
    """
    Finds repeated sequences of a given minimum length in the ciphertext and calculates the distances between them.

    :param ciphertext: The ciphertext to analyze
    :param min_sequence_length: Minimum length of repeating sequences to look for
    :return: A dictionary where keys are the sequences and values are lists of distances between each occurrence
    """
    # Store sequences and their positions
    sequences = defaultdict(list)

    # Iterate over the ciphertext to find repeating sequences
    for i in range(len(ciphertext)):
        for j in range(i + min_sequence_length, len(ciphertext) + 1):
            sequence = ciphertext[i:j]
            sequences[sequence].append(i)

    # Filter out non-repeating sequences
    repeated_sequences = {seq: pos for seq, pos in sequences.items() if len(pos) > 1}

    # Calculate distances between each occurrence of each sequence
    distances = {}
    for seq, pos in repeated_sequences.items():
        if len(pos) > 1:
            seq_distances = [pos[i] - pos[i - 1] for i in range(1, len(pos))]
            distances[seq] = seq_distances

    return distances


ciphertext = (
            "iyselxmteqsjtfxfbteezsrfeheeiysgtveitcnxidrzomrvmsvapoidctfzaxavioqsmo"
            "pcupcmfwdkjelaevbmjezswimwceevqjqmqszaqwiytehbemacusulmxhzhxlwptmsmztq"
            "swfpxpgrztfcezsmssjwadepfneytrgulrppirgzvqctfzaxudewomezzzbhlrpdkvfcra"
            "cdwmtxmgpoqapurrhjzrexkitpwfwvgbxirtzguppeiiideydtnwuswtdihfchmirpmzgw"
            "hrbelwtdihfcoqnrgbxefivfpqjmrkhipoqntcoeeucjtjqxkhzljyhqevbeprfperftkt"
            "igostxkrysdvfuijrvpxaxkgxthqjkwmtwmizcoelqsvgxlwqmksodmhtcmjyzqhkwhlxq"
            "srbelrmapgfoxttvlqpvuteqfhmfwkvflrmapgjdsriysepwspmswlpgpszftrexxvudmz"
            "ifhiphqhzuoavaevfutiedwqsjtfdxfbalurrzhzvuiyatlqacxguelqbrbzoiervbelrf"
            "hftusiptjkizwqhkfvnxggvkbdfmhvrpyjqxjhfwtqgdiulxudeospxttaoqlrqhvtbdxq"
            "ctfzaxudeomrsdxkvnlrpiysbfwfgrzjlrxdbwbwkagzhixraivhilxmachipendmsnprf"
            "xfbfogdnghprvmeywddceivatlvqeiwwlxqzvmtjwftdgjytdxmoupoqntfzaxahpgupqe"
            "qfhielqteqsjtfxfbbyhfwvrfnvkekwpyoqnjospwqrisulrptzhipvfwvgbxiagkvfvra"
            "lcseriaufbfzjfwvajdwguwwdtizikcepxqgdwopxttfhipvfwzgjdatngfjgeftbszdce"
            "ivatlvqpcgpnexavrtjqytkfjnwkhksndhuuwwflrpwvzmxezxehszhgrvrusiodeqfaxa"
            "ugicwmozvmdccbifgzdxqbjdvmpurbsznvkekctjwftdgbwwarrzmphmhpanpxdxtgzdxq"
            "bjitpxiduwgqidtehlpcedesjdtgqcwdhluavhipsfwvfjdoqekgfnvqitzflvxnzhjdvq"
            "flwsphfwrhdzqbjkworxttjsdcifzvmgcsyiysqffxxtcoplmhkccpmziiodeenavhiciq"
            "svgjrreqrgfosziysozxudecgaynazqlpcenjhfxwitisqffxxjvfovukvgudlmbzfbyhm"
            "scsnlrewfkfolalkvfqeoiffjdefxfbqcsnavadzyxsssvdipifqpywfglqultgqcwdvik"
            "rimqesenjhfxxtxjwtelqlvzmvraleftlgdnghpdceivanpvwavooolqacabyyetuhipoz"
            "pggbnobgfpmpquckvftvodegucyoizcoxgqazsdpfgxchbdceivaxsmowrdqwmqsvfszvo"
            "diffnxucxqpoiearhfcmztcubxexrzhfppspusttkztuoqffxxtyfjgdnghpdceivavdmz"
            "vkvfomerisuppavrfjelyeiccwiybzzmpvmcuypmpuiqgvrkqhksefwucxsmwmbizqdfvh"
            "tjhpoiexxbqffxxtyfjgdnghpdceivat"
              )

repeated_sequences = find_repeated_sequences(ciphertext)

for sequence, dist in repeated_sequences.items():
    print(f"Sequence: {sequence}, Distances: {dist}")
