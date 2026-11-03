#!/usr/bin/env python3
"""Wrap app.html (the page body, also used for the Claude preview) into a standalone index.html."""
from pathlib import Path

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Drive Chart">
<meta name="theme-color" content="#161e19" media="(prefers-color-scheme: dark)">
<meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">
<style>
:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);-webkit-text-size-adjust:100%;text-size-adjust:100%}
body{margin:0}
img{max-width:100%}
[hidden]{display:none!important}
</style>
</head>
<body>
"""
FOOT = "\n</body>\n</html>\n"

root = Path(__file__).parent
(root / "index.html").write_text(HEAD + (root / "app.html").read_text() + FOOT)
print("wrote index.html")
