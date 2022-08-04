---
layout: page
title: common/help2man (English)
description: "Produce simple man pages from an executable's `--help` and `--version` output."
content_hash: e5954f45e1f3afcd6a9dedf1439d8a232744a87b
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

- Output to a file instead of stdout:

`help2man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display detailed help:

`help2man --help`
