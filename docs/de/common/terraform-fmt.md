---
layout: page
title: common/terraform-fmt (Deutsch)
description: "Formatierung der Konfiguration gemäß den Konventionen der Terraform-Sprache."
content_hash: d26aa212c8920372b5a9e3ea11631c52bec989a4
related_topics:
  - title: English version
    url: /en/common/terraform-fmt.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># terraform fmt

Formatierung der Konfiguration gemäß den Konventionen der Terraform-Sprache.
Weitere Informationen: <https://www.terraform.io/docs/commands/fmt.html>.

- Formatieren der Konfiguration im aktuellen Verzeichnis:

`terraform fmt`

- Formatieren der Konfiguration im aktuellen Verzeichnis und den Unterverzeichnissen:

`terraform fmt -recursive`

- Anzeige der Unterschiede bei Formatierungsänderungen:

`terraform fmt -diff`

- Die Dateien mit Formatierungsinkonsistenzen werden nicht auf stdout ausgegeben:

`terraform fmt -list=false`
