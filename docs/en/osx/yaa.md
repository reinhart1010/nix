---
layout: page
title: osx/yaa (English)
description: "Create and manipulate YAA archives."
content_hash: 17989613e53b3d98a733953b99b6835f3ce1bdb1
last_modified_at: 2024-01-31
related_topics:
  - title: español version
    url: /es/osx/yaa.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yaa

Create and manipulate YAA archives.
More information: <https://keith.github.io/xcode-man-pages/yaa.1.html>.

- Create an archive from a directory:

`yaa archive -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.yaa</span>

- Create an archive from a file:

`yaa archive -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.yaa</span>

- Extract an archive to the current directory:

`yaa extract -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive_file.yaa</span>

- List the contents of an archive:

`yaa list -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive_file.yaa</span>

- Create an archive with a specific compression algorithm:

`yaa archive -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">algorithm</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.yaa</span>

- Create an archive with an 8 MB block size:

`yaa archive -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8m</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.yaa</span>
