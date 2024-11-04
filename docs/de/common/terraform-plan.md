---
layout: page
title: common/terraform-plan (Deutsch)
description: "Erzeugen und Anzeigen von Terraform-Ausführungsplänen."
content_hash: e01b8b0d39110322e5c1fb653247909df713ff75
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/terraform-plan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# terraform plan

Erzeugen und Anzeigen von Terraform-Ausführungsplänen.
Weitere Informationen: <https://developer.hashicorp.com/terraform/cli/commands/plan>.

- Erzeugen und Anzeigen des Ausführungsplans im aktuellen Verzeichnis:

`terraform plan`

- Einen Plan zur Zerstörung aller derzeit existierenden entfernten Objekte anzeigen:

`terraform plan -destroy`

- Anzeigen eines Plans zur Aktualisierung des Terraform-Status und der Ausgabewerte:

`terraform plan -refresh-only`

- Werte für Eingabevariablen festlegen:

`terraform plan -var '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name1</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wert1</span>`' -var '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name2</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wert2</span>`'`

- Anzeigen eines Plans auf eine Teilmenge von Ressourcen:

`terraform plan -target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_type.resource_name[index]</span>

- Ausgabe eines Plans als JSON:

`terraform plan -json`

- Ausgabe eines Plans in eine separate Datei:

`terraform plan -no-color > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>
