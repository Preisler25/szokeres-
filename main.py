# Beimportáljuk a szavak.txt fájlt
def import_txt():
    f = open('szavak.txt', 'r', encoding='utf-8').read()
    lines = f.strip().split('\n')
    return lines

def count_key_letters(key, lst):
    # Létrehozzuk a szótárat az egyezések tárolására
    matches = {}

    # Végigmegyünk a lista elemein
    for item in lst:
        # A kulcs betűinek száma
        if len(item) == 14:
            count = 0

            # Másolatot készítünk az elemről, hogy ne változtassuk meg az eredetit
            item_copy = item.lower()

            # Végigmegyünk a kulcs betűin
            for letter in key:
                # Megnézzük, hogy a kulcs betűje szerepel-e az elem másolatában
                if letter in item_copy:
                    # Ha igen, akkor eltávolítjuk az elem másolatából, és növeljük az egyezések számát
                    item_copy = item_copy.replace(letter, '', 1)
                    count += 1
            # Elmentjük az egyezések számát a szótárban
            matches[item] = count

    # Visszaadjuk a szótárat
    return matches

def write_matches(Map):
    # Megnyitjuk a fájlt
    f = open('eredmeny.txt', 'w', encoding='utf-8')

    # Végigmegyünk a szótár kulcsain
    for key in Map:
        # Ha az egyezések száma 14, akkor kiírjuk az elemet a fájlba
        if Map[key] == 14:
            f.write(key + '\n')

    # Bezárjuk a fájlt
    f.close()
#test
key = 'plasmfhéasyűaráktlbpcris'
lst = import_txt()
WMap = count_key_letters(key, lst)
write_matches(WMap)