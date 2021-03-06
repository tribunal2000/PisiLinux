#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("src/bluetooth.conf", '(group=")plugdev', r"\1removable")
    autotools.autoreconf("-fi")
    autotools.configure("--enable-network \
                         --enable-hid2hci \
                         --enable-serial \
                         --enable-input \
                         --enable-audio \
                         --enable-service \
                         --enable-gstreamer \
                         --enable-alsa \
                         --enable-usb \
                         --enable-tools \
                         --enable-bccmd \
                         --enable-dfutool \
                         --enable-cups \
                         --enable-hidd \
                         --enable-dund \
                         --enable-pand \
                         --enable-test \
                         --enable-pcmcia \
                         --with-systemdunitdir=/lib/systemd/system \
                         --with-ouifile=/usr/share/misc/oui.txt \
                         --enable-hid2hci \
                         --enable-wiimote \
                         --libexecdir=/lib")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Install conf files
    for i in ["audio", "input", "network"]:
        pisitools.insinto("/etc/bluetooth", "%s/%s.conf" % (i,i))

    # Simple test tools
    for i in ["test-adapter", "test-audio", "test-discovery",
              "test-health-sink", "test-manager", "test-network",
              "test-proximity", "test-serial", "test-service",
              "test-attrib", "test-device", "test-health", "test-input",
              "test-nap", "test-oob", "test-sap-server", "test-serial-proxy",
              "test-telephony", "test-thermometer", "monitor-bluetooth",
              "simple-agent", "simple-endpoint", "simple-player",
              "simple-service", "sap-client", "list-devices", "hsplay", "hsmicro"]:
        pisitools.dobin("test/%s" % i)

    # Additional tools
    pisitools.dosbin("tools/hcisecfilter")
    pisitools.dosbin("tools/ppporc")

    # Install documents
    pisitools.dodoc("AUTHORS", "ChangeLog", "README")
