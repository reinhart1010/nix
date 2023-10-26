---
layout: page
title: windows/robocopy (italiano)
description: "Copia robusta di file e directory."
content_hash: d171372f215100b27fae9ccafa263e7c8cf915ae
last_modified_at: 2023-10-26
related_topics:
  - title: Deutsch version
    url: /de/windows/robocopy.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/robocopy.html
    icon: bi bi-globe
---
# robocopy

Copia robusta di file e directory.
Di default, i file saranno copiati solo se la sorgente e la destinazione hanno timestamp o dimensioni diverse.
Maggiori informazioni: <https://learn.microsoft.com/it-it/windows-server/administration/windows-commands/robocopy>.

- Copia tutti i file `.jpg` e `.bmp` da una directory ad un'altra:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso\della\directory_sorgente</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso\della\directory_destinazione</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.bmp</span>

- Copia tutti i file e le sottodirectory, includento anche quelle vuote:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso\della\directory_sorgente</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso\della\directory_destinazione</span>` /E`

- Mirror/Sincronizza una directory, eliminando tutto ciò che non è nella sorgente e includendo tutti gli attributi e le autorizzazioni:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso\della\directory_sorgente</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso\della\directory_destinazione</span>` /MIR /COPYALL`

- Copia tutti i file e le sottodirectory, escludendo i file di origine più vecchi rispetto ai file di destinazione:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso\della\directory_sorgente</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso\della\directory_destinazione</span>` /E /XO`

- Elencare tutti i file di dimensioni maggiori o uguali a 50 MB anziché copiarli:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso\della\directory_sorgente</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso\della\directory_destinazione</span>` /MIN:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">52428800</span>` /L`

- Consenti la ripresa se la connessione di rete viene interrotta, limita i tentativi di ripresa a 5 ed il tempo di attesa a 15 secondi:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso\della\directory_sorgente</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso\della\directory_destinazione</span>` /Z /R:5 /W:15`

- Mostra l'aiuto dettagliato:

`robocopy /?`
