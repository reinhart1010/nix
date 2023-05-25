---
layout: page
title: common/git-mv (English)
description: "Move or rename files and update the Git index."
content_hash: 711ce51c717c2deadfdb7d5e9a45c8d042bfd498
last_modified_at: 2023-05-25
related_topics:
  - title: español version
    url: /es/common/git-mv.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-mv.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-mv.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-mv.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-mv.html
    icon: bi bi-globe
---
# git mv

Move or rename files and update the Git index.
More information: <https://git-scm.com/docs/git-mv>.

- Move a file inside the repo and add the movement to the next commit:

`git mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new/path/to/file</span>

- Rename a file or directory and add the renaming to the next commit:

`git mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination</span>

- Overwrite the file or directory in the target path if it exists:

`git mv --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination</span>
