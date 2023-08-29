---
layout: page
title: common/checksec (English)
description: "Check security properties of executables."
content_hash: 80e01b56c7bd67b191c9ba52fec23b4b569f754e
last_modified_at: 2023-08-29
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># checksec

Check security properties of executables.
More information: <https://github.com/slimm609/checksec.sh>.

- List security properties of an executable binary file:

`checksec --file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- List security properties recursively of all executable files in a directory:

`checksec --dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- List security properties of a process:

`checksec --proc=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- List security properties of the running kernel:

`checksec --kernel`
