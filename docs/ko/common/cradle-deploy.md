---
layout: page
title: common/cradle-deploy (한국어)
description: "Cradle 배포 관리."
content_hash: 118572ae645d31b8a3cf80b73597cfcb90e5d9cc
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/cradle-deploy.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cradle-deploy.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cradle-deploy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cradle deploy

Cradle 배포 관리.
더 많은 정보: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#deploy>.

- 서버에 Cradle을 배포:

`cradle deploy production`

- 아마존 S3에 정적 자산 배포:

`cradle deploy s3`

- Yarn "components" 디렉토리를 포함하여 정적 자산 배포:

`cradle deploy s3 --include-yarn`

- "upload" 디렉토리를 포함한 정적 자산 배포:

`cradle deploy s3 --include-upload`
