---
layout: page
title: linux/urpme (English)
description: "Uninstall packages in Mageia."
content_hash: de2e25753319e058b12de3f4c38b410a370bea68
last_modified_at: 2024-01-16
tldri18n_status: 2
---
# urpme

Uninstall packages in Mageia.
See also: `urpmi`, `urpmi.update`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmf`, `urpmq`.
More information: <https://wiki.mageia.org/en/URPMI#urpme>.

- Uninstall a package:

`sudo urpme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Uninstall orphan packages (Note: use it with caution as it might unintentionally remove important packages):

`sudo urpme --auto-orphans`

- Uninstall a package and its dependencies:

`sudo urpme --auto-orphans `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>
