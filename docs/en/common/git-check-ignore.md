---
layout: page
title: common/git-check-ignore (English)
description: "Analyze and debug Git ignore/exclude (\".gitignore\") files."
content_hash: 248fb24db4de9552ed4850bb4a56897397fdc5c7
last_modified_at: 2023-06-13
related_topics:
  - title: español version
    url: /es/common/git-check-ignore.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-check-ignore.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-check-ignore.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-check-ignore.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-check-ignore.html
    icon: bi bi-globe
---
# git check-ignore

Analyze and debug Git ignore/exclude (".gitignore") files.
More information: <https://git-scm.com/docs/git-check-ignore>.

- Check whether a file or directory is ignored:

`git check-ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Check whether multiple files or directories are ignored:

`git check-ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Use pathnames, one per line, from `stdin`:

`git check-ignore --stdin < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_list</span>

- Do not check the index (used to debug why paths were tracked and not ignored):

`git check-ignore --no-index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/files_or_directories</span>

- Include details about the matching pattern for each path:

`git check-ignore --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/files_or_directories</span>
