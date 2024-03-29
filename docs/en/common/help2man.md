---
layout: page
title: common/help2man (English)
description: "Produce simple man pages from an executable's `--help` and `--version` output."
content_hash: 8f61bffea0c327e54a757a2404bb63db9e9c1654
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# help2man

Produce simple man pages from an executable's `--help` and `--version` output.
More information: <https://www.gnu.org/software/help2man>.

- Generate a man page for an executable:

`help2man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable</span>

- Specify the "name" paragraph in the man page:

`help2man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Specify the section for the man page (defaults to 1):

`help2man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable</span>` --section `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">section</span>

- Output to a file instead of `stdout`:

`help2man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display help:

`help2man --help`
