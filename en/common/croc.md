---
layout: page
title: common/croc (English)
description: "Send and receive files easily and securely over any network."
content_hash: 875aab589311ae41d8429c9d8bf65d72f521e4cd
---
# croc

Send and receive files easily and securely over any network.
More information: <https://github.com/schollz/croc>.

- Send a file or directory:

`croc send `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Send a file or directory with a specific passphrase:

`croc send --code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">passphrase</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Receive a file or directory on receiving machine:

`croc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">passphrase</span>

- Send and connect over a custom relay:

`croc --relay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_to_relay</span>` send `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Receive and connect over a custom relay:

`croc --relay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_to_relay</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">passphrase</span>

- Host a croc relay on the default ports:

`croc relay`

- Display parameters and options for a croc command:

`croc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">send|relay</span>` --help`
