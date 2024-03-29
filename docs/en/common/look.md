---
layout: page
title: common/look (English)
description: "Display lines beginning with a prefix in a sorted file."
content_hash: 2067c2fe2d20c0bbfdcea94c75fb16b2b4e78fcb
last_modified_at: 2024-02-05
tldri18n_status: 2
---
# look

Display lines beginning with a prefix in a sorted file.
Note: the lines in the file must be sorted.
See also: `grep`, `sort`.
More information: <https://man.openbsd.org/look>.

- Search for lines beginning with a specific prefix in a specific file:

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Case-insensitively ([f]) search only on alphanumeric characters ([d]):

`look -f -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Specify a string [t]ermination character (space by default):

`look -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>

- Search in `/usr/share/dict/words` (`-d` and `-f` are assumed):

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>
