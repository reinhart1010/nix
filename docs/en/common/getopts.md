---
layout: page
title: common/getopts (English)
description: "Parse shell options from arguments."
content_hash: ec2f26abf74628e56b04f728ef923d329637afb5
last_modified_at: 2024-12-26
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/getopts.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># getopts

Parse shell options from arguments.
This command does not support longform options and thus using `getopt` is recommended instead.
More information: <https://www.gnu.org/software/bash/manual/bash.html#index-getopts>.

- Check if an option is set:

`getopts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opt</span>`; echo $opt`

- Set an option to require an argument and check said argument:

`getopts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x</span>`: `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opt</span>`; echo $OPTARG`

- Check for multiple options:

`while getopts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xyz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opt</span>`; do case $opt in x) echo x is set;; y) echo y is set;; z) echo z is set;; esac; done`

- Set `getopts` to silent mode and handle option errors:

`while getopts :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x:</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opt</span>`; do case $opt in x) ;; :) echo "Argument required";; ?) echo "Invalid argument" esac;; done`

- Reset `getopts`:

`OPTIND=1`
