---
layout: page
title: common/aws-history (Indonesia)
description: "Tampilkan riwayat pemanggilan perintah dalam AWS CLI (fitur perekaman riwayat perintah AWS CLI harus diaktifkan terlebih dahulu)."
content_hash: 566177c5e0841eb317833b4b5fdd06833d0e0017
last_modified_at: 2024-10-25
related_topics:
  - title: English version
    url: /en/common/aws-history.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-history.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aws-history.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-history.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws history

Tampilkan riwayat pemanggilan perintah dalam AWS CLI (fitur perekaman riwayat perintah AWS CLI harus diaktifkan terlebih dahulu).
Informasi lebih lanjut: <https://docs.aws.amazon.com/cli/latest/reference/history/>.

- Tampilkan daftar riwayat perintah yang dipanggil melalui AWS CLI beserta nomor induknya (command ID):

`aws history list`

- Tampilkan daftar kejadian yang berkaitan dengan suatu perintah berdasarkan nomor induknya (command ID):

`aws history show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_id</span>
