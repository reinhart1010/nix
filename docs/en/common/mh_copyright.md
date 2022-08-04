---
layout: page
title: common/mh_copyright (English)
description: "Adjust copyright headers for MATLAB or Octave code."
content_hash: 0f30e8532c01e99eade5abc8ad086667f2e3d847
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mh_copyright

Adjust copyright headers for MATLAB or Octave code.
More information: <https://misshit.org>.

- Update the year (range) to include the current year for the specified files:

`mh_copyright --primary-entity="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">entity</span>`" --update-year `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1.m path/to/file_or_director2.m ...</span>

- Update the year (range) to include the current year for all files:

`mh_copyright --primary-entity="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">entity</span>`" --update-year`
