---
layout: page
title: common/lsar (English)
description: "List an archive file's contents."
content_hash: a0deefcaf6c3d8cabf49f799e2a4c740a32c951b
last_modified_at: 2024-05-16
tldri18n_status: 2
---
# lsar

List an archive file's contents.
See also: `unar`, `ar`.
More information: <https://manned.org/lsar>.

- List an archive file's contents:

`lsar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive</span>

- List a password protected archive file's contents:

`lsar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Print al[L] available information about each file in the archive (it's very long):

`lsar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-L|--verylong</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive</span>

- Test the integrity of the files in the archive (if possible):

`lsar --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive</span>

- List the archive file's contents in JSON format:

`lsar --json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive</span>

- Display help:

`lsar --help`
