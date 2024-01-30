---
layout: page
title: linux/phar (English)
description: "Create, update or extract PHP archives (PHAR)."
content_hash: 59a85df37a7fc1765ebcdc18e4f4c45233e9d8ac
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# phar

Create, update or extract PHP archives (PHAR).
More information: <https://manned.org/phar>.

- Add space-separated files or directories to a Phar file:

`phar add -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/phar_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">files_or_directories</span>

- Display the contents of a Phar file:

`phar list -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/phar_file</span>

- Delete the specified file or directory from a Phar file:

`phar delete -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/phar_file</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_or_directory</span>

- Compress or uncompress files and directories in a Phar file:

`phar compress -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/phar_file</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">algorithm</span>

- Get information about a Phar file:

`phar info -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/phar_file</span>

- Sign a Phar file with a specific hash algorithm:

`phar sign -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/phar_file</span>` -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">algorithm</span>

- Sign a Phar file with an OpenSSL private key:

`phar sign -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/phar_file</span>` -h openssl -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/private_key</span>

- Display help and available hashing/compression algorithms:

`phar help`
