---
layout: page
title: linux/unopkg (English)
description: "LibreOffice extensions manager."
content_hash: fd0823f3cb69f0b389721a261caef99f8a5998aa
last_modified_at: 2024-10-11
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/unopkg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># unopkg

LibreOffice extensions manager.
Download extensions from <https://extensions.libreoffice.org>.
See also: `libreoffice`.
More information: <https://manned.org/unopkg>.

- Add and deploy given extension:

`unopkg add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/extension</span>

- Remove extension:

`unopkg remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">extensions_id</span>

- Display information about deployed extensions:

`unopkg list`

- Raise extensions dialog (GUI):

`unopkg gui`

- Reinstall all deployed extensions:

`unopkg reinstall`

- Display help:

`unopkg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
