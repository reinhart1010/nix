---
layout: page
title: common/aws-vault (Deutsch)
description: "Ein Tresor für Entwicklungsumgebungen, um AWS Sicherheitsschlüssel sicher speichern und abrufen zu können."
content_hash: 7c2d91220db5e9575e85d8671e02e4ed8ab778a9
related_topics:
  - title: English version
    url: /en/common/aws-vault.html
    icon: bi bi-globe
---
# aws-vault

Ein Tresor für Entwicklungsumgebungen, um AWS Sicherheitsschlüssel sicher speichern und abrufen zu können.
Weitere Informationen: <https://github.com/99designs/aws-vault>.

- Füge einen Sicherheitsschlüssel als Profil zu einem Tresor hinzu:

`aws-vault add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profil</span>

- Führe einen Befehl mit AWS Sicherheitsschlüsseln aus dem angegebenen Profil aus:

`aws-vault exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profil</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws s3 ls</span>

- Öffne ein Browserfenster für den Login in die AWS Konsole:

`aws-vault login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profil</span>

- Liste alle Profile zusammen mit deren Sicherheitsschlüsseln und Sitzungen auf:

`aws-vault list`

- Rotiere die AWS Sicherheitsschlüssel für ein Profil:

`aws-vault rotate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profil</span>

- Entferne Sicherheitsschlüsseln eines Profils aus dem Tresor:

`aws-vault remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profil</span>
