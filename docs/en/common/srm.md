---
layout: page
title: common/srm (English)
description: "Securely remove files or directories."
content_hash: f7b6c293b0ac6dd5978111a867575ada841a5b42
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# srm

Securely remove files or directories.
Overwrites the existing data one or multiple times. Drop in replacement for rm.
More information: <http://srm.sourceforge.net/srm.html>.

- Remove a file after a single-pass overwriting with random data:

`srm -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Remove a file after seven passes of overwriting with random data:

`srm -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Recursively remove a directory and its contents overwriting each file with a single-pass of random data:

`srm -r -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Prompt before every removal:

`srm -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\*</span>
