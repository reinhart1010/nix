---
layout: page
title: linux/mmcli (English)
description: "Control and monitor the ModemManager."
content_hash: 8409260624fafc3c32b8d54ce0f990460acdb936
---
# mmcli

Control and monitor the ModemManager.
More information: <https://www.freedesktop.org/software/ModemManager/man/latest/mmcli.1.html>.

- List SMS messages available on the modem:

`sudo mmcli --modem=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modem</span>` --messaging-list-sms`

- Delete a message from the modem, specifying its path:

`sudo mmcli --modem=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modem</span>` --messaging-delete-sms=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/message_file</span>
