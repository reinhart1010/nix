---
layout: page
title: common/pulumi-login (English)
description: "Log in to the Pulumi cloud."
content_hash: 3ef486dee35993b2c7482ba2cbc09e12869d7eff
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/pulumi-login.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/pulumi-login.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pulumi login

Log in to the Pulumi cloud.
More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_login/>.

- Log in to the managed Pulumi Cloud backend, defaults to `app.pulumi.cloud`:

`pulumi login`

- Log in to a self-hosted Pulumi Cloud backend on a specified URL:

`pulumi login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Use Pulumi locally, independent of a Pulumi Cloud:

`pulumi login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--local</span>
