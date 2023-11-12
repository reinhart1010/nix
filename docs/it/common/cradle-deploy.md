---
layout: page
title: common/cradle-deploy (italiano)
description: "Gestisci distribuzioni Cradle."
content_hash: 01df5260e88eabdeda03da29742a90800b7d5046
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/cradle-deploy.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cradle-deploy.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cradle-deploy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cradle deploy

Gestisci distribuzioni Cradle.
Maggiori informazioni: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#deploy>.

- Distribuisci Cradle su un server:

`cradle deploy production`

- Distribuisci assets statici ad Amazon S3:

`cradle deploy s3`

- Distribuisci assets statici, inclusa la directory "components" di Yarn:

`cradle deploy s3 --include-yarn`

- Distribuisci assets statici, includendo la directory "upload":

`cradle deploy s3 --include-upload`
