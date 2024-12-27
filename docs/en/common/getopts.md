---
layout: page
title: common/getopts (English)
description: "Parse shell options from arguments."
content_hash: ec2f26abf74628e56b04f728ef923d329637afb5
last_modified_at: 2024-12-27
tldri18n_status: 2
---
# getopts

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
