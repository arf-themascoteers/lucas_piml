from ann_simple import ANNSimple
from ann_simple_10 import ANNSimple10
from ann_simple_sum import ANNSimpleSum
from ann_savi_rev import ANNSAVIRev


def get_ann_by_name(algorithm):
    if algorithm == "ann_simple":
        return ANNSimple
    elif algorithm == "ann_simple_10":
        return ANNSimple10
    elif algorithm == "ann_simple_sum":
        return ANNSimpleSum
    elif algorithm == "ann_savi_rev":
        return ANNSAVIRev


