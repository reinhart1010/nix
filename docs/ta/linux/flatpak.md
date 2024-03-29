---
layout: page
title: linux/flatpak (தமிழ்)
description: "பிளாட்பேக் பயன்பாடுகள் மற்றும் இயக்க நேரங்களை உருவாக்கவும், நிறுவவும் மற்றும் இயக்கவும்."
content_hash: efebfcf4529218ccf8ee40ae2dc1f3abb7d2ad40
last_modified_at: 2023-11-15
related_topics:
  - title: English version
    url: /en/linux/flatpak.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/flatpak.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/flatpak.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/flatpak.html
    icon: bi bi-globe
tldri18n_status: 2
---
# flatpak

பிளாட்பேக் பயன்பாடுகள் மற்றும் இயக்க நேரங்களை உருவாக்கவும், நிறுவவும் மற்றும் இயக்கவும்.
மேலும் விவரத்திற்கு: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak>.

- நிறுவப்பட்ட பயன்பாட்டை இயக்கவும்:

`flatpak run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பெயர்</span>

- தொலைநிலை மூலத்திலிருந்து பயன்பாட்டை நிறுவவும்:

`flatpak install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ரிமோட்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பெயர்</span>

- நிறுவப்பட்ட அனைத்து பயன்பாடுகளையும் இயக்க நேரங்களையும் பட்டியலிடுங்கள்:

`flatpak list`

- நிறுவப்பட்ட அனைத்து பயன்பாடுகளையும் இயக்க நேரங்களையும் புதுப்பிக்கவும்:

`flatpak update`

- தொலைநிலை மூலத்தைச் சேர்க்கவும்:

`flatpak remote-add --if-not-exists `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ரிமோட்_பெயர்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ரிமோட்_முகவரி</span>

- நிறுவப்பட்ட பயன்பாட்டை அகற்றவும்:

`flatpak remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பெயர்</span>

- பயன்படுத்தப்படாத அனைத்து பயன்பாடுகளையும் அகற்றவும்:

`flatpak remove --unused`

- நிறுவப்பட்ட பயன்பாட்டைப் பற்றிய தகவலைக் காட்டு:

`flatpak info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பெயர்</span>
