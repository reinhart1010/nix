---
layout: page
title: common/samtools (English)
description: "Tools for handling high-throughput sequencing (genomics) data."
content_hash: e24589afc8217dfbbcea5c3c6ee630f2c1903bb8
last_modified_at: 2022-12-04
---
# samtools

Tools for handling high-throughput sequencing (genomics) data.
Used for reading/writing/editing/indexing/viewing of data in SAM/BAM/CRAM format.
More information: <https://www.htslib.org>.

- Convert a SAM input file to BAM stream and save to file:

`samtools view -S -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.sam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.bam</span>

- Take input from `stdin` (-) and print the SAM header and any reads overlapping a specific region to `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">other_command</span>` | samtools view -h - chromosome:start-end`

- Sort file and save to BAM (the output format is automatically determined from the output file's extension):

`samtools sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.bam</span>

- Index a sorted BAM file (creates `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sorted_input.bam.bai</span>`):

`samtools index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sorted_input.bam</span>

- Print alignment statistics about a file:

`samtools flagstat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sorted_input</span>

- Count alignments to each index (chromosome / contig):

`samtools idxstats `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sorted_indexed_input</span>

- Merge multiple files:

`samtools merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input1 input2 …</span>

- Split input file according to read groups:

`samtools split `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">merged_input</span>
