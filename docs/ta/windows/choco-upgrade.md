---
layout: page
title: windows/choco-upgrade (தமிழ்)
description: "சாக்லேட்டியுடன் ஒன்று அல்லது அதற்கு மேற்பட்ட தொகுப்புகளை மேம்படுத்தவும்."
content_hash: 906f18adbbe17bb4d602b8ebde97ddd042265390
last_modified_at: 2022-12-03
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-upgrade.html
    icon: bi bi-globe
---
# choco upgrade

சாக்லேட்டியுடன் ஒன்று அல்லது அதற்கு மேற்பட்ட தொகுப்புகளை மேம்படுத்தவும்.
மேலும் விவரத்திற்கு: <https://chocolatey.org/docs/commands-upgrade>.

- ஒன்று அல்லது அதற்கு மேற்பட்ட இடம் பிரிக்கப்பட்ட தொகுப்புகளை மேம்படுத்தவும்:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு(கள்)</span>

- தொகுப்பின் குறிப்பிட்ட பதிப்பிற்கு மேம்படுத்தவும்:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பதிப்பு</span>

- அனைத்து தொகுப்புகளையும் மேம்படுத்தவும்:

`choco upgrade all`

- குறிப்பிட்ட காற்புள்ளியால் பிரிக்கப்பட்ட தொகுப்புகளைத் தவிர அனைத்தையும் மேம்படுத்தவும்:

`choco upgrade all --except "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு(கள்)</span>`"`

- அனைத்து அறிவுறுத்தல்களையும் தானாக உறுதிப்படுத்தவும்:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு</span>` --yes`

- தொகுப்புகளைப் பெற தனிப்பயன் மூலத்தைக் குறிப்பிடவும்:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூல_முகவரி|alias</span>

- அங்கீகாரத்திற்கான பயனர்பெயர் மற்றும் கடவுச்சொல்லை வழங்கவும்:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பயனர்பெயர்</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கடவுச்சொல்</span>
