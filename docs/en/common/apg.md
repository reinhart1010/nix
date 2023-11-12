---
layout: page
title: common/apg (English)
description: "Creates arbitrarily complex random passwords."
content_hash: 55e432f6e18a6d43c3aa367eae5468775c531f4e
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/apg.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/apg.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/apg.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/apg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/apg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/apg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apg

Creates arbitrarily complex random passwords.
More information: <https://manned.org/apg>.

- Create random passwords (default password length is 8):

`apg`

- Create a password with at least 1 symbol (S), 1 number (N), 1 uppercase (C), 1 lowercase (L):

`apg -M SNCL`

- Create a password with 16 characters:

`apg -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>

- Create a password with maximum length of 16:

`apg -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>

- Create a password that doesn't appear in a dictionary (the dictionary file has to be provided):

`apg -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/dictionary_file</span>
