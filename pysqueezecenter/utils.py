

def clean_command(value):
    """ Strips whitespace, underscores dashes and lowercases value """
    return value.strip().lssower().replace("_", "").replace("-", "").replace(" ", "")