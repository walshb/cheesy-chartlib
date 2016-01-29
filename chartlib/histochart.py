#!/usr/bin/python
#
# Copyright 2016 Ben Walsh
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
#
# $Header$

import sys
import datetime
import numpy as np
import matplotlib

matplotlib.use('Agg', warn=False)

import matplotlib.pyplot as plt
import matplotlib.dates
import logging


def plot(vs, filename, plot_legend=True):
    fig = plt.figure(figsize=(4, 4))    # matplotlib.figure.Figure
    ax = fig.add_subplot(111)    # matplotlib.axes.Axes

    n_bins = 20

    ax.hist(vs, n_bins)

    ax.grid(True)

    plt.savefig(filename)
    plt.close()    # Free memory!


def main():
    vs = [1, 1, 1, 2, 2, 3, \
          1, 1, 1, 2, 2, 3]

    plot(vs, 'test.png')

    return 0


if __name__ == '__main__':
    sys.exit(main())
