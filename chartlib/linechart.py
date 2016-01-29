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


def plot(xys, filename, plot_legend=True, width=3.5, fancy_func=None):
    """Takes an array of (legend, xs, ys) tuples"""

    size_x = width
    size_y = 4.0 + (plot_legend and 0.3 * float(len(xys)) or 0.0)

    fig = plt.figure(figsize=(size_x, size_y))    # matplotlib.figure.Figure

    top_height = 3.5 / size_y

    ax = fig.add_axes((0.1, 1.0 - 0.9 * top_height, 0.8, 0.8 * top_height))    # matplotlib.axes.Axes

    lines = []
    texts = []
    for (legend_text, xs, ys) in xys:
##        logging.debug('Plotting %s %s' % (legend_text, len(xs)))
        if len(xs) <= 1:
            continue

        try:
            plot_lines = ax.plot(xs, ys)
        except ValueError, e:
            logging.error('xs = %s' % repr(xs))
            logging.error('ys = %s' % repr(ys))
            raise e

        if legend_text and plot_legend:
            lines.extend(plot_lines)
            texts.append(legend_text)

    if len(xs) > 0 and isinstance(xs[0], datetime.datetime):
        if xs[-1] - xs[0] < datetime.timedelta(days=1):
            time_fmt = matplotlib.dates.DateFormatter('%H:%M:%S')
            time_locator = matplotlib.dates.HourLocator()    # every hour
        else:
            time_fmt = matplotlib.dates.DateFormatter('%Y%m%d')
            if xs[-1] - xs[0] < datetime.timedelta(days=31):
                time_locator = matplotlib.dates.DayLocator()
            else:
                time_locator = matplotlib.dates.MonthLocator()

        # format the ticks
        ax.xaxis.set_major_locator(time_locator)

##ax.xaxis.set_major_locator(years)
        ax.xaxis.set_major_formatter(time_fmt)
##ax.xaxis.set_minor_locator(months)

##datemin = datetime.date(r.date.min().year, 1, 1)
##datemax = datetime.date(r.date.max().year+1, 1, 1)
##ax.set_xlim(datemin, datemax)

### format the coords message box
##def price(x): return '$%1.2f'%x

        ax.format_xdata = time_fmt
##ax.format_ydata = price

    ax.grid(True)

    if fancy_func:
        fancy_func(ax)

    # rotates and right aligns the x labels, and moves the bottom of the
    # axes up to make room for them
    fig.autofmt_xdate()

    ax2 = fig.add_axes((0.0, 0.0, 1.0, 0.9 * (1.0 - top_height)), frameon=False)
    ax2.xaxis.set_visible(False)
    ax2.yaxis.set_visible(False)

    if texts:
##        leg = fig.legend(lines, texts, loc=1, \
##                         bbox_to_anchor=(0, 0, 1.0, 0))
        leg = ax2.legend(lines, texts, mode='expand', borderaxespad=0.0)


        for t in leg.get_texts():
            t.set_fontsize('small')

##    plt.show()

    plt.savefig(filename)
    plt.close()    # Free memory!


def main():
    text = 'hello'

    xs = [datetime.datetime(2010, 1, 1, 12, 0, 0), \
          datetime.datetime(2010, 1, 1, 14, 0, 0), \
          datetime.datetime(2010, 1, 1, 15, 0, 0)]

    ys = [6.0, 8.0, 3.0]

    plot([(text, xs, ys)], '/tmp/foo.png')

    xs = [12, 14, 15]

##    plot([(text, xs, ys)])

    return 0


if __name__ == '__main__':
    sys.exit(main())
