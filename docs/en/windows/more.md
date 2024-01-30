---
layout: page
title: windows/more (English)
description: "Display paginated output from `stdin` or a file."
content_hash: 215cf9507ba1c9f92d4c7b5c2aac607ffad9be2b
last_modified_at: 2024-01-30
related_topics:
  - title: 中文 version
    url: /zh/windows/more.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/more.html
    icon: bi bi-globe
tldri18n_status: 2
---
# more

Display paginated output from `stdin` or a file.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/more>.

- Display paginated output from `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo test</span>` | more`

- Display paginated output from one or more files:

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>

- Convert tabs to the specified number of spaces:

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>` /t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">spaces</span>

- Clear the screen before displaying the page:

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>` /c`

- Display the output starting at line 5:

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>` +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- Enable extended interactive mode (see help for usage):

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>` /e`

- Display help:

`more /?`
