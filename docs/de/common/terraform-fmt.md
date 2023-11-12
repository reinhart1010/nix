---
layout: page
title: common/terraform-fmt (Deutsch)
description: "Formatierung der Konfiguration gemäß den Konventionen der Terraform-Sprache."
content_hash: d22d7acd9cd7b0d7fbfab0fc762cd8d89da877f8
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/terraform-fmt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# terraform fmt

Formatierung der Konfiguration gemäß den Konventionen der Terraform-Sprache.
Weitere Informationen: <https://www.terraform.io/docs/commands/fmt.html>.

- Formatieren der Konfiguration im aktuellen Verzeichnis:

`terraform fmt`

- Formatieren der Konfiguration im aktuellen Verzeichnis und den Unterverzeichnissen:

`terraform fmt -recursive`

- Anzeige der Unterschiede bei Formatierungsänderungen:

`terraform fmt -diff`

- Die Dateien mit Formatierungsinkonsistenzen werden nicht auf `stdout` ausgegeben:

`terraform fmt -list=false`
