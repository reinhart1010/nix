---
layout: page
title: common/gpg (English)
description: "GNU Privacy Guard."
content_hash: ce60f94e12daaa3d5eaafdc33e99dc5b120c3532
related_topics:
  - title: Deutsch version
    url: /de/common/gpg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/gpg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/gpg.html
    icon: bi bi-globe
---
# gpg

GNU Privacy Guard.
See `gpg2` for GNU Privacy Guard 2.
More information: <https://gnupg.org>.

- Create a GPG public and private key interactively:

`gpg --full-generate-key`

- Sign `doc.txt` without encryption (writes output to `doc.txt.asc`):

`gpg --clearsign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt</span>

- Encrypt `doc.txt` for alice@example.com (output to `doc.txt.gpg`):

`gpg --encrypt --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt</span>

- Encrypt `doc.txt` with only a passphrase (output to `doc.txt.gpg`):

`gpg --symmetric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt</span>

- Decrypt `doc.txt.gpg` (output to stdout):

`gpg --decrypt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt.gpg</span>

- Import a public key:

`gpg --import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">public.gpg</span>

- Export public key for alice@example.com (output to stdout):

`gpg --export --armor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>

- Export private key for alice@example.com (output to stdout):

`gpg --export-secret-keys --armor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>
