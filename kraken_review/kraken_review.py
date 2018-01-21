import csv
import re

from pathlib import Path

import ete3
import toytree

__all__ = [
    'KrakenSummary']

INDENT_UNIT = 2


class KrakenSummary(object):
    def __init__(self, infile, ignore_unclassified=False):
        self.infile = Path(infile).expanduser().resolve()
        self.ignore_unclassified = ignore_unclassified

        nodes = {}
        current_root_index = 0
        re_indent = re.compile('^\s*')

        tree = ete3.Tree()
        root = tree.add_child(name='root')

        nodes[current_root_index] = root

        with self.infile.open() as handle:
            for line in csv.reader(handle, delimiter='\t'):
                fraction, cumulative, count, order, tax_id, taxa_entry = line

                indent_size = len(re_indent.match(taxa_entry).group())
                taxa_name = re_indent.sub('', taxa_entry)

                if taxa_name == 'root':
                    continue

                if not ignore_unclassified and taxa_name == 'unclassified':
                    tree.add_child(name='unclassified')

                if indent_size >= current_root_index:
                    parent = nodes[current_root_index]
                else:
                    parent = nodes[indent_size - INDENT_UNIT]

                child = parent.add_child(name=taxa_name)
                current_root_index = indent_size
                nodes[current_root_index] = child

        self.tree = tree

    @property
    def newick(self):
        return self.tree.write()

    @property
    def toytree(self):
        return toytree.tree(self.newick)

    def __repr__(self):
        return (
            f'{self.__class__.__name__}('
            f'"{self.infile}", '
            f'ignore_unclassified={self.ignore_unclassified})')
