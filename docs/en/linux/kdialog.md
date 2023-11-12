---
layout: page
title: linux/kdialog (English)
description: "Show KDE dialog boxes from within shell scripts."
content_hash: a03df8f53b67a1f5fa436cdb93c5f67946f491d9
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# kdialog

Show KDE dialog boxes from within shell scripts.
More information: <https://develop.kde.org/deploy/kdialog/>.

- Open a dialog box displaying a specific message:

`kdialog --msgbox "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optional_detailed_message</span>`"`

- Open a question dialog with a `yes` and `no` button, returning `0` and `1`, respectively:

`kdialog --yesno "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`"`

- Open a warning dialog with a `yes`, `no`, and `cancel` button, returning `0`, `1`, or `2` respectively:

`kdialog --warningyesnocancel "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`"`

- Open an input dialog box and print the input to `stdout` when `OK` is pressed:

`kdialog --inputbox "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optional_default_text</span>`"`

- Open a dialog to prompt for a specific password and print it to `stdout`:

`kdialog --password "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`"`

- Open a dialog containing a specific dropdown menu and print the selected item to `stdout`:

`kdialog --combobx "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">item1</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">item2</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">...</span>`"`

- Open a file chooser dialog and print the selected file's path to `stdout`:

`kdialog --getopenfilename`

- Open a progressbar dialog and print a DBUS reference for communication to `stdout`:

`kdialog --progressbar "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`"`
