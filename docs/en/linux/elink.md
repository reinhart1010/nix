---
layout: page
title: linux/elink (English)
description: "Look up precomputed neighbors within a database, or find associated records in other databases."
content_hash: 7f0b007bfdc80420ca3d27aaa313c582f65e0931
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# elink

Look up precomputed neighbors within a database, or find associated records in other databases.
It is part of the `edirect` package.
More information: <https://www.ncbi.nlm.nih.gov/books/NBK179288/>.

- Search pubmed then find related sequences:

`esearch -db pubmed -query "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">selective serotonin reuptake inhibitor</span>`" | elink -target nuccore`

- Search nucleotide then find related biosamples:

`esearch -db nuccore -query "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">insulin [PROT] AND rodents [ORGN]</span>`" | elink -target biosample`
