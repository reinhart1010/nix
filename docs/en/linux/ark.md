---
layout: page
title: linux/ark (English)
description: "KDE's archiving tool."
content_hash: 003615db6fe3568de1f5118ef4509f251e3f8643
last_modified_at: 2022-12-02
related_topics:
  - title: Deutsch version
    url: /de/linux/ark.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ark.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/ark.html
    icon: bi bi-globe
---
# ark

KDE's archiving tool.
More information: <https://docs.kde.org/stable5/en/ark/ark/>.

- Extract a specific archive into the current directory:

`ark --batch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive</span>

- Extract an archive into a specific directory:

`ark --batch --destination `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive</span>

- Create an archive if it does not exist and add specific files to it:

`ark --add-to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>
