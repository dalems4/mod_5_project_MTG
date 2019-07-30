from mtgsdk import Card


def collect_magic_set(mtg_set_code="###"):
    """Uses Wizards API to fetch data from Wizard's website"""
    magic_set = Card.where(set=mtg_set_code).all()
    return magic_set

def get_df(magic_set):
    """Takes the 3 charactor MTG set code and outputs a pandas DataFrame"""
    # magic_set = collect_magic_set(mtg_set_code)
    magic_set_json = get_just_text(magic_set)
    magic_set_df = pd.DataFrame(magic_set_json)
    return magic_set_df

def get_just_text(magic_set):
    """Takes raw Magic card data and returns the text of the card and card color(s) as a json"""
    magic_set_json = []
    for card in magic_set:
        cards = {
            'text' : card.text,
            'colors' : card.colors,
        }
        
        whole_set.append(cards)
    return magic_set_json


def prep_df(magic_set_df):
    """Preprocesses the DataFrames from get_df"""
    magic_set_df = magic_set_df.replace('\n',' ', regex=True)
    magic_set_df['colors'] = magic_set_df['colors'].apply(lambda x : str(x))
    mask = magic_set_df.applymap(lambda x: x is None)
    cols = magic_set_df.columns[(mask).any()]
    magic_set_df = magic_set_df.replace('[]', "['Colorless']")
    for col in magic_set_df[cols]:
        magic_set_df.loc[mask[col], col] = ''
    return magic_set_df