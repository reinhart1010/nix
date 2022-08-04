---
layout: page
title: common/tac (italiano)
description: "Stampa e concatena file al contrario."
content_hash: 4dec5f22a58d44d376de4192c7c24b7820d8b51c
related_topics:
  - title: English version
    url: /en/common/tac.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tac.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tac

Stampa e concatena file al contrario.
Maggiori informazioni: <https://www.gnu.org/software/coreutils/tac>.

- Stampa il contenuto di *file1* al contrario su standard output:

`tac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>

- Concatena multipli file al contrario in un nuovo file:

`tac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuovo_file</span>
