---
layout: page
title: common/crackle (English)
description: "Crack and decrypt Bluetooth Low Energy (BLE) encryption."
content_hash: 11e62e9c8fa8616988fc660f4a8a119f991da982
last_modified_at: 2024-08-11
tldri18n_status: 2
---
# crackle

Crack and decrypt Bluetooth Low Energy (BLE) encryption.
More information: <https://github.com/mikeryan/crackle>.

- Check whether the recorded BLE communications contain the packets necessary for recovering temporary keys (TKs):

`crackle -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pcap</span>

- Use brute force to recover the TK of the recorded pairing events and use it to decrypt all subsequent communications:

`crackle -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pcap</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/decrypted.pcap</span>

- Use the specified long-term key (LTK) to decrypt the recorded communication:

`crackle -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pcap</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/decrypted.pcap</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">81b06facd90fe7a6e9bbd9cee59736a7</span>
