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
    text = Corpus(ds.cldf_reader())
    text.check_glosses()

    con = text.get_concordance(ctype='grammar')
    text.write_concordance(con, filename=output / 'grammatical-concordance.tsv')

    con = text.get_concordance(ctype='lexicon')
    text.write_concordance(con, filename=output / 'lexical-concordance.tsv')

    con = text.get_concordance(ctype='forms')
    text.write_concordance(con, filename=output / 'form-concordance.tsv')

    res = text.get_concepts(ctype='lexicon')
    text.write_concepts(res[0], res[1], filename=output / 'automated-concepts.tsv')

    res = text.get_concepts(ctype='grammar')
    text.write_concepts(res[0], res[1], filename=output / 'automated-glosses.tsv')

    wl = text.get_wordlist(doculect='Qiang', profile=ds.etc_dir / 'orthography.tsv')
    wl.output(
        'tsv',
        filename='qiang-wordlist',
        prettify=False,
        ignore='all',
        subset=True,
        cols=[h for h in wl.columns] + ['crossid'])

    profile = text.get_profile(clts=args.clts.api)
    text.write_profile(profile, filename=ds.dir / 'output' / 'automated-orthography.tsv')
    text.write_app(dest=ds.dir / 'app')
