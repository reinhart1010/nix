---
layout: page
title: common/chromium (Nederlands)
description: "Open-source webbrowser voornamelijk ontwikkeld en onderhouden door Google."
content_hash: 84c697470db9be72696270ccab2f2cd8d59c9a4a
last_modified_at: 2023-11-18
related_topics:
  - title: Deutsch version
    url: /de/common/chromium.html
    icon: bi bi-globe
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
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/chromium.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># chromium

Open-source webbrowser voornamelijk ontwikkeld en onderhouden door Google.
Meer informatie: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- Open een specifieke URL of bestand:

`chromium `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com|pad/naar/bestand.html</span>

- Open in de incognito-modus:

`chromium --incognito `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Open in een nieuw venster:

`chromium --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Open in de applicatiemodus (zonder toolbars, URL-balk, knoppen, etc.):

`chromium --app=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Gebruik een proxyserver:

`chromium --proxy-server="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">socks5://hostname:66</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Open met een aangepaste profielmap:

`chromium --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>

- Open zonder CORS validatie (nuttig om een API te testen):

`chromium --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>` --disable-web-security`

- Open met een DevTools venster voor elk geopend tabblad:

`chromium --auto-open-devtools-for-tabs`
