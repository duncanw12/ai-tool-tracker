// POST /submit  (Submit a tool + Sponsor forms)
// Delivery, first available wins:
//  1. env.RESEND_API_KEY  -> email via Resend (FROM: env.MAIL_FROM, default onboarding@resend.dev)
//  2. env.SUBMISSIONS     -> KV namespace binding, key "sub:<ISO time>:<rand>"
//  3. neither            -> logged only (visible in Pages Functions logs)
const TO = "duncan.welch30@gmail.com";
const FIELDS = { "submit-tool": ["tool-name","url","description","email"], "sponsor": ["name","company","email","message"] };
export async function onRequestPost({ request, env }) {
  const thanks = new URL("/thanks.html", request.url).toString();
  let fd; try { fd = await request.formData(); } catch { return new Response("Bad request", { status: 400 }); }
  if ((fd.get("bot-field") || "").toString().trim()) return Response.redirect(thanks, 303); // honeypot
  const form = (fd.get("form-name") || "").toString();
  if (!FIELDS[form]) return new Response("Unknown form", { status: 400 });
  const data = {};
  for (const k of FIELDS[form]) data[k] = (fd.get(k) || "").toString().slice(0, 2000).trim();
  if (!data.email || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(data.email)) return new Response("A valid email is required.", { status: 400 });
  const rec = { form, at: new Date().toISOString(), ip: request.headers.get("cf-connecting-ip") || "", ua: request.headers.get("user-agent") || "", ...data };
  let via = "log";
  try {
    if (env.RESEND_API_KEY) {
      const r = await fetch("https://api.resend.com/emails", { method: "POST",
        headers: { Authorization: `Bearer ${env.RESEND_API_KEY}`, "Content-Type": "application/json" },
        body: JSON.stringify({ from: env.MAIL_FROM || "AI Tool Tracker <onboarding@resend.dev>", to: [TO], reply_to: data.email,
          subject: `[AI Tool Tracker] ${form === "sponsor" ? "Sponsor inquiry" : "Tool submission"}: ${data["tool-name"] || data.company || data.name || data.email}`,
          text: Object.entries(rec).map(([k, v]) => `${k}: ${v}`).join("\n") }) });
      if (!r.ok) throw new Error("resend " + r.status + " " + (await r.text()));
      via = "resend";
    }
  } catch (e) { console.error(e.message); }
  if (env.SUBMISSIONS && via !== "resend") {
    await env.SUBMISSIONS.put(`sub:${rec.at}:${crypto.randomUUID().slice(0, 8)}`, JSON.stringify(rec));
    via = "kv";
  }
  console.log("submission", via, JSON.stringify(rec));
  return Response.redirect(thanks, 303);
}
export const onRequestGet = ({ request }) => Response.redirect(new URL("/#submit", request.url).toString(), 302);
