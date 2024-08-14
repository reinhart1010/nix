---
layout: page
title: common/aspell (English)
description: "Interactive spell checker."
content_hash: 844823fa3bd6fb534e2ad976cf96c89c716a5966
last_modified_at: 2024-08-14
related_topics:
  - title: Deutsch version
    url: /de/common/aspell.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/common/aspell.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aspell.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/aspell.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/aspell.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aspell

Interactive spell checker.
More information: <http://aspell.net/>.

- Spell check a single file:

`aspell check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- List misspelled words from `stdin`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | aspell list`

- Show available dictionary languages:

`aspell dicts`

- Run `aspell` with a different language (takes two-letter ISO 639 language code):

`aspell --lang=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cs</span>

- List misspelled words from `stdin` and ignore words from personal word list:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | aspell --personal=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">personal-word-list.pws</span>` list`
