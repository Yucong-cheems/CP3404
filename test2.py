def vigenere_cipher_encrypt(message:str, keys=()):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    translated = ''
    n = 0

    keylen = len(keys)
    message = message.upper()
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            key =  keys[n % keylen]
            translatedIndex= (symbolIndex + key) % 26
            translated = translated + SYMBOLS[translatedIndex]
            n = n + 1
        else:
            translated = translated + symbol
    print(translated)


def vigenere_cipher_encrypt_by_keystring(message:str, keystring:str):
    keys = translate_keystring(keystring)
    vigenere_cipher_encrypt(message, keys)


def vigenere_cipher_decrypt(message:str, keys=()):
    SYMBOLS = 'abcdefghijklmnopqrstuvwxyz'
    translated = ''
    n = 0

    keylen = len(keys)
    message = message.lower()
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex= (symbolIndex - keys[n % keylen])%26
            translated = translated + SYMBOLS[translatedIndex]
            n = n + 1
        else:
            translated = translated + symbol
    print(translated)


def vigenere_cipher_decrypt_by_keystring(message:str, keystring:str):
    keys = translate_keystring(keystring)
    vigenere_cipher_decrypt(message, keys)


def translate_keystring(keystring:str):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    keys = []

    keystring = keystring.upper()
    for symbol in keystring:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            keys.append(symbolIndex)
        else:
            keys.append(-1)

    return tuple(keys)


message_to_decrypt = "iyselxmteqsjtfxfbteezsrfeheeiysgtveitcnxidrzomrvmsvapoidctfzaxavioqsmopcupcmfwdkjelaevbmjezswimwceevqjqmqszaqwiytehbemacusulmxhzhxlwptmsmztqswfpxpgrztfcezsmssjwadepfneytrgulrppirgzvqctfzaxudewomezzzbhlrpdkvfcracdwmtxmgpoqapurrhjzrexkitpwfwvgbxirtzguppeiiideydtnwuswtdihfchmirpmzgwhrbelwtdihfcoqnrgbxefivfpqjmrkhipoqntcoeeucjtjqxkhzljyhqevbeprfperftktigostxkrysdvfuijrvpxaxkgxthqjkwmtwmizcoelqsvgxlwqmksodmhtcmjyzqhkwhlxqsrbelrmapgfoxttvlqpvuteqfhmfwkvflrmapgjdsriysepwspmswlpgpszftrexxvudmzifhiphqhzuoavaevfutiedwqsjtfdxfbalurrzhzvuiyatlqacxguelqbrbzoiervbelrfhftusiptjkizwqhkfvnxggvkbdfmhvrpyjqxjhfwtqgdiulxudeospxttaoqlrqhvtbdxqctfzaxudeomrsdxkvnlrpiysbfwfgrzjlrxdbwbwkagzhixraivhilxmachipendmsnprfxfbfogdnghprvmeywddceivatlvqeiwwlxqzvmtjwftdgjytdxmoupoqntfzaxahpgupqeqfhielqteqsjtfxfbbyhfwvrfnvkekwpyoqnjospwqrisulrptzhipvfwvgbxiagkvfvralcseriaufbfzjfwvajdwguwwdtizikcepxqgdwopxttfhipvfwzgjdatngfjgeftbszdceivatlvqpcgpnexavrtjqytkfjnwkhksndhuuwwflrpwvzmxezxehszhgrvrusiodeqfaxaugicwmozvmdccbifgzdxqbjdvmpurbsznvkekctjwftdgbwwarrzmphmhpanpxdxtgzdxqbjitpxiduwgqidtehlpcedesjdtgqcwdhluavhipsfwvfjdoqekgfnvqitzflvxnzhjdvqflwsphfwrhdzqbjkworxttjsdcifzvmgcsyiysqffxxtcoplmhkccpmziiodeenavhiciqsvgjrreqrgfosziysozxudecgaynazqlpcenjhfxwitisqffxxjvfovukvgudlmbzfbyhmscsnlrewfkfolalkvfqeoiffjdefxfbqcsnavadzyxsssvdipifqpywfglqultgqcwdvikrimqesenjhfxxtxjwtelqlvzmvraleftlgdnghpdceivanpvwavooolqacabyyetuhipozpggbnobgfpmpquckvftvodegucyoizcoxgqazsdpfgxchbdceivaxsmowrdqwmqsvfszvodiffnxucxqpoiearhfcmztcubxexrzhfppspusttkztuoqffxxtyfjgdnghpdceivavdmzvkvfomerisuppavrfjelyeiccwiybzzmpvmcuypmpuiqgvrkqhksefwucxsmwmbizqdfvhtjhpoiexxbqffxxtyfjgdnghpdceivat"
keystring_for_decryption = "problem"
vigenere_cipher_decrypt_by_keystring(message_to_decrypt, keystring_for_decryption)

