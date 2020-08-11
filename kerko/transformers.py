"""
Data transformation utilities.
"""

import re
from collections.abc import Iterable


def find(regex, flags=0, group=1, max_matches=1):
    """
    Return a callable that finds all non-overlapping matches in a given string.

    :param str regex: Regular expression to search.

    :param int flags: Flags controlling the regular expression's behavior.

    :param int group: Number of the match group to retrieve from the match
    object.

    :param int max_matches: Maximum number of matching strings to return. A
        value of `0` means no maximum. If set to `1`, the returned value will be
        a string; otherwise a list.
    """
    regex = re.compile(regex, flags)

    def _find(value):
        matches = []
        if value:
            if isinstance(value, str):
                value = [value]
            if isinstance(value, Iterable):
                for v in value:
                    if isinstance(v, str):
                        for i, match in enumerate(regex.finditer(v)):
                            if max_matches and i == max_matches:
                                break
                            if match:
                                matches.append(match.group(group))
            if max_matches == 1:
                return matches[0] if matches else ''
        return matches if max_matches != 1 else ''

    return _find


def split(sep=None, maxsplit=-1):
    def _split(value):
        if isinstance(value, str):
            return [v.strip() for v in value.split(sep, maxsplit)]
        return []
    return _split


ZOTERO_URI_TO_ITEM_ID_REGEX = (
    r'(^|\s)(https?://(www\.)?zotero\.org/|zotero://select/)'
    r'(library|((groups|users)/[0-9]+))/items/([A-Z0-9]+)(?=$|\s)'
)

zotero_uri_to_item_id_single = find(
    # Parse a single Zotero Item URI and/or Zotero Select URI in a multiline
    # string. Return a string with the found item ID.
    regex=ZOTERO_URI_TO_ITEM_ID_REGEX,
    flags=re.MULTILINE,
    group=7,
    max_matches=1,
)

zotero_uri_to_item_id_multiple = find(
    # Parse multiple Zotero Item URIs and/or Zotero Select URIs in a multiline
    # string. Return the list of found item IDs.
    regex=ZOTERO_URI_TO_ITEM_ID_REGEX,
    flags=re.MULTILINE,
    group=7,
    max_matches=0,
)
