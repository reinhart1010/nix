---
layout: page
title: common/hunspell (English)
description: "Check spelling."
content_hash: 6d7384af31affbb3f380830d69a05c38b74b5e6b
related_topics:
  - title: русский version
    url: /ru/common/hunspell.html
    icon: bi bi-globe
---
# hunspell

Check spelling.
More information: <https://github.com/hunspell/hunspell>.

- Check the spelling of a file:

`hunspell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Check the spelling of a file with the en_US dictionary:

`hunspell -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en_US</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- List misspelled words in a file:

`hunspell -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
