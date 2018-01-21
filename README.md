<h1 align="center">kraken-review</h2>

<p align="center">A Python 3.6+ library for analyzing Kraken output</p>

<p align="center">
  <a href="#introduction"><strong>Introduction</strong></a>
  ·
  <a href="#tutorial"><strong>Tutorial</strong></a>
  ·
  <a href="#installation"><strong>Installation</strong></a>
</p>

<p align="center">
  <a href="https://github.com/clintval/kraken-review/issues">
    <img src="https://img.shields.io/github/issues/clintval/kraken-review.svg"></img>
  </a>
  <a href="https://github.com/clintval/kraken-review/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/clintval/kraken-review.svg"></img>
  </a>
</p>

<br>

<h3 align="center">Introduction</h3>

This library demonstrations parsing the summary results from the taxonomic sequence classifier [Kraken](https://ccb.jhu.edu/software/kraken/) into a tree representation.

Features that may be implemented include:

- Bar plot or scatter plot integration showing the magnitude of sequences assigned to each node in the phylogenetic tree.
- Method for _forcing_ all counts either up or down a linear branch to simplify sequence classification.
- Clade collapsing based on taxonomic assignment and phylogenetic order.

<br>

<h3 align="center">Tutorial</h3>

```python
>>> from kraken_review import KrakenSummary
>>> summary = KrakenSummary('sample-report.txt')
>>> summary.newick
'(((Mus musculus musculus:1):1,(Rattus norvegicus albus:1):1,Homo sapiens:1),unclassified:1);'
```

```python
>>> canvas, coords = summary.toytree.draw(
>>>     width=500,
>>>     height=175,
>>>     tip_labels_color=['red', 'black', 'black', 'black'],
>>>     # Make Carl Linnaeus proud and italicize those species names!
>>>     tip_labels=[f'<i>{l}</i>' for l in summary.toytree.get_tip_labels()])
```
![Simple Tree Example][simple-tree]

<h3 align="center">Installation</h3>

```bash
❯ pip install git+git://github.com/clintval/kraken-review.git
```


[simple-tree]: docs/simple-tree.png
