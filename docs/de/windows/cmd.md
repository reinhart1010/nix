---
layout: page
title: windows/cmd (Deutsch)
description: "Auch Windows-Eingabeaufforderung genannt, der Windows-Befehlsinterpreter."
content_hash: d417cf483bc99f487c759aedaa5ba823ed9d7517
last_modified_at: 2023-12-19
related_topics:
  - title: English version
    url: /en/windows/cmd.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/cmd.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/cmd.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/cmd.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/cmd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/cmd.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/cmd.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/windows/cmd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/cmd.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/cmd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cmd

Auch Windows-Eingabeaufforderung genannt, der Windows-Befehlsinterpreter.
Weitere Informationen: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmd>.

- Starten einer interaktiven Shell-Sitzung:

`cmd`

- Ausführen eines Befehls (Command):

`cmd /c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Hallo Welt</span>

- Ausführen eines Skripts:

`cmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Pfad\zur\Datei.bat</span>

- Ausführen eines Befehls und anschließendes Aufrufen einer interaktiven Shell:

`cmd /k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Hallo Welt</span>

- Starten einer interaktiven Shell-Sitzung, bei der `echo` in der Befehlsausgabe deaktiviert ist:

`cmd /q`

- Starten einer interaktiven Shell-Sitzung mit aktivierter oder deaktivierter verzögerter Erweiterung der Umgebungsvariablen:

`cmd /v:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Starten einer interaktiven Shell-Sitzung mit aktivierten oder deaktivierten Befehleerweiterungen:

`cmd /e:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Starten einer interaktiven Shell-Sitzung mit Unicode-Kodierung:

`cmd /u`
