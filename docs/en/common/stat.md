---
layout: page
title: common/stat (English)
description: "Display file and filesystem information."
content_hash: f65b81c589d302e0c0e3fe3d459cae2d2429a84c
last_modified_at: 2023-11-12
related_topics:
  - title: русский version
    url: /ru/common/stat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# stat

Display file and filesystem information.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/stat-invocation.html>.

- Display properties about a specific file such as size, permissions, creation and access dates among others:

`stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display properties about a specific file such as size, permissions, creation and access dates among others without labels:

`stat --terse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display information about the filesystem where a specific file is located:

`stat --file-system `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Show only octal file permissions:

`stat --format="%a %n" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Show the owner and group of a specific file:

`stat --format="%U %G" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Show the size of a specific file in bytes:

`stat --format="%s %n" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
