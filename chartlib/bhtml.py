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

# $Header$

import sys
import os

import linechart
import scatterchart

import logging

logger = logging.getLogger('root.' + __name__)

class HtmlDoc:
    def __init__(self, dirname):
        self.dirname = dirname
        self.html = []
        self.fnames = {}

        try:
            os.makedirs(self.dirname)
        except:
            pass


    def add(self, s):
        if isinstance(s, HtmlDoc):
            self.html.extend(s.html)
            return

        self.html.append(s)


    def add_line_chart(self, xys, file_prefix, **kwargs):
        fname = file_prefix + '.png'
        fpath = os.path.join(self.dirname, fname)

        assert fname not in self.fnames

        linechart.plot(xys, fpath, **kwargs)
        if not xys or len(xys[0][1]) == 0:
            logger.debug('fname = %s xys = %s' % (fname, xys))
        self.fnames[fname] = True

        self.add('<img src="%s">' % fname)


    def add_scatter_chart(self, xs, ys, file_prefix, **kwargs):
        fname = file_prefix + '.png'
        fpath = os.path.join(self.dirname, fname)

        assert fname not in self.fnames

        scatterchart.plot(xs, ys, fpath, **kwargs)
        self.fnames[fname] = True

        self.add('<img src="%s">' % fname)


    def write(self, fname='index.html'):
        fpath = os.path.join(self.dirname, fname)

        logger.debug('Writing %s' % fpath)

        f = open(fpath, 'w')
        f.write('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">\n')
        f.write('\n'.join(self.html).encode('utf-8'))
        f.write('\n')
        f.close()
