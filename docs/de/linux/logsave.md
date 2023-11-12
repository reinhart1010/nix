---
layout: page
title: linux/logsave (Deutsch)
description: "Speichert die Ausgabe eines Befehls in eine Logdatei."
content_hash: 88fffd493cd277bce94de3035b71aa818df06cf3
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/logsave.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/logsave.html
    icon: bi bi-globe
tldri18n_status: 2
---
# logsave

Speichert die Ausgabe eines Befehls in eine Logdatei.
Weitere Informationen: <https://manned.org/logsave>.

- Führe einen Befehl mit angegebenen Argumenten aus und speichere die Ausgabe in eine Logdatei:

`logsave `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/logdatei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>

- Übernimm die Eingabe der Standardeingabe und speichere diese in eine Logdatei:

`logsave `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logdatei</span>` -`

- Hänge die Ausgabe an eine Logdatei an, anstatt deren aktuellen Inhalt zu ersetzen:

`logsave -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>

- Zeige die ausführliche Ausgabe an:

`logsave -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>
