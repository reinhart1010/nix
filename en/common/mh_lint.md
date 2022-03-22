---
layout: page
title: common/mh_lint (English)
description: "Attempt to find bugs in MATLAB or Octave code."
content_hash: e10e6a2a988e69d3464e33a8c6af53e9362900d3
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mh_lint

Attempt to find bugs in MATLAB or Octave code.
Please note that this tool is neither sound nor complete.
More information: <https://misshit.org>.

- Check the current directory:

`mh_lint`

- Check a specific directory recursively:

`mh_lint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Check a MATLAB file:

`mh_lint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.m</span>

- Check an Octave file:

`mh_lint --octave `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.m</span>
