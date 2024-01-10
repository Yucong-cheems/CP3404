import itertools
from collections import Counter


def vigenere_decrypt(ciphertext, key):
    decrypted_text = ""
    for i, char in enumerate(ciphertext):
        if char.islower():
            shift = ord(key[i % len(key)]) - ord('a')
            decrypted_char = chr((ord(char) - shift) % 26 + ord('a'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

ciphertext = "iyselxmteqsjtfxfbteezsrfeheeiysgtveitcnxidrzomrvmsvapoidctfzaxavioqsmopcupcmfwdkjelaevbmjezswimwceevqjqmqszaqwiytehbemacusulmxhzhxlwptmsmztqswfpxpgrztfcezsmssjwadepfneytrgulrppirgzvqctfzaxudewomezzzbhlrpdkvfcracdwmtxmgpoqapurrhjzrexkitpwfwvgbxirtzguppeiiideydtnwuswtdihfchmirpmzgwhrbelwtdihfcoqnrgbxefivfpqjmrkhipoqntcoeeucjtjqxkhzljyhqevbeprfperftktigostxkrysdvfuijrvpxaxkgxthqjkwmtwmizcoelqsvgxlwqmksodmhtcmjyzqhkwhlxqsrbelrmapgfoxttvlqpvuteqfhmfwkvflrmapgjdsriysepwspmswlpgpszftrexxvudmzifhiphqhzuoavaevfutiedwqsjtfdxfbalurrzhzvuiyatlqacxguelqbrbzoiervbelrfhftusiptjkizwqhkfvnxggvkbdfmhvrpyjqxjhfwtqgdiulxudeospxttaoqlrqhvtbdxqctfzaxudeomrsdxkvnlrpiysbfwfgrzjlrxdbwbwkagzhixraivhilxmachipendmsnprfxfbfogdnghprvmeywddceivatlvqeiwwlxqzvmtjwftdgjytdxmoupoqntfzaxahpgupqeqfhielqteqsjtfxfbbyhfwvrfnvkekwpyoqnjospwqrisulrptzhipvfwvgbxiagkvfvralcseriaufbfzjfwvajdwguwwdtizikcepxqgdwopxttfhipvfwzgjdatngfjgeftbszdceivatlvqpcgpnexavrtjqytkfjnwkhksndhuuwwflrpwvzmxezxehszhgrvrusiodeqfaxaugicwmozvmdccbifgzdxqbjdvmpurbsznvkekctjwftdgbwwarrzmphmhpanpxdxtgzdxqbjitpxiduwgqidtehlpcedesjdtgqcwdhluavhipsfwvfjdoqekgfnvqitzflvxnzhjdvqflwsphfwrhdzqbjkworxttjsdcifzvmgcsyiysqffxxtcoplmhkccpmziiodeenavhiciqsvgjrreqrgfosziysozxudecgaynazqlpcenjhfxwitisqffxxjvfovukvgudlmbzfbyhmscsnlrewfkfolalkvfqeoiffjdefxfbqcsnavadzyxsssvdipifqpywfglqultgqcwdvikrimqesenjhfxxtxjwtelqlvzmvraleftlgdnghpdceivanpvwavooolqacabyyetuhipozpggbnobgfpmpquckvftvodegucyoizcoxgqazsdpfgxchbdceivaxsmowrdqwmqsvfszvodiffnxucxqpoiearhfcmztcubxexrzhfppspusttkztuoqffxxtyfjgdnghpdceivavdmzvkvfomerisuppavrfjelyeiccwiybzzmpvmcuypmpuiqgvrkqhksefwucxsmwmbizqdfvhtjhpoiexxbqffxxtyfjgdnghpdceivat"

groups = [
    ['e', 'p', 'i'],  # Group 1
    ['r', 'c', 'v'],  # Group 2
    ['d', 'o', 'h'],  # Group 3
    ['b', 'm', 'f'],  # Group 4
    ['l', 'w', 'p'],  # Group 5
    ['t', 'e', 'x'],  # Group 6
    ['m', 'x', 'q'],  # Group 7
]

possible_keys = list(itertools.product(*groups))

for key_tuple in possible_keys:
    key = ''.join(key_tuple)
    decrypted_text = vigenere_decrypt(ciphertext, key)
    print(f"Key: {key} -> {decrypted_text[:30]}...")

