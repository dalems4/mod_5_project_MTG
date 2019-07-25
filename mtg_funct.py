def collect_magic_set(mtg_set_code="###"):
    cards = Card.where(set=mtg_set_code).all()
    return cards

def get_text(magic_set):
    """Uses Wizards API to build a dictionary of cards for one "magic_set": name, text, and colors"""
    whole_set = []
    for card in magic_set:
        cards = {
            'text' : card.text,
            'colors' : card.colors,
        }
        
        whole_set.append(cards)
    return whole_set

def get_df(mtg_set_alias):
    magic_set = collect_magic_set(mtg_set_alias)
    magic_set_json = get_text(magic_set)
    magic_set_df = pd.DataFrame(magic_set_json)
    magic_set_df['vanilla_creature'] = magic_set_df['text'].apply(lambda x : 1 if x is None else 0)
    magic_set_df = magic_set_df.replace('\n',' ', regex=True)
    return magic_set_df