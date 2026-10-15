import json,re,html,os
S="https://aitrackertool.dev"
GA_TAG='<script async src="https://www.googletagmanager.com/gtag/js?id=G-VMR6RG9R83"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag(\'js\',new Date());gtag(\'config\',\'G-VMR6RG9R83\');</script>'
C={"coding":"Coding & Vibe Coding","chat":"Chat Assistants","image":"Image","video":"Video","audio":"Voice & Audio","writing":"Writing","agents":"Agents & Automation","research":"Productivity & Research","design":"Design & Websites","itsec":"AI for IT & Cybersecurity"}
# name,cat,url,desc,free(True/None),price,tags
T=[
("Cursor","coding","https://cursor.com","AI-first code editor with agent mode, codebase chat and tab completion.",True,"Paid plans from $8/mo","editor,agent,ide"),
("Bolt.new","coding","https://bolt.cello.so/MFwNDwJhlUB","Prompt, run, edit and deploy full-stack web apps right in your browser.",None,"","vibe coding,web apps,browser"),
("v0","coding","https://v0.app","Vercel's AI app builder that turns prompts into React/Next.js apps and UI.",True,"Plus from $30/mo","vibe coding,react,ui"),
("Lovable","coding","https://lovable.dev","Build full-stack web apps by chatting with an AI engineer.",True,"","vibe coding,web apps,no-code"),
("Replit","coding","https://replit.com","Browser IDE with Replit Agent that builds and deploys apps from a prompt.",True,"Core from $20/mo ($18/mo billed annually)","vibe coding,ide,deploy"),
("GitHub Copilot","coding","https://github.com/features/copilot","AI pair programmer and coding agent inside VS Code, JetBrains and GitHub.",True,"Pro from $10/mo","autocomplete,agent,github"),
("Devin","coding","https://devin.ai","Cognition's coding agents: Devin Desktop (the editor formerly called Windsurf) plus Devin cloud agents.",True,"Pro from $20/mo","editor,agent,ide,cloud agents"),
("Zed","coding","https://zed.dev","Fast open-source code editor with AI edit predictions, an agent panel and bring-your-own-key support.",True,"Pro from $10/mo","editor,open source,ide"),
("OpenRouter","coding","https://openrouter.ai","One OpenAI-compatible API for 500+ models from 80+ providers, with fallback routing.",True,"Pay-as-you-go; 5.5% fee on credit purchases","api,models,routing"),
("Hugging Face","coding","https://huggingface.co","The hub for open models, datasets and Spaces demos, plus hosted inference.",True,"PRO from $9/mo","open models,hosting,ml"),
("Claude Code","coding","https://claude.com/product/claude-code","Anthropic's agentic coding tool for the terminal, IDE and web.",None,"Included with paid Claude plans","agent,terminal,cli"),
("OpenAI Codex","coding","https://openai.com/codex/","OpenAI's coding agent for the CLI, IDE and cloud tasks.",None,"","agent,cli,openai"),
("Warp","coding","https://www.warp.dev","Agentic terminal and development environment with built-in AI agents.",True,"Build from $20/mo","terminal,agent"),
("Cline","coding","https://cline.bot","Open-source autonomous coding agent for VS Code.",None,"Open source","agent,open source,vs code"),
("Aider","coding","https://aider.chat","Open-source AI pair programming in your terminal, with git integration.",None,"Open source","cli,open source,git"),
("ChatGPT","chat","https://chatgpt.com","OpenAI's general-purpose AI assistant for chat, writing, code and images.",True,"","assistant,openai"),
("Claude","chat","https://claude.ai","Anthropic's AI assistant for writing, analysis and coding.",True,"Pro from $17/mo billed annually ($20 monthly)","assistant,anthropic"),
("Gemini","chat","https://gemini.google.com","Google's AI assistant, connected to Google apps and search.",True,"Google AI Plus from $4.99/mo (US)","assistant,google"),
("Grok","chat","https://grok.com","xAI's AI assistant with real-time knowledge from X and the web.",None,"","assistant,xai"),
("Microsoft Copilot","chat","https://copilot.microsoft.com","Microsoft's AI companion for chat, search and creation.",None,"","assistant,microsoft"),
("Le Chat (Mistral)","chat","https://chat.mistral.ai","Mistral AI's chat assistant.",None,"","assistant,mistral,europe"),
("Ollama","chat","https://ollama.com","Run open models locally with one command, or use Ollama's cloud models when your machine isn't enough.",True,"Paid plans from $20/mo","local models,open weights,privacy"),
("LM Studio","chat","https://lmstudio.ai","Desktop app (now with the Bionic agent) for downloading and running local LLMs via llama.cpp and MLX.",True,"Bionic+ from $20/mo","local models,desktop,privacy"),
("DeepSeek","chat","https://chat.deepseek.com","Chat assistant powered by DeepSeek's open-weight models.",None,"","assistant,open weights"),
("Midjourney","image","https://www.midjourney.com","AI image generator known for its distinctive artistic style.",None,"","image generation,art"),
("Ideogram","image","https://ideogram.ai","AI image generator that's strong at rendering text in images.",None,"","image generation,typography"),
("Leonardo.Ai","image","https://leonardo.ai","AI image and video generation platform for creators and game assets.",None,"","image generation,assets"),
("Krea","image","https://www.krea.ai","Real-time AI image and video generation and enhancement.",True,"Pro from $21/mo billed yearly ($35 monthly)","image generation,upscaling,real-time"),
("Adobe Firefly","image","https://www.adobe.com/products/firefly.html","Adobe's generative AI for images, video and design, built into Creative Cloud.",None,"","image generation,adobe"),
("Black Forest Labs (FLUX)","image","https://bfl.ai","Makers of the FLUX image generation models.",None,"","image models,api"),
("Recraft","image","https://www.recraft.ai","AI image generator for designers, with vector and brand-style output.",True,"","vector,design,image generation"),
("Runway","video","https://runway.com","AI video generation and editing tools for filmmakers and creators.",True,"Standard from $12/mo billed annually","video generation,editing"),
("Synthesia","video","https://www.synthesia.io","Create videos with AI avatars and voiceovers from text.",True,"Starter from $29/mo","avatars,video generation,training"),
("Pika","video","https://pika.art","AI video generator for short creative clips and effects.",True,"Starter from $10/mo","video generation,effects"),
("Luma AI","video","https://lumalabs.ai","AI video generation with the Dream Machine and Ray models.",None,"Plus from $30/mo","video generation"),
("HeyGen","video","https://www.heygen.com","AI avatar videos, translation and lip-sync.",True,"Creator from $29/mo","avatars,translation"),
("Descript","video","https://www.descript.com","Edit video and podcasts by editing the transcript, with AI tools.",True,"Hobbyist from $16/mo billed annually ($24 monthly)","editing,podcast,transcription"),
("Kling AI","video","https://kling.ai","Kuaishou's AI video generation model and app.",None,"","video generation"),
("ElevenLabs","audio","https://elevenlabs.io","AI voice generation, cloning, dubbing and speech-to-text.",True,"Creator from $22/mo","text to speech,voice cloning"),
("Suno","audio","https://suno.com","Generate full songs with vocals from a text prompt.",True,"Pro from $8/mo billed yearly","music generation"),
("Udio","audio","https://www.udio.com","AI music generation and remixing.",None,"","music generation"),
("Murf AI","audio","https://murf.ai","AI voiceover studio with a library of voices.",None,"","text to speech,voiceover"),
("Jasper","writing","https://www.jasper.ai","AI content platform for marketing teams.",None,"Pro from $59/mo","marketing,content"),
("Writesonic","writing","https://writesonic.com","AI writing and SEO/AI-search visibility platform.",None,"Starter from $79/mo billed annually","seo,content"),
("Copy.ai","writing","https://www.copy.ai","AI platform for go-to-market copy and workflows.",None,"Paid plans from $29/mo","marketing,copywriting"),
("Grammarly","writing","https://www.grammarly.com","AI writing assistant for grammar, tone and rewriting.",True,"Pro from $12/mo","grammar,editing"),
("QuillBot","writing","https://quillbot.com","AI paraphrasing, grammar checking and summarizing.",None,"","paraphrasing,summarizing"),
("n8n","agents","https://n8n.io","Workflow automation with AI agents; self-hostable and fair-code.",True,"Cloud Starter from €20/mo billed annually; self-hosted Community Edition free","automation,self-hosted,agents"),
("Zapier","agents","https://zapier.com","Automate work across 7,000+ apps with Zaps and AI agents.",True,"Professional from $19.99/mo","automation,no-code,integrations"),
("Make","agents","https://www.make.com","Visual automation platform with AI agents.",None,"","automation,no-code,visual"),
("Relay.app","agents","https://www.relay.app","AI workflow automation with human-in-the-loop steps.",None,"","automation,agents"),
("Muse (Meta)","agents","https://muse.ai","Meta's personal AI agent that uses apps for you: email, travel, shopping and more, via app, web or WhatsApp. US-only at launch (Sept 8, 2026).",True,"Paid plans for heavier use","personal agent,meta,whatsapp,new"),
("Hermes Agent","agents","https://hermes-agent.nousresearch.com","Nous Research's open-source personal agent with app connectors, a plugin catalog and one-click local models.",None,"Open source (MIT)","open source,agents,local models"),
("Lindy","agents","https://www.lindy.ai","Build AI agents that handle email, meetings and workflows.",None,"Team from $29.99/mo; $50 in starter credits","agents,assistant"),
("Perplexity","research","https://www.perplexity.ai","AI answer engine that searches the web and cites sources.",None,"","search,research,citations"),
("Gemini Notebook","research","https://notebook.google","Google's AI research notebook (formerly NotebookLM), grounded in your own sources, with audio overviews.",None,"","research,notes,google"),
("Granola","research","https://www.granola.ai","Bot-free AI meeting notes that enhance your own jottings, with chat across meetings.",True,"Business from $14/user/mo","meetings,notes"),
("Notion AI","research","https://www.notion.com","Notion's workspace with built-in AI for writing, search and agents.",True,"Plus from $10/mo","notes,workspace"),
("Otter.ai","research","https://otter.ai","AI meeting notes, transcription and summaries.",True,"Pro $16.99/user/mo billed monthly","meetings,transcription"),
("Fireflies.ai","research","https://fireflies.ai","AI notetaker that records, transcribes and summarizes meetings.",True,"Pro from $10/seat/mo billed annually ($18 monthly)","meetings,transcription"),
("Elicit","research","https://elicit.com","AI research assistant for finding and analyzing papers.",None,"Plus from $11/mo","academic,papers"),
("Consensus","research","https://consensus.app","AI search engine for scientific research.",None,"","academic,search"),
("Gamma","design","https://gamma.app","Create presentations, docs and websites with AI.",None,"","presentations,slides"),
("Framer","design","https://www.framer.com","Design and publish websites, with AI site generation.",True,"Basic from $10/mo","websites,no-code"),
("Figma","design","https://www.figma.com","Collaborative design platform with Figma AI and Figma Make.",True,"Professional from $16/mo per full seat","ui design,prototyping"),
("Canva","design","https://www.canva.com","Online design tool with Magic Studio AI features.",None,"","graphic design,templates"),
("Webflow","design","https://webflow.com","Visual website builder and CMS with AI tools.",True,"Basic site plan from $15/mo billed yearly","websites,cms,no-code"),
("Napkin AI","design","https://www.napkin.ai","Turns text into editable diagrams, flowcharts, mind maps and charts.",True,"Plus from $9/person/mo","diagrams,visuals,slides"),
("Uizard","design","https://uizard.io","AI UI design tool that turns prompts and sketches into mockups.",True,"Pro from $12/mo billed annually","ui design,prototyping"),
("TryHackMe (Echo)","itsec","https://tryhackme.com/echo","Hands-on cyber training labs with Echo, a built-in AI tutor that gives context-aware hints without handing you the answer.",None,"","cert study,labs,beginner"),
("HTB Academy (HTB Coach)","itsec","https://academy.hackthebox.com","Hack The Box's training modules with HTB Coach (beta): AI explanations, section summaries and quizzes tied to what you're studying.",None,"","cert study,labs,pentesting"),
("PentestGPT","itsec","https://github.com/GreyDGL/PentestGPT","Open-source autonomous pentesting agent from USENIX Security 2024 research, with staged recon-to-exploit runs for CTFs and lab targets.",None,"Open source (MIT)","pentesting,open source,home lab"),
("Burp AI (PortSwigger)","itsec","https://portswigger.net/burp/ai","AI pentesting partner built into Repeater in Burp Suite Professional for validating findings and cutting scan noise.",None,"","web security,pentesting,bug bounty"),
("Microsoft Security Copilot","itsec","https://www.microsoft.com/en-us/security/business/ai-machine-learning/microsoft-security-copilot","Generative AI for security teams across Microsoft Defender, Sentinel, Entra, Intune and Purview: summarize incidents, write queries and reverse-engineer malicious scripts in plain English.",None,"Pay-as-you-go: $4 per provisioned SCU/hour","soc,microsoft,incident response"),
("Google Security Operations","itsec","https://cloud.google.com/security/products/security-operations","Google's SecOps platform (SIEM + SOAR) with Gemini for natural-language search, detection writing and investigation.",None,"","siem,soc,gemini"),
("CrowdStrike Charlotte AI","itsec","https://www.crowdstrike.com/en-us/platform/charlotte-ai/","Agentic security analyst in the CrowdStrike platform that triages detections and speeds up investigations.",None,"","soc,edr,triage"),
("Splunk AI Assistant","itsec","https://www.splunk.com/en_us/products/splunk-ai-assistant.html","Natural-language assistant in Splunk for finding dashboards, reports and data and getting help with searches over your logs.",None,"","log analysis,spl,siem"),
("Elastic Security AI","itsec","https://www.elastic.co/security/ai","AI in Elastic Security: automated alert triage and hypothesis-driven threat hunts with ES|QL over your SIEM data.",None,"","log analysis,siem,threat hunting"),
]
sl=lambda s:re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')
e=html.escape
data=[dict(name=n,slug=sl(n),category=c,catName=C[c],url=u,desc=d,freeTier=f,pricing=p,tags=t.split(',')) for n,c,u,d,f,p,t in T]
def pclass(x):
  p=x["pricing"] or "";fr=x["freeTier"] or p.startswith("Open source")
  pd=bool(p) and not p.startswith("Open source")
  return "both" if fr and pd else "free" if fr else "paid" if pd else ""
