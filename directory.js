// Directory data. Pricing/free tier only where verified on the official site (Oct 14-15, 2026); omitted otherwise.
const CATEGORIES={"coding": "Coding & Vibe Coding", "chat": "Chat Assistants", "image": "Image", "video": "Video", "audio": "Voice & Audio", "writing": "Writing", "agents": "Agents & Automation", "research": "Productivity & Research", "design": "Design & Websites", "itsec": "AI for IT & Cybersecurity"};
const DIRECTORY=[
{
"name": "Cursor",
"slug": "cursor",
"category": "coding",
"catName": "Coding & Vibe Coding",
"url": "https://cursor.com",
"desc": "AI-first code editor with agent mode, codebase chat and tab completion.",
"freeTier": true,
"pricing": "Paid plans from $8/mo",
"tags": [
"editor",
"agent",
"ide"
],
"pf": "both"
},
{
"name": "Bolt.new",
"slug": "bolt-new",
"category": "coding",
"catName": "Coding & Vibe Coding",
"url": "https://bolt.cello.so/MFwNDwJhlUB",
"desc": "Prompt, run, edit and deploy full-stack web apps right in your browser.",
"freeTier": true,
"pricing": "Pro from $25/mo",
"tags": [
"vibe coding",
"web apps",
"browser"
],
"pf": "both"
},
{
"name": "v0",
"slug": "v0",
"category": "coding",
"catName": "Coding & Vibe Coding",
"url": "https://v0.app",
"desc": "Vercel's AI app builder that turns prompts into React/Next.js apps and UI.",
"freeTier": true,
"pricing": "Plus from $30/mo",
"tags": [
"vibe coding",
"react",
"ui"
],
"pf": "both"
},
{
"name": "Lovable",
"slug": "lovable",
"category": "coding",
"catName": "Coding & Vibe Coding",
"url": "https://lovable.dev",
"desc": "Build full-stack web apps by chatting with an AI engineer.",
"freeTier": true,
"tags": [
"vibe coding",
"web apps",
"no-code"
],
"pf": "free"
},
{
"name": "Replit",
"slug": "replit",
"category": "coding",
"catName": "Coding & Vibe Coding",
"url": "https://replit.com",
"desc": "Browser IDE with Replit Agent that builds and deploys apps from a prompt.",
"freeTier": true,
"pricing": "Core from $20/mo ($18/mo billed annually)",
"tags": [
"vibe coding",
"ide",
"deploy"
],
"pf": "both"
},
{
"name": "GitHub Copilot",
"slug": "github-copilot",
"category": "coding",
"catName": "Coding & Vibe Coding",
"url": "https://github.com/features/copilot",
"desc": "AI pair programmer and coding agent inside VS Code, JetBrains and GitHub.",
"freeTier": true,
"pricing": "Pro from $10/mo",
"tags": [
"autocomplete",
"agent",
"github"
],
"pf": "both"
},
{
"name": "Devin",
"slug": "devin",
"category": "coding",
"catName": "Coding & Vibe Coding",
"url": "https://devin.ai",
"desc": "Cognition's coding agents: Devin Desktop (the editor formerly called Windsurf) plus Devin cloud agents.",
"freeTier": true,
"pricing": "Pro from $20/mo",
"tags": [
"editor",
"agent",
"ide",
"cloud agents"
],
"pf": "both"
},
{
"name": "Zed",
"slug": "zed",
"category": "coding",
"catName": "Coding & Vibe Coding",
"url": "https://zed.dev",
"desc": "Fast open-source code editor with AI edit predictions, an agent panel and bring-your-own-key support.",
"freeTier": true,
"pricing": "Pro from $10/mo",
"tags": [
"editor",
"open source",
"ide"
],
"pf": "both"
},
{
"name": "OpenRouter",
"slug": "openrouter",
"category": "coding",
"catName": "Coding & Vibe Coding",
"url": "https://openrouter.ai",
"desc": "One OpenAI-compatible API for 500+ models from 80+ providers, with fallback routing.",
"freeTier": true,
"pricing": "Pay-as-you-go; 5.5% fee on credit purchases",
"tags": [
"api",
"models",
"routing"
],
"pf": "both"
},
{
"name": "Muse Spark Open (Meta)",
"slug": "muse-spark-open-meta",
"category": "coding",
"catName": "Coding & Vibe Coding",
"url": "https://dev.meta.ai/models/muse-spark-open",
"desc": "Meta's open-weight multimodal MoE model (816B total, 42B active, 1M context) built for coding and agent work. Released Oct 15, 2026.",
"freeTier": true,
"pricing": "Free open weights (Muse Model License); hosted via OpenRouter, Groq, Together and others",
"tags": [
"open weights",
"models",
"meta",
"new"
],
"pf": "both"
},
{
"name": "Hugging Face",
"slug": "hugging-face",
"category": "coding",
"catName": "Coding & Vibe Coding",
"url": "https://huggingface.co",
"desc": "The hub for open models, datasets and Spaces demos, plus hosted inference.",
"freeTier": true,
"pricing": "PRO from $9/mo",
"tags": [
"open models",
"hosting",
"ml"
],
"pf": "both"
},
{
"name": "Claude Code",
"slug": "claude-code",
"category": "coding",
"catName": "Coding & Vibe Coding",
"url": "https://claude.com/product/claude-code",
"desc": "Anthropic's agentic coding tool for the terminal, IDE and web.",
"pricing": "Included with paid Claude plans",
"tags": [
"agent",
"terminal",
"cli"
],
"pf": "paid"
},
{
"name": "OpenAI Codex",
"slug": "openai-codex",
"category": "coding",
"catName": "Coding & Vibe Coding",
"url": "https://openai.com/codex/",
"desc": "OpenAI's coding agent for the CLI, IDE and cloud tasks.",
"freeTier": true,
"pricing": "Included with ChatGPT plans (limited on Free and Go)",
"tags": [
"agent",
"cli",
"openai"
],
"pf": "both"
},
{
"name": "Warp",
"slug": "warp",
"category": "coding",
"catName": "Coding & Vibe Coding",
"url": "https://www.warp.dev",
"desc": "Agentic terminal and development environment with built-in AI agents.",
"freeTier": true,
"pricing": "Build from $20/mo",
"tags": [
"terminal",
"agent"
],
"pf": "both"
},
{
"name": "Cline",
"slug": "cline",
"category": "coding",
"catName": "Coding & Vibe Coding",
"url": "https://cline.bot",
"desc": "Open-source autonomous coding agent for VS Code.",
"pricing": "Open source",
"tags": [
"agent",
"open source",
"vs code"
],
"pf": "free"
},
{
"name": "Aider",
"slug": "aider",
"category": "coding",
"catName": "Coding & Vibe Coding",
"url": "https://aider.chat",
"desc": "Open-source AI pair programming in your terminal, with git integration.",
"pricing": "Open source",
"tags": [
"cli",
"open source",
"git"
],
"pf": "free"
},
{
"name": "ChatGPT",
"slug": "chatgpt",
"category": "chat",
"catName": "Chat Assistants",
"url": "https://chatgpt.com",
"desc": "OpenAI's general-purpose AI assistant for chat, writing, code and images.",
"freeTier": true,
"tags": [
"assistant",
"openai"
],
"pf": "free"
},
{
"name": "Claude",
"slug": "claude",
"category": "chat",
"catName": "Chat Assistants",
"url": "https://claude.ai",
"desc": "Anthropic's AI assistant for writing, analysis and coding.",
"freeTier": true,
"pricing": "Pro from $17/mo billed annually ($20 monthly)",
"tags": [
"assistant",
"anthropic"
],
"pf": "both"
},
{
"name": "Gemini",
"slug": "gemini",
"category": "chat",
"catName": "Chat Assistants",
"url": "https://gemini.google.com",
"desc": "Google's AI assistant, connected to Google apps and search.",
"freeTier": true,
"pricing": "Google AI Plus from $4.99/mo (US)",
"tags": [
"assistant",
"google"
],
"pf": "both"
},
{
"name": "Grok",
"slug": "grok",
"category": "chat",
"catName": "Chat Assistants",
"url": "https://grok.com",
"desc": "xAI's AI assistant with real-time knowledge from X and the web.",
"tags": [
"assistant",
"xai"
],
"pf": ""
},
{
"name": "Microsoft Copilot",
"slug": "microsoft-copilot",
"category": "chat",
"catName": "Chat Assistants",
"url": "https://copilot.microsoft.com",
"desc": "Microsoft's AI companion for chat, search and creation.",
"tags": [
"assistant",
"microsoft"
],
"pf": ""
},
{
"name": "Le Chat (Mistral)",
"slug": "le-chat-mistral",
"category": "chat",
"catName": "Chat Assistants",
"url": "https://chat.mistral.ai",
"desc": "Mistral AI's chat assistant, with Mistral Vibe for coding in the CLI, IDE or web.",
"freeTier": true,
"pricing": "Pro from $14.99/mo",
"tags": [
"assistant",
"mistral",
"europe"
],
"pf": "both"
},
{
"name": "Ollama",
"slug": "ollama",
"category": "chat",
"catName": "Chat Assistants",
"url": "https://ollama.com",
"desc": "Run open models locally with one command, or use Ollama's cloud models when your machine isn't enough.",
"freeTier": true,
"pricing": "Paid plans from $20/mo",
"tags": [
"local models",
"open weights",
"privacy"
],
"pf": "both"
},
{
"name": "LM Studio",
"slug": "lm-studio",
"category": "chat",
"catName": "Chat Assistants",
"url": "https://lmstudio.ai",
"desc": "Desktop app (now with the Bionic agent) for downloading and running local LLMs via llama.cpp and MLX.",
"freeTier": true,
"pricing": "Bionic+ from $20/mo",
"tags": [
"local models",
"desktop",
"privacy"
],
"pf": "both"
},
{
"name": "DeepSeek",
"slug": "deepseek",
"category": "chat",
"catName": "Chat Assistants",
"url": "https://chat.deepseek.com",
"desc": "Chat assistant powered by DeepSeek's open-weight models.",
"tags": [
"assistant",
"open weights"
],
"pf": ""
},
{
"name": "Midjourney",
"slug": "midjourney",
"category": "image",
"catName": "Image",
"url": "https://www.midjourney.com",
"desc": "AI image and video generator known for its distinctive artistic style.",
"pricing": "Basic from $10/mo ($8/mo billed annually)",
"tags": [
"image generation",
"art"
],
"pf": "paid"
},
{
"name": "Ideogram",
"slug": "ideogram",
"category": "image",
"catName": "Image",
"url": "https://ideogram.ai",
"desc": "AI image generator that's strong at rendering text in images.",
"freeTier": true,
"pricing": "Plus from $15/mo billed annually ($20 monthly)",
"tags": [
"image generation",
"typography"
],
"pf": "both"
},
{
"name": "Leonardo.Ai",
"slug": "leonardo-ai",
"category": "image",
"catName": "Image",
"url": "https://leonardo.ai",
"desc": "AI image and video generation platform for creators and game assets.",
"freeTier": true,
"pricing": "Essential from $12/mo; free plan has 150 tokens/day",
"tags": [
"image generation",
"assets"
],
"pf": "both"
},
{
"name": "Krea",
"slug": "krea",
"category": "image",
"catName": "Image",
"url": "https://www.krea.ai",
"desc": "Real-time AI image and video generation and enhancement.",
"freeTier": true,
"pricing": "Pro from $21/mo billed yearly ($35 monthly)",
"tags": [
"image generation",
"upscaling",
"real-time"
],
"pf": "both"
},
{
"name": "Adobe Firefly",
"slug": "adobe-firefly",
"category": "image",
"catName": "Image",
"url": "https://www.adobe.com/products/firefly.html",
"desc": "Adobe's generative AI for images, video and design, built into Creative Cloud.",
"tags": [
"image generation",
"adobe"
],
"pf": ""
},
{
"name": "Black Forest Labs (FLUX)",
"slug": "black-forest-labs-flux",
"category": "image",
"catName": "Image",
"url": "https://bfl.ai",
"desc": "Makers of the FLUX image models, including FLUX 3 Image Klein (Oct 15, 2026): open weights, native 4K, runs on consumer GPUs.",
"freeTier": true,
"pricing": "API from $0.009/image (FLUX 3 Image Klein at 1K); open weights free for individuals and companies under $5M revenue",
"tags": [
"image models",
"api"
],
"pf": "both"
},
{
"name": "Recraft",
"slug": "recraft",
"category": "image",
"catName": "Image",
"url": "https://www.recraft.ai",
"desc": "AI image generator for designers, with vector and brand-style output.",
"freeTier": true,
"tags": [
"vector",
"design",
"image generation"
],
"pf": "free"
},
{
"name": "Runway",
"slug": "runway",
"category": "video",
"catName": "Video",
"url": "https://runway.com",
"desc": "AI video generation and editing tools for filmmakers and creators.",
"freeTier": true,
"pricing": "Standard from $12/mo billed annually",
"tags": [
"video generation",
"editing"
],
"pf": "both"
},
{
"name": "Synthesia",
"slug": "synthesia",
"category": "video",
"catName": "Video",
"url": "https://www.synthesia.io",
"desc": "Create videos with AI avatars and voiceovers from text.",
"freeTier": true,
"pricing": "Starter from $29/mo",
"tags": [
"avatars",
"video generation",
"training"
],
"pf": "both"
},
{
"name": "Pika",
"slug": "pika",
"category": "video",
"catName": "Video",
"url": "https://pika.art",
"desc": "AI video generator for short creative clips and effects.",
"freeTier": true,
"pricing": "Starter from $10/mo",
"tags": [
"video generation",
"effects"
],
"pf": "both"
},
{
"name": "Luma AI",
"slug": "luma-ai",
"category": "video",
"catName": "Video",
"url": "https://lumalabs.ai",
"desc": "AI video generation with the Dream Machine and Ray models.",
"pricing": "Plus from $30/mo",
"tags": [
"video generation"
],
"pf": "paid"
},
{
"name": "HeyGen",
"slug": "heygen",
"category": "video",
"catName": "Video",
"url": "https://www.heygen.com",
"desc": "AI avatar videos, translation and lip-sync.",
"freeTier": true,
"pricing": "Creator from $29/mo",
"tags": [
"avatars",
"translation"
],
"pf": "both"
},
{
"name": "Descript",
"slug": "descript",
"category": "video",
"catName": "Video",
"url": "https://www.descript.com",
"desc": "Edit video and podcasts by editing the transcript, with AI tools.",
"freeTier": true,
"pricing": "Hobbyist from $16/mo billed annually ($24 monthly)",
"tags": [
"editing",
"podcast",
"transcription"
],
"pf": "both"
},
{
"name": "Kling AI",
"slug": "kling-ai",
"category": "video",
"catName": "Video",
"url": "https://kling.ai",
"desc": "Kuaishou's AI video generation model and app.",
"tags": [
"video generation"
],
"pf": ""
},
{
"name": "ElevenLabs",
"slug": "elevenlabs",
"category": "audio",
"catName": "Voice & Audio",
"url": "https://elevenlabs.io",
"desc": "AI voice generation, cloning, dubbing and speech-to-text.",
"freeTier": true,
"pricing": "Creator from $22/mo",
"tags": [
"text to speech",
"voice cloning"
],
"pf": "both"
},
{
"name": "Suno",
"slug": "suno",
"category": "audio",
"catName": "Voice & Audio",
"url": "https://suno.com",
"desc": "Generate full songs with vocals from a text prompt.",
"freeTier": true,
"pricing": "Pro from $8/mo billed yearly",
"tags": [
"music generation"
],
"pf": "both"
},
{
"name": "Udio",
"slug": "udio",
"category": "audio",
"catName": "Voice & Audio",
"url": "https://www.udio.com",
"desc": "AI music generation and remixing.",
"freeTier": true,
"pricing": "Standard from $10/mo ($8/mo billed annually)",
"tags": [
"music generation"
],
"pf": "both"
},
{
"name": "Murf AI",
"slug": "murf-ai",
"category": "audio",
"catName": "Voice & Audio",
"url": "https://murf.ai",
"desc": "AI voiceover studio and text-to-speech API with 150+ voices in 35+ languages.",
"pricing": "API from $0.01 per 1,000 characters (Falcon); $10 free API credit",
"tags": [
"text to speech",
"voiceover"
],
"pf": "paid"
},
{
"name": "Jasper",
"slug": "jasper",
"category": "writing",
"catName": "Writing",
"url": "https://www.jasper.ai",
"desc": "AI content platform for marketing teams.",
"pricing": "Pro from $59/mo",
"tags": [
"marketing",
"content"
],
"pf": "paid"
},
{
"name": "Writesonic",
"slug": "writesonic",
"category": "writing",
"catName": "Writing",
"url": "https://writesonic.com",
"desc": "AI writing and SEO/AI-search visibility platform.",
"pricing": "Starter from $79/mo billed annually",
"tags": [
"seo",
"content"
],
"pf": "paid"
},
{
"name": "Copy.ai",
"slug": "copy-ai",
"category": "writing",
"catName": "Writing",
"url": "https://www.copy.ai",
"desc": "AI platform for go-to-market copy and workflows.",
"pricing": "Paid plans from $29/mo",
"tags": [
"marketing",
"copywriting"
],
"pf": "paid"
},
{
"name": "Grammarly",
"slug": "grammarly",
"category": "writing",
"catName": "Writing",
"url": "https://www.grammarly.com",
"desc": "AI writing assistant for grammar, tone and rewriting.",
"freeTier": true,
"pricing": "Pro from $12/mo",
"tags": [
"grammar",
"editing"
],
"pf": "both"
},
{
"name": "QuillBot",
"slug": "quillbot",
"category": "writing",
"catName": "Writing",
"url": "https://quillbot.com",
"desc": "AI paraphrasing, grammar checking and summarizing.",
"tags": [
"paraphrasing",
"summarizing"
],
"pf": ""
},
{
"name": "n8n",
"slug": "n8n",
"category": "agents",
"catName": "Agents & Automation",
"url": "https://n8n.io",
"desc": "Workflow automation with AI agents; self-hostable and fair-code.",
"freeTier": true,
"pricing": "Cloud Starter from \u20ac20/mo billed annually; self-hosted Community Edition free",
"tags": [
"automation",
"self-hosted",
"agents"
],
"pf": "both"
},
{
"name": "Zapier",
"slug": "zapier",
"category": "agents",
"catName": "Agents & Automation",
"url": "https://zapier.com",
"desc": "Automate work across 7,000+ apps with Zaps and AI agents.",
"freeTier": true,
"pricing": "Professional from $19.99/mo",
"tags": [
"automation",
"no-code",
"integrations"
],
"pf": "both"
},
{
"name": "Make",
"slug": "make",
"category": "agents",
"catName": "Agents & Automation",
"url": "https://www.make.com/?pc=aitrackertool",
"desc": "Visual automation platform with AI agents.",
"freeTier": true,
"pricing": "Free plan with 1,000 credits/mo; paid plans priced by credits",
"tags": [
"automation",
"no-code",
"visual"
],
"pf": "both"
},
{
"name": "Relay.app",
"slug": "relay-app",
"category": "agents",
"catName": "Agents & Automation",
"url": "https://www.relay.app",
"desc": "AI workflow automation with human-in-the-loop steps.",
"tags": [
"automation",
"agents"
],
"pf": ""
},
{
"name": "Muse (Meta)",
"slug": "muse-meta",
"category": "agents",
"catName": "Agents & Automation",
"url": "https://muse.ai",
"desc": "Meta's personal AI agent that uses apps for you: email, travel, shopping and more, via app, web or WhatsApp. US-only at launch (Sept 8, 2026).",
"freeTier": true,
"pricing": "Paid plans for heavier use",
"tags": [
"personal agent",
"meta",
"whatsapp",
"new"
],
"pf": "both"
},
{
"name": "Hermes Agent",
"slug": "hermes-agent",
"category": "agents",
"catName": "Agents & Automation",
"url": "https://hermes-agent.nousresearch.com",
"desc": "Nous Research's open-source personal agent with app connectors, a plugin catalog and one-click local models.",
"pricing": "Open source (MIT)",
"tags": [
"open source",
"agents",
"local models"
],
"pf": "free"
},
{
"name": "Lindy",
"slug": "lindy",
"category": "agents",
"catName": "Agents & Automation",
"url": "https://www.lindy.ai",
"desc": "Build AI agents that handle email, meetings and workflows.",
"pricing": "Team from $29.99/mo; $50 in starter credits",
"tags": [
"agents",
"assistant"
],
"pf": "paid"
},
{
"name": "Perplexity",
"slug": "perplexity",
"category": "research",
"catName": "Productivity & Research",
"url": "https://www.perplexity.ai",
"desc": "AI answer engine that searches the web and cites sources.",
"tags": [
"search",
"research",
"citations"
],
"pf": ""
},
{
"name": "Gemini Notebook",
"slug": "gemini-notebook",
"category": "research",
"catName": "Productivity & Research",
"url": "https://notebook.google",
"desc": "Google's AI research notebook (formerly NotebookLM), grounded in your own sources, with audio overviews.",
"tags": [
"research",
"notes",
"google"
],
"pf": ""
},
{
"name": "Granola",
"slug": "granola",
"category": "research",
"catName": "Productivity & Research",
"url": "https://www.granola.ai",
"desc": "Bot-free AI meeting notes that enhance your own jottings, with chat across meetings.",
"freeTier": true,
"pricing": "Business from $14/user/mo",
"tags": [
"meetings",
"notes"
],
"pf": "both"
},
{
"name": "Notion AI",
"slug": "notion-ai",
"category": "research",
"catName": "Productivity & Research",
"url": "https://www.notion.com",
"desc": "Notion's workspace with built-in AI for writing, search and agents.",
"freeTier": true,
"pricing": "Plus from $10/mo",
"tags": [
"notes",
"workspace"
],
"pf": "both"
},
{
"name": "Otter.ai",
"slug": "otter-ai",
"category": "research",
"catName": "Productivity & Research",
"url": "https://otter.ai",
"desc": "AI meeting notes, transcription and summaries.",
"freeTier": true,
"pricing": "Pro $16.99/user/mo billed monthly",
"tags": [
"meetings",
"transcription"
],
"pf": "both"
},
{
"name": "Fireflies.ai",
"slug": "fireflies-ai",
"category": "research",
"catName": "Productivity & Research",
"url": "https://fireflies.ai/?fpr=duncan-873b18",
"desc": "AI notetaker that records, transcribes and summarizes meetings.",
"freeTier": true,
"pricing": "Pro from $10/seat/mo billed annually ($18 monthly)",
"tags": [
"meetings",
"transcription"
],
"pf": "both"
},
{
"name": "Elicit",
"slug": "elicit",
"category": "research",
"catName": "Productivity & Research",
"url": "https://elicit.com",
"desc": "AI research assistant for finding and analyzing papers.",
"pricing": "Plus from $11/mo",
"tags": [
"academic",
"papers"
],
"pf": "paid"
},
{
"name": "Consensus",
"slug": "consensus",
"category": "research",
"catName": "Productivity & Research",
"url": "https://consensus.app",
"desc": "AI search engine for scientific research.",
"tags": [
"academic",
"search"
],
"pf": ""
},
{
"name": "Gamma",
"slug": "gamma",
"category": "design",
"catName": "Design & Websites",
"url": "https://gamma.app",
"desc": "Create presentations, docs and websites with AI.",
"tags": [
"presentations",
"slides"
],
"pf": ""
},
{
"name": "Framer",
"slug": "framer",
"category": "design",
"catName": "Design & Websites",
"url": "https://www.framer.com",
"desc": "Design and publish websites, with AI site generation.",
"freeTier": true,
"pricing": "Basic from $10/mo",
"tags": [
"websites",
"no-code"
],
"pf": "both"
},
{
"name": "Figma",
"slug": "figma",
"category": "design",
"catName": "Design & Websites",
"url": "https://www.figma.com",
"desc": "Collaborative design platform with Figma AI and Figma Make.",
"freeTier": true,
"pricing": "Professional from $16/mo per full seat",
"tags": [
"ui design",
"prototyping"
],
"pf": "both"
},
{
"name": "Canva",
"slug": "canva",
"category": "design",
"catName": "Design & Websites",
"url": "https://www.canva.com",
"desc": "Online design tool with Magic Studio AI features.",
"tags": [
"graphic design",
"templates"
],
"pf": ""
},
{
"name": "Webflow",
"slug": "webflow",
"category": "design",
"catName": "Design & Websites",
"url": "https://webflow.com",
"desc": "Visual website builder and CMS with AI tools.",
"freeTier": true,
"pricing": "Basic site plan from $15/mo billed yearly",
"tags": [
"websites",
"cms",
"no-code"
],
"pf": "both"
},
{
"name": "Napkin AI",
"slug": "napkin-ai",
"category": "design",
"catName": "Design & Websites",
"url": "https://www.napkin.ai",
"desc": "Turns text into editable diagrams, flowcharts, mind maps and charts.",
"freeTier": true,
"pricing": "Plus from $9/person/mo",
"tags": [
"diagrams",
"visuals",
"slides"
],
"pf": "both"
},
{
"name": "Uizard",
"slug": "uizard",
"category": "design",
"catName": "Design & Websites",
"url": "https://uizard.io",
"desc": "AI UI design tool that turns prompts and sketches into mockups.",
"freeTier": true,
"pricing": "Pro from $12/mo billed annually",
"tags": [
"ui design",
"prototyping"
],
"pf": "both"
},
{
"name": "TryHackMe (Echo)",
"slug": "tryhackme-echo",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://tryhackme.com/echo",
"desc": "Hands-on cyber training labs with Echo, a built-in AI tutor that gives context-aware hints without handing you the answer.",
"tags": [
"cert study",
"labs",
"beginner"
],
"pf": ""
},
{
"name": "HTB Academy (HTB Coach)",
"slug": "htb-academy-htb-coach",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://academy.hackthebox.com",
"desc": "Hack The Box's training modules with HTB Coach (beta): AI explanations, section summaries and quizzes tied to what you're studying.",
"tags": [
"cert study",
"labs",
"pentesting"
],
"pf": ""
},
{
"name": "PentestGPT",
"slug": "pentestgpt",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://github.com/GreyDGL/PentestGPT",
"desc": "Open-source autonomous pentesting agent from USENIX Security 2024 research, with staged recon-to-exploit runs for CTFs and lab targets.",
"pricing": "Open source (MIT)",
"tags": [
"pentesting",
"open source",
"home lab"
],
"pf": "free"
},
{
"name": "Burp AI (PortSwigger)",
"slug": "burp-ai-portswigger",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://portswigger.net/burp/ai",
"desc": "AI pentesting partner built into Repeater in Burp Suite Professional for validating findings and cutting scan noise.",
"tags": [
"web security",
"pentesting",
"bug bounty"
],
"pf": ""
},
{
"name": "Snyk",
"slug": "snyk",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://snyk.io",
"desc": "Developer security platform that scans your code, open-source dependencies, containers and IaC from the IDE, CLI and repos.",
"freeTier": true,
"pricing": "Team from $25/mo (up to 10 developers)",
"tags": [
"code security",
"sca",
"sast",
"beginner"
],
"pf": "both"
},
{
"name": "Semgrep",
"slug": "semgrep",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://semgrep.dev",
"desc": "Fast code scanner (SAST, supply chain, secrets) with AI-powered detection, triage and autofix. Great for scanning your own home-lab scripts.",
"freeTier": true,
"pricing": "Free for up to 10 contributors (60 AI credits); Teams Code from $30/contributor/mo",
"tags": [
"code security",
"sast",
"open source",
"autofix"
],
"pf": "both"
},
{
"name": "GitHub Copilot Autofix",
"slug": "github-copilot-autofix",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://docs.github.com/en/code-security/concepts/code-scanning/autofix-for-code-scanning",
"desc": "AI fixes for CodeQL code scanning alerts. Agentic autofix (GA Oct 15, 2026) investigates alerts and opens a draft PR with a validated fix.",
"freeTier": true,
"pricing": "Free on public repos; private repos need GitHub Code Security",
"tags": [
"code scanning",
"github",
"autofix",
"codeql"
],
"pf": "both"
},
{
"name": "VirusTotal Code Insight",
"slug": "virustotal-code-insight",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://www.virustotal.com",
"desc": "AI summaries in VirusTotal that explain what a suspicious script (starting with PowerShell) or decompiled code actually does. Handy for malware-analysis practice.",
"freeTier": true,
"pricing": "Free for community users on eligible uploads; Code Insight API limited to 50 requests/day",
"tags": [
"malware analysis",
"soc",
"beginner",
"threat intel"
],
"pf": "both"
},
{
"name": "Tines",
"slug": "tines",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://www.tines.com",
"desc": "Security and IT workflow automation (SOAR) with built-in AI and bring-your-own-model support, used by SOC and IT teams.",
"freeTier": true,
"pricing": "Free edition: 3 live workflows + one-time $50 AI allowance; paid editions on request",
"tags": [
"soar",
"automation",
"soc",
"it ops"
],
"pf": "both"
},
{
"name": "SentinelOne Purple AI",
"slug": "sentinelone-purple-ai",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://www.sentinelone.com/platform/purple/",
"desc": "Agentic AI security analyst in the SentinelOne Singularity Platform: ask questions in plain English, auto-triage alerts and run guided investigations.",
"tags": [
"soc",
"edr",
"triage",
"incident response"
],
"pf": ""
},
{
"name": "Microsoft Security Copilot",
"slug": "microsoft-security-copilot",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://www.microsoft.com/en-us/security/business/ai-machine-learning/microsoft-security-copilot",
"desc": "Generative AI for security teams across Microsoft Defender, Sentinel, Entra, Intune and Purview: summarize incidents, write queries and reverse-engineer malicious scripts in plain English.",
"pricing": "Pay-as-you-go: $4 per provisioned SCU/hour",
"tags": [
"soc",
"microsoft",
"incident response"
],
"pf": "paid"
},
{
"name": "Google Security Operations",
"slug": "google-security-operations",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://cloud.google.com/security/products/security-operations",
"desc": "Google's SecOps platform (SIEM + SOAR) with Gemini for natural-language search, detection writing and investigation.",
"tags": [
"siem",
"soc",
"gemini"
],
"pf": ""
},
{
"name": "CrowdStrike Charlotte AI",
"slug": "crowdstrike-charlotte-ai",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://www.crowdstrike.com/en-us/platform/charlotte-ai/",
"desc": "Agentic security analyst in the CrowdStrike platform that triages detections and speeds up investigations.",
"tags": [
"soc",
"edr",
"triage"
],
"pf": ""
},
{
"name": "Splunk AI Assistant",
"slug": "splunk-ai-assistant",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://www.splunk.com/en_us/products/splunk-ai-assistant.html",
"desc": "Natural-language assistant in Splunk for finding dashboards, reports and data and getting help with searches over your logs.",
"tags": [
"log analysis",
"spl",
"siem"
],
"pf": ""
},
{
"name": "Elastic Security AI",
"slug": "elastic-security-ai",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://www.elastic.co/security/ai",
"desc": "AI in Elastic Security: automated alert triage and hypothesis-driven threat hunts with ES|QL over your SIEM data.",
"tags": [
"log analysis",
"siem",
"threat hunting"
],
"pf": ""
}
];
