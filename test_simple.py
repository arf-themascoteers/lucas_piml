from evaluator import Evaluator
import spec_utils

if __name__ == "__main__":
    column_groups = [
        spec_utils.get_wavelengths()
    ]
    algorithms = ["ann_simple"]
    alphas = [0]
    c = Evaluator(prefix="test_simple", folds=10, algorithms=algorithms, column_groups=column_groups, alphas=alphas)
    c.process()