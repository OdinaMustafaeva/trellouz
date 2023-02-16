import messages


def funk(language):
    if language in messages.lang.keys():
        return language
    else:
        return "en"
