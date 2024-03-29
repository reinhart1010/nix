---
layout: page
title: common/ssh-agent (Deutsch)
description: "Erstelle einen SSH Agenten-Prozess."
content_hash: 1d985d1dcd50be64bbc1b9172411e89424f9dc03
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ssh-agent.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ssh-agent.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ssh-agent.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ssh-agent

Erstelle einen SSH Agenten-Prozess.
Ein SSH Agent behält die hinzugefügten SSH Schlüssel solange verschlüsselt im Arbeitsspeicher, bis diese entfernt werden oder der Agenten-Prozess beendet wird.
Siehe auch `ssh-add`, um Schlüssel zu verwalten.
Weitere Informationen: <https://man.openbsd.org/ssh-agent>.

- Starte einen SSH Agenten-Prozesses für die aktuelle Shell:

`eval $(ssh-agent)`

- Beende den aktuell laufenden SSH Agenten-Prozesses:

`ssh-agent -k`
