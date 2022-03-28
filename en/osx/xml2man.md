---
layout: page
title: osx/xml2man (English)
description: "Compile MPGL to mdoc."
content_hash: db81bfe9638ed51d9dbd62b79d9b5cb511cd48e8
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># xml2man

Compile MPGL to mdoc.
More information: <https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/HeaderDoc/mpgl/mpgl.html>.

- Compile an MPGL file to a viewable man page:

`xml2man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/command.mxml</span>

- Compile an MPGL file to a specific output file:

`xml2man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/service.mxml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/service.7</span>

- Compile an MPGL file to a specific output file, overwriting if it already exists:

`xml2man -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/function.mxml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/function.3</span>
