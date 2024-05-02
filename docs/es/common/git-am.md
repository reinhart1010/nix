---
layout: page
title: common/git-am (español)
description: "Aplica archivos de parche. Útil cuando se reciben commits por correo electrónico."
content_hash: d34cf041a477ef9ae67d9be8af7c6acbabe14e08
last_modified_at: 2024-05-02
related_topics:
  - title: Deutsch version
    url: /de/common/git-am.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-am.html
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
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git am

Aplica archivos de parche. Útil cuando se reciben commits por correo electrónico.
Vea también `git format-patch`, comando que genera archivos de parche.
Más información: <https://git-scm.com/docs/git-am>.

- Aplica un archivo de parche:

`git am `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.patch</span>

- Aplica un archivo de parche remoto:

`curl -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://ejemplo.com/file.patch</span>` | git apply`

- Aborta el proceso de aplicar un archivo de parche:

`git am --abort`

- Aplica todo lo posible de un archivo de parche y guarda los fragmentos fallidos para rechazar archivos:

`git am --reject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.patch</span>
