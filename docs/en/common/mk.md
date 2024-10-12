---
layout: page
title: common/mk (English)
description: "Task runner for targets described in Mkfile."
content_hash: b392641b91e16b4596bcaa853174f1f482aa328b
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# mk

Task runner for targets described in Mkfile.
Mostly used to control the compilation of an executable from source code.
More information: <https://doc.cat-v.org/plan_9/4th_edition/papers/mk>.

- Call the first target specified in the Mkfile (usually named "all"):

`mk`

- Call a specific target:

`mk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>

- Call a specific target, executing 4 jobs at a time in parallel:

`NPROC=4 mk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>

- Force mking of a target, even if source files are unchanged:

`mk -w`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>

- Assume all targets to be out of date. Thus, update `target` and all of its dependencies:

`mk -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>

- Keep going as far as possible on error:

`mk -k`
