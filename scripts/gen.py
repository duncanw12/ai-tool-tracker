import json,re,html,os,hashlib
S="https://aitrackertool.dev"
GA_TAG='<script async src="https://www.googletagmanager.com/gtag/js?id=G-VMR6RG9R83"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag(\'js\',new Date());gtag(\'config\',\'G-VMR6RG9R83\');</script>'
C={"coding":"Coding & Vibe Coding","chat":"Chat Assistants","image":"Image","video":"Video","audio":"Voice & Audio","writing":"Writing","agents":"Agents & Automation","research":"Productivity & Research","design":"Design & Websites","itsec":"AI for IT & Cybersecurity"}
# name,cat,url,desc,free(True/None),price,tags
T=[
("Cursor","coding","https://cursor.com","AI-first code editor with agent mode, codebase chat and tab completion. Now sold as part of The X Subscription (Oct 13, 2026); existing Cursor plans keep working as legacy plans.",True,"Plus from $8/mo (Grok models only); Premium $30/mo adds cloud agents and third-party models at API list price","editor,agent,ide"),
("Bolt.new","coding","https://bolt.cello.so/MFwNDwJhlUB","Prompt, run, edit and deploy full-stack web apps right in your browser.",True,"Pro from $25/mo","vibe coding,web apps,browser"),
("v0","coding","https://v0.app","Vercel's AI app builder that turns prompts into React/Next.js apps and UI.",True,"Plus from $30/mo","vibe coding,react,ui"),
("Lovable","coding","https://lovable.dev","Build full-stack web apps by chatting with an AI engineer.",True,"Pro from $25/mo ($21/mo billed annually); free plan has 5 daily credits","vibe coding,web apps,no-code"),
("Replit","coding","https://replit.com","Browser IDE with Replit Agent that builds and deploys apps from a prompt.",True,"Core from $20/mo ($18/mo billed annually)","vibe coding,ide,deploy"),
("GitHub Copilot","coding","https://github.com/features/copilot","AI pair programmer and coding agent inside VS Code, JetBrains and GitHub.",True,"Pro from $10/mo","autocomplete,agent,github"),
("Devin","coding","https://devin.ai","Cognition's coding agents: Devin Desktop (the editor formerly called Windsurf) plus Devin cloud agents. Fusion mode in Devin Desktop and CLI pairs a frontier lead model with a cheaper sidekick; with Opus 5.5 and GPT-6 Luna it scores 68.1 on the Artificial Analysis Coding Agent Index.",True,"Pro from $20/mo","editor,agent,ide,cloud agents"),
("Zed","coding","https://zed.dev","Fast open-source code editor with AI edit predictions, an agent panel and bring-your-own-key support.",True,"Pro from $10/mo","editor,open source,ide"),
("OpenRouter","coding","https://openrouter.ai","One OpenAI-compatible API for 500+ models from 80+ providers, with fallback routing.",True,"Pay-as-you-go; 5.5% fee on credit purchases","api,models,routing"),
("Muse Spark Open (Meta)","coding","https://dev.meta.ai/models/muse-spark-open","Meta's open-weight multimodal MoE model (816B total, 42B active, 1M context) built for coding and agent work. Released Oct 15, 2026.",True,"Free open weights (Muse Model License); hosted via OpenRouter, Groq, Together and others","open weights,models,meta,new"),
("NVIDIA Nemotron 3.5 Bolt","coding","https://ollama.com/library/nemotron-3.5-bolt","NVIDIA's open local model (74B total, 9B active, 256K context) for coding, reasoning, vision and tool use. Fits about 24GB of GPU memory via Ollama, llama.cpp or LM Studio (NVIDIA GPUs; no Apple silicon yet). Released Oct 15, 2026.",True,"Free open weights (OpenMDW License 1.1)","open weights,local models,nvidia,new"),
("OpenCode","coding","https://opencode.ai","Open-source AI coding agent for the terminal, desktop app and IDE. Use its free included models, connect 75+ providers (including local models), or sign in with GitHub Copilot or ChatGPT Plus/Pro. Security note: on Oct 17, 2026 OpenCode disclosed a breach of a legacy system behind its hosted Console that may have exposed provider API keys saved in Console workspaces (1.4% of Console users, all notified by email). Keys you add locally in the CLI or desktop app weren't part of it. Since then Anthropic has revoked affected Claude keys, Google has blocked exposed Gemini keys, OpenAI has refunded API credits used in the attack and OpenCode says its own refunds are underway. If you were notified, replace those keys and check usage back to Oct 16.",True,"Open source (MIT); optional Zen pay-as-you-go models","agent,terminal,open source,cli"),
("Hugging Face","coding","https://huggingface.co","The hub for open models, datasets and Spaces demos, plus hosted inference.",True,"PRO from $9/mo","open models,hosting,ml"),
("Claude Code","coding","https://claude.com/product/claude-code","Anthropic's agentic coding tool for the terminal, IDE and web.",None,"Included with paid Claude plans","agent,terminal,cli"),
("OpenAI Codex","coding","https://openai.com/codex/","OpenAI's coding agent for the CLI, IDE and cloud tasks.",True,"Included with ChatGPT plans (limited on Free and Go)","agent,cli,openai"),
("Warp","coding","https://www.warp.dev","Agentic terminal and development environment with built-in AI agents.",True,"Build from $20/mo","terminal,agent"),
("Cline","coding","https://cline.bot","Open-source autonomous coding agent for VS Code.",None,"Open source","agent,open source,vs code"),
("Aider","coding","https://aider.chat","Open-source AI pair programming in your terminal, with git integration.",None,"Open source","cli,open source,git"),
("ChatGPT","chat","https://chatgpt.com","OpenAI's general-purpose AI assistant for chat, writing, code and images.",True,"Plus $20/mo; lower-cost Go plan also available","assistant,openai"),
("Claude","chat","https://claude.ai","Anthropic's AI assistant for writing, analysis and coding.",True,"Pro from $17/mo billed annually ($20 monthly)","assistant,anthropic"),
("Gemini","chat","https://gemini.google.com","Google's AI assistant, connected to Google apps and search. For work, the new Gemini agent (Oct 8, 2026) runs inside Gmail, Docs, Sheets and Calendar.",True,"Google AI Plus from $4.99/mo (US)","assistant,google"),
("Grok","chat","https://grok.com","xAI's AI assistant with real-time knowledge from X and the web.",True,"Free on the web and in the apps; SuperGrok paid upgrade for higher limits","assistant,xai"),
("Microsoft Copilot","chat","https://copilot.microsoft.com","Microsoft's AI companion for chat, search and creation.",None,"","assistant,microsoft"),
("Le Chat (Mistral)","chat","https://chat.mistral.ai","Mistral AI's chat assistant, with Mistral Vibe for coding in the CLI, IDE or web.",True,"Pro from $14.99/mo","assistant,mistral,europe"),
("Ollama","chat","https://ollama.com","Run open models locally with one command, or use Ollama's cloud models when your machine isn't enough.",True,"Paid plans from $20/mo","local models,open weights,privacy"),
("LM Studio","chat","https://lmstudio.ai","Desktop app (now with the Bionic agent) for downloading and running local LLMs via llama.cpp and MLX.",True,"Bionic+ from $20/mo","local models,desktop,privacy"),
("DeepSeek","chat","https://chat.deepseek.com","Chat assistant powered by DeepSeek's open-weight models.",None,"","assistant,open weights"),
("Midjourney","image","https://www.midjourney.com","AI image and video generator known for its distinctive artistic style.",None,"Basic from $10/mo ($8/mo billed annually)","image generation,art"),
("Ideogram","image","https://ideogram.ai","AI image generator that's strong at rendering text in images.",True,"Plus from $15/mo billed annually ($20 monthly)","image generation,typography"),
("Leonardo.Ai","image","https://leonardo.ai","AI image and video generation platform for creators and game assets.",True,"Essential from $12/mo; free plan has 150 tokens/day","image generation,assets"),
("Krea","image","https://www.krea.ai","Real-time AI image and video generation and enhancement.",True,"Pro from $21/mo billed yearly ($35 monthly)","image generation,upscaling,real-time"),
("Adobe Firefly","image","https://www.adobe.com/products/firefly.html","Adobe's generative AI for images, video and design, built into Creative Cloud.",None,"","image generation,adobe"),
("Black Forest Labs (FLUX)","image","https://bfl.ai","Makers of the FLUX image models, including FLUX 3 Image Klein (Oct 15, 2026): open weights, native 4K, runs on consumer GPUs.",True,"API from $0.009/image (FLUX 3 Image Klein at 1K); open weights free for individuals and companies under $5M revenue","image models,api"),
("InvokeAI","image","https://github.com/invoke-ai/InvokeAI","Free, open-source AI image studio you run on your own GPU: a unified canvas for inpainting and outpainting, node-based workflows and a gallery, with support for SDXL, SD 3.5, FLUX.1, FLUX.2, Qwen Image and more. About 28,700 GitHub stars; v7.0 is in alpha.",None,"Open source (Apache-2.0)","local models,open source,canvas,stable diffusion"),
("Recraft","image","https://www.recraft.ai","AI image generator for designers, with vector and brand-style output.",True,"","vector,design,image generation"),
("Runway","video","https://runway.com","AI video generation and editing tools for filmmakers and creators.",True,"Standard from $12/mo billed annually","video generation,editing"),
("Synthesia","video","https://www.synthesia.io","Create videos with AI avatars and voiceovers from text.",True,"Starter from $29/mo","avatars,video generation,training"),
("Pika","video","https://pika.art","AI video generator for short creative clips and effects.",True,"Starter from $10/mo","video generation,effects"),
("Luma AI","video","https://lumalabs.ai","AI video generation with the Dream Machine and Ray models.",None,"Plus from $30/mo","video generation"),
("HeyGen","video","https://www.heygen.com","AI avatar videos, translation and lip-sync.",True,"Creator from $29/mo","avatars,translation"),
("Descript","video","https://www.descript.com","Edit video and podcasts by editing the transcript, with AI tools.",True,"Hobbyist from $16/mo billed annually ($24 monthly)","editing,podcast,transcription"),
("Kling AI","video","https://kling.ai","Kuaishou's AI video generation model and app.",None,"","video generation"),
("ElevenLabs","audio","https://elevenlabs.io","AI voice generation, cloning, dubbing and speech-to-text. New Oct 15: Instant Soundtracks scores an uploaded video with original music and timed sound effects.",True,"Starter from $6/mo; Creator $22/mo (first month 50% off)","text to speech,voice cloning,music"),
("Suno","audio","https://suno.com","Generate full songs with vocals from a text prompt.",True,"Pro from $8/mo billed yearly","music generation"),
("Udio","audio","https://www.udio.com","AI music generation and remixing.",True,"Standard from $10/mo ($8/mo billed annually)","music generation"),
("Fish Audio","audio","https://fish.audio","AI text-to-speech and voice cloning with a web studio, mobile apps and an API. Its Drama 3 model (Oct 13, 2026) takes plain-language direction (whisper this line, laugh here) and voices multi-character scenes, and the weights are open: free for commercial use under $500K annual revenue (Fish Audio Community License). Its fish-speech repo has about 33,000 GitHub stars. Self-hosting needs a 48GB NVIDIA GPU.",True,"Plus from $11/mo billed annually ($15 monthly); free plan has 8,000 credits/mo","text to speech,voice cloning,open weights"),
("Murf AI","audio","https://murf.ai","AI voiceover studio and text-to-speech API with 150+ voices in 35+ languages.",None,"API from $0.01 per 1,000 characters (Falcon); $10 free API credit","text to speech,voiceover"),
("Jasper","writing","https://www.jasper.ai","AI content platform for marketing teams.",None,"Pro from $59/mo","marketing,content"),
("Writesonic","writing","https://writesonic.com","AI writing and SEO/AI-search visibility platform.",None,"Starter from $79/mo billed annually","seo,content"),
("Copy.ai","writing","https://www.copy.ai","AI platform for go-to-market copy and workflows.",None,"Paid plans from $29/mo","marketing,copywriting"),
("Grammarly","writing","https://www.grammarly.com","AI writing assistant for grammar, tone and rewriting.",True,"Pro from $12/mo","grammar,editing"),
("QuillBot","writing","https://quillbot.com","AI paraphrasing, grammar checking and summarizing.",None,"","paraphrasing,summarizing"),
("n8n","agents","https://n8n.io","Workflow automation with AI agents; self-hostable and fair-code.",True,"Cloud Starter from €20/mo billed annually; self-hosted Community Edition free","automation,self-hosted,agents"),
("Zapier","agents","https://zapier.com","Automate work across 7,000+ apps with Zaps and AI agents.",True,"Professional from $19.99/mo","automation,no-code,integrations"),
("Make","agents","https://www.make.com/?pc=aitrackertool","Visual automation platform with AI agents.",True,"Free plan with 1,000 credits/mo; paid plans priced by credits","automation,no-code,visual"),
("Relay.app","agents","https://www.relay.app","AI workflow automation with human-in-the-loop steps.",None,"","automation,agents"),
("Muse (Meta)","agents","https://muse.ai","Meta's personal AI agent that uses apps for you: email, travel, shopping and more, via app, web or WhatsApp. US-only at launch (Sept 8, 2026).",True,"Paid plans for heavier use","personal agent,meta,whatsapp,new"),
("Hermes Agent","agents","https://hermes-agent.nousresearch.com","Nous Research's open-source personal agent with app connectors, a plugin catalog and one-click local models.",None,"Open source (MIT)","open source,agents,local models"),
("Harness2 (Google Research)","agents","https://github.com/google-research/harness2","Open-source framework from Google Cloud AI Research that improves an agent's harness (prompts, tools, memory, skills, subagents) instead of its model: it proposes edits, tests them on the same task and keeps what worked for next time. Runs OpenCode or Codex as the executor. About 13,500 GitHub stars two weeks after release; research code, not an official Google product.",None,"Open source (Apache-2.0)","agents,open source,self-improving,research"),
("Lindy","agents","https://www.lindy.ai","Build AI agents that handle email, meetings and workflows.",None,"Team from $29.99/mo; $50 in starter credits","agents,assistant"),
("Perplexity","research","https://www.perplexity.ai","AI answer engine that searches the web and cites sources.",None,"","search,research,citations"),
("Gemini Notebook","research","https://notebook.google","Google's AI research notebook (formerly NotebookLM), grounded in your own sources, with audio overviews.",None,"","research,notes,google"),
("Granola","research","https://www.granola.ai","Bot-free AI meeting notes that enhance your own jottings, with chat across meetings.",True,"Business from $14/user/mo","meetings,notes"),
("Notion AI","research","https://www.notion.com","Notion's workspace with built-in AI for writing, search and agents.",True,"Plus from $10/mo","notes,workspace"),
("Otter.ai","research","https://otter.ai","AI meeting notes, transcription and summaries.",True,"Pro $16.99/user/mo billed monthly","meetings,transcription"),
("Fireflies.ai","research","https://fireflies.ai/?fpr=duncan-873b18","AI notetaker that records, transcribes and summarizes meetings.",True,"Pro from $10/seat/mo billed annually ($18 monthly)","meetings,transcription"),
("Elicit","research","https://elicit.com","AI research assistant for finding and analyzing papers.",None,"Plus from $11/mo","academic,papers"),
("Consensus","research","https://consensus.app","AI search engine for scientific research.",None,"","academic,search"),
("Gamma","design","https://try.gamma.app/74bhdc77mraq","Create presentations, docs and websites with AI.",None,"","presentations,slides"),
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
("Snyk","itsec","https://snyk.io","Developer security platform that scans your code, open-source dependencies, containers and IaC from the IDE, CLI and repos.",True,"Team from $25/mo (up to 10 developers)","code security,sca,sast,beginner"),
("Semgrep","itsec","https://semgrep.dev","Fast code scanner (SAST, supply chain, secrets) with AI-powered detection, triage and autofix. Great for scanning your own home-lab scripts.",True,"Free for up to 10 contributors (60 AI credits); Teams Code from $30/contributor/mo","code security,sast,open source,autofix"),
("GitHub Copilot Autofix","itsec","https://docs.github.com/en/code-security/concepts/code-scanning/autofix-for-code-scanning","AI fixes for CodeQL code scanning alerts. Agentic autofix (GA Oct 15, 2026) investigates alerts and opens a draft PR with a validated fix.",True,"Free on public repos; private repos need GitHub Code Security","code scanning,github,autofix,codeql"),
("VirusTotal Code Insight","itsec","https://www.virustotal.com","AI summaries in VirusTotal that explain what a suspicious script (starting with PowerShell) or decompiled code actually does. Handy for malware-analysis practice.",True,"Free for community users on eligible uploads; Code Insight API limited to 50 requests/day","malware analysis,soc,beginner,threat intel"),
("Tines","itsec","https://www.tines.com","Security and IT workflow automation (SOAR) with built-in AI and bring-your-own-model support, used by SOC and IT teams.",True,"Free edition: 3 live workflows + one-time $50 AI allowance; paid editions on request","soar,automation,soc,it ops"),
("SentinelOne Purple AI","itsec","https://www.sentinelone.com/platform/purple/","Agentic AI security analyst in the SentinelOne Singularity Platform: ask questions in plain English, auto-triage alerts and run guided investigations.",None,"","soc,edr,triage,incident response"),
("Wazuh","itsec","https://wazuh.com","Free, open-source SIEM and XDR used by home labbers and SOC teams for log analysis, threat detection and compliance. Wazuh documents AI threat hunting with local models via Ollama, and Wazuh 5.0 (now in release candidate) adds a built-in AI Assistant.",True,"Free and open source (self-hosted); Wazuh Cloud is a paid hosted option","siem,xdr,open source,home lab,beginner"),
("CyberStrikeAI","itsec","https://github.com/AIPentest/CyberStrikeAI","Open-source AI pentesting platform written in Go: agents run 100+ security tools over MCP, with human approval steps, audit logs and CTF roles. Only for labs and systems you're authorized to test.",None,"Open source (Apache-2.0)","pentesting,open source,mcp,ctf"),
("Sophos AI Defense","itsec","https://www.sophos.com/en-us/products/ai-defense","Finds the AI tools employees and apps are using, including unapproved shadow AI, and enforces real-time guardrails on prompts and data across endpoint, network, identity and browser. Generally available Oct 16, 2026.",None,"Quote-based add-on for Sophos EDR, XDR and MDR customers","shadow ai,governance,msp,data protection"),
("garak (NVIDIA)","itsec","https://github.com/NVIDIA/garak","NVIDIA's open-source LLM vulnerability scanner: probes chatbots and AI apps for prompt injection, jailbreaks, data leakage, hallucination and toxicity, then reports what got through. v0.17.1 shipped Oct 16, 2026.",None,"Open source (Apache-2.0)","ai red teaming,llm security,open source,home lab"),
("Atera","itsec","https://www.atera.com","All-in-one IT management (RMM, help desk, ticketing and patching) priced per technician, with AI Copilot built into every plan for scripts, ticket summaries and knowledge-base drafts. Robin, its end-user AI agent, is sold separately.",None,"Professional from $149/technician/mo billed annually ($169 monthly); 30-day free trial","rmm,help desk,msp,it ops"),
("Security Onion","itsec","https://securityonion.net","Free and open platform for threat hunting, network security monitoring and log management (2+ million downloads), a staple of SOC home labs. Security Onion 3 shipped in 2026. Onion AI, its assistant for alert analysis and detection tuning (now with local model support), comes with Security Onion Pro.",True,"Free and open; Onion AI is part of Security Onion Pro (contact sales)","siem,nsm,threat hunting,home lab"),
("promptfoo","itsec","https://www.promptfoo.dev","Open-source CLI for testing and red-teaming LLM apps and agents: write evals in YAML, compare models side by side and scan for prompt injection, jailbreaks and data leaks. About 26,000 GitHub stars; the site says 300,000+ developers use it.",True,"Community edition free and open source (MIT), red teaming up to 10k probes/mo; Enterprise custom","ai red teaming,llm security,evals,open source"),
("Nuclei (ProjectDiscovery)","itsec","https://github.com/projectdiscovery/nuclei","Fast open-source vulnerability scanner built on thousands of community YAML templates, with an -ai option that generates and runs a template from a plain-English prompt. About 32,000 GitHub stars. Only scan systems you own or are authorized to test.",None,"Open source (MIT); free AI template editor on ProjectDiscovery Cloud","vulnerability scanning,pentesting,open source,home lab"),
("Freshservice","itsec","https://www.freshworks.com/freshservice/","Cloud IT service desk (ITSM) from Freshworks: ticket and incident queues, knowledge base, self-service portal and service catalog, with Freddy AI Copilot as an add-on. A common help desk platform you can practice on with the free trial.",None,"Starter from $19/agent/mo billed annually; Freddy AI Copilot add-on $29/agent/mo; free trial","help desk,itsm,ticketing,it ops"),
("Microsoft Security Copilot","itsec","https://www.microsoft.com/en-us/security/business/ai-machine-learning/microsoft-security-copilot","Generative AI for security teams across Microsoft Defender, Sentinel, Entra, Intune and Purview: summarize incidents, write queries and reverse-engineer malicious scripts in plain English.",None,"Pay-as-you-go: $4 per provisioned SCU/hour","soc,microsoft,incident response"),
("Google Security Operations","itsec","https://cloud.google.com/security/products/security-operations","Google's SecOps platform (SIEM + SOAR) with Gemini for natural-language search, detection writing and investigation.",None,"","siem,soc,gemini"),
("CrowdStrike Charlotte AI","itsec","https://www.crowdstrike.com/en-us/platform/charlotte-ai/","Agentic security analyst in the CrowdStrike platform that triages detections and speeds up investigations.",None,"","soc,edr,triage"),
("Splunk AI Assistant","itsec","https://www.splunk.com/en_us/products/splunk-ai-assistant.html","Natural-language assistant in Splunk for finding dashboards, reports and data and getting help with searches over your logs.",None,"No additional fee for Splunk Cloud Platform and Splunk Enterprise customers","log analysis,spl,siem"),
("Mantis (Google)","itsec","https://github.com/google/mantis","Google's open-source toolkit of skills that lets AI coding agents find, reproduce and patch vulnerabilities in your code, from threat modelling to the final report, plus a reference harness you can point at a repo with a plain-English focus like look for IDOR. About 2,500 GitHub stars. Google says to run it only in isolated environments and to verify every finding by hand.",None,"Open source (Apache-2.0); model usage billed by your AI provider","code security,appsec,ai agents,open source"),
("Jira Service Management","itsec","https://www.atlassian.com/software/jira/service-management","Atlassian's IT service desk: request portal, queues, SLAs, knowledge base, incident and change management, with Rovo AI agents and search on paid plans. One of the most common ticketing tools in help desk job posts, and the free plan is enough to build a practice service desk.",True,"Free for up to 3 agents; Standard adds Rovo AI agents (per-agent pricing, 14-day free trial)","help desk,itsm,ticketing,it ops"),
("Elastic Security AI","itsec","https://www.elastic.co/security/ai","AI in Elastic Security: automated alert triage and hypothesis-driven threat hunts with ES|QL over your SIEM data.",None,"Elastic AI Assistant included in Serverless Security Analytics Complete, from $0.11/GB ingested plus retention","log analysis,siem,threat hunting"),
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
DROP="/drop-2026-10-20.html"
DROPDATE="Oct 20, 2026"
PREVDROP="/drop-2026-10-19.html"
PREVDATE="Oct 19, 2026"
import datetime
# Build date: override with BUILD_DATE=YYYY-MM-DD; a tool can carry its own "verified":"YYYY-MM-DD".
BUILD=datetime.date.fromisoformat(os.environ["BUILD_DATE"]) if os.environ.get("BUILD_DATE") else datetime.date.today()
def vdate(x): return datetime.date.fromisoformat(x["verified"]) if x.get("verified") else BUILD
def mdy(d): return d.strftime("%b ")+str(d.day)+d.strftime(", %Y")
VER=BUILD.strftime("%m/%d")
INTRO={"itsec":'<div class="note-box"><div class="nb-h">Breaking into IT? Start here</div><p><b>Cert study and labs:</b> TryHackMe\'s Echo tutor and HTB Coach. <b>Scripting and PowerShell:</b> practice with <a href="/tools/github-copilot.html">GitHub Copilot</a> or <a href="/tools/warp.html">Warp</a>, then scan your own scripts for free with <a href="/tools/semgrep.html">Semgrep</a> or <a href="/tools/snyk.html">Snyk</a>. <b>SOC and malware practice:</b> stand up <a href="/tools/wazuh.html">Wazuh</a>, the free open-source SIEM, or <a href="/tools/security-onion.html">Security Onion</a> for network monitoring and threat hunting, in your home lab and point it at a few VMs, paste a suspicious PowerShell sample into <a href="/tools/virustotal-code-insight.html">VirusTotal Code Insight</a> and build a small alert workflow on the <a href="/tools/tines.html">Tines</a> free edition. <b>Help desk and MSP work:</b> start the 30-day free trial of <a href="/tools/atera.html">Atera</a>, the RMM and ticketing platform many MSPs run, and practice working tickets and generating scripts with its built-in AI Copilot. For internal IT help desk roles, the <a href="/tools/freshservice.html">Freshservice</a> free trial lets you practice incidents, a knowledge base and a self-service portal, and the free plan of <a href="/tools/jira-service-management.html">Jira Service Management</a> (up to 3 agents, no time limit) lets you build a practice service desk with a portal, queues and SLAs that you can show in interviews. <b>Vulnerability scanning:</b> run <a href="/tools/nuclei-projectdiscovery.html">Nuclei</a> against your own lab VMs (never anything you don\'t own) and try its <code>-ai</code> option to turn a plain-English check into a template. <b>AI security:</b> point <a href="/tools/garak-nvidia.html">garak</a> at a local model to see how prompt injection and jailbreaks actually work, then write your own red-team tests with <a href="/tools/promptfoo.html">promptfoo</a>. To see how AI agents hunt bugs in code, run Google\'s <a href="/tools/mantis-google.html">Mantis</a> on a deliberately vulnerable practice app inside an isolated VM. <b>Home lab:</b> run local models with <a href="/tools/ollama.html">Ollama</a> and turn notes into quizzes with <a href="/tools/gemini-notebook.html">Gemini Notebook</a>. The SOC copilots further down (Security Copilot, Purple AI, Charlotte AI) are enterprise tools you\'ll likely meet on the job, so their docs are worth a read even before you can use them.</p></div>',
 "coding":'<div class="note-box"><div class="nb-h">Rethinking your Cursor plan?</div><p>See our side-by-side <a href="/cursor-alternatives.html">Cursor alternatives (2026)</a> page: editors, terminal agents and open-source options with checked pricing.</p></div>'}
LOGO='<svg viewBox="0 0 28 28" width="26" height="26" aria-hidden="true" focusable="false"><path d="M5 6L14 14 23 8M14 14L9 23M14 14L23 21" stroke="currentColor" stroke-width="1.5" fill="none"/><circle cx="5" cy="6" r="2.5" fill="currentColor"/><circle cx="23" cy="8" r="2.5" fill="currentColor"/><circle cx="9" cy="23" r="2.5" fill="currentColor"/><circle cx="23" cy="21" r="2.5" fill="currentColor"/><circle cx="14" cy="14" r="3.5" fill="#00ff9c"/></svg>'
ICONS='<link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><meta name="theme-color" content="#0d1520">'
MENUJS='<script>(function(){var d=document.querySelector(".mmenu");if(!d)return;function c(){d.open=false}d.addEventListener("click",function(e){if(e.target.closest(".mpanel a"))c()});document.addEventListener("pointerdown",function(e){if(d.open&&!d.contains(e.target))c()});document.addEventListener("keydown",function(e){if(e.key==="Escape"&&d.open){c();d.querySelector("summary").focus()}})})()</script>'
def _h(f): return hashlib.md5(open(f,'rb').read()).hexdigest()[:8]
AV={f:_h(f) for f in ['style.css','filter.js','config.js','tools.js']}
def bust(h):
  for f,v in AV.items(): h=re.sub(r'((?:href|src)="/?'+re.escape(f)+r')(\?v=[0-9a-f]+)?"',lambda m:m.group(1)+'?v='+v+'"',h)
  return h
def nav():
  return ('<a class="skip" href="#main">Skip to content</a><header class="bar"><a class="logo" href="/" aria-label="AI Tool Tracker home"><span class="lg-mark">'+LOGO+'</span><span data-sitename>AI Tool Tracker</span></a>'
   '<details class="mmenu"><summary class="mbtn" aria-label="Menu"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18" stroke="currentColor" stroke-width="2" fill="none"/></svg><span>menu</span></summary>'
   f'<nav class="mpanel" aria-label="Mobile"><a href="/#directory">Directory</a><a href="{DROP}">Today\'s drop</a><a href="/#newsletter">Newsletter</a><a class="cta" href="/#submit">Submit a tool</a></nav></details>'
   f'<nav class="top" id="topnav" aria-label="Main"><a href="/#directory">Directory</a><a href="{DROP}">Today\'s drop</a><a href="/#newsletter">Newsletter</a><a class="cta" href="/#submit">Submit a tool</a></nav></header>'+MENUJS)
def side(cur=None,home=False):
  it=[]
  if home: it.append(f'<a class="chip fi on" href="#directory" data-c="all"><span class="fn">All tools</span><span class="n">{len(data)}</span></a>')
  else: it.append(f'<a class="fi" href="/#directory"><span class="fn">All tools</span><span class="n">{len(data)}</span></a>')
  for k,v in C.items():
    on=k==cur
    it.append(f'<a class="{"chip " if home else ""}fi{" on" if on else ""}" href="{"#cat-"+k if home else "/categories/"+k+".html"}" data-c="{k}"{" aria-current=\"page\"" if on else ""}><span class="fn">{e(v)}</span><span class="n">{CNT[k]}</span></a>')
  return (f'<aside class="side" aria-label="Categories"><div class="side-h">Categories</div><nav class="tree"{" id=\"cats\"" if home else ""} aria-label="Categories">{"".join(it)}</nav>'
   f'<div class="side-h sh2">Start here</div><nav class="tree t2" aria-label="Quick links"><a class="fi" href="/categories/itsec.html"><span class="fn">Breaking into IT</span></a><a class="fi" href="/cursor-alternatives.html"><span class="fn">Cursor alternatives</span></a><a class="fi" href="{DROP}"><span class="fn">Today\'s drop</span></a><a class="fi" href="/issue-001.html"><span class="fn">Newsletter issue #001</span></a></nav></aside>')
def mkfoot():
  cl="".join(f'<li><a href="/categories/{k}.html">{e(v)}</a></li>' for k,v in C.items())
  return (f'<footer class="site"><div class="fgrid"><div><a class="logo" href="/"><span class="lg-mark">{LOGO}</span>AI Tool Tracker</a><p class="mut">Hand-checked AI tools for builders and IT folks, updated daily.</p><p><a href="https://x.com/AITRACKERTOOL" target="_blank" rel="noopener">@AITRACKERTOOL on X</a> · <a href="https://aitrackertool.beehiiv.com/subscribe" target="_blank" rel="noopener">Newsletter</a></p></div>'
   f'<div><h4>Categories</h4><ul class="flist">{cl}</ul></div><div><h4>Site</h4><ul class="flist one"><li><a href="/#directory">Directory</a></li><li><a href="{DROP}">Today\'s drop</a></li><li><a href="/cursor-alternatives.html">Cursor alternatives</a></li><li><a href="/issue-001.html">Issue #001</a></li><li><a href="/#submit">Submit / Sponsor</a></li></ul></div></div>'
   '<div class="disc">© 2026 <span data-sitename>AI Tool Tracker</span>. <b>Affiliate disclosure:</b> some links on this site are affiliate links (marked "affiliate link"). If you sign up through them we may earn a commission at no extra cost to you. It never affects which tools we pick. This site uses Google Analytics to count visits.</div></footer>')
FOOTER=mkfoot()
SCROLL='<script>(function(){var a=document.querySelector(".side .fi.on");if(a&&innerWidth<900)a.parentNode.parentNode.scrollLeft=a.offsetLeft-12})()</script>'
NLBAND=lambda idn='': (f'<section class="nlband"{idn} aria-label="Newsletter signup"><div class="nlt"><b>Get the weekly drop</b><span>The best new AI tools, one email a week. Free.</span></div>'
 '<div class="nlembed"><script async src="https://subscribe-forms.beehiiv.com/v3/loader.js" data-beehiiv-form="6370ffac-0fdf-4341-bc97-5159de9c02fd"></script><noscript><a href="https://aitrackertool.beehiiv.com/subscribe">Subscribe on beehiiv</a></noscript></div></section>')
def shell(main,cur=None,home=False): return '<div class="shell">'+side(cur,home)+'<main id="main" class="main">'+main+FOOTER+'</main></div>'+SCROLL
def head(t,d,path,ld):
  return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(t)}</title><meta name="description" content="{e(d)}"><link rel="canonical" href="{S}/{path}"><meta property="og:title" content="{e(t)}"><meta property="og:description" content="{e(d)}"><meta property="og:url" content="{S}/{path}"><meta name="twitter:card" content="summary"><meta name="twitter:site" content="@AITRACKERTOOL"><script type="application/ld+json">{json.dumps(ld)}</script>{ICONS}<link rel="stylesheet" href="/style.css">'+GA_TAG+'</head><body>'+nav()
