---
layout: page
title: common/chromium (Deutsch)
description: "Open-Source-Webbrowser von Google."
content_hash: bffd90b7134bef97c480108d0455c9e8142bbdfe
last_modified_at: 2023-12-28
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
  - title: Nederlands version
    url: /nl/common/chromium.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/chromium.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chromium

Open-Source-Webbrowser von Google.
Weitere Informationen: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- Öffne eine bestimmte Datei oder URL:

`chromium `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://beispiel.com|pfad/zu/datei.html</span>

- Öffne eine URL im Inkognito-Modus:

`chromium --incognito `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">beispiel.com</span>

- Öffne eine URL in einem neuen Fenster:

`chromium --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">beispiel.com</span>

- Öffne eine URL im Anwendungsmodus (ohne Symbolleisten, Suchleiste, Schaltflächen usw.):

`chromium --app=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://beispiel.com</span>

- Öffne eine URL und verwende einen Proxy-Server:

`chromium --proxy-server="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">socks5://hostname:66</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">beispiel.com</span>

- Öffne Chromium mit einem eigenen Profil-Verzeichnis:

`chromium --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>

- Öffne Chromium ohne CORS-Verifizierung (nützlich, um eine API zu testen):

`chromium --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>` --disable-web-security`

- Öffne Chromium mit einem `DevTools`-Fenster für jeden geöffneten Tab:

`chromium --auto-open-devtools-for-tabs`
