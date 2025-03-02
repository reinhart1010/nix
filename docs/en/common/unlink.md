---
layout: page
title: common/unlink (English)
description: "Remove a link to a file from the filesystem."
content_hash: ad8258131ec6fd8b4dbaef648190e97aba92977e
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/unlink.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/unlink.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/unlink.html
    icon: bi bi-globe
tldri18n_status: 2
---
# unlink

Remove a link to a file from the filesystem.
The file contents is lost if the link is the last one to the file.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/unlink-invocation.html>.

- Remove the specified file if it is the last link:

`unlink `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
