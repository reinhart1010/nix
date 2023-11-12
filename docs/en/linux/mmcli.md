---
layout: page
title: linux/mmcli (English)
description: "Control and monitor the ModemManager."
content_hash: fe8ea4d026f395746bd639fbb302ed2441794830
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mmcli

Control and monitor the ModemManager.
More information: <https://www.freedesktop.org/software/ModemManager/man/latest/mmcli.1.html>.

- List available modems:

`mmcli --list-modems`

- Print information about a modem:

`mmcli --modem=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modem</span>

- Enable a modem:

`mmcli --modem=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modem</span>` --enable`

- List SMS messages available on the modem:

`sudo mmcli --modem=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modem</span>` --messaging-list-sms`

- Delete a message from the modem, specifying its path:

`sudo mmcli --modem=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modem</span>` --messaging-delete-sms=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/message_file</span>
