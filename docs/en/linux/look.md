---
layout: page
title: linux/look (English)
description: "Display lines beginning with a prefix in a file."
content_hash: 2afc463ceb6ada22f5d1b528167a565044d27e02
last_modified_at: 2024-02-05
tldri18n_status: 2
---
# look

Display lines beginning with a prefix in a file.
NOTE: the lines in the file must be sorted.
See also: `grep`, `sort`.
More information: <https://manned.org/look>.

- Search for lines beginning with a specific prefix in a specific file:

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Case-insensitively search only on blank and alphanumeric characters:

`look -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f|-ignore-case</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">d|-alphanum</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Specify a string [t]ermination character (space by default):

`look -{t|-terminate} `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>

- Search in `/usr/share/dict/words` (`--ignore-case` and `--alphanum` are assumed):

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>

- Search in `/usr/share/dict/web2` (`--ignore-case` and `--alphanum` are assumed):

`look -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a|-alternative</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>
