from ann_simple import ANNSimple
from ann_savi_rev import ANNSAVIRev


def get_ann_by_name(algorithm):
    if algorithm == "ann_simple":
        return ANNSimple
    if algorithm == "ann_savi_rev":
        return ANNSAVIRev


