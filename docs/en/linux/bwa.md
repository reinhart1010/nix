---
layout: page
title: linux/bwa (English)
description: "Burrows-Wheeler Alignment tool."
content_hash: 2bc84351fc3bbeb0b482c9c1b988af79da427145
last_modified_at: 2024-05-14
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/bwa.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bwa

Burrows-Wheeler Alignment tool.
Short, low-divergent DNA sequences mapper against a large reference genome, such as the human genome.
More information: <https://github.com/lh3/bwa>.

- Index the reference genome:

`bwa index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/reference.fa</span>

- Map single-end reads (sequences) to indexed genome using 32 [t]hreads and compress the result to save space:

`bwa mem -t 32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/reference.fa</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/read_single_end.fq.gz</span>` | gzip > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/alignment_single_end.sam.gz</span>

- Map pair-end reads (sequences) to the indexed genome using 32 [t]hreads and compress the result to save space:

`bwa mem -t 32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/reference.fa</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/read_pair_end_1.fq.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/read_pair_end_2.fq.gz</span>` | gzip > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/alignment_pair_end.sam.gz</span>

- Map pair-end reads (sequences) to the indexed genome using 32 [t]hreads with [M]arking shorter split hits as secondary for output SAM file compatibility in Picard software and compress the result:

`bwa mem -M -t 32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/reference.fa</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/read_pair_end_1.fq.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/read_pair_end_2.fq.gz</span>` | gzip > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/alignment_pair_end.sam.gz</span>

- Map pair-end reads (sequences) to indexed genome using 32 [t]hreads with FASTA/Q [C]omments (e.g. BC:Z:CGTAC) appending to a compressed result:

`bwa mem -C -t 32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/reference.fa</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/read_pair_end_1.fq.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/read_pair_end_2.fq.gz</span>` | gzip > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/alignment_pair_end.sam.gz</span>
