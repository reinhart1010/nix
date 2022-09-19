---
layout: page
title: common/java (தமிழ்)
description: "ஜாவா பயன்பாட்டு துவக்கி."
content_hash: ae1f0f0701b1acdeb496a1dfea29b10d4d38d692
related_topics:
  - title: English version
    url: /en/common/java.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/java.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/java.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/java.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/java.html
    icon: bi bi-globe
---
# java

ஜாவா பயன்பாட்டு துவக்கி.
மேலும் விவரத்திற்கு: <https://docs.oracle.com/en/java/javase/17/docs/specs/man/java.html>.

- ஜாவா `.class` கோப்பை இயக்கவும், அதில் ஒரு முக்கிய முறையைக் கொண்டு, வகுப்புப் பெயரை மட்டும் பயன்படுத்தவும்:

`java `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">வகுப்பு_பெயர்</span>

- ஒரு ஜாவா நிரலை இயக்கவும் மற்றும் கூடுதல் மூன்றாம் தரப்பு அல்லது பயனர் வரையறுக்கப்பட்ட வகுப்புகளைப் பயன்படுத்தவும்:

`java -classpath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/வகுப்புகள்1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/வகுப்புகள்2</span>`:. `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">வகுப்புபெயர்</span>

- ஒரு `.jar` நிரலை இயக்கவும்:

`java -jar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்புபெயர்.jar</span>

- போர்ட் 5005 இல் இணைக்க காத்திருக்கும் பிழைத்திருத்தத்துடன் `.jar` நிரலை இயக்கவும்:

`java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்புபெயர்.jar</span>

- JDK, JRE மற்றும் HotSpot பதிப்புகளைக் காண்பி:

`java -version`

- ஜாவா கட்டளைக்கான பயன்பாட்டுத் தகவலைக் காண்பி:

`java -help`