for x in data: x["pf"]=pclass(x)
for x in data:
  if x["freeTier"] is None: del x["freeTier"]
  if not x["pricing"]: del x["pricing"]
open("directory.js","w").write("// Directory data. Pricing/free tier only where verified on the official site (Oct 14-15, 2026); omitted otherwise.\nconst CATEGORIES="+json.dumps(C)+";\nconst DIRECTORY="+json.dumps(data,indent=0)+";\n")
CNT={c:sum(1 for y in data if y["category"]==c) for c in C}
DROP="/drop-2026-10-15.html"
import datetime
# Build date: override with BUILD_DATE=YYYY-MM-DD; a tool can carry its own "verified":"YYYY-MM-DD".
BUILD=datetime.date.fromisoformat(os.environ["BUILD_DATE"]) if os.environ.get("BUILD_DATE") else datetime.date.today()
def vdate(x): return datetime.date.fromisoformat(x["verified"]) if x.get("verified") else BUILD
def mdy(d): return d.strftime("%b ")+str(d.day)+d.strftime(", %Y")
VER=BUILD.strftime("%m/%d")
INTRO={"itsec":'<div class="note-box"><div class="nb-h">Breaking into IT? Start here</div><p>Start with the learning tools here (TryHackMe\'s Echo tutor, HTB Coach) for cert study and labs. Practice scripting and PowerShell with <a href="/tools/github-copilot.html">GitHub Copilot</a> or <a href="/tools/warp.html">Warp</a>, run local models in your home lab with <a href="/tools/ollama.html">Ollama</a>, and turn study notes into quizzes with <a href="/tools/gemini-notebook.html">Gemini Notebook</a>. The SOC copilots further down are enterprise tools you\'ll likely meet on the job, so their docs are worth a read even before you can use them.</p></div>'}
LOGO='<svg viewBox="0 0 28 28" width="26" height="26" aria-hidden="true" focusable="false"><path d="M5 6L14 14 23 8M14 14L9 23M14 14L23 21" stroke="currentColor" stroke-width="1.5" fill="none"/><circle cx="5" cy="6" r="2.5" fill="currentColor"/><circle cx="23" cy="8" r="2.5" fill="currentColor"/><circle cx="9" cy="23" r="2.5" fill="currentColor"/><circle cx="23" cy="21" r="2.5" fill="currentColor"/><circle cx="14" cy="14" r="3.5" fill="#00ff9c"/></svg>'
ICONS='<link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><meta name="theme-color" content="#0d1520">'
def nav():
  return ('<a class="skip" href="#main">Skip to content</a><header class="bar"><a class="logo" href="/" aria-label="AI Tool Tracker home"><span class="lg-mark">'+LOGO+'</span><span data-sitename>AI Tool Tracker</span></a>'
   f'<nav class="top" aria-label="Main"><a href="/#directory">Directory</a><a href="{DROP}">Today\'s drop</a><a href="/#newsletter">Newsletter</a><a class="cta" href="/#submit">Submit a tool</a></nav></header>')
