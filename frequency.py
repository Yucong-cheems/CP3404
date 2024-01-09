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

key_length = 6
groups = ['' for _ in range(key_length)]

for i, letter in enumerate(ciphertext):
    groups[i % key_length] += letter

for i, group in enumerate(groups, 1):
    print(f"Group {i}: {group}")
