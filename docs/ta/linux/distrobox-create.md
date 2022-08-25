---
layout: page
title: linux/distrobox-create (தமிழ்)
description: "உள்ளீட்டு பெயர் மற்றும் படத்துடன் டிஸ்ட்ரோபாக்ஸ் கொள்கலன்களை உருவாக்கவும்."
content_hash: 283f8158b8f0b2ad88f063610e7f466a88f3a100
related_topics:
  - title: English version
    url: /en/linux/distrobox-create.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># distrobox-create

உள்ளீட்டு பெயர் மற்றும் படத்துடன் டிஸ்ட்ரோபாக்ஸ் கொள்கலன்களை உருவாக்கவும்.
உருவாக்கப்பட்ட கொள்கலன் ஹோஸ்டுடன் இறுக்கமாக ஒருங்கிணைக்கப்படும், இது பயனரின் HOME கோப்பகம், வெளிப்புற சேமிப்பு, வெளிப்புற USB சாதனங்கள் மற்றும் வரைகலை பயன்பாடுகள் (X11/Wayland) மற்றும் ஆடியோவைப் பகிர அனுமதிக்கிறது.
மேலும் விவரத்திற்கு: <https://distrobox.privatedns.org>.

- ஆல்பைன் படத்தைப் பயன்படுத்தி டிஸ்ட்ரோபாக்ஸை உருவாக்கவும்:

`distrobox-create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கொள்கலன்_பெயர்</span>` --image alpine`

- ஒரு டிஸ்ட்ரோபாக்ஸ் குளோன்:

`distrobox-create --clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கொள்கலன்_பெயர்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">குளோன்_செய்யப்பட்ட_கன்டெய்னர்_பெயர்</span>
