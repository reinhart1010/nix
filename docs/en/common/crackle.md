---
layout: page
title: common/crackle (English)
description: "Crack and decrypt Bluetooth Low Energy (BLE) encryption."
content_hash: 11e62e9c8fa8616988fc660f4a8a119f991da982
last_modified_at: 2024-08-10
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/crackle.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># crackle

Crack and decrypt Bluetooth Low Energy (BLE) encryption.
More information: <https://github.com/mikeryan/crackle>.

- Check whether the recorded BLE communications contain the packets necessary for recovering temporary keys (TKs):

`crackle -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pcap</span>

- Use brute force to recover the TK of the recorded pairing events and use it to decrypt all subsequent communications:

`crackle -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pcap</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/decrypted.pcap</span>

- Use the specified long-term key (LTK) to decrypt the recorded communication:

`crackle -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pcap</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/decrypted.pcap</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">81b06facd90fe7a6e9bbd9cee59736a7</span>
