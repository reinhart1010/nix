---
layout: page
title: common/calibredb (English)
description: "Tool to manipulate the your e-book database."
content_hash: 2fbd04234019861d0379a0f7f7d9deb17916ca1f
related_topics:
  - title: italiano version
    url: /it/common/calibredb.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/calibredb.html
    icon: bi bi-globe
---
# calibredb

Tool to manipulate the your e-book database.
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

- Recursively add all e-books under a directory to the library:

`calibredb add -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Remove one or more e-books from the library. You need the e-book IDs (see above):

`calibredb remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id1 id2 …</span>
