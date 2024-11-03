---
layout: page
title: common/npm-star (English)
description: "Mark a package as favorite."
content_hash: b9a5c7876b8810e6a8004df9be6563b6d0ef250b
last_modified_at: 2024-11-03
tldri18n_status: 2
---
# npm star

Mark a package as favorite.
More information: <https://docs.npmjs.com/cli/commands/npm-star>.

- Star a public package from the default registry:

`npm star `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Star a package within a specific scope:

`npm star @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scope</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Star a package from a specific registry:

`npm star `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>` --registry=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">registry_url</span>

- Star a private package that requires authentication:

`npm star `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>` --auth-type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">legacy|oauth|web|saml</span>

- Star a package by providing an OTP for two-factor authentication:

`npm star `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>` --otp=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">otp</span>

- Star a package with detailed logging:

`npm star `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>` --loglevel=verbose`

- List all your starred packages:

`npm star --list`

- List your starred packages from a specific registry:

`npm star --list --registry=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">registry_url</span>
