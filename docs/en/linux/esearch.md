---
layout: page
title: linux/esearch (English)
description: "Perform a new Entrez search using terms in indexed fields."
content_hash: 4da9cc5516628746793a2467f200198d44790154
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# esearch

Perform a new Entrez search using terms in indexed fields.
It is part of the `edirect` package.
More information: <https://www.ncbi.nlm.nih.gov/books/NBK179288/>.

- Search the pubmed database for selective serotonin reuptake inhibitor:

`esearch -db pubmed -query "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">selective serotonin reuptake inhibitor</span>`"`

- Search the protein database using a query and regexp:

`esearch -db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">protein</span>` -query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'Escherichia*'</span>

- Search the nucleotide database for sequences whose metadata contain insulin and rodents:

`esearch -db nuccore -query "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">insulin [PROT] AND rodents [ORGN]</span>`"`

- Display [h]elp:

`esearch -h`
