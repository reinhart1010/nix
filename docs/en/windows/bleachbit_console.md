---
layout: page
title: windows/bleachbit_console (English)
description: "Clean junk files on the filesystem."
content_hash: 87ffe445dc244f22b2b352f3935e6fc03fc3e7e9
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# bleachbit_console

Clean junk files on the filesystem.
More information: <https://docs.bleachbit.org/doc/command-line-interface.html>.

- Start the graphical user interface (GUI) version of Bleachbit:

`bleachbit_console.exe --gui`

- Shred a file:

`bleachbit_console.exe --shred `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- List available cleaner options:

`bleachbit_console.exe --list-cleaners`

- Preview the files that will be deleted and other changes that will be made before actually performing the clean-up operation:

`bleachbit_console.exe --preview `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--preset|cleaner1.option1 cleaner2.* ...</span>

- Perform the clean-up operation and delete files:

`bleachbit_console.exe --clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--preset|cleaner1.option1 cleaner2.* ...</span>
