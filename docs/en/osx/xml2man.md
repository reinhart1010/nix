---
layout: page
title: osx/xml2man (English)
description: "Compile MPGL to mdoc."
content_hash: 306bfe2d71626e8c01c7c22db7b146a6fb2bc6d6
last_modified_at: 2023-02-20
---
# xml2man

Compile MPGL to mdoc.
More information: <https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/HeaderDoc/mpgl/mpgl.html>.

- Compile an MPGL file to a viewable man page:

`xml2man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/command_file.mxml</span>

- Compile an MPGL file to a specific output file:

`xml2man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/service_file.mxml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/service_file.7</span>

- Compile an MPGL file to a specific output file, overwriting if it already exists:

`xml2man -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/function_file.mxml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/function_file.3</span>
