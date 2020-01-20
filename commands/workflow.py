"""

"""
from pyigt import Corpus
from cldfbench_lapollaqiang import Dataset
from cldfbench.cli_util import add_catalog_spec


def register(parser):
    add_catalog_spec(parser, 'clts')


def run(args):
    ds = Dataset()
    output = ds.dir / 'output'
    text = Corpus.from_cldf(ds.cldf_reader())
    text.check_glosses()

    text.write_concordance('grammar', filename=output / 'grammatical-concordance.tsv')
    text.write_concordance('lexicon', filename=output / 'lexical-concordance.tsv')
    text.write_concordance('form', filename=output / 'form-concordance.tsv')

    text.write_concepts('lexicon', filename=output / 'automated-concepts.tsv')

    text.write_concepts('grammar', filename=output / 'automated-glosses.tsv')

    wl = text.get_wordlist(doculect='Qiang', profile=ds.etc_dir / 'orthography.tsv')
    wl.output(
        'tsv',
        filename='qiang-wordlist',
        prettify=False,
        ignore='all',
        subset=True,
        cols=[h for h in wl.columns] + ['crossid'])

    profile = text.get_profile(clts=args.clts.api, filename=ds.dir / 'output' / 'automated-orthography.tsv')
    text.write_app(dest=ds.dir / 'app')
