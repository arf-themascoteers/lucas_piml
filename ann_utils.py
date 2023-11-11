from ann_simple import ANNSimple
from ann_simple_10 import ANNSimple10
from ann_simple_sum import ANNSimpleSum
from ann_simple_10_sum import ANNSimple10Sum
from ann_simple_100_sum import ANNSimple100Sum
from ann_simple_1000_sum import ANNSimple1000Sum
from ann_savi_rev import ANNSAVIRev


def get_ann_by_name(algorithm):
    if algorithm == "ann_simple":
        return ANNSimple
    elif algorithm == "ann_simple_10":
        return ANNSimple10
    elif algorithm == "ann_simple_sum":
        return ANNSimpleSum
    elif algorithm == "ann_simple_10_sum":
        return ANNSimple10Sum
    elif algorithm == "ann_simple_100_sum":
        return ANNSimple100Sum
    elif algorithm == "ann_simple_1000_sum":
        return ANNSimple1000Sum
    elif algorithm == "ann_savi_rev":
        return ANNSAVIRev


