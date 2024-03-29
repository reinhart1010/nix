---
layout: page
title: linux/bluetoothctl (മലയാളം)
description: "കമാൻഡ് ലൈനിൽ നിന്ന് ബ്ലൂടൂത്ത് ഉപകരണങ്ങൾ മാനേജുചെയ്യുക."
content_hash: 9d29b05a9bfff818cb9770e3fef5d467493687d8
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/bluetoothctl.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/bluetoothctl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/bluetoothctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/bluetoothctl.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bluetoothctl

കമാൻഡ് ലൈനിൽ നിന്ന് ബ്ലൂടൂത്ത് ഉപകരണങ്ങൾ മാനേജുചെയ്യുക.
കൂടുതൽ വിവരങ്ങൾ: <https://bitbucket.org/serkanp/bluetoothctl>.

- ബ്ലൂടൂത്ത്സിറ്റിഎൽ ഷെല്ലിൽ കേറാൻ:

`bluetoothctl`

- ഉപകരണങ്ങളുടെ പട്ടിക കാണാൻ:

`bluetoothctl --devices`

- ഒരു ഉപകരണം ജോടിയാക്കുക:

`bluetoothctl --pair `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">മാക്_വിലാസം</span>

- ഒരു ഉപകരണം നീക്കംചെയ്യുക:

`bluetoothctl --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">മാക്_വിലാസം</span>

- ജോഡിയായ ഉപകരണവുമായി ബന്ധിപ്പിക്കുക:

`bluetoothctl --connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">മാക്_വിലാസം</span>

- ഒരു ജോഡിയായ ഉപകരണവുമായുള്ള ബന്ധം വിച്ഛേദിക്കുക:

`bluetoothctl --disconnect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">മാക്_വിലാസം</span>
