---
layout: page
title: windows/more (English)
description: "Display paginated output from stdin or a file."
content_hash: 28f8bb946e0d6dd05c42feb4dab05054b6a49b63
related_topics:
  - title: 中文 version
    url: /zh/windows/more.html
    icon: bi bi-globe
---
# more

Display paginated output from stdin or a file.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/more>.

- Display paginated output from stdin:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo test</span>` | more`

- Display paginated output from one or more files:

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Convert tabs to the specified number of spaces:

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` /t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">spaces</span>

- Clear the screen before displaying the page:

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` /c`

- Display the output starting at line 5:

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- Enable extended interactive mode (see help for usage):

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` /e`

- Display full usage information:

`more /?`
