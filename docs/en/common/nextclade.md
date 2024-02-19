---
layout: page
title: common/nextclade (English)
description: "Bioinformatics tool for virus genome alignment, clade assignment and qc checks."
content_hash: 435e831d33643c098617d8f7dbf10d59c231515d
last_modified_at: 2024-02-19
tldri18n_status: 2
---
# nextclade

Bioinformatics tool for virus genome alignment, clade assignment and qc checks.
More information: <https://docs.nextstrain.org/projects/nextclade/en/stable/user/nextclade-cli/index.html>.

- Align sequences to user provided [r]eference, [o]utputting the alignment to a file:

`nextclade run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/sequences.fa</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/reference.fa</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/alignment.fa</span>

- Create a [t]SV report, auto-downloading the latest [d]ataset:

`nextclade run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/fasta</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dataset_name</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/report.tsv</span>

- List all available datasets:

`nextclade dataset list`

- Download the latest SARS-CoV-2 dataset:

`nextclade dataset get --name sars-cov-2 --output-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Use a downloaded [D]ataset, producing all [O]utputs:

`nextclade run -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/dataset_dir</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_dir</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/sequences.fasta</span>

- Run on multiple files:

`nextclade run -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dataset_name</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_tsv</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_fasta_1 path/to/input_fasta_2 ...</span>

- Try reverse complement if sequence does not align:

`nextclade run --retry-reverse-complement -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dataset_name</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_tsv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_fasta</span>