END='<script src="/config.js"></script><script type="text/javascript" async src="https://subscribe-forms.beehiiv.com/attribution.js"></script></body></html>'
def isaff(x): return "bolt.cello.so" in x["url"] or "make.com/?pc=" in x["url"] or "fireflies.ai/?fpr=" in x["url"] or "try.gamma.app" in x["url"]
CLEAN={"bolt.cello.so":"https://bolt.new","make.com/?pc=":"https://www.make.com","fireflies.ai/?fpr=":"https://fireflies.ai","try.gamma.app":"https://gamma.app"}
def clean(u): return next((v for k,v in CLEAN.items() if k in u),u)
AFFNOTE='<span class="affnote">Affiliate link: we may earn a commission if you sign up, at no extra cost to you.</span>'
def tags(x):
  p=x["pf"]
  t={"free":'<span class="t free">FREE</span>',"both":'<span class="t free">FREE TIER</span>',"paid":'<span class="t paid">PAID</span>'}.get(p,'<span class="t na">See site</span>')
  if isaff(x): t+='<span class="t aff">AFFILIATE</span>'
  if p or x.get("pricing"): t+=f'<span class="chk">checked {vdate(x).strftime("%m/%d")}</span>'
  return t
def visit(x,cls="go"):
  return f'<a class="{cls}" href="/go/{x["slug"]}" target="_blank" rel="{"sponsored nofollow noopener" if isaff(x) else "nofollow noopener"}" aria-label="Visit {e(x["name"])} (opens in new tab)">Visit ↗</a>'
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
  ld={"@context":"https://schema.org","@type":"SoftwareApplication","name":x["name"],"applicationCategory":x["catName"],"operatingSystem":"Web","description":x["desc"],"url":clean(x["url"])}
  if "freeTier" in x: ld["offers"]={"@type":"Offer","price":"0","priceCurrency":"USD"}
  rel=[y for y in data if y["category"]==x["category"] and y is not x]
  b=head(f'{x["name"]}: pricing, free tier & alternatives | AI Tool Tracker',f'{x["name"]}: {x["desc"]} Pricing, free tier and related {x["catName"]} tools.',f'tools/{x["slug"]}.html',ld)
  free={"free":"Yes","both":"Yes","paid":"No"}.get(x["pf"],"Check site")
  m=(f'<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/categories/{x["category"]}.html">{e(x["catName"])}</a> / <span aria-current="page">{e(x["name"])}</span></nav>'
   f'<article class="detail"><h1>{e(x["name"])}</h1><p class="lede">{e(x["desc"])}</p><div class="c-tags">{tags(x)}</div>'
   f'<dl class="facts"><div><dt>Category</dt><dd><a href="/categories/{x["category"]}.html">{e(x["catName"])}</a></dd></div><div><dt>Price</dt><dd>{e(x.get("pricing") or "See official site")}</dd></div><div><dt>Free option</dt><dd>{free}</dd></div><div><dt>Last checked</dt><dd>{mdy(vdate(x))}</dd></div></dl>'
   '<p class="kw">'+"".join(f'<code>{e(t)}</code>' for t in x["tags"])+f'</p><p>{visit(x,"btn").replace("Visit ↗","Visit "+e(x["name"])+" ↗")}'+(' <b class="afftag">(affiliate link)</b>' if isaff(x) else '')+'</p>'+('<p class="note">This is an affiliate link: we may earn a commission if you sign up, at no extra cost to you.</p>' if isaff(x) else '')+
   f'</article>'+NLBAND()+f'<section class="grp-s"><div class="gh"><h2>Related {e(x["catName"])} tools <span class="n">{len(rel)}</span></h2><a href="/categories/{x["category"]}.html">See all</a></div>{table([row(y,filt=False) for y in rel])}</section>')
  open(f'tools/{x["slug"]}.html','w').write(b+shell(m,x["category"])+END); urls.append(f'tools/{x["slug"]}.html')
