# ========================================================================
# Copyright 2020 Emory University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========================================================================
from collections import Counter
from typing import List, Tuple, Dict, Any


def read_data(filename: str):
    data, sentence = [], []
    fin = open(filename)

    for line in fin:
        l = line.split()
        if l:
            sentence.append((l[0], l[1]))
        else:
            data.append(sentence)
            sentence = []

    return data


def to_probs(model: Dict[Any, Counter]) -> Dict[str, List[Tuple[str, float]]]:
    probs = dict()
    for feature, counter in model.items():
        ts = counter.most_common()
        total = sum([count for _, count in ts])
        probs[feature] = [(label, count/total) for label, count in ts]
    return probs


def evaluate(data: List[List[Tuple[str, str]]], *args):
    total, correct = 0, 0
    for sentence in data:
        tokens, gold = tuple(zip(*sentence))
        pred = [t[0] for t in predict(tokens, args)]
        total += len(tokens)
        correct += len([1 for g, p in zip(gold, pred) if g == p])
    accuracy = 100.0 * correct / total
    return accuracy


def train(data: List[List[Tuple[str, str]]]) -> Tuple:
    """
    :param data: a list of tuple lists where each inner list represents a sentence and every tuple is a (word, pos) pair.
    :return: a tuple of a variable number of models
    """
    # TODO: to be updated
    # e.g., returned tuple = (cw_dict, pp_dict, pw_dict, nw_dict)
    return tuple()


def predict(tokens: List[str], *args) -> List[Tuple[str, float]]:
    """
    :param tokens: a list of tokens.
    :param args: a variable number of arguments
    :return: a list of tuple where each tuple represents a pair of (POS, score) of the corresponding token.
    """
    # TODO: to be updated
    return [('XX', 0) for _ in range(len(tokens))]


def experiment(trn_data: List[List[Tuple[str, str]]], dev_data: List[List[Tuple[str, str]]]) -> Tuple:
    """
    :param trn_data: the training set
    :param dev_data: the development set
    :return: a tuple of all parameters necessary to perform part-of-speech tagging
    """
    # TODO: to be updated
    return ()

if __name__ == '__main__':
    path = 'cs329/dat/pos/'
    trn_data = read_data(path + 'wsj-pos.trn.gold.tsv')
    dev_data = read_data(path + 'wsj-pos.dev.gold.tsv')
    experiment(trn_data, dev_data)
