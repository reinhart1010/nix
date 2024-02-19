---
layout: page
title: common/bedtools (English)
description: "A swiss-army knife of tools for genomic-analysis tasks."
content_hash: 418e688bdc15d0ce75e5432c8e91c97202a6f9dd
last_modified_at: 2024-02-19
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

- Intersect file [a] and file(s) [b] regarding the sequences' [s]trand and save the result to a specific file:

`bedtools intersect -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_A</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_B1 path/to/file_B2 ...</span>` -s > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Intersect two files with a [l]eft [o]uter [j]oin, i.e. report each feature from `file1` and NULL if no overlap with `file2`:

`bedtools intersect -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>` -loj > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Using more efficient algorithm to intersect two pre-sorted files:

`bedtools intersect -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>` -sorted > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- [g]roup a file based on the first three and the fifth [c]olumn and apply the sum [o]peration on the sixth column:

`bedtools groupby -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -c 1-3,5 -g 6 -o sum`

- Convert bam-formatted [i]nput file to a bed-formatted one:

`bedtools bamtobed -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bed</span>

- Find for all features in `file1.bed` the closest one in `file2.bed` and write their [d]istance in an extra column (input files must be sorted):

`bedtools closest -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.bed</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.bed</span>` -d`
