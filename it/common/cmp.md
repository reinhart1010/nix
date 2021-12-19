---
layout: page
title: common/cmp (italiano)
description: "Compara due file."
content_hash: 6354542f8bb3fb4eec122ba750bd2333037beaa9
related_topics:
  - title: English version
    url: /en/common/cmp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cmp.html
    icon: bi bi-globe
---
# cmp

Compara due file.
Maggiori informazioni: <https://www.gnu.org/software/diffutils/manual/html_node/Invoking-cmp.html>.

- Trova l'indice del primo byte e della prima riga differente tra due file:

`cmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>

- Trova ogni coppia di byte differenti ed il relativo indice:

`cmp -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>
