def convert_dict_to_tags(tags: list | dict) -> list:
    new_tags: list = []

    if type(tags) is list:
        return tags
    elif type(tags) is dict:
        for key, value in tags.items():
            new_tags.append({"Key": key, "Value": value})

    return new_tags
