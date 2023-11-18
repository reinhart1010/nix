---
layout: page
title: common/ppmtompeg (English)
description: "Encode an MPEG-1 stream."
content_hash: 8265a439946539b58477261e55b66e880cee820e
last_modified_at: 2023-11-18
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ppmtompeg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ppmtompeg

Encode an MPEG-1 stream.
More information: <https://netpbm.sourceforge.net/doc/ppmtompeg.html>.

- Produce an MPEG-1 stream using the parameter file to specify inputs and outputs:

`ppmtompeg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/parameter_file</span>

- Encode the GOP with the specified number only:

`ppmtompeg -gop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gop_num</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/parameter_file</span>

- Specify the first and last frame to encode:

`ppmtompeg -frames `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">first_frame</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">last_frame</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/parameter_file</span>

- Combine multiple MPEG frames into a single MPEG-1 stream:

`ppmtompeg -combine_frames `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/parameter_file</span>
