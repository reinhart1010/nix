---
layout: page
title: linux/urpme (English)
description: "Uninstall packages in Mageia."
content_hash: de2e25753319e058b12de3f4c38b410a370bea68
last_modified_at: 2024-01-15
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/urpme.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># urpme

Uninstall packages in Mageia.
See also: `urpmi`, `urpmi.update`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmf`, `urpmq`.
More information: <https://wiki.mageia.org/en/URPMI#urpme>.

- Uninstall a package:

`sudo urpme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Uninstall orphan packages (Note: use it with caution as it might unintentionally remove important packages):

`sudo urpme --auto-orphans`

- Uninstall a package and its dependencies:

`sudo urpme --auto-orphans `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>