def side(cur=None,home=False):
  it=[]
  if home: it.append(f'<a class="chip fi on" href="#directory" data-c="all"><span class="fn">All tools</span><span class="n">{len(data)}</span></a>')
  else: it.append(f'<a class="fi" href="/#directory"><span class="fn">All tools</span><span class="n">{len(data)}</span></a>')
  for k,v in C.items():
    on=k==cur
    it.append(f'<a class="{"chip " if home else ""}fi{" on" if on else ""}" href="{"#cat-"+k if home else "/categories/"+k+".html"}" data-c="{k}"{" aria-current=\"page\"" if on else ""}><span class="fn">{e(v)}</span><span class="n">{CNT[k]}</span></a>')
  return (f'<aside class="side" aria-label="Categories"><div class="side-h">Categories</div><nav class="tree"{" id=\"cats\"" if home else ""} aria-label="Categories">{"".join(it)}</nav>'
   f'<div class="side-h sh2">Start here</div><nav class="tree t2" aria-label="Quick links"><a class="fi" href="/categories/itsec.html"><span class="fn">Breaking into IT</span></a><a class="fi" href="{DROP}"><span class="fn">Today\'s drop</span></a><a class="fi" href="/issue-001.html"><span class="fn">Newsletter issue #001</span></a></nav></aside>')
