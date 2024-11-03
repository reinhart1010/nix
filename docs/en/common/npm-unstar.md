---
layout: page
title: common/npm-unstar (English)
description: "Remove the favorite/star mark from a package."
content_hash: 33372c9893f8d3f2663ac93ea4c81abe943d2bd0
last_modified_at: 2024-11-03
tldri18n_status: 2
---
# npm unstar

Remove the favorite/star mark from a package.
More information: <https://docs.npmjs.com/cli/commands/npm-unstar>.

- Unstar a public package from the default registry:

`npm unstar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Unstar a package within a specific scope:

`npm unstar @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scope</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Unstar a package from a specific registry:

`npm unstar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>` --registry=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">registry_url</span>

- Unstar a private package that requires authentication:

`npm unstar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>` --auth-type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">legacy|oauth|web|saml</span>

- Unstar a package by providing an OTP for two-factor authentication:

`npm unstar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>` --otp=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">otp</span>

- Unstar a package with a specific logging level:

`npm unstar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>` --loglevel=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">silent|error|warn|notice|http|timing|info|verbose|silly</span>
