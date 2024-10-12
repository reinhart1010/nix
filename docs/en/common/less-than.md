---
layout: page
title: common/less-than (English)
description: "Redirect data to `stdin`."
content_hash: 48c706545ccd584cfb5340b9258f4b7878301090
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# Less than

Redirect data to `stdin`.
More information: <https://gnu.org/software/bash/manual/bash.html#Redirecting-Input>.

- Redirect a file to `stdin` (achieves the same effect as `cat file.txt |`):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Create a here document and pass that into `stdin` (requires a multiline command):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` << `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">EOF</span>` <Enter> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">multiline_data</span>` <Enter> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">EOF</span>

- Create a here string and pass that into `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` <<< `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>
