---
layout: page
title: common/pulumi-login (español)
description: "Inicia sesión en Pulumi Cloud."
content_hash: 21e333cc08c0106234acbb901d76a92e8d5a7775
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/pulumi-login.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pulumi-login.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pulumi login

Inicia sesión en Pulumi Cloud.
Más información: <https://www.pulumi.com/docs/cli/commands/pulumi_login/>.

- Inicia sesión en el servidor administrado Pulumi Cloud, de manera predeterminada en `app.pulumi.cloud`:

`pulumi login`

- Inicia sesión en un backend Pulumi Cloud autoalojado en una URL especificada:

`pulumi login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Utiliza Pulumi localmente, independientemente de Pulumi Cloud:

`pulumi login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--local</span>
