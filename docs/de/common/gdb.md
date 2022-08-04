---
layout: page
title: common/gdb (Deutsch)
description: "Der GNU Debugger."
content_hash: 4508a762c84a94e6c160955c7075bd9c93375c23
related_topics:
  - title: English version
    url: /en/common/gdb.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/gdb.html
    icon: bi bi-globe
---
# gdb

Der GNU Debugger.
Weitere Informationen: <https://www.gnu.org/software/gdb>.

- Debugge eine ausführbare Datei:

`gdb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ausführbare_datei</span>

- Binde einen Prozess an gdb:

`gdb -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prozess_ID</span>

- Debugge mit einer Kerndatei:

`gdb -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kerndatei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ausführbare_datei</span>

- Führe angegebene Befehle beim Start von gdb aus:

`gdb -ex "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehle</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ausführbare_datei</span>

- Starte gdb und übergib Argumente an die ausführbare Datei:

`gdb --args `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ausführbare_datei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument2</span>
