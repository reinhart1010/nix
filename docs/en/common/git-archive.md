---
layout: page
title: common/git-archive (English)
description: "Create an archive of files from a named tree."
content_hash: 4886e5f503552c9da4d93afc90b1d72e3710d9dc
last_modified_at: 2024-01-03
related_topics:
  - title: Deutsch version
    url: /de/common/git-archive.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-archive.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-archive.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-archive.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-archive.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git archive

Create an archive of files from a named tree.
More information: <https://git-scm.com/docs/git-archive>.

- Create a tar archive from the contents of the current HEAD and print it to `stdout`:

`git archive --verbose HEAD`

- Create a zip archive from the current HEAD and print it to `stdout`:

`git archive --verbose --format zip HEAD`

- Same as above, but write the zip archive to file:

`git archive --verbose --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zip</span>` HEAD`

- Create a tar archive from the contents of the latest commit on a specific branch:

`git archive --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Create a tar archive from the contents of a specific directory:

`git archive --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tar</span>` HEAD:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Prepend a path to each file to archive it inside a specific directory:

`git archive --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tar</span>` --prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/prepend</span>`/ HEAD`
