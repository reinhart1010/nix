---
layout: page
title: common/env (English)
description: "Show the environment or run a program in a modified environment."
content_hash: 754f1a401d47bc5f910ebecbc5ab64437d750b39
last_modified_at: 2024-01-31
related_topics:
  - title: français version
    url: /fr/common/env.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/env.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/env.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/env.html
    icon: bi bi-globe
tldri18n_status: 2
---
# env

Show the environment or run a program in a modified environment.
More information: <https://www.gnu.org/software/coreutils/env>.

- Show the environment:

`env`

- Run a program. Often used in scripts after the shebang (#!) for looking up the path to the program:

`env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Clear the environment and run a program:

`env -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Remove variable from the environment and run a program:

`env -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Set a variable and run a program:

`env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Set one or more variables and run a program:

`env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable1</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable2</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable3</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>
