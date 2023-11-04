---
layout: page
title: windows/del (italiano)
description: "Cancella uno o più file."
content_hash: 366d39d20006fbe5b3243815da217837c811f124
last_modified_at: 2023-11-04
related_topics:
  - title: العربية version
    url: /ar/windows/del.html
    icon: bi bi-globe
  - title: বাংলা version
    url: /bn/windows/del.html
    icon: bi bi-globe
  - title: bosanski version
    url: /bs/windows/del.html
    icon: bi bi-globe
  - title: català version
    url: /ca/windows/del.html
    icon: bi bi-globe
  - title: čeština version
    url: /cs/windows/del.html
    icon: bi bi-globe
  - title: dansk version
    url: /da/windows/del.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/windows/del.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/del.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/del.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/windows/del.html
    icon: bi bi-globe
  - title: suomi version
    url: /fi/windows/del.html
    icon: bi bi-globe
  - title: français version
    url: /fr/windows/del.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/del.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/del.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/del.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/del.html
    icon: bi bi-globe
  - title: ລາວ version
    url: /lo/windows/del.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/windows/del.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/windows/del.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/del.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/windows/del.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/del.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/del.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/windows/del.html
    icon: bi bi-globe
  - title: română version
    url: /ro/windows/del.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/del.html
    icon: bi bi-globe
  - title: српски version
    url: /sr/windows/del.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/windows/del.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/del.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/windows/del.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/windows/del.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/windows/del.html
    icon: bi bi-globe
  - title: o‘zbek version
    url: /uz/windows/del.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/del.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/del.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/del.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># del

Cancella uno o più file.
Maggiori informazioni: <https://learn.microsoft.com/windows-server/administration/windows-commands/del>.

- Cancella uno o più (separati da uno spazio) file o pattern:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern_di_file</span>

- Chiedi conferma prima di cancellare ogni file:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern_di_file</span>` /p`

- Forza l'eliminazione di un file a sola lettura:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern_di_file</span>` /f`

- Elimina in modo ricorsivo i file da tutte le sottodirectory:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern_di_file</span>` /s`

- Non chiedere conferma quando si eliminano i file in base a un carattere globale:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern_di_file</span>` /q`

- Mostra il messaggio d'aiuto e fà vedere la lista di attributi disponibili:

`del /?`

- Cancella dei file in base a degli attributi specifici:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern_di_file</span>` /a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">attributo</span>
