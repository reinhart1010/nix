---
layout: page
title: common/aws-s3 (italiano)
description: "CLI per AWS S3 - fornisce spazio di archiviazione tramite le interfacce di Amazon Web Services."
content_hash: 8581cd1481a8850b215e5c6ed73f08535f0d0898
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/aws-s3.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aws-s3.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-s3.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aws-s3.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-s3.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws s3

CLI per AWS S3 - fornisce spazio di archiviazione tramite le interfacce di Amazon Web Services.
Maggiori informazioni: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/index.html>.

- Mostra file in un bucket:

`aws s3 ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_bucket</span>

- Sincronizza file e directory locali su un bucket:

`aws s3 sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/dei/file</span>` s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_bucket</span>

- Sincronizza file e directory da un bucket in locle:

`aws s3 sync s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_bucket</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_cartella</span>

- Sincronizza file e directory escludendo alcuni file o directory:

`aws s3 sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/dei/file</span>` s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_bucket</span>` --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>` --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory</span>`/*`

- Rimuovi un file dal bucket:

`aws s3 rm s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>

- Mostra solo un'anteprima dei cambiamenti:

`aws s3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">qualsiasi_comando</span>` --dryrun`
