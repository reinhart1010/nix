---
layout: page
title: common/aws-ec2 (Deutsch)
description: "CLI für AWS EC2."
content_hash: 121c66c61fa1373cda3de5b9a8cba8e099517215
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/aws-ec2.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aws-ec2.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-ec2.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-ec2.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws ec2

CLI für AWS EC2.
AWS EC2 stellt eine sichere und skalierbare Einheit in der AWS Cloud zur Verfügung, um ein schnelleres Entwickeln und Ausrollen von Software zu ermöglichen.
Weitere Informationen: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html>.

- Liste Informationen zu einer bestimmten Instanz auf:

`aws ec2 describe-instances --instance-ids `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instanz_id</span>

- Liste Informationen zu allen Instanzen auf:

`aws ec2 describe-instances`

- Liste Informationen zu allen EC2 Volumen auf:

`aws ec2 describe-volumes`

- Lösche ein EC2 Volumen:

`aws ec2 delete-volume --volume-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volumen_id</span>

- Erstelle einen Snapshot basierend auf einem EC2 Volumen:

`aws ec2 create-snapshot --volume-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volumen_id</span>

- Liste alle verfügbaren AMIs (Amazon Machine Images) auf:

`aws ec2 describe-images`

- Liste alle verfügbaren EC2 Befehle auf:

`aws ec2 help`

- Zeige Hilfe für bestimmte EC2 Unterbefehle an:

`aws ec2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unterbefehl</span>` help`
