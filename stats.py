def get_book_text(filepath: str):
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def get_num_words(filepath: str):
    return len(get_book_text(filepath).split())

def get_num_letters(text: str):
    characters = {}
    lowered_text = text.lower()
    for cha in lowered_text:
        if (cha not in characters):
            characters[cha] = 0
        characters[cha] += 1

    return characters

def sort_on(dict):
    return dict["num"]

def get_sorted_dic(dic: dict[str, int]):
    list = [{"char":k,"num": v} for k, v in dic.items() if k.isalpha()]
    list.sort(reverse=True, key=sort_on)

    return list

