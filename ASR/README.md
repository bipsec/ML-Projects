# About Dataset
Competition Name: ASR For Regional Dialects

About this Competition:

- The prime goal of this competition is to come up with a solution system to transcribe Bengali speech with various regional dialects following the orthography set by linguists. The speech corpus for this competition has been developed by Bengali.AI from one of their ongoing large-scale research projects. The corpus consists of spontaneous speech on everyday topics from 373 individuals with various regional dialects from ten different geographical locations such as Rangpur, Kishoreganj, Narail, Chittagong, Narsingdi, Tangail, Barishal, Habiganj, Sylhet & Sandwip. The cumulative length of this entire speech corpus is over 79+ hours. Your efforts could improve the Bengali speech recognition technology using this unique speech recognition dataset for the very first time in history which is dealing with the regional speech domain. In addition, your submission will be among the first open-source speech recognition methods for Bengali.

Data Description: <br>
- The recordings are 16kHz *.wav audio files. The data are coming from 373 different speakers from 10 regions in Bangladesh (rangpur, kishoreganj, narail, chittagong, narsingdi, tangail, habiganj, barishal, sylhet, sandwip) There are in total 13610 samples in the train set (63:08:42 hrs) and 1703 samples in the phase 1 test set (8:01:11 hrs).

    <> notation is present throughout the train and test sets where the there exists a word, but not intelligible (due to noise, slurred speech, overlap etc). Newline operators (\n) are present only in the training data but not in the test ground truth files.

    The unicode of the validation (Phase 1 test set)/test (Phase 2 test set) dataset ground truth is normalized using bnunicodenormalizer.


Files
- id - wav file name. (lorem1.wav)
- sentence - transcript of file.



# Audio Transcribe
This notebook refers to audio transcription of diffrerent regional dialects for Bengali Language. I have participated in this contest and applied **tugstugi** model inference for audio transcription.

Notebook Link: https://www.kaggle.com/code/biplabkumarsarkar/asr-for-regional-dialects
Dataset Link: https://www.kaggle.com/competitions/ben10/data
