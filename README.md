# Experiments with [NeuralCoref](https://github.com/huggingface/neuralcoref)

This repository contains code of experiments on [NeuralCoref](https://github.com/huggingface/neuralcoref), a coreference resolution system, conducted by a group of students from University of Potsdam: Polina Gusenkova, Karina Hensel and Iana Palacheva. This is a part of final project for **PM in Machine Learning: Coreference Resolution**, the lecturer is [Sharid Loáiciga](https://sites.google.com/site/loaicigasharid/).


## Description
* **[rucor_to_neuralcoref.ipynb](https://github.com/YanaPalacheva/experiments_neuralcoref/blob/master/rucor_to_neuralcoref.ipynb)**: this adaptation is supposed to     convert [RuCor](http://rucoref.maimbava.net/): Russian language corpus annotated with coreferential relations to the suitable for [NeuralCoref](https://github.com/huggingface/neuralcoref) format.

  It employs [rucor_to_conllu](https://github.com/fostroll/rucor_to_conllu): a conversation script for RuCor corpus to CoNLL-U format.  
  Prerequisites: RuCor corpus preprocessed by [rucor_to_conllu](https://github.com/fostroll/rucor_to_conllu) (instructions are explicitly described in the repo).  

* 
