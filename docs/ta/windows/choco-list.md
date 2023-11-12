---
layout: page
title: windows/choco-list (தமிழ்)
description: "சாக்லேட்டியுடன் ஒன்று அல்லது அதற்கு மேற்பட்ட தொகுப்புகளை நிறுவவும்."
content_hash: b0bbe8192ea93c5fcc43013dd41f323c69daff70
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-list.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-list.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-list.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-list.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-list.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco list

சாக்லேட்டியுடன் ஒன்று அல்லது அதற்கு மேற்பட்ட தொகுப்புகளை நிறுவவும்.
மேலும் விவரத்திற்கு: <https://chocolatey.org/docs/commands-list>.

- கிடைக்கக்கூடிய அனைத்து தொகுப்புகளையும் காண்பி:

`choco list`

- உள்நாட்டில் நிறுவப்பட்ட அனைத்து தொகுப்புகளையும் காண்பி:

`choco list --local-only`

- உள்ளூர் நிரல்களை உள்ளடக்கிய பட்டியலைக் காண்பி:

`choco list --include-programs`

- அங்கீகரிக்கப்பட்ட தொகுப்புகளை மட்டும் காண்பி:

`choco list --approved-only`

- இதிலிருந்து தொகுப்புகளைக் காண்பிக்க தனிப்பயன் மூலத்தைக் குறிப்பிடவும்:

`choco list --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூல_முகவரி|alias</span>

- அங்கீகாரத்திற்கான பயனர்பெயர் மற்றும் கடவுச்சொல்லை வழங்கவும்:

`choco list --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பயனர்பெயர்</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கடவுச்சொல்</span>
