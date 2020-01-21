---
geometry:
- top=30mm
- left=20mm
---
# Source code and data accompanying the study «Towards a sustainable handling of inter-linear-glossed text in language documentation»

This repository is intended to run the users through the workflow described in the paper.

## 1 Preliminaries

We assume that users are familiar with the commandline on their respective system, that they have Python in a version equal or higher to 3.5 installed, and that they also have the GIT version control software on their machine.

## 2 Getting started

### Python packages

In order to run through the workflow, some python packages must be installed. This is best done
in a [virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/),
in order to keep your system's python installation unaffected. Thus, in an activated virtual environment,
with `ìgt-paper/` as working directroy, run
```shell script
$ pip install -e .
```
This will install the packages listed in [`setup.py`](setup.py), under `"install_requires"`.


### CLDF Catalogs

The workflow decribed in this paper requires access to several catalogs:
- [Glottolog](https://github.com/glottolog/glottolog) - to lookup language metadata,
- [Concepticon](https://github.com/concepticon/concepticon-data) - to lookup information about lexical concepts - and
- [CLTS](https://github.com/cldf-clts/clts) - for information about transcription systems.

We will "install" these using the `cldfbench` command, installed with the `cldfbench` package 
(see the [`README`](https://github.com/cldf/cldfbench/#catalogs)):
```shell script
cldfbench catconfig
```

Since Glottolog requires downloading about 500MB of data, this may take some time. It also requires about 1.2 GB of
free disk space:
```shell script
$ du -sh .config/cldf/*
4,0K	.config/cldf/_catalog.ini
4,0K	.config/cldf/catalog.ini
43M	.config/cldf/clts
122M	.config/cldf/concepticon
994M	.config/cldf/glottolog
```


## 3 Converting the "raw" data to a CLDF dataset

The Quiang corpus used in this paper comes as simple, line-based text file: [`Qiang.txt`](raw/Qiang.txt).
First attempts at parsing this file led to detection of errors in the original digitized version.
These were corrected in the file [`Qiang-2.txt`](raw/Qiang-2.txt). (`Qiang.txt` is kept in this repository
in case users are interested to inspect the actual errors).

Conversion to CLDF is implemented within the [`cldfbench` framework](https://github.com/cldf/cldfbench/#implementing-cldf-creation),
i.e. by providing some [Python code](cldfbench_lapollaqiang.py), which is invoked via
```shell script
$ cldfbench makecldf cldfbench_lapollaqiang.py
```

This will (re-)create the CLDF dataset in the [`cldf/`](cldf/) directory. The remainder of the workflow will
use [`cldf/examples.csv`](cldf/examples.csv) as its main input.


## 4 Running the five-stage workflow

The workflow described in the paper is implemented as 
[dataset specific command](https://github.com/cldf/cldfbench/blob/master/src/cldfbench/commands/README.md#dataset-specific-commands)
to be run with `cldfbench`. The code is available in [`commands/workflow.py`](commands/workflow.py).

In the following sections we will follow through this code in an interactive Python session.


### 4.1 Getting Started

You can inspect the IGTs in the dataset using the `igt` command, installed with `pyigt`, to get some
summary statistics:
```shell script
$ igt stats cldf/cldf-metadata.json
            count
--------  -------
example      1276
word         3954
morpheme     8256

Example properties:
  ID
  Language_ID
  Primary_Text
  Analyzed_Word
  Gloss
  Translated_Text
  Meta_Language_ID
  Comment
  Text_ID
  Sentence_Number
  Phrase_Number
```

The `Text_ID` property listed above can be used to filter IGTs for display:
```shell script
$ igt ls cldf/cldf-metadata.json -c Text_ID -m 1
Example 1:
zəple: ȵike: peji qeʴlotʂuʁɑ,
zəp-le:       ȵi-ke:       pe-ji       qeʴlotʂu-ʁɑ,
earth-DEF:CL  WH-INDEF:CL  become-CSM  in.the.past-LOC

Example 2:
mutulɑ mujuqů ʐguəzi wei,
mutu-lɑ     mujuqů    ʐguə-zi    we-i,
heaven-LOC  sun       nine-CL    exist-HS

Example 3:
zəple: ətɕhəqhɑʐəi.
zəp-le:       ə-tɕhəqhɑ-ʐ-əi.
earth-DEF:CL  DIR-burn-CAUS-HS

Example 4:
mə ȵɑ ɣlu jətʂŋuəȵi,
mə             ȵɑ    ɣlu             jə-tʂ-ŋuəȵi,
older.brother  COM   younger.sister  two-CL-TOP

Example 5:
zuɑməɸu oʐgutɑ ipiχuɑȵi,
zuɑmə-ɸu      o-ʐgu-tɑ    i-pi-χuɑ-ȵi,
cypress-tree  one-CL-LOC  DIR-hide-because-ADV

Example 6:
ɦomuxtɕuwei.
ɦo-mu-xtɕu-wei.
DIR-NEG-burn-HS

Example 7:
steketɑ mi peʴʐəs ŋuəχuɑȵi,
steke-tɑ    mi      peʴʐə-s           ŋuə-χuɑ-ȵi,
later-LOC   people  raise(child)-NOM  COP-because-ADV

Example 8:
mə ȵɑ ɣlu ləzi idʐitɕi,
mə             ȵɑ    ɣlu             lə-zi    i-dʐi-tɕi,
older.brother  COM   younger.sister  DEF-CL   DIR-discuss-3pl

Example 9:
ȵutɕuku dzuɑʁl exʂe ɦeibiȵi,
ȵutɕuku    dzuɑʁl      e-xʂe    ɦei-bi-ȵi,
each       stone.mill  one-CL   DIR-carry.on.back-ADV

Example 10:
ʁuqtɑwu ɦoɣlu,
ʁu-q-tɑ-wu             ɦo-ɣlu,
mountain-head-LOC-ABL  DIR-roll

Example 11:
dzuɑʁl jəxʂe etʂetuptu,
dzuɑʁl      jə-xʂe    e-tʂetup-tu,
stone.mill  two-CL    DIR-bump.into-LNK

Example 12:
ȵizzi oqpi pəs,
ȵizzi    oqpi        pə-s,
3dl      one:family  do-NOM

Example 13:
dzuɑʁl jəxʂe ɦoɣlustɑ,
dzuɑʁl      jə-xʂe    ɦo-ɣlu-s-tɑ,
stone.mill  two-CL    DIR-roll-NOM-LOC

Example 14:
qhuɑt etʂetupwei,
qhuɑt          e-tʂetup-wei,
as.it.happens  DIR-bump.into-HS

Example 15:
ɦɑtsəiȵike,
ɦɑ-tsəi-ȵike,
INT-this.manner-after

Example 16:
mə ȵɑ ɣlu ləzi oqpi ɦopəi.
mə             ȵɑ    ɣlu             lə-zi    oqpi        ɦo-pə-i.
older.brother  COM   younger.sister  DEF-CL   one:family  DIR-do-HS

Example 17:
əjəp peȵi,
ə-jə-p        pe-ȵi,
one-two-year  become-ADV

Example 18:
ɣlule: mi qes mɑŋ̥u̥ə̥ ke: iɕi.
ɣlu-le:                mi      qes    mɑ-ŋ̥u̥ə̥    ke:       i-ɕi.
younger.sister-DEF:CL  people  form   NEG-COP   INDEF:CL  DIR-release

Example 19:
məle: təkhueq,
mə-le:                tə-khueq,
older.brother-DEF:CL  DIR-angry

Example 20:
duɑʁlle:wu səxteȵi tɕetɕilɑ daʁů.
duɑʁl-le:-wu        sə-xte-ȵi     tɕetɕi-lɑ       da-ʁů.
scythe-DEF:CL-INST  DIR-chop-LNK  everywhere-LOC  DIR-throw(away)

Example 21:
steke lɑsʁɑ,
steke    lɑ-s-ʁɑ,
later    DEF:one-day-LOC

Example 22:
tɕetɕilɑwu mufů təlɑji,
tɕetɕi-lɑ-wu        mufů    tə-lɑ-ji,
everywhere-LOC-ABL  smoke   DIR-come-CSM

Example 23:
ɦɑtsəiȵike,
ɦɑ-tsəi-ȵike,
INT-this.manner-after

Example 24:
mi luji.
mi      lu-ji.
people  come-CSM
```


## 4.2 Checking glosses

For further inspection, we load the data in an interactive Python session:

```python
>>> from pyigt import Corpus
>>> from cldfbench_lapollaqiang import Dataset
>>> texts = Corpus.from_cldf(Dataset().cldf_reader())
```

In order to check the glosses (as essential part of our worfklow steps 1 and 2), we run
```python
>>> texts.check_glosses()
```

The output distinguishes errors by *levels*. An error in the first level means that
phrase and gloss are not well-aligned, i.e.
 a phrase has more or less elements than its corresponding glosses. A second-level error refers to
mis-alignments of morphemes in a word and corresponding gloss.

Our check yields 13 level 2 errors, where number of morphemes differs from the number of
morphemes glossed:

```
[63:5 : second level 1]
['qu', 'kəpə', 'kəi', 'ʂ,']
['ɦe', 'afraid', 'HABIT', 'NAR', 'LNK']
---
[318:2 : second level 2]
['hɑ', 'lə', 'jə', 'kui', 'tu,']
['DIR', 'come', 'REP', 'LNK']
---
[463:3 : second level 3]
['satʂů', 'le:', 'tʂi', 'le:', 'wu']
['younger', 'sister', 'DEF:CL', 'son', 'DEF:CL', 'AGT']
---
[643:1 : second level 4]
['ɦɑ', 'kə']
['that.manner']
---
[678:1 : second level 5]
['ɦɑ', 'tsəi', 'ŋuəȵi,']
['this.manner', 'TOP']
---
[745:3 : second level 6]
['ɑ', 'χtʂ']
['one.row']
---
[840:1 : second level 7]
['he', 'ɕi', 'kui']
['DIR', 'send']
---
[843:2 : second level 8]
['qɑpə', 'tɕ']
['old.man']
---
[860:2 : second level 9]
['du', 'ɸu', 'ȵi']
['run.away', 'ADV']
---
[886:3 : second level 10]
['ə', 'lɑ', 'kəi', 'tu,']
['DIR', 'come', 'LNK']
---
[928:2 : second level 11]
['ɕtɕə', 'p']
['seven.years']
---
[984:1 : second level 12]
['ɦɑ', 'kə']
['that.manner']
---
[1255:7 : second level 13]
['tɕɑu', 'ʐbə', 'kə', 'ȵi,']
['think.to.oneself', 'INF', 'ADV']
---
```


### Creation of concordances

A `Corpus` object computes three basic types of concordance upon loading:
- basic concordances that list each morpheme along with its gloss (`form`), 
- grammatical concordances which list only those items deemed to be grammatical (`grammar`), and 
- lexical concordances which are built from items supposed to be only lexical (`lexicon`).

Note: Erroneous forms as identified in the previous steps are ignored.

We can write the concordances to files as follows:

```python
>>> texts.write_concordance('forms', filename='output/form-concordance.tsv')
>>> texts.write_concordance('lexicon', filename='output/lexical-concordance.tsv')
>>> texts.write_concordance('grammar', filename='output/grammatical-concordance.tsv')
```

The concordances created above keep a full trace to each word in each original phrase. 
They can be used in further steps to normalize the data or to link it to reference catalogs.


### Mapping lexical and grammatical concepts to reference catalogs

We can use the concordances to create concept lists, both for grammatical and for lexical entries:

```python
>>> texts.write_concepts('lexicon', filename='output/automated-concepts.tsv')
>>> texts.write_concepts('grammar', filename='output/automated-glosses.tsv')
```

While there is no Grammaticon to which we could link our grammatical concepts, we can add the full 
names for each grammatical concept from the resource. This has do be done manually, but it does not 
take much time, and it has also revealed that the abbreviation list in the resource lacks a 
description for the abbreviation REDUP. The list of grammatical concepts is provided as `etc/glosses.tsv`. 

For the list of lexical concepts, we can use the Concepticon resource to automatically map our 
automatically created concept list to the data provided by the concepticon project. 
This can be done using the `concepticon` command, installed with the `pyconcepticon` package
(you may have to look up the path to the Concepticon repository clone via `cldfbench catinfo`):

```shell script
$ concepticon --repos=PATH/TO/CLONE/OF/concepticon-data map_concepts output/automated-concepts.tsv
```

This will yield a longer list as output that needs to be written to a file in order to edit it.

```
$ concepticon --repos=PATH/TO/CLONE/OF/concepticon-data map_concepts output/automated-concepts.tsv > etc/concepts-mapped.tsv
```

As we can see from the output, as many as 421 concepts can be automatically linked, which accounts for about 72% of the list. 
After manually revising this list, (see [`etc/concepts.tsv`](etc/concepts.tsv)) the number of linked items drops a bit, but it contains still a considerable amount of glosses that are describe well enough to link them to the Concepticon project and make them thus available for different studies.


### Standardizing transcriptions

The transcriptions in the original resource are not necessarily standardized. We can use the `pyigt` library 
again to make a first `orthography profile` which we then can use to further standardize the data.
(Again, you may have to look up the path to the CLTS repository clone via `cldfbench catinfo`.)

```python
>>> from pyclts import CLTS
>>> texts.get_profile(filename='output/automated-orthograpy.tsv', clts=CLTS('PATH/TO/CLONE/OF/clts'))
```

This will create an initial orthography profile that can be further refined by the users. Our refined version can be found in 
[`etc/orthography.tsv`](etc/orthography.tsv). 


### Identifying language-internal cognates

Once created and manually corrected, we can use our improved transcriptions to search for 
language-internal cognates. We do this, by envoking the following command, which will segment the 
transcriptions, iterate over all data, compare words which have the same grammatical and lexical 
gloss, and place them in the same cognate set, labelled as `CROSSID`, if their similarity is below 
a certain threshold.

```python
>>> wl = texts.get_wordlist(doculect='Qiang', profile='etc/orthography.tsv')
>>> wl.output(
...     'tsv',
...     filename='qiang-wordlist',
...     prettify=False,
...     ignore='all',
...     subset=True,
...     cols=[h for h in wl.columns])
```

The resulting wordlist [`qiang-wordlist.tsv`](qiang-wordlist.tsv) can be conveniently inspected with help of the EDICTOR tool.


### Creating the concordance browser application

The concordance browser is created from the assembled data, specifically the wordlist. It consists of a simple HTML
frontend, which includes some JavaScript code implementing the viewer's functionality, and the data, again
loaded from a JavaScript file, created via

```python
>>> texts.write_app(dest='app')
```

To open the app, just open the local file `app/index.html` in your browser. 
