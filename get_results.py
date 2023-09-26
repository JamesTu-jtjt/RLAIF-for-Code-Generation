# coding: utf-8
import sys
import jsonlines
import json
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Run a trained model to generate Python code for the MBPP benchmark."
    )

    
    parser.add_argument(
        "--task_id",
        type=int,
        default=11,
    )
    args = parser.parse_args()
    return args


def get_result(args):
    filename = "results_350M/mbpp_task" + str(args.task_id) + ".txt"
    with open(filename, "r") as fp:
        tmpD = json.load(fp)
        fp.close()
    file2 = "results_FT/mbpp_task" + str(args.task_id) + ".txt"
    with open(file2, "r") as fp2:
        tmpD2 = json.load(fp2)
        fp2.close()
    print("Prompt: ", tmpD['prompt'])
    print("Completion: ", tmpD['completions'])
    print("-----------------------------------------------------------")
    print("Completion: ", tmpD2['completions'])
    
if __name__ == "__main__":
    
    args = parse_args()
    get_result(args)