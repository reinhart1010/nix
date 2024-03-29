---
layout: page
title: common/zip2john (English)
description: "Extract password hashes from Zip archives for use with John the Ripper password cracker."
content_hash: 89cbc071da13d7fdd121b26f205d7fada0bb360d
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# zip2john

Extract password hashes from Zip archives for use with John the Ripper password cracker.
This is a utility tool usually installed as part of the John the Ripper installation.
More information: <https://www.openwall.com/john/>.

- Extract the password hash from an archive, listing all files in the archive:

`zip2john `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zip</span>

- Extract the password hash using [o]nly a specific compressed file:

`zip2john -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zip</span>

- Extract the password hash from a compressed file to a specific file (for use with John the Ripper):

`zip2john -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zip</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.hash</span>
