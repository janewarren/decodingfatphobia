# Decoding Fatphobia Source Code Repository

## Overview

This repository contains code and consolidated data for our research paper **Decoding Fatphobia: Examining Anti-Fat and Pro-Thin Bias in AI-Generated Images**, to appear in the _Findings of the Association for Computational Linguistics, NAACL 2025._

## Files Description

### generation.py
This script is responsible for generating images used in the study.

### requirements.txt
Contains a list of Python libraries required to run the code in this repository.

### table_combination.ipynb
A Jupyter notebook that:
1. Creates a consolidated dataset from individual rater files
2. Performs statistical analysis on the data
3. Generates plots and visualizations presented in the paper

## Directories

### images/
Contains plots generated by `table_combination.ipynb`.

### data/
Stores the raw data files:
- Individual Excel files for each rater's image ratings
- A consolidated final dataset combining all raters' assessments
- Instructions the raters followed

[Dataset Link](https://zenodo.org/records/13871977)
