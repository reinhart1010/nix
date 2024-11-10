---
layout: page
title: common/aws-acm (Indonesia)
description: "AWS Certificate Manager, manajer sertifikat digital untuk AWS."
content_hash: 800170d10ae6c0d9b38baf8d30ab93caf2efd3a4
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/aws-acm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aws-acm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aws-acm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws acm

AWS Certificate Manager, manajer sertifikat digital untuk AWS.
Informasi lebih lanjut: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/index.html>.

- Impor suatu sertifikat:

`aws acm import-certificate --certificate-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arn_sertifikat</span>` --certificate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sertifikat</span>` --private-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kunci_privat</span>` --certificate-chain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rantai_sertifikat</span>

- Tampilkan daftar sertifikat:

`aws acm list-certificates`

- Tampilkan deskripsi suatu sertifikat:

`aws acm describe-certificate --certificate-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arn_sertifikat</span>

- Minta sertifikat baru bagi suatu domain:

`aws acm request-certificate --domain-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_domain</span>` --validation-method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">metode_validasi</span>

- Hapus suatu sertifikat:

`aws acm delete-certificate --certificate-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arn_sertifikat</span>

- Tampilkan daftar status pengajuan validasi sertifikat:

`aws acm list-certificates --certificate-statuses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">status</span>

- Dapatkan informasi rincian suatu sertifikat:

`aws acm get-certificate --certificate-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arn_sertifikat</span>

- Mutakhirkan pengaturan terhadap suatu sertifikat:

`aws acm update-certificate-options --certificate-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arn_sertifikat</span>` --options `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pengaturan</span>