def mkfoot():
  cl="".join(f'<li><a href="/categories/{k}.html">{e(v)}</a></li>' for k,v in C.items())
  return (f'<footer class="site"><div class="fgrid"><div><a class="logo" href="/"><span class="lg-mark">{LOGO}</span>AI Tool Tracker</a><p class="mut">Hand-checked AI tools for builders and IT folks, updated daily.</p><p><a href="https://x.com/AITRACKERTOOL" target="_blank" rel="noopener">@AITRACKERTOOL on X</a> · <a href="https://aitrackertool.beehiiv.com/subscribe" target="_blank" rel="noopener">Newsletter</a></p></div>'
   f'<div><h4>Categories</h4><ul class="flist">{cl}</ul></div><div><h4>Site</h4><ul class="flist one"><li><a href="/#directory">Directory</a></li><li><a href="{DROP}">Today\'s drop</a></li><li><a href="/issue-001.html">Issue #001</a></li><li><a href="/#submit">Submit / Sponsor</a></li></ul></div></div>'
   '<div class="disc">© 2026 <span data-sitename>AI Tool Tracker</span>. <b>Affiliate disclosure:</b> some links on this site are affiliate links (marked "affiliate link"). If you sign up through them we may earn a commission at no extra cost to you. It never affects which tools we pick. This site uses Google Analytics to count visits.</div></footer>')
