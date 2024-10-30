---
layout: page
title: common/npm-adduser (English)
description: "Add a registry user account."
content_hash: 071ac12f24a53507c8f90276caf31b0005dd403f
last_modified_at: 2024-10-30
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/npm-adduser.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># npm adduser

Add a registry user account.
More information: <https://docs.npmjs.com/cli/npm-adduser>.

- Create a new user in the specified registry and save credentials to `.npmrc`:

`npm adduser --registry=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">registry_url</span>

- Log in to a private registry with a specific scope:

`npm login --scope=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@mycorp</span>` --registry=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://registry.mycorp.com</span>

- Log out from a specific scope and remove the auth token:

`npm logout --scope=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@mycorp</span>

- Create a scoped package during initialization:

`npm init --scope=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@foo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--yes</span>
