---
layout: page
title: common/for (English)
description: "Shell loop over parameters."
content_hash: 4f0fadc1ce7cc0b6bc2cb113602bdc59156b24a6
---
# for

Shell loop over parameters.
More information: <https://man.archlinux.org/man/for.n>.

- Perform a command with different arguments:

`for argument in 1 2 3; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command $argument</span>`; done`

- Perform a command in every directory:

`for d in *; do (cd $d; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`); done`
