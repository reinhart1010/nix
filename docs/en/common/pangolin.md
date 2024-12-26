---
layout: page
title: common/pangolin (English)
description: "Implements the dynamic nomenclature of SARS-CoV-2 lineages (Pango nomenclature)."
content_hash: 08799e7724dd7df21c3eea7aabc5d783b058b9d8
last_modified_at: 2024-12-26
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pangolin.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pangolin

Implements the dynamic nomenclature of SARS-CoV-2 lineages (Pango nomenclature).
More information: <https://cov-lineages.org/resources/pangolin/usage.html>.

- Run `pangolin` on the specified FASTA file:

`pangolin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.fa</span>

- Use the specified analysis engine:

`pangolin --analysis-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">accurate|fast|pangolearn|usher</span>
