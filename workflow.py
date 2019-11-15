from pyigt import Glosses

text = Glosses('qiang-igt.tsv')

text.check_glosses()

text.get_concordance(ctype='grammar', filename='output/grammatical-concordance.tsv')
text.get_concordance(ctype='lexicon', filename='output/lexical-concordance.tsv')
text.get_concordance(ctype='forms', filename='output/form-concordance.tsv')
text.get_concepts(ctype='lexicon', filename='output/automated-concepts.tsv')
text.get_concepts(ctype='grammar', filename='output/automated-glosses.tsv',)
text.get_wordlist(filename='qiang-wordlist', doculect='Qiang',
        profile='etc/orthography.tsv')
text.get_profile(filename='output/automated-orthography.tsv')
text.get_app()
