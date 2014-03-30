#!/usr/bin/env python
# encoding: utf-8
from __future__ import division

from itertools import groupby
from random import shuffle

# (1) - load source


def prep_cross_validation(sourcefile):
    groups = [] 
    uniquekeys = []
    with open(sourcefile, 'r') as lines:
        source_segs = lines.read().splitlines()
        source_tups = [(idx,seg) for idx,seg in enumerate(source_segs)]
        sorted_source = sorted(source_tups, key=lambda x: x[1])
        for k,g in groupby(sorted_source, key=lambda x: x[1]):
            groups.append(list(g))
            uniquekeys.append(k)
    
    # now shuffle
    shuffle(groups)

    # dump this splitting data to json
    splitsize = len(groups) // 10 
    # get 10 chunks
    chunks = [groups[i:i+splitsize] for i in range(0, len(groups), splitsize)]
    print(chunks)
    # get split indices
    split_indices = []
    current_index = 0
    row_keys = []
    for chunk in chunks:
        split_indices.append(current_index)
        flattened = [seg[0] for sublist in chunk for seg in sublist]

        row_keys = row_keys + flattened
        current_index += len(flattened)

    # output the structure:
    # flat index map
    # { index_order: [...,...], split_points: [index_1,...]}

    # flatten back into a list of keys
    #row_keys = [seg[0] for sublist in groups for seg in sublist]
    return row_keys,split_indices 
        
        
# BUFFER
# import sort_data
# sourcefile = '/home/chris/projects/quest-new/input/task1/en_de/source.en'
# keys,split_indices = sort_data.prep_cross_validation(sourcefile)
# TODO: serialize keys and split indices into json for each lang pair

# get the chunks
# chunks = [ keys[key[0]:key[1]] for key in zip(split_indices, split_indices[1:]) ]
# get the final chunk
# chunks.append(keys[split_indices[-1]:])

#        chunks = [ keys[key[0]:key[1]] for key in zip(keys, keys[:1]) ]