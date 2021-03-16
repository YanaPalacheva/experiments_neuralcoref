import neuralcoref
import spacy
import re
from conllu.models import TokenList, Token
import os
import shutil


def neuralcoref_to_scorer(path_conllu, path_out, nlp, ending_cut, for_cort=False):
    if os.path.exists(path_out):
        shutil.rmtree(path_out)
    os.makedirs(path_out, exist_ok=True)

    # iterate over files in dir
    for doc_name in os.listdir(path_conllu):
        if doc_name.endswith(".en.txt"):
            # if doc_name != "a2e_0029_1.en.txt":
            #     continue
            print(doc_name)

            # read the file as string
            with open(os.path.join(path_conllu, doc_name), 'r', encoding='utf-8') as f:
                data = f.read()

            sentences = []

            doc = nlp(data)
            # if for_cort:
            #     print(doc[0].dep_)
            #     return
            tokens = [[t.text, '-', t] for t in doc]
            for i, cluster in enumerate(doc._.coref_clusters):
                for mention in cluster.mentions:
                    # print(i+1, mention, mention.start, mention.end)
                    if mention.start == mention.end-1 or (tokens[mention.end - 1][0] == '\n' and mention.start == mention.end-2):
                        tokens[mention.start][1] = re.sub(r'-\|', '', tokens[mention.start][1] + '|(' + str(i+1) + ')')
                    else:
                        tokens[mention.start][1] = re.sub(r'-\|', '', tokens[mention.start][1] + '|(' + str(i+1))
                        if tokens[mention.end - 1][0] == '\n':
                            tokens[mention.end - 2][1] = re.sub(r'-\|', '', tokens[mention.end-1][1] + '|' + str(i+1) + ')')
                        else:
                            tokens[mention.end - 1][1] = re.sub(r'-\|', '', tokens[mention.end-1][1] + '|' + str(i+1) + ')')

            sentence = TokenList([])
            i=0
            for t in tokens:
                if t[0] == '\n':
                    sentences.append(sentence)
                    sentence = TokenList([])
                    i=0
                else:
                    if for_cort:
                        sentence.append(Token(
                            id=doc_name[:ending_cut],
                            form=0,
                            lemma=i,
                            upos=t[0],
                            xpos=t[2].tag_,
                            feats=t[2].dep_,
                            head='-',
                            deprel='-',
                            deps='-',
                            misc=t[1]
                        ))
                    else:
                        sentence.append(Token(
                            id=doc_name[:ending_cut],
                            form=0,
                            lemma=i,
                            upos=t[0],
                            xpos=t[1]
                        ))
                    i += 1

            # write to .conll file
            with open(os.path.join(path_out, doc_name[:-4] + '.conll'), 'a', encoding='utf-8') as f:
                f.write('#begin document (' + doc_name[:ending_cut] + '); part 000\n')
                for sentence in sentences:
                    f.write(sentence.serialize())
                f.write('#end document ')


nlp = spacy.load('en_core_web_sm')
neuralcoref.add_to_pipe(nlp)

# path_conllu = '.\\paws\\data\\plain'
# path_out = '.\\scorer\\response'
# ending_cut = -4

# path_conllu = '.\\OntoNotes\\plain'
# path_out = '.\\scorer\\response_ontonotes'
# ending_cut = -7

path_conllu = '.\\OntoNotes\\plain'
path_out = '.\\scorer\\cort\\response_ontonotes'
ending_cut = -7

neuralcoref_to_scorer(path_conllu, path_out, nlp, ending_cut, for_cort=True)