import nltk as nlp
import argparse
import os
import warnings
warnings.filterwarnings('ignore')
from matplotlib import pyplot as plt
# BEfore using BLEU(Bilingual Evaluation Understudy) score read this
# https://towardsdatascience.com/evaluating-text-output-in-nlp-bleu-at-your-own-risk-e8609665a213

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--dir", required=True,
	help="path to caption file")
args = vars(ap.parse_args())

file_lists=os.listdir(args.get("dir")+" Caption Text")
count=0
for file in file_lists:
    all_text = ''
    no_of_words = 0
    print(file)
    try:
        with open(args.get("dir")+" Caption Text/"+file) as f:
            lines = f.readlines()
            for line in lines:
                no_of_words = no_of_words + len(line.split())
                all_text = all_text + line
        count = count + 1
        Words = all_text.split()
        frequency_distribution = nlp.FreqDist(Words)
        if count == 1:
            weights=[1,0,0,0]
            # [unigram precision, ]
            bleu_score=nlp.translate.bleu_score.sentence_bleu([['this','is','a','ship'],['this','is','the','ship'],['ship','is','this']],['It','is','ship'],weights)
            print("Bleu score "+str(bleu_score))
            break
        print(frequency_distribution)
        print(frequency_distribution['<i>'])
        print(str(no_of_words))
        # vocabulary = frequency_distribution.keys()
        # print(vocabulary[:50])

    except BaseException as e:
        print(e)

