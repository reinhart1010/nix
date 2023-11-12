---
layout: page
title: common/gpg-zip (English)
description: "Encrypt files and directories in an archive using GPG."
content_hash: 55b253f4a20874148b183ee09d0b7d10306e97ad
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/common/gpg-zip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gpg-zip

Encrypt files and directories in an archive using GPG.
More information: <https://www.gnupg.org/documentation/manuals/gnupg/gpg_002dzip.html>.

- Encrypt a directory into `archive.gpg` using a passphrase:

`gpg-zip --symmetric --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.gpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Decrypt `archive.gpg` into a directory of the same name:

`gpg-zip --decrypt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.gpg</span>

- List the contents of the encrypted `archive.gpg`:

`gpg-zip --list-archive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.gpg</span>
