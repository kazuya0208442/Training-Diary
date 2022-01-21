def change_link(string, auto=0, start=0):

    if not string:
        return ''

    elif auto:
        index_embed = string.find('embed/')
        first_str = string[:index_embed + 17]
        second_str = '?autoplay=1&mute=1&start=' + str(start)
        last_str = string[index_embed + 17:]
        new_str = '<div class="wrapper"> ' + first_str + second_str + last_str + ' </div>'

        return new_str
    
    else:
        new_str = '<div class="wrapper"> ' + string + ' </div>'
        return  new_str