for c,n in C.items():
  mm=[y for y in data if y["category"]==c]
  lab=n if n.startswith("AI ") else f"{n} AI tools"
  ld={"@context":"https://schema.org","@type":"CollectionPage","name":lab,"itemListElement":[{"@type":"ListItem","position":i+1,"url":f'{S}/tools/{y["slug"]}.html',"name":y["name"]} for i,y in enumerate(mm)]}
  b=head(f'Best {lab} (2026) | AI Tool Tracker',f'{len(mm)} {n} AI tools with pricing and free-tier info: '+", ".join(y["name"] for y in mm)[:120],f'categories/{c}.html',ld)
  m=(f'<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/#directory">Categories</a> / <span aria-current="page">{e(n)}</span></nav><h1 class="ch1">{e(lab)}</h1><p class="lede">{len(mm)} tools. Prices and free tiers shown only where we checked them on the official site.</p>'+INTRO.get(c,'')+NLBAND()+
   '<div class="sticky">'+ctl(len(mm))+'</div>'+table([row(y) for y in mm]))
  open(f'categories/{c}.html','w').write(b+shell(m,c)+'<script src="/filter.js"></script>'+END); urls.append(f'categories/{c}.html')
# ---- daily drop page (static) ----
BY={y["slug"]:y for y in data}
NEWS=["jira-service-management","mantis-google","fish-audio","harness2-google-research"]
PFIX=["cursor","devin","elevenlabs","opencode"]
nit=CNT["itsec"]
dt=f"Daily Drop {DROPDATE}: Jira Service Management, Google Mantis, Fish Audio, Harness2 | AI Tool Tracker"
dd=f"{len(NEWS)} tools added on {DROPDATE}: a free help desk to practice on, Google's open-source AI vulnerability toolkit, Fish Audio's open-weight Drama 3 voice model and Google's self-improving agent framework, plus Cursor's new plans and an OpenCode breach update."
ld={"@context":"https://schema.org","@type":"Article","headline":f"Daily Drop · {DROPDATE}","datePublished":BUILD.isoformat(),"publisher":{"@type":"Organization","name":"AI Tool Tracker"},"url":f"{S}{DROP}","about":[{"@type":"SoftwareApplication","name":BY[k]["name"],"url":clean(BY[k]["url"])} for k in NEWS]}
plist="".join(f'<li><a href="/tools/{k}.html">{e(BY[k]["name"])}</a>: {e(BY[k]["pricing"])}'+(' <span class="afftag">(affiliate link on the tool page)</span>' if isaff(BY[k]) else '')+'</li>' for k in PFIX)
m=(f'<header class="phero"><span class="badge">DAILY DROP · {DROPDATE.upper()}</span><h1>Today\'s drop: {len(NEWS)} new tools, {len(PFIX)} listing updates</h1><p class="tag">The directory now lists {len(data)} hand-checked tools. <a href="/categories/itsec.html">AI for IT &amp; Cybersecurity</a> grows to {nit} tools with Jira Service Management, a free help desk you can practice on, and Mantis, Google\'s open-source toolkit for AI agents that find and patch vulnerabilities. Fish Audio joins Voice &amp; Audio with its open-weight Drama 3 model, and Google\'s Harness2 joins Agents. Plus: Cursor\'s new plans and an update on the OpenCode breach. Pricing only where the official page states it.</p><p class="mut">Previous drop: <a href="{PREVDROP}">{PREVDATE} →</a></p></header>'
 +NLBAND()+
 f'<section class="grp-s"><div class="gh"><h2>New in the directory <span class="n">{len(NEWS)}</span></h2><a href="/#directory">Browse all {len(data)}</a></div>{table([row(BY[k],True,False) for k in NEWS],True)}</section>'
 f'<section class="pc"><h2>Why these four</h2><ul><li><a href="/tools/jira-service-management.html">Jira Service Management</a> is one of the ticketing tools you\'ll see most in help desk job posts. The free plan covers up to 3 agents with no time limit, so you can build a small service desk with a request portal, queues, SLAs and a knowledge base, then walk an interviewer through it. Rovo AI agents come with the paid Standard plan.</li><li><a href="/tools/mantis-google.html">Mantis</a> is Google\'s open-source (Apache-2.0) set of skills that lets AI coding agents find, reproduce and patch vulnerabilities, with a reference harness you can point at a repo and tell what to hunt for in plain English. It has about 2,500 GitHub stars. Google\'s own README says to run it only in isolated environments and to verify every finding by hand before reporting it, so try it on a deliberately vulnerable practice app in a VM.</li><li><a href="/tools/fish-audio.html">Fish Audio</a> released Drama 3 on Oct 13: a text-to-speech model you direct in plain language (a whisper stays a whisper, a laugh lands where you put it) that also handles multi-character scenes. The weights are open and free for commercial use if your revenue is under $500,000 a year, but self-hosting needs a 48GB NVIDIA GPU. The hosted app has a free plan, and Plus is $11 a month billed annually. Fish Audio says the API is 80% off and new creator plans are 50% off until Nov 12.</li><li><a href="/tools/harness2-google-research.html">Harness2</a> from Google Cloud AI Research improves the system around an agent (prompts, tools, memory, skills) rather than the model, and keeps what worked for the next task. It runs OpenCode or Codex as the executor and passed about 13,500 GitHub stars in two weeks. It\'s research code, not an official Google product, so it\'s for tinkerers for now.</li></ul>'
 f'<h2>Listing updates</h2><p class="mut">Checked on {mdy(BUILD)} against official pages and announcements.</p><ul><li><b>Cursor</b> is now sold as part of The X Subscription. Plus is $8 a month with Grok models only; Premium, at $30, adds cloud agents, automations and third-party models such as Claude and GPT, which are billed separately at API list price. If you\'re weighing the switch, see our <a href="/cursor-alternatives.html">Cursor alternatives</a> page.</li><li><b>Devin</b>: Cognition says Fusion, which pairs Claude Opus 5.5 as the lead with GPT-6 Luna as a cheaper sidekick, scores 68.1 on the Artificial Analysis Coding Agent Index at 31% lower cost per task than Claude Code with Opus 5.5. The cost figure is Cognition\'s own. Fusion is in Devin Desktop and the Devin CLI.</li><li><b>ElevenLabs</b> added Instant Soundtracks on Oct 15: upload a video and get an original score with sound effects timed to what\'s on screen.</li></ul>'
 f'<h2>Update: OpenCode Console breach</h2><p>Since our Oct 19 note, Anthropic has revoked Claude API keys it believes were affected, Google has blocked exposed Gemini keys, and OpenAI says it has refunded API credits used in the attack. OpenCode says it has contacted every affected user and its own refunds are underway, and its follow-up email lists each exposed key and puts the earliest possible exposure at 8:30 PM ET on Oct 16. If you got the email, replace those keys (a Claude key that suddenly fails was likely revoked), check usage back to Oct 16 and set spend limits. Keys added locally in the OpenCode CLI or desktop app weren\'t affected. The <a href="/tools/opencode.html">OpenCode listing</a> is updated.</p>'
 f'<h2>Category changes</h2><ul><li><a href="/categories/itsec.html">AI for IT &amp; Cybersecurity</a> grows from 24 to {nit} tools. The <b>Breaking into IT</b> guide adds the Jira Service Management free plan to the help desk step and Mantis to the AI security step.</li><li><a href="/categories/audio.html">Voice &amp; Audio</a> grows to {CNT["audio"]} tools with Fish Audio, and <a href="/categories/agents.html">Agents &amp; Automation</a> grows to {CNT["agents"]} with Harness2.</li></ul>'
 f'<h2>Checked, not listed</h2><ul><li><b>MiniMax M3.1 Flash</b>: available now through MiniMax\'s API at $0.15 per million input tokens and $0.60 per million output. Open weights have been reported for Oct 23, though MiniMax\'s own post only says later, so we\'ll look again once they\'re out.</li><li><b>The $88,982 Codex bill</b>: a widely shared account from one developer says Codex published a <code>.env</code> file to a public Cloudflare Pages site and the exposed Google API key was then abused. It\'s a single user\'s report, not a confirmed finding. The lesson holds either way: keep secrets out of any folder an agent can deploy, and set spend limits on every key.</li></ul></section>')
