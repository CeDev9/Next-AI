# Hu and Ma (2020) Video Processing Kit

`interactionvideo` package processes videos to study human interactions. 

Please refer to  and cite the research paper: Hu and Ma (2020), "Human Interactions and Financial Investment: A Video-Based Approach", available at: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3583898

**For academic research purposes only. Please do not distribute or share.**

For feedbacks, please email: song.ma@yale.edu and allen.hu@yale.edu.



## Instruction

- `example.py` and `example.ipynb` are step-by-step tutorials. We strongly recommend you start from `example.ipynb`
- `interactionvideo` is the main package
- `data` folder includes data input
- `output` folder includes output results
- `mlmodel` folder includes pre-trained ML models
- `PythonSDK` is the Python SDK of Face++, directly downloaded from Github (https://github.com/FacePlusPlus/facepp-python-sdk)

## Overview

The video processing involves the following steps:

1. Set up folders and check dependencies (requirements)
2. Extract images and audios from a video using `pliers`
3. Extract text from audios using Google Speech2Text API
4. Process images(faces) using Face++ API
5. Process text using Loughran and McDonald (2011) Finance Dictionary and Nicolas, Bai, and Fiske (2019) Social Psychology Dictionary
6. Process audios using pre-trained ML models in `pyAudioAnalysis` and `speechemotionrecognition`
7. Aggregate information from 3V (visual, vocal, and verbal) to video level