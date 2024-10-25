---
layout: page
title: common/aws-sts (Indonesia)
description: "Security Token Service (STS), layanan manajemen token keamanan untuk meminta akses akun sementara bagi pengguna (IAM) atau pengguna dari federasi."
content_hash: 6a82d2f6a34c9937d8d9741112d4f17522e87af4
last_modified_at: 2024-10-25
related_topics:
  - title: English version
    url: /en/common/aws-sts.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aws-sts.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-sts.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws sts

Security Token Service (STS), layanan manajemen token keamanan untuk meminta akses akun sementara bagi pengguna (IAM) atau pengguna dari federasi.
Informasi lebih lanjut: <https://docs.aws.amazon.com/cli/latest/reference/sts/>.

- Dapatkan kredensial keamanan sementara untuk mengakses sumber daya AWS tertentu:

`aws sts assume-role --role-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws_role_arn</span>

- Dapatkan nama pengguna IAM atau peran (role) pengguna yang terikat kepada kredensial untuk melakukan operasi pengaturan layanan AWS:

`aws sts get-caller-identity`
