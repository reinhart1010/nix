---
layout: page
title: osx/textutil (English)
description: "Used to manipulate text files of various formats."
content_hash: e0ac8647b5ce420fbc63cb119c51a755e84b42f0
last_modified_at: 2023-02-20
related_topics:
  - title: español version
    url: /es/osx/textutil.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/textutil.html
    icon: bi bi-globe
---
# textutil

Used to manipulate text files of various formats.
More information: <https://ss64.com/osx/textutil.html>.

- Display information about `foo.rtf`:

`textutil -info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/foo.rtf</span>

- Convert `foo.rtf` into `foo.html`:

`textutil -convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/foo.rtf</span>

- Convert rich text to normal text:

`textutil `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/foo.rtf</span>` -convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">txt</span>

- Convert `foo.txt` into `foo.rtf`, using Times 10 for the font:

`textutil -convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rtf</span>` -font `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Times</span>` -fontsize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/foo.txt</span>

- Load all RTF files in the current directory, concatenates their contents, and writes the result out as `index.html` with the HTML title set to "Several Files":

`textutil -cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html</span>` -title "Several Files" -output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/index.html</span>` *.rtf`