open(DROP.lstrip("/"),"w").write(head(dt,dd,DROP.lstrip("/"),ld)+shell(m)+END)
# ---- Cursor alternatives page ----
GRP=[("AI code editors","Closest to the Cursor experience: an editor with AI built in.",["devin","zed","github-copilot"]),
 ("Terminal and CLI coding agents","Hand a task to an agent that edits files and runs commands. Pair with any editor.",["claude-code","openai-codex","warp","aider"]),
 ("Open source and bring-your-own-key","Pay model providers directly, or run models locally, so a plan change can\'t cut your quota.",["cline","aider","zed","openrouter","ollama","muse-spark-open-meta"]),
 ("Prompt-to-app builders","For vibe coders who'd rather describe an app than edit files.",["replit","bolt-new","lovable","v0"])]
seen=[]
for _,_,ks in GRP:
  for k in ks:
    if k not in seen: seen.append(k)
ld={"@context":"https://schema.org","@type":"ItemList","name":"Cursor alternatives (2026)","itemListElement":[{"@type":"ListItem","position":i+1,"url":f'{S}/tools/{k}.html',"name":BY[k]["name"]} for i,k in enumerate(seen)]}
m=(f'<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/categories/coding.html">Coding &amp; Vibe Coding</a> / <span aria-current="page">Cursor alternatives</span></nav><h1 class="ch1">Cursor alternatives (2026)</h1>'
 f'<p class="lede">Cursor is still a strong AI editor. If its plans no longer fit how you work, these are the alternatives we track, grouped by how you like to code. Prices come from each official pricing page (checked {mdy(BUILD)}). Always confirm before you buy.</p>'
 '<div class="note-box"><div class="nb-h">How to choose</div><p><b>Want the same feel?</b> Try an AI editor first. <b>Mostly use agent mode?</b> A terminal agent plus the editor you already like covers most of it. <b>Worried about quota changes?</b> Pick a tool that lets you bring your own API key or run local models. Try one on a real task for a week before you switch everything.</p></div>'
 +NLBAND()+
 "".join(f'<section class="grp-s"><div class="gh"><h2>{e(t)} <span class="n">{len(ks)}</span></h2></div><p class="mut">{e(d)}</p>{table([row(BY[k],filt=False) for k in ks])}</section>' for t,d,ks in GRP)+
 f'<section class="grp-s"><div class="gh"><h2>For reference: Cursor</h2><a href="/categories/coding.html">All coding tools</a></div>{table([row(BY["cursor"],filt=False)])}</section>')
