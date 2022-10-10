---
layout: page
title: linux/einfo (English)
description: "Provides the number of records indexed in each field of a given database, the date of the last update of the database, and the available links from the database to other Entrez databases."
content_hash: bb75f562fe42701e6c34c402d6406bbe496ee4e1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># einfo

Provides the number of records indexed in each field of a given database, the date of the last update of the database, and the available links from the database to other Entrez databases.
More information: <https://www.ncbi.nlm.nih.gov/books/NBK179288/>.

- Print all database names:

`einfo -dbs`

- Print all information of the protein database in XML format:

`einfo -db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">protein</span>

- Print all fields of the nuccore database:

`einfo -db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuccore</span>` -fields`

- Print all links of the protein database:

`einfo -db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">protein</span>` -links`
