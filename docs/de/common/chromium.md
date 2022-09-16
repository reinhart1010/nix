---
layout: page
title: common/chromium (Deutsch)
description: "Open-Source-Webbrowser von Google."
content_hash: 2a09c18086029d07b4b96ff0b19b79abd252515e
related_topics:
  - title: English version
    url: /en/common/chromium.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chromium.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chromium.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chromium.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/chromium.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/chromium.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># chromium

Open-Source-Webbrowser von Google.
Weitere Informationen: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- Öffne eine bestimmte Datei oder URL:

`chromium `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://beispiel.com|pfad/zu/datei.html</span>

- Öffne eine URL im Inkognito-Modus:

`chromium --incognito `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">beispiel.com</span>

- Öffne eine URL in einem neuen Fenster:

`chromium --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">beispiel.com</span>

- Öffne eine URL im Anwendungsmodus (ohne Symbolleisten, Suchleiste, Schaltflächen usw.):

`chromium --app='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://beispiel.com</span>`'`

- Öffne eine URL und verwende einen Proxy-Server:

`chromium --proxy-server="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">socks5://hostname:66</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">beispiel.com</span>

- Öffne Chromium mit einem eigenen Profil-Verzeichnis:

`chromium --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>

- Öffne Chromium ohne CORS-Verifizierung (nützlich, um eine API zu testen):

`chromium --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>` --disable-web-security`

- Öffne Chromium mit einem `DevTools`-Fenster für jeden geöffneten Tab:

`chromium --auto-open--devtools-for-tabs`
