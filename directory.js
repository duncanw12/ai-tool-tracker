// Directory data. Pricing/free tier only where verified on the official site (Oct 14-15, 2026); omitted otherwise.
const CATEGORIES={"coding": "Coding & Vibe Coding", "chat": "Chat Assistants", "image": "Image", "video": "Video", "audio": "Voice & Audio", "writing": "Writing", "agents": "Agents & Automation", "research": "Productivity & Research", "design": "Design & Websites", "itsec": "AI for IT & Cybersecurity"};
const DIRECTORY=[
{
"name": "Cursor",
"slug": "cursor",
"category": "coding",
"catName": "Coding & Vibe Coding",
"url": "https://cursor.com",
"desc": "AI-first code editor with agent mode, codebase chat and tab completion. Now sold as part of The X Subscription (Oct 13, 2026); existing Cursor plans keep working as legacy plans.",
"freeTier": true,
"pricing": "Plus from $8/mo (Grok models only); Premium $30/mo adds cloud agents and third-party models at API list price",
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
"pricing": "Pro from $25/mo ($21/mo billed annually); free plan has 5 daily credits",
"tags": [
"vibe coding",
"web apps",
"no-code"
],
"pf": "both"
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
"desc": "Cognition's coding agents: Devin Desktop (the editor formerly called Windsurf) plus Devin cloud agents. Fusion mode in Devin Desktop and CLI pairs a frontier lead model with a cheaper sidekick; with Opus 5.5 and GPT-6 Luna it scores 68.1 on the Artificial Analysis Coding Agent Index. Pro includes free use of Cognition's own SWE-2 model.",
"freeTier": true,
"pricing": "Free plan; Pro $20/mo; Max $200/mo; Teams from $80/mo",
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
"name": "NVIDIA Nemotron 3.5 Bolt",
"slug": "nvidia-nemotron-3-5-bolt",
"category": "coding",
"catName": "Coding & Vibe Coding",
"url": "https://ollama.com/library/nemotron-3.5-bolt",
"desc": "NVIDIA's open local model (74B total, 9B active, 256K context) for coding, reasoning, vision and tool use. Fits about 24GB of GPU memory via Ollama, llama.cpp or LM Studio (NVIDIA GPUs; no Apple silicon yet). Released Oct 15, 2026. New Oct 23: Nemotron 3.5 Bolt E4B, a small 4B-effective model (built on Gemma 4 E4B) for fast local voice and device assistants with multi-turn tool use, a conversational mode and switchable reasoning. NVIDIA's 4GB Q4_K_M GGUF used about 3.5-4.3GB of VRAM on an RTX 5070 in its tests; in Ollama it's nemotron-3.5-bolt:e4b (7.2-7.9GB download with image input, plus MLX builds for Apple silicon).",
"freeTier": true,
"pricing": "Free open weights (OpenMDW License 1.1)",
"tags": [
"open weights",
"local models",
"nvidia",
"new"
],
"pf": "both"
},
{
"name": "OpenCode",
"slug": "opencode",
"category": "coding",
"catName": "Coding & Vibe Coding",
"url": "https://opencode.ai",
"desc": "Open-source AI coding agent for the terminal, desktop app and IDE. Use its free included models, connect 75+ providers (including local models), or sign in with GitHub Copilot or ChatGPT Plus/Pro. Security note: on Oct 17, 2026 OpenCode disclosed a breach of a legacy system behind its hosted Console that may have exposed provider API keys saved in Console workspaces (1.4% of Console users, all notified by email). Keys you add locally in the CLI or desktop app weren't part of it. Since then Anthropic has revoked affected Claude keys, Google has blocked exposed Gemini keys, OpenAI has refunded API credits used in the attack and OpenCode says its own refunds are underway. If you were notified, replace those keys and check usage back to Oct 16. OpenCode 2.0 (announced Oct 12) runs one shared background service for the terminal, web and desktop apps, with a rebuilt API and background subagents. It ships as a separate package (@opencode/cli); the default install still gives you 1.x, and V1 plugins don't work on 2.0.",
"freeTier": true,
"pricing": "Open source (MIT); optional Zen pay-as-you-go models",
"tags": [
"agent",
"terminal",
"open source",
"cli"
],
"pf": "free"
},
{
"name": "Recursive Flint",
"slug": "recursive-flint",
"category": "coding",
"catName": "Coding & Vibe Coding",
"url": "https://huggingface.co/RecursiveSI/flint",
"desc": "Recursive's first model: an open-weight mixture-of-experts coding model (39.8B total, about 2.5B active per token) built for fast agentic coding on your own machine. Recursive says it leads MoE models under 50B parameters on SWE-Bench Pro v2, Terminal-Bench 2.1 and SWE-Bench Verified, and runs at 125+ tokens/sec on an M4 Pro MacBook Pro. Runs via Ollama (flint:40b), llama.cpp, LM Studio, Unsloth, vLLM or SGLang; the INT4 GGUF needs a 48GB Apple Silicon Mac and Unsloth's 3-bit GGUF fits 24GB RAM. Released Oct 21, 2026; Recursive says it may need more step-by-step guidance than big closed models.",
"freeTier": true,
"pricing": "Free open weights (Apache-2.0)",
"tags": [
"open weights",
"local models",
"coding",
"new"
],
"pf": "both"
},
{
"name": "MiniMax M3.1 Flash",
"slug": "minimax-m3-1-flash",
"category": "coding",
"catName": "Coding & Vibe Coding",
"url": "https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash",
"desc": "MiniMax's open-weight multimodal mixture-of-experts model (about 428B total, 23B active per token, up to 1M tokens of context) for coding, agentic work, computer use and cybersecurity tasks. Takes text, image and video input. MiniMax's own benchmarks put it at 73.7% on DeepSWE v1.1 and 61.7 on OSWorld 2.0, close to big closed models on several agent tests. Too big for a home PC: MiniMax recommends serving it with SGLang, vLLM or TokenSpeed, or using it through MiniMax Agent and the MiniMax API. New in October 2026.",
"freeTier": true,
"pricing": "Free open weights (MiniMax Community License: commercial use needs a 'Built with MiniMax M3.1-Flash' credit and a notice to MiniMax; written approval above $20M yearly revenue)",
"tags": [
"open weights",
"models",
"agents",
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
"pricing": "Plus $20/mo; lower-cost Go plan also available",
"tags": [
"assistant",
"openai"
],
"pf": "both"
},
{
"name": "Claude",
"slug": "claude",
"category": "chat",
"catName": "Chat Assistants",
"url": "https://claude.ai",
"desc": "Anthropic's AI assistant for writing, analysis and coding. New: Claude Duet (research preview, Oct 2026) is a proactive agent app that sends a morning brief from your email and calendar, works on tasks on its own cloud computer and asks before it sends, pays, signs or deletes anything. Waitlist only, for US Pro and Max plans; it uses your plan's usage limits.",
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
"desc": "Google's AI assistant, connected to Google apps and search. For work, the new Gemini agent (Oct 8, 2026) runs inside Gmail, Docs, Sheets and Calendar.",
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
"freeTier": true,
"pricing": "Free on the web and in the apps; SuperGrok paid upgrade for higher limits",
"tags": [
"assistant",
"xai"
],
"pf": "both"
},
{
"name": "Off Grid AI",
"slug": "off-grid-ai",
"category": "chat",
"catName": "Chat Assistants",
"url": "https://getoffgridai.co",
"desc": "Open-source AI assistant that runs entirely on your own phone or computer: chat with local GGUF models, ask about photos, transcribe speech with Whisper, generate images with Stable Diffusion, chat with your documents and call tools or MCP servers, with no account, no API key and no cloud inference. Apps for iPhone, Android and Mac, plus a desktop app for macOS, Windows and Linux with a local OpenAI-compatible API. Built by Wednesday Solutions; the developer reports 250,000+ downloads, and the mobile repo has about 3,300 GitHub stars (v0.0.118 shipped Oct 23, 2026). Optional paid Pro adds voice replies, on-device memory, phone-to-Mac sync and actions in Gmail, Linear, Jira and Notion that wait for your approval.",
"freeTier": true,
"pricing": "Free and open source (mobile MIT, desktop AGPL-3.0); Pro $119 lifetime or $7.99/mo",
"tags": [
"local models",
"offline",
"privacy",
"open source",
"new"
],
"pf": "both"
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
"desc": "Run open models locally with one command, or use Ollama's cloud models when your machine isn't enough. Recursive's new Flint coding model is in the library (ollama run flint:40b).",
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
"desc": "Chat assistant powered by DeepSeek's open-weight models. DeepSeek has also open-sourced DeepInfer (Apache-2.0), the inference framework behind its own DeepSeek V4.1 Flash service; it targets data-center GPUs (NVIDIA SM100, Huawei Ascend 950), not home PCs.",
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
"name": "InvokeAI",
"slug": "invokeai",
"category": "image",
"catName": "Image",
"url": "https://github.com/invoke-ai/InvokeAI",
"desc": "Free, open-source AI image studio you run on your own GPU: a unified canvas for inpainting and outpainting, node-based workflows and a gallery, with support for SDXL, SD 3.5, FLUX.1, FLUX.2, Qwen Image and more. About 28,700 GitHub stars; v7.0 is in alpha.",
"pricing": "Open source (Apache-2.0)",
"tags": [
"local models",
"open source",
"canvas",
"stable diffusion"
],
"pf": "free"
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
"desc": "AI avatar videos, translation and lip-sync. For developers: the HeyGen Voice Turbo Free API model (heygen-voice-1-turbo-free) is free until Nov 30, 2026 with no credit balance needed, for public voices and instant clones (not professional clones). Capacity is shared, so expect occasional 429 errors; HeyGen pitches it for tests and prototypes.",
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
"desc": "Kuaishou's AI video generation model and app. Kling 4.0 (fully available Oct 15, 2026) generates up to 30 seconds in one pass with steadier fast motion, and Omni Reference combines up to 15 reference assets and 10 keyframes. It also works through Kling MCP and CLI; 10-bit HDR output and developer API access are coming soon.",
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
"desc": "AI voice generation, cloning, dubbing and speech-to-text. New Oct 15: Instant Soundtracks scores an uploaded video with original music and timed sound effects. New Oct 21: Eleven Realtime Translation, live speech-to-speech translation into 90+ languages in a voice you choose, in alpha for ElevenAPI enterprise customers only (contact sales; no public price).",
"freeTier": true,
"pricing": "Starter from $6/mo; Creator $22/mo (first month 50% off)",
"tags": [
"text to speech",
"voice cloning",
"music"
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
"name": "Fish Audio",
"slug": "fish-audio",
"category": "audio",
"catName": "Voice & Audio",
"url": "https://fish.audio",
"desc": "AI text-to-speech and voice cloning with a web studio, mobile apps and an API. Its Drama 3 model (Oct 13, 2026) takes plain-language direction (whisper this line, laugh here) and voices multi-character scenes, and the weights are open: free for commercial use under $500K annual revenue (Fish Audio Community License). Its fish-speech repo has about 33,000 GitHub stars. Self-hosting needs a 48GB NVIDIA GPU.",
"freeTier": true,
"pricing": "Plus from $11/mo billed annually ($15 monthly); free plan has 8,000 credits/mo",
"tags": [
"text to speech",
"voice cloning",
"open weights"
],
"pf": "both"
},
{
"name": "Pocket TTS (Kyutai)",
"slug": "pocket-tts-kyutai",
"category": "audio",
"catName": "Voice & Audio",
"url": "https://github.com/kyutai-labs/pocket-tts",
"desc": "Kyutai's open-source text-to-speech that runs on a plain CPU, no GPU needed, with voice cloning from a short audio clip and streaming output. Version 4.0 (Oct 20, 2026) adds small English models of 18.2M, 6.9M and 1.9M parameters (the 1.9M ones are experimental) plus standalone binaries that don't need Python. About 10,000 GitHub stars. Only clone voices you have permission to use.",
"pricing": "Open source (MIT code; CC-BY-4.0 weights); voice cloning weights need a free Hugging Face terms click-through",
"tags": [
"text to speech",
"voice cloning",
"local models",
"open source"
],
"pf": "free"
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
"name": "Harness2 (Google Research)",
"slug": "harness2-google-research",
"category": "agents",
"catName": "Agents & Automation",
"url": "https://github.com/google-research/harness2",
"desc": "Open-source framework from Google Cloud AI Research that improves an agent's harness (prompts, tools, memory, skills, subagents) instead of its model: it proposes edits, tests them on the same task and keeps what worked for next time. Runs OpenCode or Codex as the executor. About 13,500 GitHub stars two weeks after release; research code, not an official Google product.",
"pricing": "Open source (Apache-2.0)",
"tags": [
"agents",
"open source",
"self-improving",
"research"
],
"pf": "free"
},
{
"name": "OpenAI Decisions API",
"slug": "openai-decisions-api",
"category": "agents",
"catName": "Agents & Automation",
"url": "https://openai.com/index/decisions-api/",
"desc": "OpenAI API for the small, frequent decisions inside apps and agents: classify an input, pick a route or choose the next action. You define a question and the allowed answers, send text, images or JSON, and get back a probability, a choice or a score instead of free text. Built on GPT-6 Luna; OpenAI says it's up to 10x faster than Luna through the Responses API. Generally available Oct 22, 2026, with up to 400 questions per request, prompt caching and GPT-Live integration.",
"pricing": "$0.10 per 1M input tokens ($0.01 cached); no output-token charges",
"tags": [
"api",
"openai",
"routing",
"classification",
"new"
],
"pf": "paid"
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
"name": "Exa",
"slug": "exa",
"category": "research",
"catName": "Productivity & Research",
"url": "https://exa.ai",
"desc": "Web search API built for AI apps and agents: runs its own crawler and index, returns ranked results with clean page text or short highlights, and adds deep research, monitors and an agent API. Exa 3.0 (Oct 19, 2026) brings a larger embedding model, generally available Dynamic Highlights and billions of new documents such as products, local businesses and events, plus a cheaper Lite search type. Exa says it ranks #1 on the Artificial Analysis Search Index. Also available as a hosted MCP server.",
"freeTier": true,
"pricing": "Pay-as-you-go: Lite search $4 per 1,000 requests, Auto $7 per 1,000; free tier $10 in credits each month",
"tags": [
"search api",
"agents",
"mcp",
"research"
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
"url": "https://try.gamma.app/74bhdc77mraq",
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
"name": "Wazuh",
"slug": "wazuh",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://wazuh.com",
"desc": "Free, open-source SIEM and XDR used by home labbers and SOC teams for log analysis, threat detection and compliance. Wazuh documents AI threat hunting with local models via Ollama, and Wazuh 5.0 (now in release candidate) adds a built-in AI Assistant.",
"freeTier": true,
"pricing": "Free and open source (self-hosted); Wazuh Cloud is a paid hosted option",
"tags": [
"siem",
"xdr",
"open source",
"home lab",
"beginner"
],
"pf": "both"
},
{
"name": "CyberStrikeAI",
"slug": "cyberstrikeai",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://github.com/AIPentest/CyberStrikeAI",
"desc": "Open-source AI pentesting platform written in Go: agents run 100+ security tools over MCP, with human approval steps, audit logs and CTF roles. Only for labs and systems you're authorized to test.",
"pricing": "Open source (Apache-2.0)",
"tags": [
"pentesting",
"open source",
"mcp",
"ctf"
],
"pf": "free"
},
{
"name": "Sophos AI Defense",
"slug": "sophos-ai-defense",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://www.sophos.com/en-us/products/ai-defense",
"desc": "Finds the AI tools employees and apps are using, including unapproved shadow AI, and enforces real-time guardrails on prompts and data across endpoint, network, identity and browser. Generally available Oct 16, 2026.",
"pricing": "Quote-based add-on for Sophos EDR, XDR and MDR customers",
"tags": [
"shadow ai",
"governance",
"msp",
"data protection"
],
"pf": "paid"
},
{
"name": "garak (NVIDIA)",
"slug": "garak-nvidia",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://github.com/NVIDIA/garak",
"desc": "NVIDIA's open-source LLM vulnerability scanner: probes chatbots and AI apps for prompt injection, jailbreaks, data leakage, hallucination and toxicity, then reports what got through. v0.17.1 shipped Oct 16, 2026.",
"pricing": "Open source (Apache-2.0)",
"tags": [
"ai red teaming",
"llm security",
"open source",
"home lab"
],
"pf": "free"
},
{
"name": "Atera",
"slug": "atera",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://www.atera.com",
"desc": "All-in-one IT management (RMM, help desk, ticketing and patching) priced per technician, with AI Copilot built into every plan for scripts, ticket summaries and knowledge-base drafts. Robin, its end-user AI agent, is sold separately.",
"pricing": "Professional from $149/technician/mo billed annually ($169 monthly); 30-day free trial",
"tags": [
"rmm",
"help desk",
"msp",
"it ops"
],
"pf": "paid"
},
{
"name": "Security Onion",
"slug": "security-onion",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://securityonion.net",
"desc": "Free and open platform for threat hunting, network security monitoring and log management (2+ million downloads), a staple of SOC home labs. Security Onion 3 shipped in 2026. Onion AI, its assistant for alert analysis and detection tuning (now with local model support), comes with Security Onion Pro.",
"freeTier": true,
"pricing": "Free and open; Onion AI is part of Security Onion Pro (contact sales)",
"tags": [
"siem",
"nsm",
"threat hunting",
"home lab"
],
"pf": "both"
},
{
"name": "promptfoo",
"slug": "promptfoo",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://www.promptfoo.dev",
"desc": "Open-source CLI for testing and red-teaming LLM apps and agents: write evals in YAML, compare models side by side and scan for prompt injection, jailbreaks and data leaks. About 26,000 GitHub stars; the site says 300,000+ developers use it.",
"freeTier": true,
"pricing": "Community edition free and open source (MIT), red teaming up to 10k probes/mo; Enterprise custom",
"tags": [
"ai red teaming",
"llm security",
"evals",
"open source"
],
"pf": "both"
},
{
"name": "Nuclei (ProjectDiscovery)",
"slug": "nuclei-projectdiscovery",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://github.com/projectdiscovery/nuclei",
"desc": "Fast open-source vulnerability scanner built on thousands of community YAML templates, with an -ai option that generates and runs a template from a plain-English prompt. About 32,000 GitHub stars. Only scan systems you own or are authorized to test.",
"pricing": "Open source (MIT); free AI template editor on ProjectDiscovery Cloud",
"tags": [
"vulnerability scanning",
"pentesting",
"open source",
"home lab"
],
"pf": "free"
},
{
"name": "Freshservice",
"slug": "freshservice",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://www.freshworks.com/freshservice/",
"desc": "Cloud IT service desk (ITSM) from Freshworks: ticket and incident queues, knowledge base, self-service portal and service catalog, with Freddy AI Copilot as an add-on. A common help desk platform you can practice on with the free trial.",
"pricing": "Starter from $19/agent/mo billed annually; Freddy AI Copilot add-on $29/agent/mo; free trial",
"tags": [
"help desk",
"itsm",
"ticketing",
"it ops"
],
"pf": "paid"
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
"pricing": "No additional fee for Splunk Cloud Platform and Splunk Enterprise customers",
"tags": [
"log analysis",
"spl",
"siem"
],
"pf": "paid"
},
{
"name": "Mantis (Google)",
"slug": "mantis-google",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://github.com/google/mantis",
"desc": "Google's open-source toolkit of skills that lets AI coding agents find, reproduce and patch vulnerabilities in your code, from threat modelling to the final report, plus a reference harness you can point at a repo with a plain-English focus like look for IDOR. About 2,500 GitHub stars. Google says to run it only in isolated environments and to verify every finding by hand.",
"pricing": "Open source (Apache-2.0); model usage billed by your AI provider",
"tags": [
"code security",
"appsec",
"ai agents",
"open source"
],
"pf": "free"
},
{
"name": "Jira Service Management",
"slug": "jira-service-management",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://www.atlassian.com/software/jira/service-management",
"desc": "Atlassian's IT service desk: request portal, queues, SLAs, knowledge base, incident and change management, with Rovo AI agents and search on paid plans. One of the most common ticketing tools in help desk job posts, and the free plan is enough to build a practice service desk.",
"freeTier": true,
"pricing": "Free for up to 3 agents; Standard adds Rovo AI agents (per-agent pricing, 14-day free trial)",
"tags": [
"help desk",
"itsm",
"ticketing",
"it ops"
],
"pf": "both"
},
{
"name": "ServiceNow ITSM (Now Assist)",
"slug": "servicenow-itsm-now-assist",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://www.servicenow.com/products/itsm.html",
"desc": "ServiceNow's IT service management platform (incident, problem, change and request management) with Now Assist AI that summarizes incidents, suggests fixes and drafts responses, plus AI agents on higher tiers. Shows up in a huge share of help desk and IT job posts. Anyone can get a free Personal Developer Instance with admin access to learn the platform.",
"pricing": "Quote-based packages (Foundation, Advanced, Prime); free Personal Developer Instance for learning",
"tags": [
"help desk",
"itsm",
"ticketing",
"it ops"
],
"pf": "paid"
},
{
"name": "GhidraMCP",
"slug": "ghidramcp",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://github.com/LaurieWired/GhidraMCP",
"desc": "Open-source MCP server and plugin that lets an AI assistant drive Ghidra, the NSA's free reverse-engineering suite: decompile binaries, list functions, imports and exports, and rename methods and data as it works. About 11,400 GitHub stars; v2.0 shipped Oct 10, 2026 for Ghidra 12.1.4. Analyze malware samples only inside an isolated VM.",
"pricing": "Open source (Apache-2.0); Ghidra is free; model usage billed by your AI provider",
"tags": [
"malware analysis",
"reverse engineering",
"mcp",
"open source"
],
"pf": "free"
},
{
"name": "Strix",
"slug": "strix",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://github.com/usestrix/strix",
"desc": "Open-source AI penetration testing agents that run your app, look for vulnerabilities such as injection, broken access control, SSRF and XSS, and confirm each one with a working proof of concept before reporting it, with suggested fixes. Runs locally in Docker with your own LLM API key, and can scan pull requests in CI. About 71,000 GitHub stars; v1.7.0 shipped Oct 5, 2026. Only test apps you own or have written permission to test.",
"freeTier": true,
"pricing": "Open source (Apache-2.0); Strix Cloud Pro $29/seat/mo, pentests billed separately",
"tags": [
"pentesting",
"appsec",
"ai agents",
"open source"
],
"pf": "free"
},
{
"name": "Shannon (Keygraph)",
"slug": "shannon-keygraph",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://github.com/KeygraphHQ/shannon",
"desc": "Open-source autonomous AI pentester for web apps and APIs from Keygraph. It reads your source code to find likely attack paths, then runs real exploits against the running app and reports only what it could prove ('no exploit, no report'). Runs from the command line with npx and Docker on your own model provider account. About 49,000 GitHub stars; v3.4.0 shipped Oct 6, 2026. Keygraph says never to point it at production or at anything you aren't authorized to test.",
"freeTier": true,
"pricing": "Shannon open source free (AGPL-3.0); Keygraph Pro $50/developer/mo",
"tags": [
"pentesting",
"appsec",
"ai agents",
"open source"
],
"pf": "both"
},
{
"name": "PentAGI",
"slug": "pentagi",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://github.com/vxcontrol/pentagi",
"desc": "Open-source, self-hosted multi-agent system for autonomous penetration testing from VXControl. Describe a target and goal in plain language and a team of AI agents plans the work, runs 20+ tools such as nmap, Metasploit and sqlmap inside an isolated Docker sandbox, remembers what worked and writes a report, with a web UI plus REST and GraphQL APIs. Works with 10+ cloud model providers or local models through Ollama or vLLM. About 32,000 GitHub stars; v2.2.0 shipped Oct 5, 2026. For authorized testing only.",
"pricing": "Open source (MIT); PentAGI Enterprise available",
"tags": [
"pentesting",
"open source",
"self-hosted",
"home lab",
"local models"
],
"pf": "free"
},
{
"name": "SkillSpector (NVIDIA)",
"slug": "skillspector-nvidia",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://github.com/NVIDIA/SkillSpector",
"desc": "NVIDIA's open-source scanner that checks AI agent skills (for Claude Code, Codex, Gemini CLI and MCP) before you install them. It looks for 71 vulnerability patterns across 17 categories, including prompt injection, data exfiltration, privilege escalation, supply-chain risk and MCP tool poisoning, then gives a 0-100 risk score with JSON, Markdown or SARIF reports. Fast static checks work offline; an optional LLM pass adds deeper review. Scans Git repos, URLs, zip files or folders, and runs in Docker. About 21,000 GitHub stars; v2.13.1 shipped Oct 23, 2026.",
"pricing": "Open source (Apache-2.0); optional LLM analysis billed by your AI provider",
"tags": [
"ai security",
"agent skills",
"supply chain",
"open source"
],
"pf": "free"
},
{
"name": "Snyk Agent Scan",
"slug": "snyk-agent-scan",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://github.com/snyk/agent-scan",
"desc": "Snyk's open-source scanner that finds the AI agents, MCP servers and skills already installed on your machine (Claude Code and Desktop, Cursor, VS Code, GitHub Copilot, Windsurf, Gemini CLI, Codex, OpenCode and more) and checks them for prompt injection, tool poisoning, private-data exposure, destructive capabilities, malicious code and hardcoded secrets. Asks before it starts or contacts each MCP server, and Snyk recommends a sandbox or VM for untrusted configs. Runs with uvx or a signed standalone binary and needs a free Snyk API token; component details are sent to Snyk's Agent Scan API for analysis, with secrets redacted. About 3,200 GitHub stars; v0.6.9 shipped Oct 20, 2026.",
"freeTier": true,
"pricing": "Open source (Apache-2.0); free Snyk account and API token required",
"tags": [
"ai security",
"mcp",
"agent skills",
"open source",
"new"
],
"pf": "free"
},
{
"name": "Cisco Skill Scanner",
"slug": "cisco-skill-scanner",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://github.com/cisco-ai-defense/skill-scanner",
"desc": "Cisco AI Defense's open-source scanner for AI agent skills (Agent Skills format used by Codex and Cursor, plus Claude Code commands with --lenient). It combines YAML and YARA-X rules, code and dataflow analysis and an optional LLM judge that can use cloud or local models, and outputs SARIF for GitHub Code Scanning with a ready-made GitHub Action and a pre-commit hook. Cisco publishes its own measured detection and false-positive rates: rules alone caught 7.7% of malicious test skills at HIGH, and with the LLM judge 66.7% reached MEDIUM or above at a 15.4% false-positive rate, so it says a clean scan is not a guarantee. About 2,600 GitHub stars; 2.3.1 shipped Oct 21, 2026.",
"pricing": "Open source (Apache-2.0); optional LLM judge billed by your AI provider",
"tags": [
"ai security",
"agent skills",
"ci",
"open source",
"new"
],
"pf": "free"
},
{
"name": "Elastic Security AI",
"slug": "elastic-security-ai",
"category": "itsec",
"catName": "AI for IT & Cybersecurity",
"url": "https://www.elastic.co/security/ai",
"desc": "AI in Elastic Security: automated alert triage and hypothesis-driven threat hunts with ES|QL over your SIEM data.",
"pricing": "Elastic AI Assistant included in Serverless Security Analytics Complete, from $0.11/GB ingested plus retention",
"tags": [
"log analysis",
"siem",
"threat hunting"
],
"pf": "paid"
}
];
