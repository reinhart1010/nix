---
layout: page
title: common/emacsclient (Deutsch)
description: "Öffnet Dateien in einem laufenden Emacs-Server."
content_hash: 61b4e48a49899ffe446df5cd10e6c0868a9f37ad
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/common/emacsclient.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/emacsclient.html
    icon: bi bi-globe
tldri18n_status: 2
---
# emacsclient

Öffnet Dateien in einem laufenden Emacs-Server.
Siehe auch `emacs`.
Weitere Informationen: <https://www.gnu.org/software/emacs/manual/html_node/emacs/emacsclient-Options.html>.

- Öffne eine Datei in einem laufenden Emacs-Server (mit GUI wenn möglich):

`emacsclient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Öffne eine Datei in der Konsole (ohne X-Fenster):

`emacsclient --no-window-system `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Öffne eine Datei in einem neuen Emacs Fenster:

`emacsclient --create-frame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Führe einen Befehl aus und schreibe das Ergebnis in `stdout`:

`emacsclient --eval '(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>`)'`

- Gib einen alternativen Editor an für den Fall, dass kein Emacs-Server läuft:

`emacsclient --alternate-editor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">editor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Beende einen laufenden Emacs-Server und alle Instanzen und frage nach Bestätigung für ungespeicherte Dateien:

`emacsclient --eval '(save-buffers-kill-emacs)'`
