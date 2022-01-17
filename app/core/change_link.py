def change_link(string, start):

    index_iframe = string.find('iframe')
    index_embed = string.find('embed/')

    first_str = string[:index_iframe + 7]
    second_str = 'class="content" '
    third_str = string[index_iframe + 7: index_embed + 17]
    forth_str = '?autoplay=1&mute=1&start=' + str(start)
    last_str = string[index_embed + 17:]

    new_str = first_str + second_str + third_str + forth_str + last_str

    return new_str