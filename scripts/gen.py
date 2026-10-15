import json,re,html,os
S="https://aitrackertool.dev"
C={"coding":"Coding & Vibe Coding","chat":"Chat Assistants","image":"Image","video":"Video","audio":"Voice & Audio","writing":"Writing","agents":"Agents & Automation","research":"Productivity & Research","design":"Design & Websites"}
# name,cat,url,desc,free(True/None),price,tags
T=[
("Cursor","coding","https://cursor.com","AI-first code editor with agent mode, codebase chat and tab completion.",True,"Paid plans from $8/mo","editor,agent,ide"),
("Bolt.new","coding","https://bolt.cello.so/MFwNDwJhlUB","Prompt, run, edit and deploy full-stack web apps right in your browser.",None,"","vibe coding,web apps,browser"),
("v0","coding","https://v0.app","Vercel's AI app builder that turns prompts into React/Next.js apps and UI.",True,"Plus from $30/mo","vibe coding,react,ui"),
("Lovable","coding","https://lovable.dev","Build full-stack web apps by chatting with an AI engineer.",None,"","vibe coding,web apps,no-code"),
("Replit","coding","https://replit.com","Browser IDE with Replit Agent that builds and deploys apps from a prompt.",True,"","vibe coding,ide,deploy"),
("GitHub Copilot","coding","https://github.com/features/copilot","AI pair programmer and coding agent inside VS Code, JetBrains and GitHub.",True,"Pro from $10/mo","autocomplete,agent,github"),
("Windsurf","coding","https://windsurf.com","Agentic AI code editor with the Cascade coding agent.",True,"Pro from $20/mo","editor,agent,ide"),
("Claude Code","coding","https://www.anthropic.com/claude-code","Anthropic's agentic coding tool for the terminal, IDE and web.",None,"Included with paid Claude plans","agent,terminal,cli"),
("OpenAI Codex","coding","https://openai.com/codex/","OpenAI's coding agent for the CLI, IDE and cloud tasks.",None,"","agent,cli,openai"),
("Warp","coding","https://www.warp.dev","Agentic terminal and development environment with built-in AI agents.",True,"","terminal,agent"),
("Tabnine","coding","https://www.tabnine.com","AI code assistant focused on privacy and enterprise deployment.",None,"","autocomplete,enterprise"),
("Cline","coding","https://cline.bot","Open-source autonomous coding agent for VS Code.",None,"Open source","agent,open source,vs code"),
("Aider","coding","https://aider.chat","Open-source AI pair programming in your terminal, with git integration.",None,"Open source","cli,open source,git"),
("ChatGPT","chat","https://chatgpt.com","OpenAI's general-purpose AI assistant for chat, writing, code and images.",True,"","assistant,openai"),
("Claude","chat","https://claude.ai","Anthropic's AI assistant for writing, analysis and coding.",True,"Pro from $17/mo billed annually ($20 monthly)","assistant,anthropic"),
("Gemini","chat","https://gemini.google.com","Google's AI assistant, connected to Google apps and search.",None,"","assistant,google"),
("Grok","chat","https://grok.com","xAI's AI assistant with real-time knowledge from X and the web.",None,"","assistant,xai"),
("Microsoft Copilot","chat","https://copilot.microsoft.com","Microsoft's AI companion for chat, search and creation.",None,"","assistant,microsoft"),
("Le Chat (Mistral)","chat","https://chat.mistral.ai","Mistral AI's chat assistant.",None,"","assistant,mistral,europe"),
("DeepSeek","chat","https://chat.deepseek.com","Chat assistant powered by DeepSeek's open-weight models.",None,"","assistant,open weights"),
("Midjourney","image","https://www.midjourney.com","AI image generator known for its distinctive artistic style.",None,"","image generation,art"),
("Ideogram","image","https://ideogram.ai","AI image generator that's strong at rendering text in images.",None,"","image generation,typography"),
("Leonardo.Ai","image","https://leonardo.ai","AI image and video generation platform for creators and game assets.",None,"","image generation,assets"),
("Krea","image","https://www.krea.ai","Real-time AI image and video generation and enhancement.",True,"","image generation,upscaling,real-time"),
("Adobe Firefly","image","https://www.adobe.com/products/firefly.html","Adobe's generative AI for images, video and design, built into Creative Cloud.",None,"","image generation,adobe"),
("Black Forest Labs (FLUX)","image","https://bfl.ai","Makers of the FLUX image generation models.",None,"","image models,api"),
("Recraft","image","https://www.recraft.ai","AI image generator for designers, with vector and brand-style output.",True,"","vector,design,image generation"),
("Runway","video","https://runwayml.com","AI video generation and editing tools for filmmakers and creators.",True,"Standard from $12/mo billed annually","video generation,editing"),
("Synthesia","video","https://www.synthesia.io","Create videos with AI avatars and voiceovers from text.",None,"","avatars,video generation,training"),
("Pika","video","https://pika.art","AI video generator for short creative clips and effects.",True,"Starter from $10/mo","video generation,effects"),
("Luma AI","video","https://lumalabs.ai","AI video generation with the Dream Machine and Ray models.",None,"Plus from $30/mo","video generation"),
("HeyGen","video","https://www.heygen.com","AI avatar videos, translation and lip-sync.",True,"Creator from $29/mo","avatars,translation"),
("Descript","video","https://www.descript.com","Edit video and podcasts by editing the transcript, with AI tools.",True,"","editing,podcast,transcription"),
("Kling AI","video","https://klingai.com","Kuaishou's AI video generation model and app.",None,"","video generation"),
("ElevenLabs","audio","https://elevenlabs.io","AI voice generation, cloning, dubbing and speech-to-text.",True,"Creator from $22/mo","text to speech,voice cloning"),
("Suno","audio","https://suno.com","Generate full songs with vocals from a text prompt.",True,"","music generation"),
("Udio","audio","https://www.udio.com","AI music generation and remixing.",None,"","music generation"),
("Murf AI","audio","https://murf.ai","AI voiceover studio with a library of voices.",None,"","text to speech,voiceover"),
("Jasper","writing","https://www.jasper.ai","AI content platform for marketing teams.",None,"Pro from $59/mo","marketing,content"),
("Writesonic","writing","https://writesonic.com","AI writing and SEO/AI-search visibility platform.",None,"","seo,content"),
("Copy.ai","writing","https://www.copy.ai","AI platform for go-to-market copy and workflows.",None,"","marketing,copywriting"),
("Grammarly","writing","https://www.grammarly.com","AI writing assistant for grammar, tone and rewriting.",True,"Pro from $12/mo","grammar,editing"),
("QuillBot","writing","https://quillbot.com","AI paraphrasing, grammar checking and summarizing.",None,"","paraphrasing,summarizing"),
("n8n","agents","https://n8n.io","Workflow automation with AI agents; self-hostable and fair-code.",None,"","automation,self-hosted,agents"),
("Zapier","agents","https://zapier.com","Automate work across 7,000+ apps with Zaps and AI agents.",True,"","automation,no-code,integrations"),
("Make","agents","https://www.make.com","Visual automation platform with AI agents.",None,"","automation,no-code,visual"),
("Relay.app","agents","https://www.relay.app","AI workflow automation with human-in-the-loop steps.",None,"","automation,agents"),
("Lindy","agents","https://www.lindy.ai","Build AI agents that handle email, meetings and workflows.",None,"","agents,assistant"),
("Perplexity","research","https://www.perplexity.ai","AI answer engine that searches the web and cites sources.",None,"","search,research,citations"),
("NotebookLM","research","https://notebooklm.google","Google's AI research notebook grounded in your own sources, with audio overviews.",None,"","research,notes,google"),
("Notion AI","research","https://www.notion.com","Notion's workspace with built-in AI for writing, search and agents.",True,"Plus from $10/mo","notes,workspace"),
("Otter.ai","research","https://otter.ai","AI meeting notes, transcription and summaries.",True,"","meetings,transcription"),
("Fireflies.ai","research","https://fireflies.ai","AI notetaker that records, transcribes and summarizes meetings.",True,"","meetings,transcription"),
("Elicit","research","https://elicit.com","AI research assistant for finding and analyzing papers.",None,"Plus from $11/mo","academic,papers"),
("Consensus","research","https://consensus.app","AI search engine for scientific research.",None,"","academic,search"),
("Gamma","design","https://gamma.app","Create presentations, docs and websites with AI.",None,"","presentations,slides"),
("Framer","design","https://www.framer.com","Design and publish websites, with AI site generation.",True,"Basic from $10/mo","websites,no-code"),
("Figma","design","https://www.figma.com","Collaborative design platform with Figma AI and Figma Make.",None,"","ui design,prototyping"),
("Canva","design","https://www.canva.com","Online design tool with Magic Studio AI features.",None,"","graphic design,templates"),
("Webflow","design","https://webflow.com","Visual website builder and CMS with AI tools.",None,"","websites,cms,no-code"),
("Uizard","design","https://uizard.io","AI UI design tool that turns prompts and sketches into mockups.",None,"","ui design,prototyping"),
]
sl=lambda s:re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')
e=html.escape
data=[dict(name=n,slug=sl(n),category=c,catName=C[c],url=u,desc=d,freeTier=f,pricing=p,tags=t.split(',')) for n,c,u,d,f,p,t in T]
for x in data:
  if x["freeTier"] is None: del x["freeTier"]
  if not x["pricing"]: del x["pricing"]
