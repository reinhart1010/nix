---
layout: page
title: common/trans (English)
description: "Translate Shell is a command-line translator."
content_hash: f5545b77a467fdaabe2d4d24323e9cb27b4f6c93
---
# trans

Translate Shell is a command-line translator.
More information: <https://github.com/soimort/translate-shell>.

- Translate a word (language is detected automatically):

`trans "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">word_or_sentence_to_translate</span>`"`

- Get a brief translation:

`trans --brief "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">word_or_sentence_to_translate</span>`"`

- Translate a word into french:

`trans :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fr</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">word</span>

- Translate a word from German to English:

`trans `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">de</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Schmetterling</span>

- Behave like a dictionary to get the meaning of a word:

`trans -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">word</span>
