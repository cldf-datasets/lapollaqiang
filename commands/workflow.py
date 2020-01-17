"""

"""
from pyigt import Glosses2
from cldfbench_lapollaqiang import Dataset


def register(parser):
    pass


def run(args):
    text = Glosses2(Dataset().cldf_reader())
    text.check_glosses()

    #text.get_concordance(ctype='grammar')
    #text.get_concordance(ctype='lexicon', filename='output/lexical-concordance.tsv')
    #text.get_concordance(ctype='forms', filename='output/form-concordance.tsv')
    #text.get_concepts(ctype='lexicon', filename='output/automated-concepts.tsv')
    #text.get_concepts(ctype='grammar', filename='output/automated-glosses.tsv',)
    #text.get_wordlist(filename='qiang-wordlist', doculect='Qiang',
    #        profile='etc/orthography.tsv')
    #text.get_profile(filename='output/automated-orthography.tsv')
    #text.get_app()