open("directory.js","w").write("// Directory data. Pricing/free tier only where verified on the official site (Oct 14, 2026); omitted otherwise.\nconst CATEGORIES="+json.dumps(C)+";\nconst DIRECTORY="+json.dumps(data,indent=0)+";\n")
def head(t,d,path,ld):
  return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(t)}</title><meta name="description" content="{e(d)}"><link rel="canonical" href="{S}/{path}"><meta property="og:title" content="{e(t)}"><meta property="og:description" content="{e(d)}"><meta property="og:url" content="{S}/{path}"><meta name="twitter:card" content="summary"><meta name="twitter:site" content="@AITRACKERTOOL"><script type="application/ld+json">{json.dumps(ld)}</script><link rel="stylesheet" href="/style.css"></head><body><header class="wrap"><p><a href="/">← AI Tool Tracker</a> · <a href="/#directory">Directory</a></p></header>'
foot='<footer><div class="wrap">© 2026 AI Tool Tracker. <b>Affiliate disclosure:</b> some links on this site are affiliate links (marked "affiliate link"). If you sign up through them we may earn a commission at no extra cost to you. It never affects which tools we pick.</div></footer></body></html>'
def link(x):
  aff="bolt.cello.so" in x["url"]
  return f'<a href="{x["url"]}" target="_blank" rel="{"sponsored noopener" if aff else "noopener"}">Visit {e(x["name"])} ↗</a>'+(' <b>(affiliate link)</b>' if aff else '')
