---
layout: page
title: windows/comp (English)
description: "Compare the contents of two files or sets of files."
content_hash: 9ffae7982ea8523cfebf0975395ddb699e9c12a0
last_modified_at: 2023-11-12
related_topics:
  - title: தமிழ் version
    url: /ta/windows/comp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/comp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# comp

Compare the contents of two files or sets of files.
Use wildcards (*) to compare sets of files.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/comp>.

- Compare files interactively:

`comp`

- Compare two specified files:

`comp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file2</span>

- Compare two sets of files:

`comp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory1</span>`\* `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory2</span>`\*`

- Display differences in decimal format:

`comp /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file2</span>

- Display differences in ASCII format:

`comp /a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file2</span>

- Display line numbers for differences:

`comp /l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file2</span>

- Compare files case-insensitively:

`comp /c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file2</span>

- Compare only the first 5 lines of each file:

`comp /n=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file2</span>
