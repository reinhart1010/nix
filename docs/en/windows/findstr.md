---
layout: page
title: windows/findstr (English)
description: "Find specified text within one or more files."
content_hash: c76d4f93c759d5d2a247b5f62fdf2debdaedb5e0
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/windows/findstr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# findstr

Find specified text within one or more files.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/findstr>.

- Find space-separated string(s) in all files:

`findstr "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>`" *`

- Find space-separated string(s) in a piped command's output:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dir</span>` | findstr "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>`"`

- Find space-separated string(s) in all files recur[s]ively:

`findstr /s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>`" *`

- Find strings using a case-insensitive search:

`findstr /i "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>`" *"`

- Find strings in all files using regular expressions:

`findstr /r "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression</span>`" *`

- Find a literal string (containing spaces) in all text files:

`findstr /c:"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>`" *.txt`

- Display the line number before each matching line:

`findstr /n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>`" *`

- Display only the filenames that contain a match:

`findstr /m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>`" *`
