---
layout: page
title: common/git-am (polski)
description: "Zastosuj pliki poprawki i utwórz commit. Przydatne przy otrzymywaniu commitów przez email."
content_hash: abc1d86d47620f1f73448fdcdc5361d156e9abf5
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/git-am.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-am.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-am.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-am.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-am.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-am.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-am.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-am.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-am.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git am

Zastosuj pliki poprawki i utwórz commit. Przydatne przy otrzymywaniu commitów przez email.
Zobacz także `git format-patch`, który może generować pliki poprawki.
Więcej informacji: <https://git-scm.com/docs/git-am>.

- Zastosuj i komituj zmiany z lokalnego pliku poprawki:

`git am `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku.patch</span>

- Zastosuj i komituj zmiany ze zdalnego pliku poprawki:

`curl -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/plik.patch</span>` | git apply`

- Przerwij proces zastosowania pliku poprawki:

`git am --abort`

- Zastosuj jak największą część pliku poprawki, zapisując nieudane fragmenty w plikach odrzuceń (pliki `.rej`):

`git am --reject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku.patch</span>
