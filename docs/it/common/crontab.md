---
layout: page
title: common/crontab (italiano)
description: "Programma cron job per essere eseguiti a determinati intervalli di tempo per l'utente corrente."
content_hash: 2a0a23725d70aa1a087c34bb98704747bf7dcd78
related_topics:
  - title: English version
    url: /en/common/crontab.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crontab.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/crontab.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># crontab

Programma cron job per essere eseguiti a determinati intervalli di tempo per l'utente corrente.
Formato definizione di un job: "(minuto) (ora) (giorno_del_mese) (mese) (giorno_della_settimana) comando_da_eseguire".
Maggiori informazioni: <https://crontab.guru/>.

- Modifica il file crontab per l'utente corrente:

`crontab -e`

- Elenca i cron job esistenti per l'utente corrente:

`crontab -l`

- Rimuovi tutti i cron job per l'utente corrente:

`crontab -r`

- Esempio di un job eseguito alle 10:00 ogni giorno (* vuol dire qualsiasi valore):

`0 10 * * * `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando_da_eseguire</span>

- Esempio di un job eseguito ogni minuto il 3 Aprile:

`* * 3 Apr * `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando_da_eseguire</span>

- Esempio di un job che esegue un determinato script alle 02:30 ogni venerdì:

`30 2 * * Fri `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/percorso/assoluto/dello/script.sh</span>
