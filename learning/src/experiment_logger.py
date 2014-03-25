#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function
import json


# log the data associated with ML experiments
class ExperimentLogger:
    def __init__(self, log_file):
        self.log_file_name = log_file
#         self.features = []
        self.dropped_features = []
        self.predictions = []
        
        # map the numpy rows to the instances that actually were selected
        self.test_data_row_map = {}
#         self.train_data_row_map = []
        
    def write_log(self):
        print("log file name is: " + self.log_file_name)
        output = open(self.log_file_name, 'w')

        output.write("ALL FEATURES\n")
        feats_str = json.dumps(self.features)
        output.write(feats_str + '\n')

        output.write("DROPPED FEATURES\n")
        dropped_feats_str = json.dumps(self.dropped_features)
        output.write(dropped_feats_str + '\n')

        sorted_predictions = self.sort_predictions_by_error()
        output.write("PREDICTIONS\n")
        for prediction in sorted_predictions:
            output.write(json.dumps(prediction) + '\n')
            
        output.close()

    # sort the predictions by the severity of the classifier error (adds an 'error' field)
    def sort_predictions_by_error(self):
        predictions = self.predictions
        predictions_with_error = []
        for p in predictions:
            p['error'] = abs(p['predicted_value'] - p['actual_value'])
            predictions_with_error.append(p)
        return sorted(predictions, key=lambda x: x['error'], reverse=True)

    def map_predictions_to_row_indices(self, ml_predictions, actual_values):
        assert(len(self.test_data_row_map.keys()) == len(ml_predictions))
        predictions = []
        for idx, prediction in enumerate(ml_predictions):
            predictions.append({'instance': self.test_data_row_map[idx], 'predicted_value': prediction, 'actual_value': actual_values[idx] })
            
        return predictions
        
#     def write(self, data):
#         self.output.write(data + '\n')
        