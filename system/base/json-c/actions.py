#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    options = "--disable-static \
               --enable-shared"

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

    autotools.configure(options)

def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "README", "ChangeLog", "AUTHORS", "NEWS")
