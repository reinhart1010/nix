---
layout: page
title: windows/clip (Deutsch)
description: "Kopieren von Inhalten der Befehlsausgabe in die Windows Zwischenablage."
content_hash: 9f1cebe9bf5c665df2bfac070cc776993d69a57a
last_modified_at: 2022-12-06
related_topics:
  - title: English version
    url: /en/windows/clip.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/clip.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/clip.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/clip.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># clip

Kopieren von Inhalten der Befehlsausgabe in die Windows Zwischenablage.
Weitere Informationen: <https://learn.microsoft.com/windows-server/administration/windows-commands/clip>.

- Kopiere die Ausgabe eines Befehls in die Windows Zwischenablage:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dir</span>` | clip`

- Kopiere den Inhalt einer Datei in die Windows Zwischenablage:

`clip < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.txt</span>

- Kopiere Text mit einem nachfolgenden Zeilenumbruch in die Windows Zwischenablage:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">irgendein text</span>` | clip`

- Kopiere Text ohne nachfolgenden Zeilenumbruch in die Windows Zwischenablage:

`echo | set /p="irgendein text" | clip`
