# Experiments with [NeuralCoref](https://github.com/huggingface/neuralcoref)

This repository contains code of experiments on [NeuralCoref](https://github.com/huggingface/neuralcoref), a coreference resolution system, conducted by a group of students from University of Potsdam: Polina Gusenkova, Karina Hensel and Iana Palacheva. This is a part of final project for **PM in Machine Learning: Coreference Resolution**, the lecturer is [Sharid Loáiciga](https://sites.google.com/site/loaicigasharid/).


## Description
* **[rucor_to_neuralcoref.ipynb](https://github.com/YanaPalacheva/experiments_neuralcoref/blob/master/rucor_to_neuralcoref.ipynb)**: this adaptation is supposed to     convert [RuCor](http://rucoref.maimbava.net/): Russian language corpus annotated with coreferential relations to the suitable for [NeuralCoref](https://github.com/huggingface/neuralcoref) format.

  It employs [rucor_to_conllu](https://github.com/fostroll/rucor_to_conllu): a conversation script for RuCor corpus to CoNLL-U format.  
  Prerequisites: RuCor corpus preprocessed by [rucor_to_conllu](https://github.com/fostroll/rucor_to_conllu) (instructions are explicitly described in the repo).  

## Training the Russian model with NeuralCoref

NeuralCoref's developer provide [instruction](https://github.com/YanaPalacheva/neuralcoref/blob/master/neuralcoref/train/training.md) on training a model for other language. Below we provide specific instructions how to train a Russian model on [RuCor](http://rucoref.maimbava.net/) corpus.

### Preparation steps
- Download [RuCor](http://rucoref.maimbava.net/), unpack it and run it first through [rucor_to_conllu](https://github.com/fostroll/rucor_to_conllu) script, then through [rucor_to_neuralcoref.ipynb](https://github.com/YanaPalacheva/experiments_neuralcoref/blob/master/rucor_to_neuralcoref.ipynb) script. It will convert the original data into suitable for NeuralCoref system format.
- In order to construct a complete dataset, run the following commands:
   ~~~~  
   cd rucoref_29.10.2015/parsed_testset_neuralcoref
   cat */*.v4_gold_conll >> train.russian.v4_gold_conll
   ~~~~  
   For convenience, we provide ready-to-use dataset in this repository TODO
- Next, clone the original NeuralCoref repository (we strongly recommend to do it in a virtual environment (venv or conda), python>=3.6):
   ~~~~  
   git clone https://github.com/huggingface/neuralcoref.git
   cd neuralcoref
   pip install -r requirements.txt
   ~~~~  
- For parsing, it's neessary to additionally install a Russian language model. Unfortunately, spaCy (v.<3.0) which is used by default does not provide such a model. 
We use stanza wrapper model instead, it behaves like spaCy model:
   ~~~~  
   pip install spacy-stanza<0.3.0
   ~~~~  
   Then, download the Russian language model:
   ~~~~  
   python
   import stanza
   from spacy_stanza import StanzaLanguage
   stanza.download("ru")
   ~~~~  
### The first training step
   The first step is to give the train data to the rule-based mentions-detection module which uses tagger, parser and NER annotations to identify a set of potential coreference mentions and gathers the mention features in a set of numpy arrays to be used as input for the neural net model. This module is conllparser.py, in this repository its vesion is adapted for Russian, in order to continue training, replace the original [conllparser.py](https://github.com/huggingface/neuralcoref/blob/master/neuralcoref/train/conllparser.py) with [this version](). Then run this command:
   ~~~~  
   pip install -e .
   ~~~~
   Prepare the data:
   1. Move the dataset (train.russian.v4_gold_conll) to neuralcoref/train/data/train folder and 
   2. Put the [ru_embeddings\*]() folder  into **train** subfolder.
   3. Run the following command (while staying in **train** subfolder):
   ~~~~
   python -m neuralcoref.train.conllparser --path ./data/train/
   ~~~~  
   \*the embeddings are taken from [this Coreference Resulution system repo](https://github.com/annkupriyanova/Coreference-Resolution) since it is not clear how to construct own word embeddings in suitable for NeuralCoref format, it very well may be the reason why the following training is not working.
### The second training step
- TBD
