---
layout: post
title: "Apply cpplint to the visual studio"
date: 2017-12-01
---

cpplint.py is a code style examination tool for the checking of google C++ style

1. Tools - External tools - Add - Title：cpplint - Command：C:\Python27\python.exe - Arguments：C:\cpplint\cpplint.py --filter=-readability/utf8 --output=vs7 $(ItemPath) - Initial Directory：$(ItemDir) - Use Output Window。

2. Tools - Options - Environment - Keyboard - Show commands containing：external - Tools.ExternalCommand1 - Press shortcut keys：Alt+L，其中ExternalCommand6是根据1中Add的顺序来定的。
