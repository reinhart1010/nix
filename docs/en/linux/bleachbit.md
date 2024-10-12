---
layout: page
title: linux/bleachbit (English)
description: "Clean junk files on the filesystem."
content_hash: e09f8dccb32ba21482d6fae9a55f1a950fca46f7
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# bleachbit

Clean junk files on the filesystem.
More information: <https://docs.bleachbit.org/doc/command-line-interface.html>.

- Start the graphical user interface (GUI) version of Bleachbit:

`bleachbit --gui`

- Shred a file:

`bleachbit --shred `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- List available cleaner options:

`bleachbit --list-cleaners`

- Preview the files that will be deleted and other changes that will be made before actually performing the clean-up operation:

`bleachbit --preview `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--preset|cleaner1.option1 cleaner2.* ...</span>

- Perform the clean-up operation and delete files:

`bleachbit --clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--preset|cleaner1.option1 cleaner2.* ...</span>
