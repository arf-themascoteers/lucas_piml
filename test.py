from evaluator import Evaluator
import spec_utils

if __name__ == "__main__":
    column_groups = [
        spec_utils.get_wavelengths() + ["savi"]
    ]
    algorithms = ["ann_savi_rev" for i in range(11)]
    alphas = [i/10 for i in range(11)]
    c = Evaluator(prefix="test", folds=10, algorithms=algorithms, column_groups=column_groups, alphas=alphas)
    c.process()