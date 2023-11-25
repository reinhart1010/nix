---
layout: page
title: common/thinkjettopbm (English)
description: "Convert a HP ThinkJet printer commands file to a PBM file."
content_hash: 2ee37ff128d3315d73885a44dac46b65c7d40ec8
last_modified_at: 2023-11-25
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/thinkjettopbm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># thinkjettopbm

Convert a HP ThinkJet printer commands file to a PBM file.
More information: <https://netpbm.sourceforge.net/doc/thinkjettopbm.html>.

- Convert a HP ThinkJet printer commands file to a PBM file:

`thinkjettopbm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pbm</span>

- Print debug information to `stderr`:

`thinkjettopbm -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pbm</span>
