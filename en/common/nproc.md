---
layout: page
title: common/nproc (English)
description: "Print the number of processing units (normally CPUs) available."
content_hash: f48a356d7714ffeac53c805d690a937232e50e1f
---
# nproc

Print the number of processing units (normally CPUs) available.
More information: <https://www.gnu.org/software/coreutils/nproc>.

- Display the number of available processing units:

`nproc`

- Display the number of installed processing units, including any inactive ones:

`nproc --all`

- If possible, subtract a given number of units from the returned value:

`nproc --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>
