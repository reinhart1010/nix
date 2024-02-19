---
layout: page
title: common/calibredb (English)
description: "Manipulate an e-book database."
content_hash: 95b70ad2c4c6a235506566390ca3a6f5255447d6
last_modified_at: 2024-02-19
related_topics:
  - title: italiano version
    url: /it/common/calibredb.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/calibredb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# calibredb

Manipulate an e-book database.
Part of the Calibre e-book library.
More information: <https://manual.calibre-ebook.com/generated/en/calibredb.html>.

- List e-books in the library with additional information:

`calibredb list`

- Search for e-books displaying additional information:

`calibredb list --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>

- Search for just ids of e-books:

`calibredb search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>

- Add one or more e-books to the library:

`calibredb add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1 file2 …</span>

- [r]ecursively add all e-books under a directory to the library:

`calibredb add -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Remove one or more e-books from the library. You need the e-book IDs (see above):

`calibredb remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id1 id2 …</span>