open("cursor-alternatives.html","w").write(head("Cursor alternatives 2026: AI editors, coding agents & open-source options | AI Tool Tracker",f"{len(seen)} Cursor alternatives with checked pricing: Devin Desktop, Zed, GitHub Copilot, Claude Code, Codex, Warp, Aider, Cline and more, grouped by how you code.","cursor-alternatives.html",ld)+shell(m,"coding")+END)
sm=open("sitemap.xml").read()
sm=re.sub(r'\s*<url><loc>https://aitrackertool.dev/(tools|categories)/[^<]*</loc>.*?</url>','',sm,flags=re.S)
sm=sm.replace("</urlset>","".join(f"<url><loc>{S}/{u}</loc><lastmod>{BUILD.isoformat()}</lastmod></url>\n" for u in urls)+"</urlset>")
for u in ["",DROP.lstrip("/"),"cursor-alternatives.html"]:
  sm=re.sub(r'\s*<url><loc>'+re.escape(S+"/"+u)+r'</loc>.*?</url>','',sm,flags=re.S)
sm=sm.replace('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"\n<url><loc>{S}/{u}</loc><lastmod>{BUILD.isoformat()}</lastmod></url>" for u in ["",DROP.lstrip("/"),"cursor-alternatives.html"]),1)
open("sitemap.xml","w").write(sm)
ll=open("llms.txt").read().split("\n## Directory")[0].rstrip()
_dl=f"- [Daily Drop {DROPDATE}]({S}{DROP}): "+", ".join(BY[k]["name"] for k in NEWS)
if DROP not in ll: ll=ll.replace("## Drops\n","## Drops\n"+_dl+"\n",1)
if "cursor-alternatives" not in ll: ll=ll.replace("## Notes","## Guides\n- [Cursor alternatives (2026)]("+S+"/cursor-alternatives.html): AI editors, terminal coding agents, open-source/BYOK options and app builders, with checked pricing.\n\n## Notes",1)
ll+="\n\n## Directory\n"+"".join(f"\n### {n}\n"+"".join(f'- [{y["name"]}]({S}/tools/{y["slug"]}.html): {y["desc"]}'+(f' Pricing: {y["pricing"]}.' if "pricing" in y else '')+(' Free tier: yes.' if "freeTier" in y else '')+"\n" for y in data if y["category"]==c) for c,n in C.items())
open("llms.txt","w").write(ll)
print(len(data),len(urls))
# ---- /go/<slug> short links (Cloudflare Pages _redirects, 302) ----
_rd=open("_redirects").read()
_rd=re.sub(r'\n?# BEGIN go-links.*?# END go-links\n?','\n',_rd,flags=re.S).rstrip()+"\n"
_go=[f'/go/{y["slug"]} {y["url"]} 302' for y in data]
GO_ALIAS={"fireflies":"fireflies-ai","bolt":"bolt-new","garak":"garak-nvidia","nuclei":"nuclei-projectdiscovery","mantis":"mantis-google","harness2":"harness2-google-research","jira":"jira-service-management","jsm":"jira-service-management"}  # short aliases for posts/newsletter
_go+=[f'/go/{a} {BY[t]["url"]} 302' for a,t in GO_ALIAS.items() if t in BY]
assert len(_go)<1900
open("_redirects","w").write(_rd+"# BEGIN go-links (generated by scripts/gen.py)\n"+"\n".join(_go)+"\n# END go-links\n")
print("go links:",len(_go),"affiliate:",[y["slug"] for y in data if isaff(y)])

# ---- homepage + static pages ----
ix=open("index.html").read()
hd=ix[:ix.index("<body>")]
hd=re.sub(r'<link rel="(icon|apple-touch-icon)"[^>]*>|<meta name="theme-color"[^>]*>','',hd).replace('<link rel="stylesheet" href="/style.css">',ICONS+'<link rel="stylesheet" href="/style.css">')
if "G-VMR6RG9R83" not in hd: hd=hd.replace("</head>",GA_TAG+"</head>",1)
IMPACT="<meta name='impact-site-verification' value='d43de056-cf95-49c5-a795-7bb116df2f89'>"
if IMPACT not in hd: hd=hd.replace("</head>",IMPACT+"</head>",1)
hd+="<body>"
sub=ix[ix.index('<section class="wrap" id="submit">') if '<section class="wrap" id="submit">' in ix else ix.index('<section id="submit"'):]
sub=sub[:sub.index('</section>')+10]
sub=re.sub(r'^<section[^>]*>','<section id="submit" class="blk">',sub).replace('<h2 class="sec">','<h2>').replace('<div class="grid">','<div class="two">').replace('<div class="card">','<div class="panel">')
nfree=sum(1 for y in data if y["pf"] in("free","both"));npaid=sum(1 for y in data if y["pf"] in("paid","both"))
groups="".join(f'<section class="grp" id="cat-{k}" data-c="{k}"><div class="gh"><h3>{e(v)} <span class="n">{CNT[k]}</span></h3><a href="/categories/{k}.html">Open category</a></div>{table([row(y) for y in data if y["category"]==k])}</section>' for k,v in C.items())
feat=[y for y in data if y["slug"] in("jira-service-management","mantis-google","fish-audio","security-onion","make")]
body=nav()+shell(f'''<section class="intro"><div class="kicker">Updated {mdy(BUILD)} · {len(data)} tools checked by hand</div><h1>AI tools people actually use. Checked by hand.</h1><p class="lede">A clean, current index for vibe coders and IT and security folks: real pricing, Free or Paid at a glance, and the date we last checked every listing.</p>
<p class="statline">{len(data)} tools · {nfree} with a free option · {npaid} paid · updated {VER}</p><p class="jump"><a class="btn" href="#directory">Browse all tools</a> <a class="btn ghost" href="/categories/itsec.html">Breaking into IT</a></p></section>
{NLBAND(' id="newsletter"')}
<section id="drop" class="grp-s"><div class="gh"><h2>Today's drop · {DROPDATE}</h2><a href="{DROP}">See full drop →</a></div><div class="tbl compact" role="table" id="preview"></div></section>
<section id="directory" class="dir"><h2 class="dh">AI tool directory</h2><div class="sticky">{ctl(len(data))}</div>{groups}</section>
<section class="grp-s" id="featured"><div class="gh"><h2>Featured picks</h2><a href="{DROP}">More new tools</a></div>{table([row(y,True,False) for y in feat],True)}</section>
<section id="subscribe" class="blk nl"><div><h2>Get the weekly drop</h2><p class="mut">One email a week with the best new AI tools. Unsubscribe anytime.</p></div><p><a class="btn ghost" href="#newsletter">Sign up at the top of the page</a></p><p class="note"><a href="https://aitrackertool.beehiiv.com/subscribe" target="_blank" rel="noopener">Subscribe on beehiiv</a> · <a href="/issue-001.html">Read Issue #001</a></p></section>
{sub}''',None,True)
js='''<script src="/config.js"></script><script src="/tools.js"></script><script>(function(){function x(s){return String(s).replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})}document.getElementById('preview').innerHTML='<div class="row head drop" role="row"><div role="columnheader">Tool</div><div role="columnheader">Type</div><div role="columnheader">Price</div><div role="columnheader"><span class="sr">Link</span></div></div>'+DROP_2026_10_20.slice(0,3).map(function(t){return '<div class="row drop" role="row"><div class="c-name" role="cell"><a class="nm" href="'+x(t.url)+'" target="_blank" rel="noopener">'+x(t.name)+'</a><span class="ds">'+x(t.desc)+'</span></div><div class="c-cat" role="cell">'+x(t.category)+'</div><div class="c-price" role="cell"><span class="lbl">Price </span>'+x(t.pricing||'See site')+'</div><div class="c-go" role="cell"><a class="go" href="'+x(t.url)+'" target="_blank" rel="noopener">Visit ↗</a></div></div>'}).join('')})()</script>
<script src="/filter.js"></script><script type="text/javascript" async src="https://subscribe-forms.beehiiv.com/attribution.js"></script></body></html>'''
open("index.html","w").write(hd+"\n"+body+js)
for p in ["drop-2026-10-19.html","drop-2026-10-18.html","drop-2026-10-17.html","drop-2026-10-16.html","drop-2026-10-15.html","drop-2026-10-14.html","issue-001.html","thanks.html"]:
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
# ---- 404 page (Cloudflare Pages serves 404.html with a 404 status) ----
_nf=head("Page not found | AI Tool Tracker","That page doesn't exist on AI Tool Tracker.","404",{"@context":"https://schema.org","@type":"WebPage","name":"Page not found"}).replace('<link rel="canonical" href="'+S+'/404">','<meta name="robots" content="noindex">').replace('<meta property="og:url" content="'+S+'/404">','')
_nm=(f'<header class="phero"><span class="badge">404 · NOT FOUND</span><h1>That page doesn\'t exist</h1><p class="tag">The link may be old or mistyped. Every tool we track is in the directory.</p><p class="jump"><a class="btn" href="/#directory">Browse all {len(data)} tools</a> <a class="btn ghost" href="{DROP}">Today\'s drop</a></p></header>')
open("404.html","w").write(_nf+shell(_nm)+END)
# cache-bust static asset links on every page
import glob as _g
for _f in _g.glob("*.html")+_g.glob("tools/*.html")+_g.glob("categories/*.html"):
  _s=open(_f).read();_b=bust(_s)
  if _b!=_s: open(_f,"w").write(_b)

# ---- canonical/OG/sitemap/llms URLs: extensionless (Cloudflare Pages 308-redirects .html) ----
_ex=lambda t: re.sub(r'(https://aitrackertool\.dev/[A-Za-z0-9/_-]+)\.html\b',r'\1',t)
for _f in _g.glob("*.html")+_g.glob("tools/*.html")+_g.glob("categories/*.html")+["llms.txt"]:
  _s=open(_f).read();_b=_ex(_s)
  if _b!=_s: open(_f,"w").write(_b)
_sm=_ex(open("sitemap.xml").read());_seen=set();_out=[]
for _ln in _sm.split("\n"):
  _m=re.search(r'<loc>([^<]+)</loc>',_ln)
  if _m:
    if _m.group(1) in _seen: continue
    _seen.add(_m.group(1))
  _out.append(_ln)
open("sitemap.xml","w").write("\n".join(_out))
