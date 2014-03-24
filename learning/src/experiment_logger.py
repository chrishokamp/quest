#!/usr/bin/env python
# encoding: utf-8


# log the data associated with ML experiments
class ExperimentLogger:
    def __init__(self, log_file):
        self.output = open(log_file, 'w')
        self.features = []
        self.dropped_features = []
        
        # map the numpy rows to the instances that actually were selected
        self.test_data_row_map = {}
#         self.train_data_row_map = []
        
        
    def write_log(self):
        self.output.write('')
        
    def map_predictions_to_row_indices(self, ml_predictions, actual_values):
        assert(len(self.test_data_row_map.keys()) == len(ml_predictions))
        predictions = []
        for idx, prediction in enumerate(ml_predictions):
            predictions.append({'instance': self.test_data_row_map[idx], 'predicted_value': prediction, 'actual_value': actual_values[idx] })
            
        return predictions
        
#     def write(self, data):
#         self.output.write(data + '\n')
        