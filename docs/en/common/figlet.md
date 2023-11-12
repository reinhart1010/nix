---
layout: page
title: common/figlet (English)
description: "Generate ASCII banners from user input."
content_hash: 68502ed532a5f8518592acce518244ebe51399a3
last_modified_at: 2023-11-12
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

- Use a custom font file:

`figlet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_text</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/font_file.flf</span>

- Use a font from the default font directory (the extension can be omitted):

`figlet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_text</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">font_filename</span>

- Pipe command output through FIGlet:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | figlet`

- Show available FIGlet fonts:

`showfigfonts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optional_string_to_display</span>