def card(x):
  return f'<div class="card"><div class="cat">{e(x["catName"])}</div><h3><a href="/tools/{x["slug"]}.html">{e(x["name"])}</a></h3><p>{e(x["desc"])}</p></div>'
urls=[]
for x in data:
  pr=[]
  if "freeTier" in x: pr.append("Free tier: yes")
  if "pricing" in x: pr.append(x["pricing"])
  ld={"@context":"https://schema.org","@type":"SoftwareApplication","name":x["name"],"applicationCategory":x["catName"],"operatingSystem":"Web","description":x["desc"],"url":x["url"] if "cello" not in x["url"] else "https://bolt.new"}
  if "freeTier" in x: ld["offers"]={"@type":"Offer","price":"0","priceCurrency":"USD"}
  rel=[y for y in data if y["category"]==x["category"] and y is not x]
  b=head(f'{x["name"]}: pricing, free tier & alternatives | AI Tool Tracker',f'{x["name"]}: {x["desc"]} Pricing, free tier and related {x["catName"]} tools.',f'tools/{x["slug"]}.html',ld)
  b+=f'<main class="wrap"><div class="card"><div class="cat"><a href="/categories/{x["category"]}.html">{e(x["catName"])}</a></div><h1>{e(x["name"])}</h1><p>{e(x["desc"])}</p>'+(f'<p class="price">💰 {e(" · ".join(pr))}</p>' if pr else '<p class="price">💰 Pricing: see official site</p>')+f'<p>Tags: {e(", ".join(x["tags"]))}</p><p>{link(x)}</p>'+('<p class="note">This is an affiliate link: we may earn a commission if you sign up, at no extra cost to you.</p>' if "cello" in x["url"] else '')+f'</div><h2>Related {e(x["catName"])} tools</h2><div class="grid">{"".join(map(card,rel))}</div></main>'+foot
  open(f'tools/{x["slug"]}.html','w').write(b); urls.append(f'tools/{x["slug"]}.html')
for c,n in C.items():
  m=[y for y in data if y["category"]==c]
  ld={"@context":"https://schema.org","@type":"CollectionPage","name":f"{n} AI tools","itemListElement":[{"@type":"ListItem","position":i+1,"url":f'{S}/tools/{y["slug"]}.html',"name":y["name"]} for i,y in enumerate(m)]}
  b=head(f'Best {n} AI tools (2026) | AI Tool Tracker',f'{len(m)} {n} AI tools with pricing and free-tier info: '+", ".join(y["name"] for y in m)[:120],f'categories/{c}.html',ld)
  b+=f'<main class="wrap"><h1>{e(n)} AI tools</h1><p>Other categories: '+" · ".join(f'<a href="/categories/{k}.html">{e(v)}</a>' for k,v in C.items() if k!=c)+f'</p><div class="grid">{"".join(map(card,m))}</div></main>'+foot
  open(f'categories/{c}.html','w').write(b); urls.append(f'categories/{c}.html')
sm=open("sitemap.xml").read()
sm=re.sub(r'\s*<url><loc>https://aitrackertool.dev/(tools|categories)/[^<]*</loc>.*?</url>','',sm,flags=re.S)
sm=sm.replace("</urlset>","".join(f"<url><loc>{S}/{u}</loc><lastmod>2026-10-14</lastmod></url>\n" for u in urls)+"</urlset>")
open("sitemap.xml","w").write(sm)
ll=open("llms.txt").read().split("\n## Directory")[0].rstrip()
ll+="\n\n## Directory\n"+"".join(f"\n### {n}\n"+"".join(f'- [{y["name"]}]({S}/tools/{y["slug"]}.html): {y["desc"]}'+(f' Pricing: {y["pricing"]}.' if "pricing" in y else '')+(' Free tier: yes.' if "freeTier" in y else '')+"\n" for y in data if y["category"]==c) for c,n in C.items())
open("llms.txt","w").write(ll)
print(len(data),len(urls))
