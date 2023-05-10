---
layout: page
title: common/rarcrack (English)
description: "Password cracker for rar, zip and 7z archives."
content_hash: 891ebbfad71b6327dd5f2f5ed3e970f9a0b4c9b3
last_modified_at: 2023-05-10
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rarcrack

Password cracker for rar, zip and 7z archives.

- Brute force the password for an archive (tries to guess the archive type):

`rarcrack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zip</span>

- Specify the archive type:

`rarcrack --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rar|zip|7z</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zip</span>

- Use multiple threads:

`rarcrack --threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zip</span>
