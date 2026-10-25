/* QuietlyChanged — small progressive enhancements. Every page works without this file. */
(() => {
  "use strict";
  const root = document.body.dataset.root || "";
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const store = {
    get(k, d) { try { const v = localStorage.getItem(k); return v === null ? d : JSON.parse(v); } catch (e) { return d; } },
    set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  };
  const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
  const fmt = s => { const [y, m, d] = s.split("-"); return MON[m - 1] + " " + (+d); };
  const today = (() => { const d = new Date(); d.setHours(0, 0, 0, 0); return d; })();
  const daysTo = s => Math.round((new Date(s + "T00:00:00") - today) / 864e5);
  const reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;

  function toast(msg) {
    const t = document.createElement("div"); t.className = "toast"; t.setAttribute("role", "status"); t.textContent = msg;
    document.body.appendChild(t); setTimeout(() => t.remove(), 2200);
  }

  /* theme */
  const themeBtn = $("[data-theme-toggle]");
  if (themeBtn) themeBtn.addEventListener("click", () => {
    const cur = document.documentElement.dataset.theme || (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    const next = cur === "dark" ? "light" : "dark";
    document.documentElement.dataset.theme = next;
    try { localStorage.setItem("qc-theme", next); } catch (e) {}
  });

  /* live countdowns (the built page has them as of build day) */
  const cd = n => n === 0 ? "today" : n === 1 ? "tomorrow" : n > 1 ? `in ${n} days` : n === -1 ? "yesterday" : `${-n} days ago`;
  $$("[data-countdown]").forEach(el => { el.textContent = cd(daysTo(el.dataset.countdown)); });
  $$("[data-days]").forEach(el => {
    const n = Math.max(0, daysTo(el.dataset.days)); const sm = el.querySelector("small");
    el.firstChild.nodeValue = n; if (sm) sm.textContent = n === 1 ? "day" : "days";
    const card = el.closest(".dc"); if (card) card.classList.toggle("hot", n <= 7);
  });

  /* the strike: drawn once as each blackline scrolls into view */
  if (!reduced && "IntersectionObserver" in window) {
    const bls = $$(".exhibit .bl");
    bls.forEach(b => b.classList.add("pre"));
    const io = new IntersectionObserver(es => es.forEach(e => {
      if (e.isIntersecting) { setTimeout(() => e.target.classList.remove("pre"), 250); io.unobserve(e.target); }
    }), { rootMargin: "0px 0px -12% 0px" });
    bls.forEach(b => io.observe(b));
    setTimeout(() => bls.forEach(b => b.classList.remove("pre")), 2500); // never leave a strike undrawn
  }

  /* data (lazy) */
  let idxP = null;
  const index = () => idxP || (idxP = fetch(root + "search.json").then(r => r.json()).catch(() => []));

  /* search */
  let dlg = null, sel = 0;
  function openSearch() {
    if (!dlg) {
      dlg = document.createElement("dialog"); dlg.className = "search"; dlg.setAttribute("aria-label", "Search");
      dlg.innerHTML = '<label class="sr" for="qc-q">Search changes, services and threads</label><input id="qc-q" type="search" placeholder="Search changes, services, threads…" autocomplete="off"><ul role="listbox" id="qc-res"></ul>';
      document.body.appendChild(dlg);
      const q = $("#qc-q", dlg), ul = $("#qc-res", dlg);
      const run = async () => {
        const all = await index(); const terms = q.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
        let res;
        if (!terms.length) res = all.filter(x => x.k !== "service" && x.k !== "thread").slice(0, 8);
        else res = all.map(x => {
          const hay = (x.t + " " + x.s + " " + (x.x || "")).toLowerCase(); let sc = 0;
          for (const t of terms) { if (!hay.includes(t)) return null; if (x.s.toLowerCase().startsWith(t)) sc += 5; if (x.t.toLowerCase().includes(t)) sc += 3; }
          return [sc + (x.k === "service" ? 2 : 0) + (x.i || 0) * .3, x];
        }).filter(Boolean).sort((a, b) => b[0] - a[0]).slice(0, 12).map(a => a[1]);
        sel = 0;
        ul.innerHTML = res.length ? res.map((x, i) => `<li><a href="${root + x.u}" role="option" aria-selected="${i === 0}"><span class="k">${x.k === "service" ? '<span class="mono-badge">' + esc(x.s[0].toUpperCase()) + "</span>" : x.k === "thread" ? '<span class="kind" style="color:var(--red-ink)">Thread</span>' : `<span class="kind ${x.k}">${x.k}</span>`}</span><b>${x.k === "service" || x.k === "thread" ? esc(x.t) : esc(x.s) + ": " + esc(x.t)}</b><small>${x.d ? fmt(x.d) + " · " : ""}${esc(x.x || "")}</small></a></li>`).join("")
          : `<li class="hint">Nothing matches “${esc(q.value)}”.</li>`;
      };
      q.addEventListener("input", run);
      q.addEventListener("keydown", e => {
        const items = $$("a", ul); if (!items.length) return;
        if (e.key === "ArrowDown" || e.key === "ArrowUp") {
          e.preventDefault(); sel = (sel + (e.key === "ArrowDown" ? 1 : -1) + items.length) % items.length;
          items.forEach((a, i) => a.setAttribute("aria-selected", i === sel)); items[sel].scrollIntoView({ block: "nearest" });
        } else if (e.key === "Enter") { e.preventDefault(); location.href = items[sel].href; }
      });
      dlg.addEventListener("click", e => { if (e.target === dlg) dlg.close(); });
      run();
    }
    dlg.showModal(); const q = $("#qc-q", dlg); q.select();
  }
  $$("[data-search]").forEach(b => b.addEventListener("click", openSearch));
  document.addEventListener("keydown", e => {
    const typing = /^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement?.tagName) || document.activeElement?.isContentEditable;
    if ((e.key === "/" && !typing) || (e.key.toLowerCase() === "k" && (e.metaKey || e.ctrlKey))) { e.preventDefault(); openSearch(); }
  });

  /* following services ("your stack") */
  const followed = () => new Set(store.get("qc-stack", []));
  function setFollow(s, on) {
    const f = followed(); on ? f.add(s) : f.delete(s); store.set("qc-stack", [...f]); syncFollow(); drawStack(); filterTiles();
  }
  function syncFollow() {
    const f = followed();
    $$("[data-follow]").forEach(b => {
      const on = f.has(b.dataset.follow); b.setAttribute("aria-pressed", on);
      const l = $("[data-follow-label]", b); if (l) l.textContent = (on ? "Following " : "Follow ") + b.dataset.follow;
      if (b.classList.contains("star")) b.setAttribute("aria-label", (on ? "Unfollow " : "Follow ") + b.dataset.follow);
    });
  }
  $$("[data-follow]").forEach(b => b.addEventListener("click", e => {
    e.preventDefault(); const s = b.dataset.follow, on = !followed().has(s); setFollow(s, on);
    toast(on ? `Following ${s}. Its changes now show on the front page.` : `Stopped following ${s}.`);
  }));
  syncFollow();

  const stack = $("[data-stack]");
  async function drawStack() {
    if (!stack) return;
    const all = await index(); const f = followed();
    const pick = $("[data-stack-pick]", stack);
    if (!pick.dataset.ready) {
      const counts = {}; all.forEach(x => { if (x.k !== "service" && x.k !== "thread") counts[x.s] = (counts[x.s] || 0) + 1; });
      const svcs = all.filter(x => x.k === "service" && (counts[x.s] || f.has(x.s))).map(x => x.s).sort((a, b) => (counts[b] || 0) - (counts[a] || 0) || a.localeCompare(b));
      pick.innerHTML = svcs.map(s => `<li><button type="button" data-pick="${esc(s)}" aria-pressed="false">${esc(s)}${counts[s] ? ` <span class="muted mono" style="font-size:.7rem">${counts[s]}</span>` : ""}</button></li>`).join("");
      $$("[data-pick]", pick).forEach(b => b.addEventListener("click", () => setFollow(b.dataset.pick, !followed().has(b.dataset.pick))));
      pick.dataset.ready = 1;
    }
    $$("[data-pick]", pick).forEach(b => b.setAttribute("aria-pressed", f.has(b.dataset.pick)));
    const list = all.filter(x => x.k !== "service" && x.k !== "thread" && f.has(x.s));
    $("[data-stack-count]", stack).textContent = !f.size ? "Pick a few services" : list.length ? `${list.length} change${list.length > 1 ? "s" : ""} to ${f.size} service${f.size > 1 ? "s" : ""}` : `No changes yet to your ${f.size} service${f.size > 1 ? "s" : ""}`;
    $("[data-stack-list]", stack).innerHTML = list.length ? list.slice(0, 40).map(x => `<li><a href="${root + x.u}"><span class="dt">${fmt(x.d)}</span><span><span class="kind ${x.k}">${x.k}</span><br><b>${esc(x.s)}:</b> ${esc(x.t)}${x.e && daysTo(x.e) >= 0 ? ` <span class="mono" style="color:var(--red-ink);font-size:.75rem">· ${fmt(x.e)}</span>` : ""}</span></a></li>`).join("")
      : `<li class="empty">${f.size ? "Nothing has changed at the services you follow since we started tracking. We'll list it here when it does." : "Your list shows up here."}</li>`;
  }
  if (stack) drawStack();

  /* services page filters */
  const q = $("#q"), rows = $$("#rows > li"), fbtns = $$("[data-f]"), count = $("#count");
  let kf = null;
  function filterTiles() {
    if (!q) return;
    const t = q.value.toLowerCase().trim(), f = followed(); let n = 0;
    rows.forEach(r => {
      const ok = r.dataset.n.includes(t) && (!kf || (kf === "followed" ? f.has(r.dataset.s) : r.dataset.k.split(" ").includes(kf)));
      r.hidden = !ok; n += ok;
    });
    count.textContent = `${n} of ${rows.length} services shown`;
  }
  if (q) {
    q.addEventListener("input", filterTiles);
    fbtns.forEach(b => b.addEventListener("click", () => { kf = kf === b.dataset.f ? null : b.dataset.f; fbtns.forEach(x => x.setAttribute("aria-pressed", x.dataset.f === kf)); filterTiles(); }));
    filterTiles();
  }

  /* show me another */
  $$("[data-another]").forEach(b => b.addEventListener("click", async () => {
    const all = (await index()).filter(x => x.k !== "service" && x.k !== "thread" && !location.pathname.endsWith(x.u));
    if (all.length) location.href = root + all[Math.floor(Math.random() * all.length)].u;
  }));

  /* copy link */
  $$("[data-copy]").forEach(b => b.addEventListener("click", async () => {
    try { await navigator.clipboard.writeText(location.href); toast("Link copied"); } catch (e) { toast(location.href); }
  }));
})();
