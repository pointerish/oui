import io
import csv
from typing import Type
from requests import Response
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class SearchStrategy(ABC):

    item: str
    response: Type[Response]

    @abstractmethod
    def search(self):
        pass


@dataclass
class LinearSearchStrategy(SearchStrategy):

    def search(self, *args):
        tsv_data = io.StringIO(args[0].text)
        reader = csv.reader(
            filter(lambda row: row[0]!='#', tsv_data), delimiter='\t'
        )
        for row in reader:
            if self in row:
                return f'MAC: {row[0]} | Manufacturer: {row[2]}'
        return 'MAC Not Found'
