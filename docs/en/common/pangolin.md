---
layout: page
title: common/pangolin (English)
description: "Implements the dynamic nomenclature of SARS-CoV-2 lineages (Pango nomenclature)."
content_hash: 08799e7724dd7df21c3eea7aabc5d783b058b9d8
last_modified_at: 2024-12-27
tldri18n_status: 2
---
# pangolin

Implements the dynamic nomenclature of SARS-CoV-2 lineages (Pango nomenclature).
More information: <https://cov-lineages.org/resources/pangolin/usage.html>.

- Run `pangolin` on the specified FASTA file:

`pangolin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.fa</span>

- Use the specified analysis engine:

`pangolin --analysis-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">accurate|fast|pangolearn|usher</span>
