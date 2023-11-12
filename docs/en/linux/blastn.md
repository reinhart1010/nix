---
layout: page
title: linux/blastn (English)
description: "Nucleotide-Nucleotide BLAST."
content_hash: 0aa5afa9fc422c6c17b74858f159c8c26aae3f19
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# blastn

Nucleotide-Nucleotide BLAST.
More information: <https://www.ncbi.nlm.nih.gov/books/NBK279684/table/appendices.T.blastn_application_options/>.

- Align two or more sequences using megablast (default), with the e-value threshold of 1e-9, pairwise output format (default):

`blastn -query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query.fa</span>` -subject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subject.fa</span>` -evalue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1e-9</span>

- Align two or more sequences using blastn:

`blastn -task blastn -query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query.fa</span>` -subject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subject.fa</span>

- Align two or more sequences, custom tabular output format, output to file:

`blastn -query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query.fa</span>` -subject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subject.fa</span>` -outfmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'6 qseqid qlen qstart qend sseqid slen sstart send bitscore evalue pident'</span>` -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.tsv</span>

- Search nucleotide databases using a nucleotide query, 16 threads (CPUs) to use in the BLAST search, with a maximum number of 10 aligned sequences to keep:

`blastn -query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query.fa</span>` -db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/blast_db</span>` -num_threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>` -max_target_seqs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Search the remote non-redundant nucleotide database using a nucleotide query:

`blastn -query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query.fa</span>` -db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nt</span>` -remote`

- Display help (use `-help` for detailed help):

`blastn -h`
