---
layout: page
title: windows/choco-uninstall (தமிழ்)
description: "சாக்லேட்டியுடன் ஒன்று அல்லது அதற்கு மேற்பட்ட தொகுப்புகளை நிறுவல் நீக்கவும்."
content_hash: 7c4ba87943f72df4138cdc6071dd8ca6f11b21c0
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-uninstall.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-uninstall.html
    icon: bi bi-globe
  - title: français version
    url: /fr/windows/choco-uninstall.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-uninstall.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-uninstall.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-uninstall.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco uninstall

சாக்லேட்டியுடன் ஒன்று அல்லது அதற்கு மேற்பட்ட தொகுப்புகளை நிறுவல் நீக்கவும்.
மேலும் விவரத்திற்கு: <https://chocolatey.org/docs/commands-uninstall>.

- ஒன்று அல்லது அதற்கு மேற்பட்ட இடம் பிரிக்கப்பட்ட தொகுப்புகளை நிறுவல் நீக்கவும்:

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு(கள்)</span>

- தொகுப்பின் குறிப்பிட்ட பதிப்பை நிறுவல் நீக்கவும்:

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பதிப்பு</span>

- அனைத்து அறிவுறுத்தல்களையும் தானாக உறுதிப்படுத்தவும்:

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு</span>` --yes`

- நிறுவல் நீக்கும் போது அனைத்து சார்புகளையும் நீக்கவும்:

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு</span>` --remove-dependencies`

- அனைத்து தொகுப்புகளையும் நிறுவல் நீக்கவும்:

`choco uninstall all`
