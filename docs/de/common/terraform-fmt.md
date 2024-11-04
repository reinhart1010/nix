---
layout: page
title: common/terraform-fmt (Deutsch)
description: "Formatierung der Konfiguration gemäß den Konventionen der Terraform-Sprache."
content_hash: 14c1a0dcbcc28facedc5d8de58b3f21a736928d5
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/terraform-fmt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# terraform fmt

Formatierung der Konfiguration gemäß den Konventionen der Terraform-Sprache.
Weitere Informationen: <https://developer.hashicorp.com/terraform/cli/commands/fmt>.

- Formatieren der Konfiguration im aktuellen Verzeichnis:

`terraform fmt`

- Formatieren der Konfiguration im aktuellen Verzeichnis und den Unterverzeichnissen:

`terraform fmt -recursive`

- Anzeige der Unterschiede bei Formatierungsänderungen:

`terraform fmt -diff`

- Die Dateien mit Formatierungsinkonsistenzen werden nicht auf `stdout` ausgegeben:

`terraform fmt -list=false`
