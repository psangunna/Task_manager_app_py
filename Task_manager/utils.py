
def get_dict_from_wftform(form):
    """ Method to obtain a dictionary from wtf forms. """
    dictionary = dict()
    try:
        for key in form.data.keys():
            if key in ['csrf_token', 'submit']:
                continue
            dictionary[str(key)] = form[key].data
    except AttributeError as error:
        dictionary = dict()
    finally:
        return dictionary