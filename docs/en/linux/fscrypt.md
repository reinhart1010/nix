---
layout: page
title: linux/fscrypt (English)
description: "Go tool for managing Linux filesystem encryption."
content_hash: 447e058bde13ec27cc2910ed8375616bdd63b48c
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# fscrypt

Go tool for managing Linux filesystem encryption.
More information: <https://github.com/google/fscrypt>.

- Prepare the root filesystem for use with fscrypt:

`fscrypt setup`

- Enable filesystem encryption for a directory:

`fscrypt encrypt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Unlock an encrypted directory:

`fscrypt unlock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/encrypted_directory</span>

- Lock an encrypted directory:

`fscrypt lock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/encrypted_directory</span>
