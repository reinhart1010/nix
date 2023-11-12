---
layout: page
title: common/cradle-deploy (English)
description: "Manage Cradle deployments."
content_hash: d64119108f0997778626255fcce4b31ba379bac9
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/cradle-deploy.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cradle-deploy.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cradle-deploy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cradle deploy

Manage Cradle deployments.
More information: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#deploy>.

- Deploy Cradle to a server:

`cradle deploy production`

- Deploy static assets to Amazon S3:

`cradle deploy s3`

- Deploy static assets including the Yarn "components" directory:

`cradle deploy s3 --include-yarn`

- Deploy static assets including the "upload" directory:

`cradle deploy s3 --include-upload`
