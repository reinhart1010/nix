---
layout: page
title: common/auditd (français)
description: "Réponds aux requêtes depuis l'outil d'audition et de notifications du kernel."
content_hash: 00d9d5ce7eb025ab68aa7bc5128d28a020e8b9e1
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/auditd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# auditd

Réponds aux requêtes depuis l'outil d'audition et de notifications du kernel.
Il ne doit pas être utilisé manuellement.
Plus d'informations : <https://manned.org/auditd>.

- Démarre le démon :

`auditd`

- Démarre le démon en mode débogage :

`auditd -d`

- Démarre le démon à la demande depuis launchd :

`auditd -l`
