---
layout: page
title: common/snyk (English)
description: "Find vulnerabilities in your code and remediate risks."
content_hash: d9db635388861d2094362df410c2e4539ca13f02
---
# snyk

Find vulnerabilities in your code and remediate risks.
More information: <https://snyk.io>.

- Log in to your Snyk account:

`snyk auth`

- Test your code for any known vulnerabilities:

`snyk test`

- Test a local Docker image for any known vulnerabilities:

`snyk test --docker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">docker_image</span>

- Record the state of dependencies and any vulnerabilities on snyk.io:

`snyk monitor`

- Auto patch and ignore vulnerabilities:

`snyk wizard`
