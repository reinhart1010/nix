---
layout: page
title: linux/einfo (English)
description: "Provides the number of records indexed in each database field, the last update date of the database, and the available links from the database to other Entrez databases."
content_hash: fbbfc268bb1ef72fe5f67422abef2bcb02e09d7b
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# einfo

Provides the number of records indexed in each database field, the last update date of the database, and the available links from the database to other Entrez databases.
More information: <https://www.ncbi.nlm.nih.gov/books/NBK179288/>.

- Print all database names:

`einfo -dbs`

- Print all information of the protein database in XML format:

`einfo -db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">protein</span>

- Print all fields of the nuccore database:

`einfo -db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuccore</span>` -fields`

- Print all links of the protein database:

`einfo -db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">protein</span>` -links`
