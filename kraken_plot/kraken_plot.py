import csv
import re

from pathlib import Path

import ete3
import toytree

__all__ = [
    'KrakenSummary']


class KrakenSummary(object):
    def __init__(self, infile, ignore_unclassified=False):
        self.infile = Path(infile).expanduser().resolve()

        nodes = {}
        current_root_index = 0
        re_prefix = re.compile('^\s*')

        tree = ete3.Tree()

        root = tree.add_child(name='root')

        nodes[current_root_index] = root

        with self.infile.open() as handle:
            for line in csv.reader(handle, delimiter='\t'):
                fraction, cumulative, count, order, tax_id, taxa_entry = line

                num_whitespace = len(re_prefix.match(taxa_entry).group()) / 2
                taxa_name = re_prefix.sub('', taxa_entry)

                if taxa_entry == 'root':
                    continue

                if not ignore_unclassified and taxa_entry == 'unclassified':
                    tree.add_child(name='unclassified')

                if num_whitespace >= current_root_index:
                    parent = nodes[current_root_index]
                else:
                    parent = nodes[num_whitespace - 1]

                child = parent.add_child(name=taxa_name)
                current_root_index = num_whitespace
                nodes[current_root_index] = child

        self.tree = tree

    @property
    def newick(self):
        return self.tree.write()

    @property
    def toytree(self):
        return toytree.tree(self.newick)

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.infile}")'
