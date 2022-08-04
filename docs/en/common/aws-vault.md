---
layout: page
title: common/aws-vault (English)
description: "A vault for securely storing and accessing AWS credentials in development environments."
content_hash: ebd8c0159ad12250b568d3e0cca472f428499288
related_topics:
  - title: Deutsch version
    url: /de/common/aws-vault.html
    icon: bi bi-globe
---
# aws-vault

A vault for securely storing and accessing AWS credentials in development environments.
More information: <https://github.com/99designs/aws-vault>.

- Add credentials to the secure keystore:

`aws-vault add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile</span>

- Execute a command with AWS credentials in the environment:

`aws-vault exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws s3 ls</span>

- Open a browser window and login to the AWS Console:

`aws-vault login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile</span>

- List profiles, along with their credentials and sessions:

`aws-vault list`

- Rotate AWS credentials:

`aws-vault rotate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile</span>

- Remove credentials from the secure keystore:

`aws-vault remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile</span>