FOOTER=mkfoot()
SCROLL='<script>(function(){var a=document.querySelector(".side .fi.on");if(a&&innerWidth<900)a.parentNode.parentNode.scrollLeft=a.offsetLeft-12})()</script>'
def shell(main,cur=None,home=False): return '<div class="shell">'+side(cur,home)+'<main id="main" class="main">'+main+FOOTER+'</main></div>'+SCROLL
def head(t,d,path,ld):
  return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(t)}</title><meta name="description" content="{e(d)}"><link rel="canonical" href="{S}/{path}"><meta property="og:title" content="{e(t)}"><meta property="og:description" content="{e(d)}"><meta property="og:url" content="{S}/{path}"><meta name="twitter:card" content="summary"><meta name="twitter:site" content="@AITRACKERTOOL"><script type="application/ld+json">{json.dumps(ld)}</script>{ICONS}<link rel="stylesheet" href="/style.css">'+GA_TAG+'</head><body>'+nav()
END='<script src="/config.js"></script></body></html>'
def isaff(x): return "bolt.cello.so" in x["url"]
AFFNOTE='<span class="affnote">Affiliate link: we may earn a commission if you sign up, at no extra cost to you.</span>'
def tags(x):
  p=x["pf"];t=[]
  if p=="free": t.append('<span class="t free">[FREE]</span>')
  elif p=="paid": t.append('<span class="t paid">[PAID]</span>')
  elif p=="both": t+=['<span class="t free">[FREE TIER]</span>','<span class="t paid">[PAID]</span>']
  else: t.append('<span class="t na">[PRICE: SEE SITE]</span>')
  t.append(f'<span class="t ver">[VERIFIED {vdate(x).strftime("%m/%d")}]</span>' if (p or x.get("pricing")) else '<span class="t na">[CHECK SITE]</span>')
  if isaff(x): t.append('<span class="t aff">[AFFILIATE]</span>')
  return "".join(t)
