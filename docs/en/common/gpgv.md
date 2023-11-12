---
layout: page
title: common/gpgv (English)
description: "Verify OpenPGP signatures."
content_hash: 332bef5bca4a68c817f3b10e12e1ed6b2474e191
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/common/gpgv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gpgv

Verify OpenPGP signatures.
More information: <https://www.gnupg.org/documentation/manuals/gnupg/gpgv.html>.

- Verify a signed file:

`gpgv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Verify a signed file using a detached signature:

`gpgv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/signature</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Add a file to the list of keyrings (a single exported key also counts as a keyring):

`gpgv --keyring `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./alice.keyring</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/signature</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
