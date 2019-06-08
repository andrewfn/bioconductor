#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Bioconductor Project"""
MAXROWS = 3 #1000
import sys
import os
import csv

genecells = {} # count of number of cells expressing a gene

def readfile(genes, cellnames, inputfile):
  with open(inputfile, 'rb') as tsv_file:
    reader = csv.reader(tsv_file, delimiter='\t') # one row per gene. Colums are cells
    row = next(reader)
    cellnames = row[1:] # get first row, ignoring first col
    genecount = 0
    for row in reader:
      genecount += 1
      genename = row[0]
      expressions = []
      foundincells = 0 # number of cells this gene is found in
      for expression in row[1:]: # convert from string to int
        expressions.append(int(expression))
        if expression != '0': foundincells += 1
      genes[genename] = expressions 
      genecells[genename] = genecells.get(genename, 0) + foundincells

    genecells[genename] = genecells.get(genename, 0) + foundincells
    print "Found", len(cellnames), " cells and ", genecount, " genes in file: ", inputfile

# Dictionaries of genes, conttaining a list of cell counts for each gene
genes_10 = {}
genes_11 = {}
genes_14 = {}
# List of cell names for each dictionary (first row of file), since they are not the same
cellnames_10 = []
cellnames_11 = []
cellnames_14 = []

readfile(genes_10, cellnames_10, 'GSM2861510_E115_Only_Cortical_Cells_DGE.txt')
readfile(genes_11, cellnames_11, 'GSM2861511_E135_Only_Cortical_Cells_DGE.txt')
readfile(genes_14, cellnames_14, 'GSM2861514_E175_Only_Cortical_Cells_DGE.txt')

for gene in genecells:
  if genecells[gene] < 3:
    print "Only ", genecells[gene] , " cells so deleting gene from dictionary:", gene
    try: del genes_10[gene]
    except KeyError: pass
    try: del genes_11[gene]
    except KeyError: pass
    try: del genes_14[gene]
    except KeyError: pass
