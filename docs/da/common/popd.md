---
layout: page
title: common/popd (dansk)
description: "Fjern en mappe placeret på mappe-stakken via den indbyggede shell-kommando `pushd`."
content_hash: a8d12584c55ea01ac64dd548b1fcf6e42068b16a
related_topics:
  - title: English version
    url: /en/common/popd.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># popd

Fjern en mappe placeret på mappe-stakken via den indbyggede shell-kommando `pushd`.
Se `pushd` for at placere en mappe på mappe-stakken og `dirs` for at vise indholdet af mappe-stakken.
Mere information: <https://www.gnu.org/software/bash/manual/html_node/Directory-Stack-Builtins.html>.

- Fjern den øverste mappe fra mappe-stakken og `cd` til mappen:

`popd`

- Fjern den N'te mappe (starter fra 0 fra venstre i den liste `dirs` printer):

`popd +N`

- Fjern den N'te mappe (starter fra 0 fra højre fra i liste `dirs` printer):

`popd -N`
