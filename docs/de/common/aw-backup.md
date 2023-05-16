---
layout: page
title: common/aw-backup (Deutsch)
description: "Einheitliches Backup-Service zum Schutz der Amazon Web Services und der damit verbundenen Daten."
content_hash: 43cdf85f267b453c10972bfea9d107441da48b28
last_modified_at: 2023-05-16
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws backup

Einheitliches Backup-Service zum Schutz der Amazon Web Services und der damit verbundenen Daten.
Weitere Informationen: <https://docs.aws.amazon.com/cli/latest/reference/backup/index.html>.

- Gib Backup-Plan-Details für eine bestimmte Backup-Plan-ID aus:

`aws backup get-backup-plan --backup-plan-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- Erstelle einen Backup-Plan unter Verwendung eines bestimmten Backup-Plan-Namens und von Backup-Regeln:

`aws backup create-backup-plan --backup-plan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plan</span>

- Lösche einen bestimmten Backup-Plan:

`aws backup delete-backup-plan --backup-plan-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- Gib eine Liste aller aktiven Backup-Pläne für das aktuelle Konto aus:

`aws backup list-backup-plans`

- Zeige Details über die Report-Aufträge an:

`aws backup list-report-jobs`
