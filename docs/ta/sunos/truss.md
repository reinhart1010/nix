---
layout: page
title: sunos/truss (தமிழ்)
description: "சிஸ்டம் அழைப்புகளைத் தடமறிவதற்கான பிழைகாணல் கருவி."
content_hash: f3d5a61de522b1df4542addadb523009e9ba749b
related_topics:
  - title: English version
    url: /en/sunos/truss.html
    icon: bi bi-globe
---
# truss

சிஸ்டம் அழைப்புகளைத் தடமறிவதற்கான பிழைகாணல் கருவி.
ஸ்டிரேஸுக்குச் சமமான SunOS.
மேலும் விவரத்திற்கு: <https://www.unix.com/man-page/linux/1/truss>.

- அனைத்து குழந்தை செயல்முறைகளையும் பின்பற்றி, அதை செயல்படுத்துவதன் மூலம் ஒரு நிரலைக் கண்டறியத் தொடங்குங்கள்:

`truss -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்</span>

- ஒரு குறிப்பிட்ட செயல்முறையை அதன் PID மூலம் கண்டறியத் தொடங்குங்கள்:

`truss -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- ஒரு நிரலை இயக்குவதன் மூலம், வாதங்கள் மற்றும் சூழல் மாறிகளைக் காண்பிப்பதன் மூலம் அதைக் கண்டுபிடிக்கத் தொடங்குங்கள்:

`truss -a -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்</span>

- ஒவ்வொரு கணினி அழைப்பிற்கும் நேரம், அழைப்புகள் மற்றும் பிழைகளை எண்ணி, நிரல் வெளியேறும் போது சுருக்கத்தைப் புகாரளிக்கவும்:

`truss -c -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- கணினி அழைப்பின் மூலம் செயல்முறை வடிகட்டுதல் வெளியீட்டைக் கண்டறியவும்:

`truss -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">அமைப்பின்_அழைப்பு_பெயர்</span>
