#!/usr/bin/env python
#
# Electrum - lightweight Bitcoin client
# Copyright (C) 2013 ecdsa@github
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import PyQt4.QtCore as QtCore
from electrum.i18n import _
from electrum import mnemonic
from qrcodewidget import QRCodeWidget

class SeedDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setModal(1)
        self.setWindowTitle('Electrum' + ' - ' + _('Seed'))


    def show_seed(self, seed, imported_keys, parent=None):

        brainwallet = ' '.join(mnemonic.mn_encode(seed))

        label1 = QLabel(_("Your wallet generation seed is")+ ":")

        seed_text = QTextEdit(brainwallet)
        seed_text.setReadOnly(True)
        seed_text.setMaximumHeight(130)
        
        msg2 =  _("Please write down or memorize these 12 words (order is important).") + " " \
              + _("This seed will allow you to recover your wallet in case of computer failure.") + " " \
              + _("Your seed is also displayed as QR code, in case you want to transfer it to a mobile phone.") + "<p>" \
              + "<b>"+_("WARNING")+":</b> " + _("Never disclose your seed. Never type it on a website.") + "</b><p>"
        if imported_keys:
            msg2 += "<b>"+_("WARNING")+":</b> " + _("Your wallet contains imported keys. These keys cannot be recovered from seed.") + "</b><p>"
        label2 = QLabel(msg2)
        label2.setWordWrap(True)

        logo = QLabel()
        logo.setPixmap(QPixmap(":icons/seed.png").scaledToWidth(56))
        logo.setMaximumWidth(60)

        qrw = QRCodeWidget(seed)

        ok_button = QPushButton(_("OK"))
        ok_button.setDefault(True)
        ok_button.clicked.connect(self.accept)

        grid = QGridLayout()
        #main_layout.addWidget(logo, 0, 0)

        grid.addWidget(logo, 0, 0)
        grid.addWidget(label1, 0, 1)

        grid.addWidget(seed_text, 1, 0, 1, 2)

        grid.addWidget(qrw, 0, 2, 2, 1)

        vbox = QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addWidget(label2)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(ok_button)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.exec_()
