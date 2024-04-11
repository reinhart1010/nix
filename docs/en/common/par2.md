---
layout: page
title: common/par2 (English)
description: "File verification and repair using PAR 2.0 compatible parity archives (.par2 files)."
content_hash: 93e19e1cbdd96e1ac9cb72b376ded0bbf28fdcd9
last_modified_at: 2024-04-11
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/par2.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># par2

File verification and repair using PAR 2.0 compatible parity archives (.par2 files).
More information: <https://github.com/Parchive/par2cmdline/>.

- Create a parity archive with a set percentage level of redundancy:

`par2 create -r`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1..100</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Create a parity archive with a chosen number of volume files (in addition to the index file):

`par2 create -n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1..32768</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Verify a file with a parity archive:

`par2 verify -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.par2</span>

- Repair a file with a parity archive:

`par2 repair -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.par2</span>
