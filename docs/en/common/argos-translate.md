---
layout: page
title: common/argos-translate (English)
description: "An open-source offline translation library and CLI tool written in Python."
content_hash: 2bba862a9ec81a18f58e288a392f03f7ec9ece65
last_modified_at: 2024-11-23
tldri18n_status: 2
---
# argos-translate

An open-source offline translation library and CLI tool written in Python.
More information: <https://www.argosopentech.com/>.

- Install translation pairs for Spanish to English translation:

`argospm install translate-es_en`

- Translate some text from Spanish (`es`) to English (`en`) (Note: only two letter language codes are supported):

`argos-translate --from-lang es --to-lang en `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">un texto corto</span>

- Translate a text file from English to Hindi:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>` | argos-translate --from-lang en --to-lang hi`

- List all installed translation pairs:

`argospm list`

- Show translation pairs from English that are available to be installed:

`argospm search --from-lang en`

- Update installed language package pairs:

`argospm update`

- Translate from `ar` to `ru` (Note: this requires the translation pairs `translate-ar_en` and `translate-en_ru` to be installed):

`argos-translate --from-lang ar --to-lang ru `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">صورة تساوي أكثر من ألف كلمة</span>
