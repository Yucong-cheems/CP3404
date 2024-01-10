from collections import Counter


def find_key_letter_for_group(group, reference_letter):
    frequency_analysis = Counter(group)
    most_common_letter = frequency_analysis.most_common(1)[0][0]
    shift = (ord(most_common_letter) - ord(reference_letter)) % 26
    return chr(shift + ord('a'))

ciphertext = "iyselxmteqsjtfxfbteezsrfeheeiysgtveitcnxidrzomrvmsvapoidctfzaxavioqsmopcupcmfwdkjelaevbmjezswimwceevqjqmqszaqwiytehbemacusulmxhzhxlwptmsmztqswfpxpgrztfcezsmssjwadepfneytrgulrppirgzvqctfzaxudewomezzzbhlrpdkvfcracdwmtxmgpoqapurrhjzrexkitpwfwvgbxirtzguppeiiideydtnwuswtdihfchmirpmzgwhrbelwtdihfcoqnrgbxefivfpqjmrkhipoqntcoeeucjtjqxkhzljyhqevbeprfperftktigostxkrysdvfuijrvpxaxkgxthqjkwmtwmizcoelqsvgxlwqmksodmhtcmjyzqhkwhlxqsrbelrmapgfoxttvlqpvuteqfhmfwkvflrmapgjdsriysepwspmswlpgpszftrexxvudmzifhiphqhzuoavaevfutiedwqsjtfdxfbalurrzhzvuiyatlqacxguelqbrbzoiervbelrfhftusiptjkizwqhkfvnxggvkbdfmhvrpyjqxjhfwtqgdiulxudeospxttaoqlrqhvtbdxqctfzaxudeomrsdxkvnlrpiysbfwfgrzjlrxdbwbwkagzhixraivhilxmachipendmsnprfxfbfogdnghprvmeywddceivatlvqeiwwlxqzvmtjwftdgjytdxmoupoqntfzaxahpgupqeqfhielqteqsjtfxfbbyhfwvrfnvkekwpyoqnjospwqrisulrptzhipvfwvgbxiagkvfvralcseriaufbfzjfwvajdwguwwdtizikcepxqgdwopxttfhipvfwzgjdatngfjgeftbszdceivatlvqpcgpnexavrtjqytkfjnwkhksndhuuwwflrpwvzmxezxehszhgrvrusiodeqfaxaugicwmozvmdccbifgzdxqbjdvmpurbsznvkekctjwftdgbwwarrzmphmhpanpxdxtgzdxqbjitpxiduwgqidtehlpcedesjdtgqcwdhluavhipsfwvfjdoqekgfnvqitzflvxnzhjdvqflwsphfwrhdzqbjkworxttjsdcifzvmgcsyiysqffxxtcoplmhkccpmziiodeenavhiciqsvgjrreqrgfosziysozxudecgaynazqlpcenjhfxwitisqffxxjvfovukvgudlmbzfbyhmscsnlrewfkfolalkvfqeoiffjdefxfbqcsnavadzyxsssvdipifqpywfglqultgqcwdvikrimqesenjhfxxtxjwtelqlvzmvraleftlgdnghpdceivanpvwavooolqacabyyetuhipozpggbnobgfpmpquckvftvodegucyoizcoxgqazsdpfgxchbdceivaxsmowrdqwmqsvfszvodiffnxucxqpoiearhfcmztcubxexrzhfppspusttkztuoqffxxtyfjgdnghpdceivavdmzvkvfomerisuppavrfjelyeiccwiybzzmpvmcuypmpuiqgvrkqhksefwucxsmwmbizqdfvhtjhpoiexxbqffxxtyfjgdnghpdceivat"
key_length = 7

groups = ['' for _ in range(key_length)]
for i, letter in enumerate(ciphertext):
    groups[i % key_length] += letter

reference_letters = ['e', 't', 'a']
keys = []
for ref_letter in reference_letters:
    key = ''.join(find_key_letter_for_group(group, ref_letter) for group in groups)
    print(f"The key for reference letter {ref_letter} is likely:", key)
