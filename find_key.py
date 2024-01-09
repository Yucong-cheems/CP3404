from collections import Counter
import string

# Define the groups as strings (replace these with your actual group strings)
group1 = "itxsiirscvpwesestchtsrsdtpcdzdcgrxwtitdihdnirnchepirixjismthsattwaippxiheddricbrhthghxgdthcdxigdgiadxneieztxnhqtxwenrtwgluwuigtwntipathuwxrduzibretrhxbdtdqaweinfwjtzixhiasqidantxkbswlixasigqrnxllniaatpgcdiaxiwsdcatrptxnivrvebcihcitxxni"
group2 = "yefrytzvticdvwvzeuzmwzmeritezkdprkvzinirrirvktjzvegyjkkzvkckrpvekpymsxfzvwxryxrvfjkvvjdeavtekyrbzvcmfgyvivdmtpfefvkjizvkcfvwkdfzgbvcvkkwvevegvfjbkdrptjueecvvktzlrkjvytkivvryezjijvzcfkffvsflcijjvegvvcugfkezzcvrvixrczuutgvkirizuqkxzjxtgv"
group3 = "sqbfscoafoukbiqahshsftspgrfwbvwohiggiwhpbhgfhctlbrosrgwcgsmwbglqvgsszvhufqfzagbbtkfkrhiootfovszwhhhsbhwawmgofghqbrwoshgvsbawcwhgfsagrfswzhrqimgdscgzagiwhswhfgzhwhwsmsccohggscqhsvgfskvfbasqqwmhwzfhaoahgpvgcshadffqhuhsoyhavsfczygssqhbyha"
group4 = "estegnmpzqpjmmjqbuxmpfsfugzohfmqjtbudufmefbpiojjefsdvxmoxojhefqffjewfuiousbhtuzeuivbpfusqbzmnbjbiiinfpdtwtjuzuisbfpsuibfefjdeoijjztptjnfmsufcdzvztbmnztgljdijffjsdodgqocdijfoglfqfubnffjqdvpudqftmtpnobibmfuodbxqsfpfbftqfpvfujcmpvemdpqfpt"
group5 = "ljehtxroascejwqwellzxcjnlzamlctazpxpesczlcxqpeqypttvptteldyllophldpltdpatjazleolszndywlpldarlflwxlppordlljypapejynyplpxvrzdtpppdgdlnjndlxzsawcdmnjwppdpqpdhpdnldpzrccfppecrozapxfodyloqdczdylvexevldpoypnptcxpdswznocxptfjddopewpmrfwfofjd"
group6 = "xteevivixmmlecmimmwtpewervxerrxprwipywhgwoejoexhrkxfxhwlwmzxrxvmrswprmhvitlvqliriwxfjtxxrxxsrwrkrxergvcvxwtoxqlthvowrvirijwixxvaecveqwhrehixmcxpvwwhxxxictlsovvvhqxisflmeirsxycwfvlhrleesyiwtisxlrgcvlyooqvygfcmmvximepkfgcmmplivpkwmvifgc"
group7 = "mfzeedmdaofazeqyaxpqgzaypquzpamuefredtmwtqfmqukqftkuaqmqqhqqmtufmrsgezqaefuuaqefpqgmqqutqqudpfxaamnfdmeqqfdqaeqffkqqpfaaafgzqtftfeqxykupzgoaobqukfamdqidegufqqxqfbtfyxmznqezuneixummeaofnxpfgketqadewqezbuooqgeoqouezxszxdezeayymuqubhexde"

# Put all the groups into a list for easier processing
groups = [group1, group2, group3, group4, group5, group6, group7]


# This function calculates the shift needed to get from a letter to 'e'
def calculate_shift_to_e(most_common):
    # Calculate the alphabetical position of 'e' and the most common letter
    pos_e = ord('e') - ord('a')
    pos_letter = ord(most_common) - ord('a')
    # Calculate the shift and adjust if it's a negative shift
    shift = (pos_letter - pos_e) % 26
    return shift


# Assuming 'E' is the most frequent letter in English plaintext
# Find the most common letter in each group and deduce the key letter
key_letters = []

for i, group in enumerate(groups, start=1):
    # Count the frequency of each letter in the group
    frequency = Counter(group)

    # Get the most common letter in this group
    most_common_letter, _ = frequency.most_common(1)[0]

    # Calculate the shift needed to get from the most common letter to 'e'
    shift = calculate_shift_to_e(most_common_letter)

    # Deduce the key letter (shift back from 'a' by the found shift)
    key_letter = string.ascii_lowercase[shift]

    key_letters.append(key_letter)

    print(f"Group {i}: Most common letter is '{most_common_letter}', key letter is '{key_letter}'")

# Combine the key letters to form the key
key = ''.join(key_letters)
print(f"The most likely key is: {key}")
