---
layout: page
title: common/emacs (Deutsch)
description: "Der erweiterbare, veränderbare und selbst-dokumentierende Echtzeit Text Editor."
content_hash: c11f1a766a3ea1a7be2ed45e0b3e626eaa1612d6
related_topics:
  - title: English version
    url: /en/common/emacs.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/emacs.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/emacs.html
    icon: bi bi-globe
---
# emacs

Der erweiterbare, veränderbare und selbst-dokumentierende Echtzeit Text Editor.
Siehe auch `emacsclient`.
Weitere Informationen: <https://www.gnu.org/software/emacs>.

- Öffne eine Datei in Emacs:

`emacs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Öffne eine Datei in einer bestimmten Zeile:

`emacs +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zeilennummer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Starte Emacs in der Konsole (ohne X-Fenster):

`emacs --no-window-system`

- Starte einen Emacs-Server im Hintergrund (aufrufbar mit `emacsclient`):

`emacs --daemon`

- Beende einen laufenden Emacs-Server und alle Instanzen und frage nach Bestätigung für ungespeicherte Dateien:

`emacsclient --eval '(save-buffers-kill-emacs)'`

- Tastenkombination zum Speichern einer Datei:

`Ctrl + X, Ctrl + S`

- Tastenkombination zum Beenden von Emacs:

`Ctrl + X, Ctrl + C`
