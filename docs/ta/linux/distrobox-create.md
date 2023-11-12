---
layout: page
title: linux/distrobox-create (தமிழ்)
description: "உள்ளீட்டு பெயர் மற்றும் படத்துடன் டிஸ்ட்ரோபாக்ஸ் கொள்கலன்களை உருவாக்கவும்."
content_hash: de008a772e37344c52dd745ec50e6d638ffa12c7
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/distrobox-create.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/distrobox-create.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/distrobox-create.html
    icon: bi bi-globe
tldri18n_status: 2
---
# distrobox-create

உள்ளீட்டு பெயர் மற்றும் படத்துடன் டிஸ்ட்ரோபாக்ஸ் கொள்கலன்களை உருவாக்கவும்.
உருவாக்கப்பட்ட கொள்கலன் ஹோஸ்டுடன் இறுக்கமாக ஒருங்கிணைக்கப்படும், இது பயனரின் வீட்டு அடைவு, வெளிப்புற சேமிப்பு, வெளிப்புற USB சாதனங்கள், வரைகலை பயன்பாடுகள் (X11/Wayland) மற்றும் ஒலியைப் பகிர அனுமதிக்கிறது.
மேலும் விவரத்திற்கு: <https://distrobox.privatedns.org/usage/distrobox-create.html>.

- உபுண்டு படத்தைப் பயன்படுத்தி டிஸ்ட்ரோபாக்ஸ் கொள்கலனை உருவாக்கவும்:

`distrobox-create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கொள்கலன்_பெயர்</span>` --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ubuntu:latest</span>

- ஒரு டிஸ்ட்ரோபாக்ஸ் கொள்கலனை நகல் செய்யுங்கள்:

`distrobox-create --clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கொள்கலன்_பெயர்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நகல்_செய்யப்பட்ட_கொள்கலன்_பெயர்</span>
