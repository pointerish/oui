## OUI Lookup Tool

This simple CLI tool does OUI lookups using Wireshark's Gitlab Repo as the source. This small project was mainly done to practice the strategy design pattern. New algorithms to perform the actual search can be implemented and used instead of the default one which is a linear search.

### Usage

For example, running the following command:
`python oui.py 00:00:36`

will return: `MAC: 00:00:36 | Manufacturer: Atari Corporation`

### TODOs

- Setup code for PyPI
