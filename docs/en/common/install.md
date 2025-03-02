---
layout: page
title: common/install (English)
description: "Copy files and set attributes."
content_hash: e5ce7231463e6d5b1722dba814022c5cef0da8cf
last_modified_at: 2025-03-02
related_topics:
  - title: français version
    url: /fr/common/install.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/install.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/install.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/install.html
    icon: bi bi-globe
tldri18n_status: 2
---
# install

Copy files and set attributes.
Copy files (often executable) to a system location like `/usr/local/bin`, give them the appropriate permissions/ownership.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/install-invocation.html>.

- Copy files to the destination:

`install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_file1 path/to/source_file2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination</span>

- Copy files to the destination, setting their ownership:

`install --owner `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_file1 path/to/source_file2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination</span>

- Copy files to the destination, setting their group ownership:

`install --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_file1 path/to/source_file2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination</span>

- Copy files to the destination, setting their `mode`:

`install --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+x</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_file1 path/to/source_file2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination</span>

- Copy files and apply access/modification times of source to the destination:

`install --preserve-timestamps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_file1 path/to/source_file2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination</span>

- Copy files and create the directories at the destination if they don't exist:

`install -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_file1 path/to/source_file2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination</span>
