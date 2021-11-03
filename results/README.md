# Folder contents

This folder contain the following files:

* `resnet50_6_25.txt`  - Scores on the test set using the resnet50 model
* `densenet121_4_30.txt` - Scores on the test set using the densenet121 model
* `inceptionv3_4_30.txt` - Scores on the test seet using de inceptionV3 model
* `inception_resnetv2_4_30.txt` - Scores on the test set using de inception-ResnetV2 model

The ensemble model described in the paper is obtained by adding the scores of these four models.

The file `radiologists_evaluation_results.csv` contains the radiologists` results on a smaller test set. The
file also contains the score using the ensemble of the previous four models for comparison
