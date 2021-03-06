#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-maintainer-mode \
                         --enable-fts \
                         --enable-datahub \
                         --enable-telepathy \
                         --enable-downloads-monitor \
                         --enable-explain-queries")
def build():
    autotools.make("LC_ALL=en_US.UTF-8")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPY*", "README", "ChangeLog", "NEWS", "AUTHORS")
