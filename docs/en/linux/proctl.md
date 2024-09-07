---
layout: page
title: linux/proctl (English)
description: "Manage projects licenses and languages, switch between templated licenses."
content_hash: 452623f4884595be1d40b16c674d9fb1140e1cde
last_modified_at: 2024-09-07
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/proctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># proctl

Manage projects licenses and languages, switch between templated licenses.
More information: <https://github.com/HeCodes2Much/proctl>.

- List available licenses:

`proctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-ll|-list-licenses</span>

- List available languages:

`proctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-lL|-list-languages</span>

- Pick a license in a FZF menu:

`proctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-pl|-pick-license</span>

- Pick a language in a FZF menu:

`proctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-pL|-pick-language</span>

- Remove all licenses from the current project:

`proctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|-remove-license</span>

- Create a new license template:

`proctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|-new-template</span>

- Delete a license from templates:

`proctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-R|-delete-license</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@license_name1 @license_name2 ...</span>

- Show this helpful list of commands:

`proctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|-help</span>
