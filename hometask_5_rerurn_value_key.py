example = {'title': 'LhmQH4viLO4S x m 2AmXECPhYu5e90k', 'pid': 'f626be28', 'name': 'Crimson Lemur', 'lang_code': 'text', 'lang': 'Text', 'paste': '<div class="text" style="font-family:monospace;"><ol><li style="font-weight: normal; vertical-align:top;"><div style="font: normal normal 1em/1.2em monospace; margin:0; padding:0; background:none; vertical-align:top;">m3DVLV1L hJn6xpNRivm8TT8KVNCBC5GnMeR9y 0AIHPFo90 pReOZsowJq iYAVNheF 2gcy &nbsp;2z7jaCow OXrwHps9o4p xKDk8t gW3MdROSbyfAE7NQvc UgT8DY</div></li>\n</ol></div>', 'created': '1507207620', 'url': 'http://text-share.com/view/f626be28', 'raw': 'm3DVLV1L hJn6xpNRivm8TT8KVNCBC5GnMeR9y 0AIHPFo90 pReOZsowJq iYAVNheF 2gcy  2z7jaCow OXrwHps9o4p xKDk8t gW3MdROSbyfAE7NQvc UgT8DY', 'hits': '0', 'hits_updated': '0', 'snipurl': '0', 'inreply': {'title': 'Re: Re: Re: Re: Re: Re: Re: Untitled', 'name': 'Gracious Kangaroo', 'url': 'http://text-share.com/view/e104ae95'}}

def get_value(dict, key):
    all_keys = dict.keys()
    if key in all_keys:
        return dict[key]
    else:
        return None

print get_value(example, 'url')
print get_value(example, 'name')
print get_value(example, 'pid')
print get_value(example, 'hello')