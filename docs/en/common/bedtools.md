---
layout: page
title: common/bedtools (English)
description: "A swiss-army knife of tools for genomic-analysis tasks."
content_hash: e9d55a87982ae50a19bf47e2a3df6842707dccb8
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/common/bedtools.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bedtools.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bedtools

A swiss-army knife of tools for genomic-analysis tasks.
Used to intersect, group, convert and count data in BAM, BED, GFF/GTF, VCF format.
More information: <https://bedtools.readthedocs.io>.

- Intersect two files regarding the sequences' strand and save the result to the specified file:

`bedtools intersect -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>` -s > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Intersect two files with a left outer join, i.e. report each feature from `file1` and NULL if no overlap with `file2`:

`bedtools intersect -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>` -lof > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Using more efficient algorithm to intersect two pre-sorted files:

`bedtools intersect -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>` -sorted > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Group file `path/to/file` based on the first three and the fifth column and summarize the sixth column by summing it up:

`bedtools groupby -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -c 1-3,5 -g 6 -o sum`

- Convert bam-formatted file to a bed-formatted one:

`bedtools bamtobed -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bed</span>

- Find for all features in `file1.bed` the closest one in `file2.bed` and write their distance in an extra column (input files must be sorted):

`bedtools closest -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.bed</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.bed</span>` -d`
