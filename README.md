---
geometry:
- top=30mm
- left=20mm
---
# Source code and data accompanying the study «Towards a sustainable handling of inter-linear-glossed text in language documentation»

This little repository is intended to run the users through the workflow described in the paper.

## 1 Preliminaries

We assume that users are familiar with the commandline on their respective system, that they have Python in a version equal or higher to 3.5 installed, and that they also have the GIT version control system on their machine.

## 2 Getting started

In order to run through the workflow, some preliminary packages must be downloaded or installed. We start by installing the required Python packages with help of the `pip` system.

```
$ pip install -r requirements.txt
```

Once the packages have been successfully installed, users can install the `pyigt` package submitted along with this repository by typing:

```
$ pip install -e pyigt/
```

As a final step, we need to download the raw data from the [Concepticon](https://concepticon.clld.org) and the [CLTS](https://clts.clld.org) projects. We do this with help of `git`:

```
$ git clone https://github.com/concepticon/concepticon-data.git
$ git clone https://github.com/cldf-clts/clts.git
```

We will need these repositories later in the code, so they should be in the same folder as the main repository. 

## 3 Convert the data to the tabular input format

We wrote an explicit parser for this step. When running this the first time, we detected errors in the original digitized version. These were corrected in the file `Qiang-2.txt`, and we leave the file `Qiang.txt` here in case users are interested to inspect the actual errors.

To run the conversion routine, just type:

```
$ python parse.txt
```

This will create (or re-create) the file `qiang-igt.tsv`.

## 4 Running the five-stage workflow

We provide a script that runs the full workflow (see `workflow.py`), but we run the users here directly through alls teps.

### 4.1 Getting Started
First, we want to load the data. So we start an interactive Python session and type:

```python
>>> from pyigt import Glosses
>>> texts = Glosses(
        'qiang-igt.tsv', 
        row='text', 
        sep=' ', 
        sepB='-')
```

We can now query the text quickly:

```python
>>> texts.print_text('Text 1', 'phrase', 'gloss')
```

The result is a very unspectacular rendering of all phrases and glosses in Text 1 of the resource.

|                       |                       |                      |                |                  |
|:----------------------|:----------------------|:---------------------|:---------------|:-----------------|
| zəp-le:               | ȵi-ke:                | pe-ji                |                |                  |
| earth-DEF:CL          | WH-INDEF:CL           | become-CSM           |                |                  |
|                       |                       |                      |                |                  |
| jə-tʂ-ŋuəȵi,          | zuɑmə-ɸu              | o-ʐgu-tɑ             |                |                  |
| two-CL-TOP            | cypress-tree          | one-CL-LOC           |                |                  |
|                       |                       |                      |                |                  |
| ŋuə-χuɑ-ȵi,           | mə                    | ȵɑ                   | ɣlu            | lə-zi            |
| COP-because-ADV       | older.brother         | COM                  | younger.sister | DEF-CL           |
|                       |                       |                      |                |                  |
| pe-ȵi,                | ɣlu-le:               | mi                   | qes            | mɑ-ŋ̥u̥ə̥           |
| become-ADV            | younger.sister-DEF:CL | people               | form           | NEG-COP          |
|                       |                       |                      |                |                  |
| ke:                   | i-ɕi.                 | mə-le:               |                |                  |
| INDEF:CL              | DIR-release           | older.brother-DEF:CL |                |                  |
|                       |                       |                      |                |                  |
| tə-khueq,             | duɑʁl-le:-wu          | sə-xte-ȵi            | tɕetɕi-lɑ      | da-ʁů.           |
| DIR-angry             | scythe-DEF:CL-INST    | DIR-chop-LNK         | everywhere-LOC | DIR-throw(away)  |
|                       |                       |                      |                |                  |
| steke                 |                       |                      |                |                  |
| later                 |                       |                      |                |                  |
|                       |                       |                      |                |                  |
| lɑ-s-ʁɑ,              | tɕetɕi-lɑ-wu          | mufů                 |                |                  |
| DEF:one-day-LOC       | everywhere-LOC-ABL    | smoke                |                |                  |
|                       |                       |                      |                |                  |
| qeʴlotʂu-ʁɑ,          | mutu-lɑ               | mujuqů               | ʐguə-zi        |                  |
| in.the.past-LOC       | heaven-LOC            | sun                  | nine-CL        |                  |
|                       |                       |                      |                |                  |
| i-pi-χuɑ-ȵi,          | ɦo-mu-xtɕu-wei.       | steke-tɑ             | mi             | peʴʐə-s          |
| DIR-hide-because-ADV  | DIR-NEG-burn-HS       | later-LOC            | people         | raise(child)-NOM |
|                       |                       |                      |                |                  |
| i-dʐi-tɕi,            | ȵutɕuku               | dzuɑʁl               | e-xʂe          |                  |
| DIR-discuss-3pl       | each                  | stone.mill           | one-CL         |                  |
|                       |                       |                      |                |                  |
| tə-lɑ-ji,             |                       |                      |                |                  |
| DIR-come-CSM          |                       |                      |                |                  |
|                       |                       |                      |                |                  |
| we-i,                 | zəp-le:               | ə-tɕhəqhɑ-ʐ-əi.      | mə             | ȵɑ               |
| exist-HS              | earth-DEF:CL          | DIR-burn-CAUS-HS     | older.brother  | COM              |
|                       |                       |                      |                |                  |
| ɣlu                   |                       |                      |                |                  |
| younger.sister        |                       |                      |                |                  |
|                       |                       |                      |                |                  |
| ɦei-bi-ȵi,            | ʁu-q-tɑ-wu            |                      |                |                  |
| DIR-carry.on.back-ADV | mountain-head-LOC-ABL |                      |                |                  |
|                       |                       |                      |                |                  |
| ɦo-ɣlu,               | dzuɑʁl                | jə-xʂe               |                |                  |
| DIR-roll              | stone.mill            | two-CL               |                |                  |
|                       |                       |                      |                |                  |
| e-tʂetup-tu,          | ȵizzi                 | oqpi                 |                |                  |
| DIR-bump.into-LNK     | 3dl                   | one:family           |                |                  |
|                       |                       |                      |                |                  |
| pə-s,                 | dzuɑʁl                | jə-xʂe               |                |                  |
| do-NOM                | stone.mill            | two-CL               |                |                  |
|                       |                       |                      |                |                  |
| ɦo-ɣlu-s-tɑ,          | qhuɑt                 |                      |                |                  |
| DIR-roll-NOM-LOC      | as.it.happens         |                      |                |                  |
|                       |                       |                      |                |                  |
| e-tʂetup-wei,         |                       |                      |                |                  |
| DIR-bump.into-HS      |                       |                      |                |                  |
|                       |                       |                      |                |                  |
| ɦɑ-tsəi-ȵike,         | mə                    | ȵɑ                   | ɣlu            | lə-zi            |
| INT-this.manner-after | older.brother         | COM                  | younger.sister | DEF-CL           |
|                       |                       |                      |                |                  |
| oqpi                  | ɦo-pə-i.              | ə-jə-p               |                |                  |
| one:family            | DIR-do-HS             | one-two-year         |                |                  |
|                       |                       |                      |                |                  |

We can also check the number of morphemes and words in our little resource:

```python
>>> texts.get_stats()
```
This yields the following table:

|  |  |
|:------|:----------|
| words | morphemes |
| 3932  | 8205      |


## 4.2 Checking glosses

In order to check the glosses (as essential part of our worfklow steps 1 and 2), we run the following command:

```python
>>> texts.check_glosses()
```

In the result, the errors are distinguished by *levels*. An error in the first level means that a phrase has more or less elements than its corresponding glosses. A second-level error refers to the problem of a misalignment between a given word in a phrase and the corresponding gloss.

Our check yields as many as 14 errors, in which the number of morphemes indicated inside a word differs from the number of morphemes glossed in the gloss.

```
[Text 5:92:3 : second level 1]
satʂů-le:-tʂi-le:-wu
younger-sister-DEF:CL-son-DEF:CL-AGT
---
[Text 5:235:1 : second level 2]
ɦɑ-kə
that.manner
---
[Text 5:262:0 : second level 3]
ɦɑ-tsəi-ŋuəȵi,
this.manner-TOP
---
[Text 5:316:3 : second level 4]
ɑ-χtʂ
one.row
---
[Text 3:358:0 : second level 5]
qu-kəpə-kəi-ʂ,
ɦe-afraid-HABIT-NAR-LNK
---
[Text 4:582:0 : second level 6]
hɑ-lə-jə-kui-tu,
DIR-come-REP-LNK
---
[Text 6:645:8 : second level 7]
he-ɕi-kui
DIR-send
---
[Text 6:648:2 : second level 8]
qɑpə-tɕ
old.man
---
[Text 6:664:2 : second level 9]
du-ɸu-ȵi
run.away-ADV
---
[Text 6:683:0 : second level 10]
ə-lɑ-kəi-tu,
DIR-come-LNK
---
[Text 6:714:2 : second level 11]
ɕtɕə-p
seven.years
---
[Text 6:727:3 : second level 12]
kɑ:-n-ɑ?”
go:PRS--2sg-Q
---
[Text 6:753:1 : second level 13]
ɦɑ-kə
that.manner
---
[Text 6:973:0 : second level 14]
tɕɑu-ʐbə-kə-ȵi,
think.to.oneself-INF-ADV
---
```

### Creation of concordances

There are three basic types of concordance which can be created: basic concordances that list each morpheme along with its gloss (`forms`), grammatical concordances which list only those items deemed to be grammatical (`grammar`), and lexical concordances which are built from items supposed to be only lexical (`lexical`).
This can be done in a straightforward way (erroneous forms as identified in the previous steps are ignored):

```python
>>> texts.get_concordance(ctype='forms', 
        filename='output/form-concordance.tsv')
>>> texts.get_concordance(ctype='lexicon', 
        filename='output/lexical-concordance.tsv')
>>> texts.get_concordance(ctype='grammar', 
        filename='output/grammatical-concordance.tsv')
```

The concordances that are created with these principle yield a full trace to each word in each original phrase. They can be used in further steps to normalize the data or to link it to reference catalogs.

### Mapping lexical and grammatical concepts to reference catalogs

Once we have inferred our concordances, we can also create concept lists, both for grammatical and for lexical entries:

```python
>>> texts.get_concepts(ctype='lexicon', 
        filename='output/automated-concepts.tsv')
>>> texts.get_concepts(ctype='grammar', 
        filename='output/automated-glosses.tsv')
```

While there is no Grammaticon to which we could link our grammatical concepts, we can add the full names for each grammatical concept from the resource. This has do be done manually, but it does not take much time, and it has also revealed that the abbreviation list in the resource lacks a description for the abbreviation REDUP. The list of grammatical concepts is provided as `etc/glosses.tsv`. 

For the list of lexical concepts, we can use the Concepticon resource to automatically map our automatically created concept list to the data provided by the concepticon project. This can be done by simply typing:

```
$ concepticon --repos=concepticon map_concepts output/automated-concepts.tsv
```

This will yield a longer list as output that needs to be written to a file in order to edit it.

```
$ concepticon --repos=concepticon map_concepts output/automated-concepts.tsv > etc/concepts-mapped.tsv
```

As we can see from the output, as many as 421 concepts can be automatically linked, which accounts for some 72%. After manually revising this list, (see `etc/concepts.tsv`) the number of linked items drops a bit, but it contains still a considerable amount of glosses that are describe well enough to link them to the Concepticon project and make them thus available for different studies.

### Standardizing transcriptions

The transcriptions in the original resource are not necessarily standardized. We can use the `pyigt` library again to make a first `orthography profile` which we can then use to further standardize the data.

```python
>>> texts.get_profile(
        filename='output/automated-orthograpy.tsv', 
        clts_dir='clts')
```

This will create an initial orthography profile that can be further refined by the users. Our refined version can be found in `etc/orthography.tsv`. 

### Identifying language-internal cognates

Once created and manually corrected, we can use our improved transcriptions to search for language-internal cognates. We do this, by envoking the folowing command, which will segmentize the transcriptions, iterate over all data, compare words which have the same grammatical and lexical gloss, and place them in the same cognate set, labelled as `CROSSID`, if their similarity is below a certain threshold.

```python
>>> texts.get_wordlist(
        doculect='Qiang', 
        profile='etc/orthography.tsv', 
        filename='qiang-wordlist.tsv')
```

The resulting wordlist `qiang-wordlist.tsv` can be conveniently inspected with help of the EDICTOR tool.

### Creating the concordance browser application

The concordance browser is created from the assembled data, specifically the wordlist. It creates essentially a larger JavaScript code with all the data, so that it can be employed by the application, which is a simple HTML file with some JavaScript code.

```python
>>> texts.get_app(dest='app')
```

To open the app, just double-click on the file `index.html` in the folder `app`. 



