---
layout: page
title: windows/fc (Nederlands)
description: "Vergelijk de verschillen tussen twee bestanden of sets van bestanden."
content_hash: fb3253dcdaaebdd46edc1ea11cf238f7ee79fcd4
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/windows/fc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/fc.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/fc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fc

Vergelijk de verschillen tussen twee bestanden of sets van bestanden.
Gebruik wildcards (*) om sets van bestanden te vergelijken.
Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/fc>.

- Vergelijk 2 opgegeven bestanden:

`fc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand2</span>

- Voer een hoofdletterongevoelige vergelijking uit:

`fc /c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand2</span>

- Vergelijk bestanden als Unicode-tekst:

`fc /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand2</span>

- Vergelijk bestanden als ASCII-tekst:

`fc /l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand2</span>

- Vergelijk bestanden als binair:

`fc /b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand2</span>

- Schakel tab-naar-spatie uitbreiding uit:

`fc /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand2</span>

- Comprimeer witruimte (tabs en spaties) voor vergelijkingen:

`fc /w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand2</span>
