def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.


    """
    full_names = []
    for person in people:
        first_name = person['first']
        last_name = person['last']
        full_name = f"{first_name} {last_name}"
        full_names.append(full_name)
    
    return full_names



names = [
{'first': 'Ada', 'last': 'Lovelace'},
{'first': 'Grace', 'last': 'Hopper'},
        ]
