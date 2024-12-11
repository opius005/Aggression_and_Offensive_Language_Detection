# Aggression_and_Offensive_Language_Detection
Aggression and Offensive Language detection in Hindi_English code-mixed data using Multi-Task-Transfer-Learning

**mask.py** file is the code to mask the tweet text extracted from twitter.

**split.py** file is the code to split whole dataset into train,test,validation sets.

**original split** folder contains of train,test,validation sets of whole dataset

**same split** folder contains files with prefix **cs** represent only codemixed data splits and files with prefix **ms** represent only monolingual data splits.

## Executing FINAL.ipynb file:
install anaconda and pytorch with code (if not possible then install with cpu)

install the packages mentioned in 1st cell of the file.

**Hyper_params** is the class where we set all the hyper parameters lo the model that will be used thorughout the file.

In 5th cell, We can set which pretrained language model we are going to use for MTTL approach, and we can alse set the paths to dataset (combined or codemixed or monolingual)

We can execure the code now and see the MAcro-F1 score of the model on MTTL apprach on test set at last cell output.

### Executing baseline pretrained language models without MTTL :
we can get the for executing baseline from the dataset paper (https://aclanthology.org/2023.woah-1.3/) given in this repository (https://github.com/surrey-nlp/woah-aggression-detection/tree/main)
