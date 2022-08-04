---
layout: page
title: linux/debsecan (English)
description: "Debian Security Analyzer, a tool to list vulnerabilities on a particular Debian installation."
content_hash: 0b3843c404894b92875d77367a7f1fad77cb4c32
---
# debsecan

Debian Security Analyzer, a tool to list vulnerabilities on a particular Debian installation.
More information: <https://gitlab.com/fweimer/debsecan>.

- List vulnerable installed packages on the current host:

`debsecan`

- List vulnerable installed packages of a specific suite:

`debsecan --suite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">release_code_name</span>

- List only fixed vulnerabilities:

`debsecan --suite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">release_code_name</span>` --only-fixed`

- List only fixed vulnerabilities of unstable ("sid") and mail to root:

`debsecan --suite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sid</span>` --only-fixed --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">report</span>` --mailto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">root</span>` --update-history`

- Upgrade vulnerable installed packages:

`sudo apt upgrade $(debsecan --only-fixed --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">packages</span>`)`
