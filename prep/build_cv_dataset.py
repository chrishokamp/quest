#!/usr/bin/env python
# encoding: utf-8
from __future__ import division

from itertools import groupby
from random import shuffle
import json

import sort_data
from argparse import ArgumentParser

import os
import sys

# (1) - load source

def serialize_cv_data(output_file, row_keys, split_indices):
    with open(output_file, 'w') as output:
        output.write(json.dumps({ "row_keys": row_keys, "split_indices": split_indices }))


def main(argv=None):
    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)
        
    try: 
        parser = ArgumentParser()
        parser.add_argument("-i", dest="input")
        parser.add_argument("-o", dest="output")
        
        args = parser.parse_args()
        
        sourcefile = args.input
        row_keys, split_indices = sort_data.prep_cross_validation(sourcefile)
        
        output = args.output
        serialize_cv_data(output, row_keys, split_indices)
    except KeyboardInterrupt:
        ### handle keyboard interrupt ###
        return 0

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

if __name__ == "__main__":
#     if DEBUG:
#         sys.argv.append("-v")

    sys.exit(main())