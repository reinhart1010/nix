---
layout: page
title: linux/blastp (English)
description: "Protein-Protein BLAST."
content_hash: 5eda3f8f451221202d2d240a18b666675df9e13c
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# blastp

Protein-Protein BLAST.
More information: <https://www.ncbi.nlm.nih.gov/books/NBK279684/table/appendices.T.blastp_application_options/>.

- Align two or more sequences using blastp, with the e-value threshold of 1e-9, pairwise output format, output to screen:

`blastp -query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query.fa</span>` -subject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subject.fa</span>` -evalue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1e-9</span>

- Align two or more sequences using blastp-fast:

`blastp -task blastp-fast -query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query.fa</span>` -subject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subject.fa</span>

- Align two or more sequences, custom tabular output format, output to file:

`blastp -query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query.fa</span>` -subject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subject.fa</span>` -outfmt '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6 qseqid qlen qstart qend sseqid slen sstart send bitscore evalue pident</span>`' -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.tsv</span>

- Search protein databases using a protein query, 16 threads to use in the BLAST search, with a maximum number of 10 aligned sequences to keep:

`blastp -query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query.fa</span>` -db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blast_database_name</span>` -num_threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>` -max_target_seqs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Search the remote non-redundant protein database using a protein query:

`blastp -query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query.fa</span>` -db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nr</span>` -remote`

- Display help (use `-help` for detailed help):

`blastp -h`
