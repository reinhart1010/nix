---
layout: page
title: common/figlet (English)
description: "Generate ASCII banners from user input."
content_hash: f20c5876e786c9b928b50922ca0e9d70d993935f
last_modified_at: 2024-03-16
related_topics:
  - title: español version
    url: /es/common/figlet.html
    icon: bi bi-globe
tldri18n_status: 2
---
# figlet

Generate ASCII banners from user input.
See also: `showfigfonts`.
More information: <http://www.figlet.org/figlet-man.html>.

- Generate by directly inputting text:

`figlet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_text</span>

- Use a custom [f]ont file:

`figlet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_text</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/font_file.flf</span>

- Use a [f]ont from the default font directory (the extension can be omitted):

`figlet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_text</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">font_filename</span>

- Pipe command output through FIGlet:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | figlet`

- Show available FIGlet fonts:

`showfigfonts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optional_string_to_display</span>

- Use the full width of the [t]erminal and [c]enter the input text:

`figlet -t -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_text</span>

- Display all characters at full [W]idth to avoid overlapping:

`figlet -W `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_text</span>
