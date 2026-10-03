#!/usr/bin/env python3
"""Render independent course notes with native, nested disclosure elements."""
from pathlib import Path
import re, html, shutil, json
from math_render import make_markdown

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'dist'
TITLE='离散数学与结构 (I)'
pages=[]
for p in sorted((ROOT/'content').glob('*.md')):
    text=p.read_text()
    pages.append({'id':p.stem,'title':text.splitlines()[0][2:],'text':text})
md=make_markdown([p['text'] for p in pages])
stats={'chapters':len(pages),'cards':0,'proofs':0,'chinese_characters':sum(len(re.findall(r'[\u4e00-\u9fff]',p['text'])) for p in pages)}

def markdown(s):
    parts=re.split(r'(?m)^@pdf (.+)$',s)
    result=md.render(parts[0])
    for i in range(1,len(parts),2):
        url=html.escape(parts[i],quote=True)
        result+=f'<div class="pdf-box"><p><a href="{url}" target="_blank" rel="noopener">在新标签页打开完整原卷 ↗</a></p><iframe data-src="{url}" title="原始试卷 PDF" loading="lazy"></iframe><p class="muted">若设备不支持内嵌 PDF，请使用上方原卷链接。</p></div>'+md.render(parts[i+1])
    return result

def render(text,prefix):
    lines=text.splitlines();chunks=[];plain=[];i=0;card=0
    def flush():
        if plain:chunks.append(markdown('\n'.join(plain)));plain.clear()
    while i<len(lines):
        line=lines[i]
        if line.startswith(':::') and line!=':::':
            flush();label=line[3:];i+=1;body=[];proof=[];proof_title=None
            while i<len(lines) and lines[i]!=':::':
                if lines[i].startswith('|||'):proof_title=lines[i][3:]
                elif proof_title is None:body.append(lines[i])
                else:proof.append(lines[i])
                i+=1
            if i==len(lines):raise ValueError(f'Unclosed block: {label}')
            card+=1;stats['cards']+=1
            kind,_,name=label.partition(' ')
            nested=''
            if proof_title:
                stats['proofs']+=1
                nested=f'<details class="proof"><summary>{html.escape(proof_title)}</summary><div class="proof-content">{markdown(chr(10).join(proof))}</div></details>'
            chunks.append(f'<details class="card" id="{prefix}-item-{card}"><summary><span class="kind">{html.escape(kind)}</span><span>{html.escape(name)}</span></summary><div class="card-content">{markdown(chr(10).join(body))}{nested}</div></details>')
        else:plain.append(line)
        i+=1
    flush();body='\n'.join(chunks);toc=[];number=0
    def head(m):
        nonlocal number
        number+=1;a=f'{prefix}-section-{number}';toc.append((a,re.sub('<[^>]*>','',m[1])))
        return f'<h2 id="{a}">{m[1]}</h2>'
    body=re.sub(r'<h2>(.*?)</h2>',head,body)
    body=body.replace('<table>','<div class="table-scroll"><table>').replace('</table>','</table></div>')
    return body,toc

def shell(title,body,active='',toc=(),pager=''):
    nav=''.join(f'<a href="{p["id"]}.html" '+('aria-current="page"' if p['id']==active else '')+f'>{html.escape(p["title"])}</a>' for p in pages)
    contents=''.join(f'<a href="#{a}">{html.escape(t)}</a>' for a,t in toc)
    return f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} · {TITLE if title!=TITLE else 'ZJZJ 学习空间'}</title><meta name="description" content="离散数学与结构 (I)：集合与逻辑、代数、组合、概率与信息、图论，含可折叠的知识条目、证明与往年试卷。"><link rel="stylesheet" href="katex/katex.min.css"><link rel="stylesheet" href="style.css"><link rel="icon" href="favicon.svg"></head><body><a class="skip" href="#main">跳到正文</a><header><a class="brand" href="index.html">ZJZJ <span>/ DISCRETE</span></a><div><a href="/">学习空间</a><a href="all.html">整本阅读</a><button id="menu" aria-controls="chapters" aria-expanded="false">目录</button></div></header><div class="layout"><nav id="chapters" aria-label="章节目录"><p class="nav-label">离散数学与结构 (I)</p>{nav}<p class="nav-foot">课程主线与历年拓展<br>整理于 2026.10.03</p></nav><main id="main"><div class="eyebrow">STRUCTURES · PROOFS · CONNECTIONS</div>{body}{pager}<footer><a href="00-guide.html">资料来源与范围</a><span>先思考，再展开。</span></footer></main><aside aria-label="本页目录"><p class="nav-label">本页内容</p>{contents}<a href="#main">回到顶部 ↑</a></aside></div><script src="app.js"></script></body></html>'''

if OUT.exists():shutil.rmtree(OUT)
OUT.mkdir()
all_bodies=[]
for i,p in enumerate(pages):
    body,toc=render(p['text'],p['id']);all_bodies.append(body)
    pager='<div class="pager">'
    for j,label in [(i-1,'上一章'),(i+1,'下一章')]:
        if 0<=j<len(pages):pager+=f'<a href="{pages[j]["id"]}.html"><small>{label}</small>{html.escape(pages[j]["title"])}</a>'
    pager+='</div>'
    (OUT/(p['id']+'.html')).write_text(shell(p['title'],body,p['id'],toc,pager))
cards=''.join(f'<a class="chapter" href="{p["id"]}.html"><span>{p["id"][:2]}</span><h2>{html.escape(p["title"].split(" · ")[-1])}</h2><b aria-hidden="true">↗</b></a>' for p in pages[1:])
home=f'''<section class="intro"><p class="edition">COURSE COMPANION / 北京大学</p><h1>{TITLE}</h1><p class="lead">从证明的语言，到结构的对称，再到随机性的力量。</p><p>按章节串起学习主线。定义、定理、引理与题目默认折叠；证明和解释在条目内单独展开。</p><div class="metrics"><span><b>17</b> 个主题章节</span><span><b>{stats['cards']}</b> 个折叠条目</span><span><b>{stats['proofs']}</b> 份证明与解释</span></div><a class="start" href="01-sets.html">开始阅读：集合与无穷 →</a></section><section class="scope"><h2>读之前，先对齐范围</h2><p>以 2025 完整课程为主线，对照 2026 已发布进度，附历年拓展。试卷保留出处；缺页扫描与归属未明的补充卷另作标记。</p><a href="00-guide.html">阅读说明与资料来源 ↗</a></section><section class="chapter-grid">{cards}</section>'''
(OUT/'index.html').write_text(shell(TITLE,home))
(OUT/'all.html').write_text(shell('整本阅读','<p class="scope">整本阅读保留全部折叠层级。使用章节目录可分章阅读。</p>'+''.join(all_bodies)))
for p in (ROOT/'assets').iterdir():
    if p.is_dir():shutil.copytree(p,OUT/p.name)
    else:shutil.copy2(p,OUT/p.name)
katex=ROOT/'node_modules/katex/dist';(OUT/'katex').mkdir()
shutil.copy2(katex/'katex.min.css',OUT/'katex/katex.min.css');shutil.copytree(katex/'fonts',OUT/'katex/fonts')
shutil.copy2(ROOT/'node_modules/katex/LICENSE',OUT/'katex/LICENSE')
(ROOT/'build-report.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2))
print(json.dumps(stats,ensure_ascii=False))
