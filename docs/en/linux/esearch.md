---
layout: page
title: linux/esearch (English)
description: "Perform a new Entrez search using terms in indexed fields."
content_hash: 8c7f37bd0518125b9573f9622f466a12b2be1a28
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># esearch

Perform a new Entrez search using terms in indexed fields.
It is part of the `edirect` package.
More information: <https://www.ncbi.nlm.nih.gov/books/NBK179288/>.

- Search the pubmed database for selective serotonin reuptake inhibitor:

`esearch -db pubmed -query "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">selective serotonin reuptake inhibitor</span>`"`

- Search the nucleotide database for sequences whose metadata contain insulin and rodents:

`esearch -db nuccore -query "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">insulin [PROT] AND rodents [ORGN]</span>`"`
