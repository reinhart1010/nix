---
layout: page
title: common/gpg2 (English)
description: "GNU Privacy Guard 2."
content_hash: 87449cddef6b166db83a880d02a1325e5caa2004
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/gpg2.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/gpg2.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gpg2

GNU Privacy Guard 2.
See `gpg` for GNU Privacy Guard 1.
More information: <https://docs.releng.linuxfoundation.org/en/latest/gpg.html>.

- List imported keys:

`gpg2 --list-keys`

- Encrypt a specified file for a specified recipient, writing the output to a new file with `.gpg` appended:

`gpg2 --encrypt --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/doc.txt</span>

- Encrypt a specified file with only a passphrase, writing the output to a new file with `.gpg` appended:

`gpg2 --symmetric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/doc.txt</span>

- Decrypt a specified file, writing the result to `stdout`:

`gpg2 --decrypt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/doc.txt.gpg</span>

- Import a public key:

`gpg2 --import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/public_key.gpg</span>

- Export the public key of a specified email address to `stdout`:

`gpg2 --export --armor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>

- Export the private key with a specified email address to `stdout`:

`gpg2 --export-secret-keys --armor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>
