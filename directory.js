// Directory data. Pricing/free tier only where verified on the official site (Oct 14, 2026); omitted otherwise.
const CATEGORIES={"coding": "Coding & Vibe Coding", "chat": "Chat Assistants", "image": "Image", "video": "Video", "audio": "Voice & Audio", "writing": "Writing", "agents": "Agents & Automation", "research": "Productivity & Research", "design": "Design & Websites"};
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
]
},
{
"name": "Bolt.new",
"slug": "bolt-new",
"category": "coding",
"catName": "Coding & Vibe Coding",
"url": "https://bolt.cello.so/MFwNDwJhlUB",
"desc": "Prompt, run, edit and deploy full-stack web apps right in your browser.",
"tags": [
"vibe coding",
"web apps",
"browser"
]
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
]
},
{
"name": "Lovable",
"slug": "lovable",
"category": "coding",
"catName": "Coding & Vibe Coding",
"url": "https://lovable.dev",
"desc": "Build full-stack web apps by chatting with an AI engineer.",
"tags": [
"vibe coding",
"web apps",
"no-code"
]
},
{
"name": "Replit",
"slug": "replit",
"category": "coding",
"catName": "Coding & Vibe Coding",
"url": "https://replit.com",
"desc": "Browser IDE with Replit Agent that builds and deploys apps from a prompt.",
"freeTier": true,
"tags": [
"vibe coding",
"ide",
"deploy"
]
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
]
},
{
"name": "Windsurf",
"slug": "windsurf",
"category": "coding",
"catName": "Coding & Vibe Coding",
"url": "https://windsurf.com",
"desc": "Agentic AI code editor with the Cascade coding agent.",
"freeTier": true,
"pricing": "Pro from $20/mo",
"tags": [
"editor",
"agent",
"ide"
]
},
{
"name": "Claude Code",
"slug": "claude-code",
"category": "coding",
"catName": "Coding & Vibe Coding",
"url": "https://www.anthropic.com/claude-code",
"desc": "Anthropic's agentic coding tool for the terminal, IDE and web.",
"pricing": "Included with paid Claude plans",
"tags": [
"agent",
"terminal",
"cli"
]
},
{
"name": "OpenAI Codex",
"slug": "openai-codex",
"category": "coding",
"catName": "Coding & Vibe Coding",
"url": "https://openai.com/codex/",
"desc": "OpenAI's coding agent for the CLI, IDE and cloud tasks.",
"tags": [
"agent",
"cli",
"openai"
]
},
{
"name": "Warp",
"slug": "warp",
"category": "coding",
"catName": "Coding & Vibe Coding",
"url": "https://www.warp.dev",
"desc": "Agentic terminal and development environment with built-in AI agents.",
"freeTier": true,
"tags": [
"terminal",
"agent"
]
},
{
"name": "Tabnine",
"slug": "tabnine",
"category": "coding",
"catName": "Coding & Vibe Coding",
"url": "https://www.tabnine.com",
"desc": "AI code assistant focused on privacy and enterprise deployment.",
"tags": [
"autocomplete",
"enterprise"
]
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
]
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
]
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
]
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
]
},
{
"name": "Gemini",
"slug": "gemini",
"category": "chat",
"catName": "Chat Assistants",
"url": "https://gemini.google.com",
"desc": "Google's AI assistant, connected to Google apps and search.",
"tags": [
"assistant",
"google"
]
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
]
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
]
},
{
"name": "Le Chat (Mistral)",
"slug": "le-chat-mistral",
"category": "chat",
"catName": "Chat Assistants",
"url": "https://chat.mistral.ai",
"desc": "Mistral AI's chat assistant.",
"tags": [
"assistant",
"mistral",
"europe"
]
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
]
},
{
"name": "Midjourney",
"slug": "midjourney",
"category": "image",
"catName": "Image",
"url": "https://www.midjourney.com",
"desc": "AI image generator known for its distinctive artistic style.",
"tags": [
"image generation",
"art"
]
},
{
"name": "Ideogram",
"slug": "ideogram",
"category": "image",
"catName": "Image",
"url": "https://ideogram.ai",
"desc": "AI image generator that's strong at rendering text in images.",
"tags": [
"image generation",
"typography"
]
},
{
"name": "Leonardo.Ai",
"slug": "leonardo-ai",
"category": "image",
"catName": "Image",
"url": "https://leonardo.ai",
"desc": "AI image and video generation platform for creators and game assets.",
"tags": [
"image generation",
"assets"
]
},
{
"name": "Krea",
"slug": "krea",
"category": "image",
"catName": "Image",
"url": "https://www.krea.ai",
"desc": "Real-time AI image and video generation and enhancement.",
"freeTier": true,
"tags": [
"image generation",
"upscaling",
"real-time"
]
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
]
},
{
"name": "Black Forest Labs (FLUX)",
"slug": "black-forest-labs-flux",
"category": "image",
"catName": "Image",
"url": "https://bfl.ai",
"desc": "Makers of the FLUX image generation models.",
"tags": [
"image models",
"api"
]
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
]
},
{
"name": "Runway",
"slug": "runway",
"category": "video",
"catName": "Video",
"url": "https://runwayml.com",
"desc": "AI video generation and editing tools for filmmakers and creators.",
"freeTier": true,
"pricing": "Standard from $12/mo billed annually",
"tags": [
"video generation",
"editing"
]
},
{
"name": "Synthesia",
"slug": "synthesia",
"category": "video",
"catName": "Video",
"url": "https://www.synthesia.io",
"desc": "Create videos with AI avatars and voiceovers from text.",
"tags": [
"avatars",
"video generation",
"training"
]
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
]
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
]
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
]
},
{
"name": "Descript",
"slug": "descript",
"category": "video",
"catName": "Video",
"url": "https://www.descript.com",
"desc": "Edit video and podcasts by editing the transcript, with AI tools.",
"freeTier": true,
"tags": [
"editing",
"podcast",
"transcription"
]
},
{
"name": "Kling AI",
"slug": "kling-ai",
"category": "video",
"catName": "Video",
"url": "https://klingai.com",
"desc": "Kuaishou's AI video generation model and app.",
"tags": [
"video generation"
]
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
]
},
{
"name": "Suno",
"slug": "suno",
"category": "audio",
"catName": "Voice & Audio",
"url": "https://suno.com",
"desc": "Generate full songs with vocals from a text prompt.",
"freeTier": true,
"tags": [
"music generation"
]
},
{
"name": "Udio",
"slug": "udio",
"category": "audio",
"catName": "Voice & Audio",
"url": "https://www.udio.com",
"desc": "AI music generation and remixing.",
"tags": [
"music generation"
]
},
{
"name": "Murf AI",
"slug": "murf-ai",
"category": "audio",
"catName": "Voice & Audio",
"url": "https://murf.ai",
"desc": "AI voiceover studio with a library of voices.",
"tags": [
"text to speech",
"voiceover"
]
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
]
},
{
"name": "Writesonic",
"slug": "writesonic",
"category": "writing",
"catName": "Writing",
"url": "https://writesonic.com",
"desc": "AI writing and SEO/AI-search visibility platform.",
"tags": [
"seo",
"content"
]
},
{
"name": "Copy.ai",
"slug": "copy-ai",
"category": "writing",
"catName": "Writing",
"url": "https://www.copy.ai",
"desc": "AI platform for go-to-market copy and workflows.",
"tags": [
"marketing",
"copywriting"
]
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
]
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
]
},
{
"name": "n8n",
"slug": "n8n",
"category": "agents",
"catName": "Agents & Automation",
"url": "https://n8n.io",
"desc": "Workflow automation with AI agents; self-hostable and fair-code.",
"tags": [
"automation",
"self-hosted",
"agents"
]
},
{
"name": "Zapier",
"slug": "zapier",
"category": "agents",
"catName": "Agents & Automation",
"url": "https://zapier.com",
"desc": "Automate work across 7,000+ apps with Zaps and AI agents.",
"freeTier": true,
"tags": [
"automation",
"no-code",
"integrations"
]
},
{
"name": "Make",
"slug": "make",
"category": "agents",
"catName": "Agents & Automation",
"url": "https://www.make.com",
"desc": "Visual automation platform with AI agents.",
"tags": [
"automation",
"no-code",
"visual"
]
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
]
},
{
"name": "Lindy",
"slug": "lindy",
"category": "agents",
"catName": "Agents & Automation",
"url": "https://www.lindy.ai",
"desc": "Build AI agents that handle email, meetings and workflows.",
"tags": [
"agents",
"assistant"
]
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
]
},
{
"name": "NotebookLM",
"slug": "notebooklm",
"category": "research",
"catName": "Productivity & Research",
"url": "https://notebooklm.google",
"desc": "Google's AI research notebook grounded in your own sources, with audio overviews.",
"tags": [
"research",
"notes",
"google"
]
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
]
},
{
"name": "Otter.ai",
"slug": "otter-ai",
"category": "research",
"catName": "Productivity & Research",
"url": "https://otter.ai",
"desc": "AI meeting notes, transcription and summaries.",
"freeTier": true,
"tags": [
"meetings",
"transcription"
]
},
{
"name": "Fireflies.ai",
"slug": "fireflies-ai",
"category": "research",
"catName": "Productivity & Research",
"url": "https://fireflies.ai",
"desc": "AI notetaker that records, transcribes and summarizes meetings.",
"freeTier": true,
"tags": [
"meetings",
"transcription"
]
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
]
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
]
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
]
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
]
},
{
"name": "Figma",
"slug": "figma",
"category": "design",
"catName": "Design & Websites",
"url": "https://www.figma.com",
"desc": "Collaborative design platform with Figma AI and Figma Make.",
"tags": [
"ui design",
"prototyping"
]
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
]
},
{
"name": "Webflow",
"slug": "webflow",
"category": "design",
"catName": "Design & Websites",
"url": "https://webflow.com",
"desc": "Visual website builder and CMS with AI tools.",
"tags": [
"websites",
"cms",
"no-code"
]
},
{
"name": "Uizard",
"slug": "uizard",
"category": "design",
"catName": "Design & Websites",
"url": "https://uizard.io",
"desc": "AI UI design tool that turns prompts and sketches into mockups.",
"tags": [
"ui design",
"prototyping"
]
}
];
