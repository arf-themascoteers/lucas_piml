from evaluator import Evaluator
import spec_utils

if __name__ == "__main__":
    column_groups = [
        spec_utils.get_wavelengths()
    ]
    algorithms = ["ann_simple","ann_simple_10_sum","ann_simple_100_sum","ann_simple_1000_sum"]
    alphas = [0,0,0,0]
    c = Evaluator(prefix="ann_simple_lr", folds=10, algorithms=algorithms, column_groups=column_groups, alphas=alphas)
    c.process()