def visit(x,cls="go"):
  return f'<a class="{cls}" href="{x["url"]}" target="_blank" rel="{"sponsored noopener" if isaff(x) else "noopener"}" aria-label="Visit {e(x["name"])} (opens in new tab)">Visit ↗</a>'
def row(x,showcat=False,filt=True):
  s=(x["name"]+" "+x["desc"]+" "+" ".join(x["tags"])+" "+x["catName"]+(" free" if "freeTier" in x or x["pf"]=="free" else "")).lower()
  attrs=f' data-c="{x["category"]}" data-p="{x["pf"]}" data-s="{e(s)}"' if filt else ''
  return (f'<div class="row{" tool" if filt else ""}" role="row"{attrs}><div class="c-name" role="cell"><a class="nm" href="/tools/{x["slug"]}.html">{e(x["name"])}</a><span class="ds">{e(x["desc"])}</span>'+(AFFNOTE if isaff(x) else '')+'</div>'
   +(f'<div class="c-cat" role="cell"><a href="/categories/{x["category"]}.html">{e(x["catName"])}</a></div>' if showcat else '')+
   f'<div class="c-price" role="cell"><span class="lbl">Price </span>{e(x.get("pricing") or "See site")}</div><div class="c-tags" role="cell">{tags(x)}</div><div class="c-go" role="cell">{visit(x)}</div></div>')
def table(rows,showcat=False):
  h='<div class="row head" role="row"><div role="columnheader">Tool</div>'+('<div role="columnheader">Category</div>' if showcat else '')+'<div role="columnheader">Price</div><div role="columnheader">Status</div><div role="columnheader"><span class="sr">Link</span></div></div>'
  return f'<div class="tbl{" wcat" if showcat else ""}" role="table">{h}{"".join(rows)}</div>'
def ctl(n):
  return (f'<div class="ctl" role="search"><label class="prompt" for="q"><span class="ps" aria-hidden="true">$ find</span><span class="sr">Search tools</span><input id="q" type="search" placeholder="Search tools..." autocomplete="off"></label>'
   '<div class="pf" role="group" aria-label="Filter by price"><button type="button" class="pfb on" data-p="all" aria-pressed="true">All</button><button type="button" class="pfb" data-p="free" aria-pressed="false">Free</button><button type="button" class="pfb" data-p="paid" aria-pressed="false">Paid</button></div></div>'
   '<p id="none" class="none" hidden>No tools match. Try a different word or switch the filter to All.</p>')
urls=[]
for x in data:
  ld={"@context":"https://schema.org","@type":"SoftwareApplication","name":x["name"],"applicationCategory":x["catName"],"operatingSystem":"Web","description":x["desc"],"url":x["url"] if "cello" not in x["url"] else "https://bolt.new"}
  if "freeTier" in x: ld["offers"]={"@type":"Offer","price":"0","priceCurrency":"USD"}
  rel=[y for y in data if y["category"]==x["category"] and y is not x]
  b=head(f'{x["name"]}: pricing, free tier & alternatives | AI Tool Tracker',f'{x["name"]}: {x["desc"]} Pricing, free tier and related {x["catName"]} tools.',f'tools/{x["slug"]}.html',ld)
  free={"free":"Yes","both":"Yes","paid":"No"}.get(x["pf"],"Check site")
  m=(f'<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/categories/{x["category"]}.html">{e(x["catName"])}</a> / <span aria-current="page">{e(x["name"])}</span></nav>'
   f'<article class="detail"><h1>{e(x["name"])}</h1><p class="lede">{e(x["desc"])}</p><div class="c-tags">{tags(x)}</div>'
   f'<dl class="facts"><div><dt>Category</dt><dd><a href="/categories/{x["category"]}.html">{e(x["catName"])}</a></dd></div><div><dt>Price</dt><dd>{e(x.get("pricing") or "See official site")}</dd></div><div><dt>Free option</dt><dd>{free}</dd></div><div><dt>Last checked</dt><dd>{mdy(vdate(x))}</dd></div></dl>'
   '<p class="kw">'+"".join(f'<code>{e(t)}</code>' for t in x["tags"])+f'</p><p>{visit(x,"btn").replace("Visit ↗","Visit "+e(x["name"])+" ↗")}'+(' <b class="afftag">(affiliate link)</b>' if isaff(x) else '')+'</p>'+('<p class="note">This is an affiliate link: we may earn a commission if you sign up, at no extra cost to you.</p>' if isaff(x) else '')+
   f'</article><section class="grp-s"><div class="gh"><h2>Related {e(x["catName"])} tools <span class="n">{len(rel)}</span></h2><a href="/categories/{x["category"]}.html">See all</a></div>{table([row(y,filt=False) for y in rel])}</section>')
  open(f'tools/{x["slug"]}.html','w').write(b+shell(m,x["category"])+END); urls.append(f'tools/{x["slug"]}.html')
