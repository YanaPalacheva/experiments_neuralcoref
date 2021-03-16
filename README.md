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
- Next, clone the original NeuralCoref repository:
   ~~~~
   ~~~~
- For parsing, it's neessary to additionally install a Russian language model. Unfortunately, spaCy (v.<3.0) which is used by default does not provide such a model. 
We use stanza wrapper model instead, it behaves like spaCy model:
   ~~~~
   ~~~~
### The first training step
-
### The second training step
- TBD
