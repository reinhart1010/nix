---
layout: page
title: common/git-archive (English)
description: "Create an archive of files from a tree."
content_hash: bebdeba3a2515f8263a7ad0071d555a0011f270a
last_modified_at: 2024-04-05
related_topics:
  - title: Deutsch version
    url: /de/common/git-archive.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-archive.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-archive.html
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

Create an archive of files from a tree.
More information: <https://git-scm.com/docs/git-archive>.

- Create a tar archive from the contents of the current HEAD and print it to `stdout`:

`git archive --verbose HEAD`

- Use the Zip format and report progress [v]erbosely:

`git archive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--verbose</span>` --format zip HEAD`

- [o]utput the Zip archive to a specific file:

`git archive -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zip</span>` HEAD`

- Create a tar archive from the contents of the latest commit of a specific branch:

`git archive -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Use the contents of a specific directory:

`git archive -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tar</span>` HEAD:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Prepend a path to each file to archive it inside a specific directory:

`git archive -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tar</span>` --prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/prepend</span>`/ HEAD`
