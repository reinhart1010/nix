---
layout: page
title: common/ln (English)
description: "Create links to files and directories."
content_hash: 7858be18802bce4162546c0dbb3a68119fe91330
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/ln.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/ln.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ln.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/ln.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ln.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ln.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ln.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ln.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ln

Create links to files and directories.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/ln-invocation.html>.

- Create a symbolic link to a file or directory:

`ln -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/symlink</span>

- Overwrite an existing symbolic link to point to a different file:

`ln -sf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/new_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/symlink</span>

- Create a hard link to a file:

`ln `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/hardlink</span>
