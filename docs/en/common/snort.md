---
layout: page
title: common/snort (English)
description: "Open-source network intrusion detection system."
content_hash: 053295de4125a68f43361ae8dab08e88006cac63
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# snort

Open-source network intrusion detection system.
More information: <https://www.snort.org/#documents>.

- Capture packets with verbose output:

`sudo snort -v -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- Capture packets and dump application layer data with verbose output:

`sudo snort -vd -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- Capture packets and display link layer packet headers with verbose output:

`sudo snort -ve -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- Capture packets and save them in the specified directory:

`sudo snort -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Capture packets according to rules and save offending packets along with alerts:

`sudo snort -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/rules.conf</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
