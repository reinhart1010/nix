---
layout: page
title: common/tr (English)
description: "Translate characters: run replacements based on single characters and character sets."
content_hash: 7878fd42e88e1ecf156f93e1f08329103e68716a
last_modified_at: 2025-03-02
related_topics:
  - title: العربية version
    url: /ar/common/tr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/tr.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/tr.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/tr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tr

Translate characters: run replacements based on single characters and character sets.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/tr-invocation.html>.

- Replace all occurrences of a character in a file, and print the result:

`tr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find_character</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replace_character</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Replace all occurrences of a character from another command's output:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>` | tr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find_character</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replace_character</span>

- Map each character of the first set to the corresponding character of the second set:

`tr '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">abcd</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jkmn</span>`' < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Delete all occurrences of the specified set of characters from the input:

`tr -d '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_characters</span>`' < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Compress a series of identical characters to a single character:

`tr -s '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_characters</span>`' < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Translate the contents of a file to upper-case:

`tr "[:lower:]" "[:upper:]" < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Strip out non-printable characters from a file:

`tr -cd "[:print:]" < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
