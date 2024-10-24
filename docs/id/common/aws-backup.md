---
layout: page
title: common/aws-backup (Indonesia)
description: "Layanan pencadangan untuk melindungi kumpulan layanan dan data terkait dalam Amazon Web Services."
content_hash: f294eeff91526bd71a6207708692be447d2518cf
last_modified_at: 2024-10-24
related_topics:
  - title: Deutsch version
    url: /de/common/aws-backup.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aws-backup.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aws-backup.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aws-backup.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aws backup

Layanan pencadangan untuk melindungi kumpulan layanan dan data terkait dalam Amazon Web Services.
Informasi lebih lanjut: <https://docs.aws.amazon.com/cli/latest/reference/backup/index.html>.

- Tampilkan rincian BackupPlan (rencana pemulihan layanan yang dicadangkan) berdasarkan nomor induknya:

`aws backup get-backup-plan --backup-plan-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nomor_induk</span>

- Buat suatu BackupPlan dengan nama dan aturan tertentu:

`aws backup create-backup-plan --backup-plan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rencana_pencadangan</span>

- Hapus suatu BackupPlan berdasarkan nomor induknya:

`aws backup delete-backup-plan --backup-plan-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nomor_induk</span>

- Tampilkan seluruh BackupPlan yang aktif dalam akun saat ini:

`aws backup list-backup-plans`

- Tampilkan rincian atas laporan pekerjaan pencadangan Anda:

`aws backup list-report-jobs`
