# YouTube Link に以下の性質を付け加える。
# 1. 自動再生 & ミュート -> "?autoplay=1&mute=1" を'embed/'の 11 文字後ろにくっつける。
# 2. 再生開始時間を自由に選択可能 -> "&start=xx" を'mute=1'の後ろにくっつける。

# 以下に例を示す。
# original_link = '<iframe width="560" height="315" src="https://www.youtube.com/embed/eZA0AnSdbBI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
# changed_link = '<div class="wrapper"> <iframe width="560" height="315" src="https://www.youtube.com/embed/eZA0AnSdbBI?autoplay=1&mute=1&start=25" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> </div>'

def change_link(string: str, auto=0, start=0) -> str:
    # 動画の指定は任意なので、無い場合もある。
    if not string:
        return ''
    # auto=1 の場合、自動再生を要求されているため、'?autoplay=1&mute=1&start=' + str(start) の文字列を'embed/'の後ろに追加する。
    elif auto:
        index_embed = string.find('embed/')
        first_str = string[:index_embed + 17]
        second_str = '?autoplay=1&mute=1&start=' + str(start)
        last_str = string[index_embed + 17:]
        new_str = '<div class="wrapper"> ' + first_str + second_str + last_str + ' </div>'

        return new_str
    # auto=0 の場合、自動再生は要求されていないので、div タグをつけるだけ。
    else:
        new_str = '<div class="wrapper"> ' + string + ' </div>'
        return  new_str