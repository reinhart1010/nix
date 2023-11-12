---
layout: page
title: windows/mklink (English)
description: "Create symbolic links."
content_hash: 4a6e73478a448ebd2ff4d958e426a6a167f93116
last_modified_at: 2023-11-12
related_topics:
  - title: 日本語 version
    url: /ja/windows/mklink.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/mklink.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mklink

Create symbolic links.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/mklink>.

- Create a symbolic link to a file:

`mklink `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\link_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source_file</span>

- Create a symbolic link to a directory:

`mklink /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\link_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source_directory</span>

- Create a hard link to a file:

`mklink /h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\link_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source_file</span>

- Create a directory junction:

`mklink /j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\link_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source_file</span>
