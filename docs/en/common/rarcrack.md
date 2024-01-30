---
layout: page
title: common/rarcrack (English)
description: "Password cracker for `rar`, `zip` and `7z` archives."
content_hash: b11e7f5fabe10a778db29d37bcd918e0bc7babc6
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# rarcrack

Password cracker for `rar`, `zip` and `7z` archives.

- Brute force the password for an archive (tries to guess the archive type):

`rarcrack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zip</span>

- Specify the archive type:

`rarcrack --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rar|zip|7z</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zip</span>

- Use multiple threads:

`rarcrack --threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zip</span>
