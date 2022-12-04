---
layout: page
title: linux/aspell (English)
description: "Interactive spell checker."
content_hash: d47b4ec88b8d9a8d8a89c8708613ca17e7458bf7
last_modified_at: 2022-12-04
related_topics:
  - title: Deutsch version
    url: /de/linux/aspell.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/aspell.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/aspell.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/linux/aspell.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/aspell.html
    icon: bi bi-globe
---
# aspell

Interactive spell checker.
More information: <http://aspell.net/>.

- Spell check a single file:

`aspell check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- List misspelled words from standard input:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | aspell list`

- Show available dictionary languages:

`aspell dicts`

- Run `aspell` with a different language (takes two-letter ISO 639 language code):

`aspell --lang=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cs</span>

- List misspelled words from standard input and ignore words from personal word list:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | aspell --personal=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">personal-word-list.pws</span>` list`
