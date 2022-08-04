---
layout: page
title: common/make (English)
description: "Task runner for targets described in Makefile."
content_hash: 5a43c4fa813ae0a50a01bdb3b773ecaf6c85b202
related_topics:
  - title: 中文 version
    url: /zh/common/make.html
    icon: bi bi-globe
---
# make

Task runner for targets described in Makefile.
Mostly used to control the compilation of an executable from source code.
More information: <https://www.gnu.org/software/make/manual/make.html>.

- Call the first target specified in the Makefile (usually named "all"):

`make`

- Call a specific target:

`make `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>

- Call a specific target, executing 4 jobs at a time in parallel:

`make -j`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>

- Use a specific Makefile:

`make --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Execute make from another directory:

`make --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory</span>

- Force making of a target, even if source files are unchanged:

`make --always-make `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>

- Override a variable defined in the Makefile:

`make `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_value</span>

- Override variables defined in the Makefile by the environment:

`make --environment-overrides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>
