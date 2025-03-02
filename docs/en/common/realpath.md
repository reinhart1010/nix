---
layout: page
title: common/realpath (English)
description: "Display the resolved absolute path for a file or directory."
content_hash: f4883e0ab211f54dcb473cbf08f50ea10252c958
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/realpath.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/realpath.html
    icon: bi bi-globe
tldri18n_status: 2
---
# realpath

Display the resolved absolute path for a file or directory.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/realpath-invocation.html>.

- Display the absolute path for a file or directory:

`realpath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Require all path components to exist:

`realpath --canonicalize-existing `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Resolve ".." components before symlinks:

`realpath --logical `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Disable symlink expansion:

`realpath --no-symlinks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Suppress error messages:

`realpath --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>
