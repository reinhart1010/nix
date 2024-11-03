---
layout: page
title: windows/chromium (Nederlands)
description: "Open-source webbrowser die voornamelijk ontwikkeld en onderhouden wordt door Google."
content_hash: b4956e8ef921649dcd02e9211230c146c4299908
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/windows/chromium.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/chromium.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chromium

Open-source webbrowser die voornamelijk ontwikkeld en onderhouden wordt door Google.
Let op: mogelijk moet je het `chromium` commando vervangen met jouw gewenste webbrowser, zoals `brave`, `google-chrome`, `microsoft-edge`/`msedge`, `opera` of `vivaldi`.
Meer informatie: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- Open een specifieke URL of bestand:

`chromium `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com|path/naar/bestand.html</span>

- Open in incognito modus (gebruik `--inprivate` voor Microsoft Edge):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chromium --incognito|msedge --inprivate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Open in een nieuw venster:

`chromium --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voorbeeld.com</span>

- Open in applicatie modus (zonder werkbalken, URL balk, knoppen, etc.):

`chromium --app=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Gebruik een proxy server:

`chromium --proxy-server="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">socks5://hostname:66</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Open met een aangepaste profiel map:

`chromium --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>

- Open zonder CORS validatie (handig om een API te testen):

`chromium --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>` --disable-web-security`

- Open met een DevTools venster voor elk geopend tabblad:

`chromium --auto-open-devtools-for-tabs`