for c,n in C.items():
  mm=[y for y in data if y["category"]==c]
  lab=n if n.startswith("AI ") else f"{n} AI tools"
  ld={"@context":"https://schema.org","@type":"CollectionPage","name":lab,"itemListElement":[{"@type":"ListItem","position":i+1,"url":f'{S}/tools/{y["slug"]}.html',"name":y["name"]} for i,y in enumerate(mm)]}
  b=head(f'Best {lab} (2026) | AI Tool Tracker',f'{len(mm)} {n} AI tools with pricing and free-tier info: '+", ".join(y["name"] for y in mm)[:120],f'categories/{c}.html',ld)
  m=(f'<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/#directory">Categories</a> / <span aria-current="page">{e(n)}</span></nav><h1 class="ch1">{e(lab)}</h1><p class="lede">{len(mm)} tools. Prices and free tiers shown only where we checked them on the official site.</p>'+INTRO.get(c,'')+
   '<div class="sticky">'+ctl(len(mm))+'</div>'+table([row(y) for y in mm]))
  open(f'categories/{c}.html','w').write(b+shell(m,c)+'<script src="/filter.js"></script>'+END); urls.append(f'categories/{c}.html')
sm=open("sitemap.xml").read()
sm=re.sub(r'\s*<url><loc>https://aitrackertool.dev/(tools|categories)/[^<]*</loc>.*?</url>','',sm,flags=re.S)
sm=sm.replace("</urlset>","".join(f"<url><loc>{S}/{u}</loc><lastmod>{BUILD.isoformat()}</lastmod></url>\n" for u in urls)+"</urlset>")
open("sitemap.xml","w").write(sm)
ll=open("llms.txt").read().split("\n## Directory")[0].rstrip()
ll+="\n\n## Directory\n"+"".join(f"\n### {n}\n"+"".join(f'- [{y["name"]}]({S}/tools/{y["slug"]}.html): {y["desc"]}'+(f' Pricing: {y["pricing"]}.' if "pricing" in y else '')+(' Free tier: yes.' if "freeTier" in y else '')+"\n" for y in data if y["category"]==c) for c,n in C.items())
open("llms.txt","w").write(ll)
print(len(data),len(urls))

