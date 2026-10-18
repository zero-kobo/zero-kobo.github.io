#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ちいさなツール工房のトップページを作るスクリプト。

ツールを足したいときは、tools.json に1つ書き足して `python3 build.py` を実行するだけ。
index.html / privacy.html / sitemap.xml / robots.txt が作り直されます。
"""
import json
import os
from html import escape

# ======== 設定 ========
BASE_URL = "https://zero-kobo.github.io/"   # 末尾は /
SITE_NAME = "ちいさなツール工房"
TITLE = "ちいさなツール工房｜ブラウザで使える無料ツール集"
DESC = "ふるさと納税の上限額・年収の壁・NISA・住宅ローンの計算、写真の塗り絵やドット絵、LINEスタンプ作り、こども向けドリル、社労士の勉強ツールなど。ブラウザで開くだけで使える、無料のちいさなツールを集めました。"
GA_ID = "G-40QSGNSQEL"   # Googleアナリティクス(GA4)の測定ID。空にするとタグは出ません
UPDATED = "2026-10-18"   # サイトマップの更新日
PRIVACY_DATE = "2026-10-11"   # プライバシーポリシーの制定日（変えない）
VER = "20261011a"       # style.css を直したときに変える（ブラウザの古い保存を避けるため）
# =======================

ROOT = os.path.dirname(os.path.abspath(__file__))
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E"
           "%3Ctext y='.9em' font-size='90'%3E🔧%3C/text%3E%3C/svg%3E")


def head(title, desc, url):
    ga = ""
    if GA_ID:
        ga = ('<!-- Google tag (GA4) -->\n'
              f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>\n'
              '<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}'
              f'gtag("js",new Date());gtag("config","{GA_ID}");</script>\n')
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc, quote=True)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#ffc61a">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{escape(title, quote=True)}">
<meta property="og:description" content="{escape(desc, quote=True)}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="ja_JP">
<meta name="twitter:card" content="summary">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Dela+Gothic+One&family=Zen+Kaku+Gothic+New:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css?v={VER}">
{ga}</head>
"""


def footer():
    return f"""<footer class="foot">
<p>一部のツールには、アフィリエイト広告（PR）が含まれます。</p>
<p><a href="/privacy.html">プライバシーポリシー</a></p>
<p class="copy">© 2026 {SITE_NAME}</p>
</footer>"""


def build_index(groups):
    n = 0
    shelves = []
    for gi, g in enumerate(groups):
        items = []
        for t in g["tools"]:
            n += 1
            items.append(
                f'<li class="tag" style="--i:{n}">'
                f'<h3><a href="/{escape(t["path"], quote=True)}">{escape(t["name"])}</a></h3>'
                f'<p>{escape(t["desc"])}</p></li>')
        shelves.append(
            f'<section class="shelf" aria-labelledby="g{gi}">\n'
            f'<h2 id="g{gi}">{escape(g["title"])}</h2>\n'
            f'<ul class="tags">\n' + "\n".join(items) + "\n</ul>\n</section>")
    body = f"""<body class="home">
<div class="wrap">
<header class="sign">
<h1 class="brand">{SITE_NAME}</h1>
<p class="lead">ブラウザで開くだけで使える、無料のちいさなツール集です。登録もインストールもいりません。</p>
</header>
<main>
{chr(10).join(shelves)}
</main>
{footer()}
</div>
</body>
</html>
"""
    return head(TITLE, DESC, BASE_URL) + body


def build_privacy():
    title = f"プライバシーポリシー｜{SITE_NAME}"
    desc = f"{SITE_NAME}のアクセス解析・広告・外部サービスの利用について。"
    body = f"""<body class="doc">
<div class="wrap">
<header class="sign slim"><p class="brand"><a href="/">{SITE_NAME}</a></p></header>
<main class="paper">
<h1>プライバシーポリシー</h1>
<h2>運営者</h2>
<p>{SITE_NAME}</p>
<h2>アクセス解析について</h2>
<p>当サイト（zero-kobo.github.io 以下のページ）では、サイトの改善のために、Google社のアクセス解析サービス「Google アナリティクス」を利用しています。Google アナリティクスは、Cookie などを使って、閲覧されたページや利用環境などのデータを、個人を特定しない形で収集します。収集されたデータは、Google社のプライバシーポリシーに基づいて管理されます。</p>
<p>Cookie の利用は、ブラウザの設定で無効にできます。また、<a href="https://tools.google.com/dlpage/gaoptout?hl=ja" target="_blank" rel="noopener noreferrer">Google アナリティクス オプトアウト アドオン</a>で、データの収集を無効にすることもできます。詳しくは、<a href="https://policies.google.com/technologies/partner-sites?hl=ja" target="_blank" rel="noopener noreferrer">Google のポリシー</a>をご確認ください。</p>
<h2>広告・アフィリエイトについて</h2>
<p>一部のツールでは、楽天アフィリエイトなどのアフィリエイトプログラムを利用して、商品やサービスを紹介しています。広告のリンクから商品を購入・申込みされた場合、運営者に報酬が支払われることがあります。広告には「PR」と表示し、広告であることが分かるようにしています。</p>
<p>広告配信事業者や、アフィリエイトサービスの提供事業者が、広告の表示や成果の確認のために、Cookie などを利用する場合があります。詳しくは、各事業者のプライバシーポリシーをご確認ください。</p>
<h2>外部サービスについて</h2>
<p>文字の表示に、Google Fonts を利用しています。ページを開くと、Google のサーバーとの通信が発生します。</p>
<h2>計算結果について</h2>
<p>シミュレーターなどの計算結果は目安です。将来の結果を保証するものではありません。大切なお金の判断は、公的な情報や専門家にもご確認ください。</p>
<p class="date">制定：{PRIVACY_DATE}</p>
</main>
{footer()}
</div>
</body>
</html>
"""
    return head(title, desc, BASE_URL + "privacy.html") + body


def build_sitemap(groups):
    urls = [(BASE_URL, "1.0")]
    for g in groups:
        for t in g["tools"]:
            urls.append((BASE_URL + t["path"], "0.8"))
            for sub in t.get("extra", []):
                urls.append((BASE_URL + t["path"] + sub, "0.5"))
    urls.append((BASE_URL + "privacy.html", "0.3"))
    rows = "\n".join(
        f"  <url><loc>{u}</loc><lastmod>{UPDATED}</lastmod><priority>{p}</priority></url>" for u, p in urls)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + rows + "\n</urlset>\n")


def write(name, text):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    with open(os.path.join(ROOT, "tools.json"), encoding="utf-8") as f:
        groups = json.load(f)["groups"]
    write("index.html", build_index(groups))
    write("privacy.html", build_privacy())
    write("sitemap.xml", build_sitemap(groups))
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {BASE_URL}sitemap.xml\n")
    count = sum(len(g["tools"]) for g in groups)
    print(f"built: index.html, privacy.html, sitemap.xml, robots.txt | tools: {count}")
