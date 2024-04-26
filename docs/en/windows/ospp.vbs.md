---
layout: page
title: windows/ospp.vbs (English)
description: "Install, activate, and manage volume licensed versions of Microsoft Office products."
content_hash: 05ea871b5f11a866356351dfef3afbce43eba4bf
last_modified_at: 2024-04-26
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/ospp.vbs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ospp.vbs

Install, activate, and manage volume licensed versions of Microsoft Office products.
Note: this command may override, deactivate, and/or remove your current volume of licensed Office product versions, so please proceed cautiously.
More information: <https://learn.microsoft.com/deployoffice/vlactivation/tools-to-manage-volume-activation-of-office>.

- Install a product key (Note: it replaces the existing key):

`cscript ospp.vbs /inpkey:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">product_key</span>

- Uninstall an installed product key with the last five digits of the product key:

`cscript ospp.vbs /unpkey:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">product_key_digits</span>

- Set a KMS host name:

`cscript ospp.vbs /sethst:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip|hostname</span>

- Set a KMS port:

`cscript ospp.vbs /setprt:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Activate installed Office product keys:

`cscript ospp.vbs /act`

- Display license information for installed product keys:

`cscript ospp.vbs /dstatus`