# ---- homepage + static pages ----
ix=open("index.html").read()
hd=ix[:ix.index("<body>")]
hd=re.sub(r'<link rel="(icon|apple-touch-icon)"[^>]*>|<meta name="theme-color"[^>]*>','',hd).replace('<link rel="stylesheet" href="/style.css">',ICONS+'<link rel="stylesheet" href="/style.css">')
if "G-VMR6RG9R83" not in hd: hd=hd.replace("</head>",GA_TAG+"</head>",1)
hd+="<body>"
sub=ix[ix.index('<section class="wrap" id="submit">') if '<section class="wrap" id="submit">' in ix else ix.index('<section id="submit"'):]
sub=sub[:sub.index('</section>')+10]
sub=re.sub(r'^<section[^>]*>','<section id="submit" class="blk">',sub).replace('<h2 class="sec">','<h2>').replace('<div class="grid">','<div class="two">').replace('<div class="card">','<div class="panel">')
nfree=sum(1 for y in data if y["pf"] in("free","both"));npaid=sum(1 for y in data if y["pf"] in("paid","both"))
groups="".join(f'<section class="grp" id="cat-{k}" data-c="{k}"><div class="gh"><h3>{e(v)} <span class="n">{CNT[k]}</span></h3><a href="/categories/{k}.html">Open category</a></div>{table([row(y) for y in data if y["category"]==k])}</section>' for k,v in C.items())
feat=[y for y in data if y["slug"] in("muse-meta","bolt-new")]
body=nav()+shell(f'''<section class="intro"><div class="kicker">Updated {mdy(BUILD)} · {len(data)} tools checked by hand</div><h1>AI tools people actually use. Checked by hand.</h1><p class="lede">A clean, current index for vibe coders and IT and security folks: real pricing, Free or Paid at a glance, and the date we last checked every listing.</p>
<dl class="stats"><div><dt>Tools</dt><dd>{len(data)}</dd></div><div><dt>Free option</dt><dd>{nfree}</dd></div><div><dt>Paid</dt><dd>{npaid}</dd></div><div><dt>Updated</dt><dd>{VER}</dd></div></dl><p class="jump"><a class="btn" href="#directory">Browse all tools</a> <a class="btn ghost" href="/categories/itsec.html">Breaking into IT</a></p></section>
<section id="drop" class="grp-s"><div class="gh"><h2>Today's drop · Oct 15, 2026</h2><a href="{DROP}">Read the full drop</a></div><div class="tbl" role="table" id="preview"></div></section>
<section class="grp-s" id="featured"><div class="gh"><h2>Featured picks</h2><a href="{DROP}">More new tools</a></div>{table([row(y,True,False) for y in feat],True)}</section>
<section id="directory" class="dir"><h2 class="dh">AI tool directory</h2><div class="sticky">{ctl(len(data))}</div>{groups}</section>
<section id="newsletter" class="blk nl"><div><h2>Get the weekly drop</h2><p class="mut">One email a week with the best new AI tools. Unsubscribe anytime.</p></div><div class="signup"><script async src="https://subscribe-forms.beehiiv.com/v3/loader.js" data-beehiiv-form="6370ffac-0fdf-4341-bc97-5159de9c02fd"></script></div><p class="note"><a href="https://aitrackertool.beehiiv.com/subscribe" target="_blank" rel="noopener">Subscribe on beehiiv</a> · <a href="/issue-001.html">Read Issue #001</a></p></section>
{sub}''',None,True)
js='''<script src="/config.js"></script><script src="/tools.js"></script><script>(function(){function x(s){return String(s).replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})}document.getElementById('preview').innerHTML='<div class="row head drop" role="row"><div role="columnheader">Tool</div><div role="columnheader">Type</div><div role="columnheader">Price</div><div role="columnheader"><span class="sr">Link</span></div></div>'+DROP_2026_10_15.map(function(t){return '<div class="row drop" role="row"><div class="c-name" role="cell"><a class="nm" href="'+x(t.url)+'" target="_blank" rel="noopener">'+x(t.name)+'</a><span class="ds">'+x(t.desc)+'</span></div><div class="c-cat" role="cell">'+x(t.category)+'</div><div class="c-price" role="cell"><span class="lbl">Price </span>'+x(t.pricing||'See site')+'</div><div class="c-go" role="cell"><a class="go" href="'+x(t.url)+'" target="_blank" rel="noopener">Visit ↗</a></div></div>'}).join('')})()</script>
<script src="/filter.js"></script><script type="text/javascript" async src="https://subscribe-forms.beehiiv.com/attribution.js"></script></body></html>'''
open("index.html","w").write(hd+"\n"+body+js)
for p in ["drop-2026-10-15.html","drop-2026-10-14.html","issue-001.html","thanks.html"]:
  h=open(p).read()
  pre=h[:h.index("<body")]; pre=re.sub(r'<link rel="(icon|apple-touch-icon)"[^>]*>|<meta name="theme-color"[^>]*>','',pre).replace('href="style.css"','href="/style.css"').replace('<link rel="stylesheet" href="/style.css">',ICONS+'<link rel="stylesheet" href="/style.css">')
  if "G-VMR6RG9R83" not in pre: pre=pre.replace("</head>",GA_TAG+"</head>",1)
  if "<!--c-->" in h: content=h[h.index("<!--c-->")+8:h.index("<!--/c-->")]
  else:
    a=h.index("</header>")+9; z=h.index("<footer"); content=h[a:z].strip()
  if "</footer>" in h: tail=h[h.index("</footer>")+9:]
  content=content.replace('<header class="hero wrap" style="padding:40px 0 20px">','<header class="phero">').replace('<header class="hero wrap">','<header class="phero">').replace(' style="font-size:2.6rem"','').replace('<section class="wrap">','<section class="pc">').replace("RECEIVED ✓","RECEIVED").replace("Today's Loot Drop","Today's drop: 5 new AI tools").replace("This Week's Loot Drop","Issue #001: this week's new AI tools").replace('href="index.html"','href="/"').replace('href="issue-001.html"','href="/issue-001.html"')
  tail=re.sub(r'^.*?(?=<script|</main>|</body>)','',tail,flags=re.S).replace('</main></div>','')
  open(p,"w").write(pre+'<body>'+nav()+'<div class="shell">'+side()+'<main id="main" class="main"><!--c-->'+content+'<!--/c-->'+FOOTER+'</main></div>'+tail)
