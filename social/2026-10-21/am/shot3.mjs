import { spawn } from 'node:child_process';
import fs from 'node:fs';
const port = 9333;
const chrome = spawn('google-chrome', ['--headless=new','--no-sandbox','--disable-gpu',`--remote-debugging-port=${port}`,'--hide-scrollbars','about:blank'], {stdio:'ignore'});
const sleep = ms => new Promise(r=>setTimeout(r,ms));
await sleep(2500);
const tabs = await (await fetch(`http://127.0.0.1:${port}/json`)).json();
const ws = new WebSocket(tabs.find(t=>t.type==='page').webSocketDebuggerUrl);
await new Promise(r=>ws.onopen=r);
let id=0; const pending={};
ws.onmessage = e => { const m=JSON.parse(e.data); if(m.id&&pending[m.id]){pending[m.id](m);delete pending[m.id];} };
const send=(method,params={})=>new Promise(r=>{const i=++id;pending[i]=r;ws.send(JSON.stringify({id:i,method,params}));});
await send('Page.enable'); await send('Runtime.enable');
await send('Emulation.setDeviceMetricsOverride',{width:540,height:900,deviceScaleFactor:2,mobile:false});
await send('Page.navigate',{url:'https://www.disneyplus.com/legal/subscriber-agreement'});
await sleep(12000);
const expr = `(() => {
  document.querySelectorAll('#onetrust-banner-sdk,#onetrust-consent-sdk').forEach(e=>e.remove());
  const sx=window.scrollX, sy=window.scrollY;
  const find=(needle)=>{const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);let n;while(n=w.nextNode()){const i=n.textContent.indexOf(needle);if(i>=0)return [n,i];}return null;};
  let [n]=find('Service Tiers With or Without Ads');
  let el=n.parentElement; while(el && !el.textContent.includes('branded content, product integrations')) el=el.parentElement;
  const r=el.getBoundingClientRect();
  const phrases=['generally free of commercial interruptions','with certain exceptions that may change from time to time','may contain limited promotional content','branded content, product integrations, or sponsorship messaging'];
  const boxes=[];
  for(const p of phrases){
    // phrase may span nodes; search within el's text nodes
    const w=document.createTreeWalker(el,NodeFilter.SHOW_TEXT); let t, nodes=[], full='';
    while(t=w.nextNode()){nodes.push([t,full.length]);full+=t.textContent;}
    const i=full.indexOf(p); if(i<0){boxes.push({p,missing:true});continue;}
    const loc=(off)=>{for(let k=nodes.length-1;k>=0;k--){if(off>=nodes[k][1])return [nodes[k][0],off-nodes[k][1]];}};
    const rg=document.createRange(); const a=loc(i), b=loc(i+p.length);
    rg.setStart(a[0],a[1]); rg.setEnd(b[0],b[1]);
    boxes.push({p,rects:[...rg.getClientRects()].map(q=>({x:q.x+sx,y:q.y+sy,w:q.width,h:q.height}))});
  }
  const u=find('Updated: 2/5/2026'); const ur=u[0].parentElement.getBoundingClientRect();
  const h=[...document.querySelectorAll('h1,h2')].find(e=>e.textContent.includes('Subscriber Agreement')); const hr=h.getBoundingClientRect();
  return JSON.stringify({para:{x:r.x+sx,y:r.y+sy,w:r.width,h:r.height},boxes,updated:{x:ur.x,y:ur.y+sy,w:ur.width,h:ur.height},title:{x:hr.x,y:hr.y+sy,w:hr.width,h:hr.height}});
})()`;
const res = await send('Runtime.evaluate',{expression:expr,returnByValue:true});
const info=JSON.parse(res.result.result.value); console.log(JSON.stringify(info,null,1));
fs.writeFileSync('rects_m.json',JSON.stringify(info));
const p=info.para;
const clip={x:p.x-16,y:p.y-16,width:p.w+32,height:p.h+32,scale:2};
const shot = await send('Page.captureScreenshot',{format:'png',clip,captureBeyondViewport:true});
fs.writeFileSync('para_m.png', Buffer.from(shot.result.data,'base64'));
const t=info.title, u=info.updated;
const clip2={x:t.x-16,y:t.y-16,width:p.w+32,height:(u.y+u.h)-(t.y)+60,scale:2};
const shot2 = await send('Page.captureScreenshot',{format:'png',clip:clip2,captureBeyondViewport:true});
fs.writeFileSync('head_m.png', Buffer.from(shot2.result.data,'base64'));
fs.writeFileSync('clips_m.json',JSON.stringify({clip,clip2}));
ws.close(); chrome.kill(); process.exit(0);
