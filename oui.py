import sys
from typing import Type
from dataclasses import dataclass
from requests import get, Response
from search_strategies import SearchStrategy
from search_strategies import LinearSearchStrategy


@dataclass
class OUISearch:

    oui_item: str
    oui_response: Type[Response]

    def __repr__(self):
        return self.oui_item

    def search(self, searching_strategy: Type[SearchStrategy]):
        return searching_strategy.search(
            self.oui_item,
            self.oui_response
        )


if __name__ == '__main__':
    response: Response = get('https://gitlab.com/wireshark/wireshark/-/raw/master/manuf')
    try:
        oui_search = OUISearch(sys.argv[1], response)
        print(f'\n\n{oui_search.search(LinearSearchStrategy)}\n\n')
    except IndexError:
        print('Please specify the MAC address for the search like so: python oui.py 00:00:00')
