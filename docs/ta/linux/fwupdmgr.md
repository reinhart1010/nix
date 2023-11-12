---
layout: page
title: linux/fwupdmgr (தமிழ்)
description: "`fwupd` ஐப் பயன்படுத்தி UEFI உட்பட சாதன நிலைபொருளைப் புதுப்பிப்பதற்கான ஒரு கருவி."
content_hash: f33097cdb13114f039d7fcac311ded98d67f6f16
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/fwupdmgr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fwupdmgr

`fwupd` ஐப் பயன்படுத்தி UEFI உட்பட சாதன நிலைபொருளைப் புதுப்பிப்பதற்கான ஒரு கருவி.
மேலும் விவரத்திற்கு: <https://fwupd.org/>.

- fwupd மூலம் கண்டறியப்பட்ட அனைத்து சாதனங்களையும் காண்பி:

`fwupdmgr get-devices`

- LVFS இலிருந்து சமீபத்திய ஃபார்ம்வேர் மெட்டாடேட்டாவைப் பதிவிறக்கவும்:

`fwupdmgr refresh`

- உங்கள் கணினியில் உள்ள சாதனங்களுக்கு கிடைக்கும் புதுப்பிப்புகளை பட்டியலிடுங்கள்:

`fwupdmgr get-updates`

- ஃபார்ம்வேர் புதுப்பிப்புகளை நிறுவவும்:

`fwupdmgr update`
