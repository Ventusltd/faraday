#!/usr/bin/env python3
"""bench/page.py - the hundred, shown as cells. One static page, made from the ledger, no server, no library.

Each test is one cell, placed by the law the Kuiper draws with (cell j at radius sqrt(j), angle j x the golden angle), so test 1 is in
the middle and test 100 at the rim. White to ice blue = CONFIRMED; the one warning colour = REFUTED; grey = BLOCKED, ERROR or TIMEOUT.
A pulse runs out from the middle and each cell switches on when the front reaches it. Tap a cell to read its record.
The black sky rule holds: a dot is never wider than a third of the gap to its neighbour.
"""
import html
import json

PAGE = r"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>The hundred, as cells</title>
<style>
html,body{margin:0;background:#000;color:#dfe9f5;font:15px/1.5 Consolas,Menlo,monospace}
#top{padding:12px 16px;border-bottom:1px solid #14323a}#top b{color:#22e0ff;letter-spacing:.12em}
#wrap{position:relative}canvas{display:block;width:100%;touch-action:manipulation}
#card{position:absolute;left:12px;right:12px;bottom:12px;max-width:640px;margin:auto;background:#02080c;border:1px solid #1d5560;padding:12px 14px;display:none}
#card h2{margin:0 0 4px;font-size:16px;color:#fff}#card .r{display:inline-block;padding:0 6px;border:1px solid;margin-right:8px;font-size:12px}
#card p{margin:6px 0}#card small{color:#8aa}#x{position:absolute;right:10px;top:6px;cursor:pointer;color:#8aa}
#foot{padding:10px 16px;color:#8aa;font-size:12px;border-top:1px solid #14323a}button{background:#02080c;color:#22e0ff;border:1px solid #1d5560;padding:8px 12px;font:inherit;letter-spacing:.08em}
</style></head><body>
<div id="top"><b>THE HUNDRED</b> &nbsp; __TALLY__ &nbsp; <button id="fire">FIRE THE PULSE</button></div>
<div id="wrap"><canvas id="c"></canvas><div id="card"><span id="x">x</span><h2 id="h"></h2><div id="b"></div></div></div>
<div id="foot">Each dot is one test that could have failed, run on an ordinary desktop computer. Tap a dot. Estimates from public data; provided as is, without warranty of any kind; a chart, not a design.</div>
<script>
const R=__DATA__;const G=Math.PI*(3-Math.sqrt(5));const c=document.getElementById('c'),x=c.getContext('2d');let W,H,S,t0=performance.now(),sel=-1;
function fit(){const d=devicePixelRatio||1;W=c.clientWidth;H=Math.min(innerHeight*0.72,W);c.width=W*d;c.height=H*d;c.style.height=H+'px';x.setTransform(d,0,0,d,0,0);S=Math.min(W,H)*0.46/Math.sqrt(R.length+1)}
function pos(j){const r=Math.sqrt(j+0.5)*S,a=j*G;return[W/2+r*Math.cos(a),H/2-r*Math.sin(a)]}
function col(r){return r.result==='CONFIRMED'?'#eaf6ff':r.result==='REFUTED'?'#ff8a3c':'#56626b'}
function draw(now){x.clearRect(0,0,W,H);const front=(now-t0)/1000*S*4.5;const dot=Math.max(1.5,S*0.30);
 x.strokeStyle='rgba(34,224,255,.55)';x.lineWidth=2;if(front<Math.sqrt(R.length)*S*1.1){x.beginPath();x.arc(W/2,H/2,front,0,7);x.stroke()}
 for(let j=0;j<R.length;j++){const p=pos(j),lit=Math.hypot(p[0]-W/2,p[1]-H/2)<=front;x.globalAlpha=lit?1:0.12;x.fillStyle=lit?col(R[j]):'#9fb3c0';
  x.beginPath();x.arc(p[0],p[1],j===sel?dot*1.5:dot,0,7);x.fill()}x.globalAlpha=1;requestAnimationFrame(draw)}
function show(j){sel=j;const r=R[j];document.getElementById('h').textContent=r.n+' - '+(r.family||'')+': '+(r.name||'');
 const n=r.numbers?Object.entries(r.numbers).map(e=>e[0].replace(/_/g,' ')+': '+e[1]).join(' - '):'';
 document.getElementById('b').innerHTML='<span class="r" style="color:'+col(r)+'">'+r.result+'</span><p>'+esc(r.question||'')+'</p><p><b>Seen:</b> '+esc(String(r.observed||''))+'</p><p><small>'+esc(n)+'</small></p>'+(r.assumed?'<p><small>'+esc(r.assumed)+'</small></p>':'')+(r.command?'<p><small><b>pop command:</b> '+esc(r.command.slice(0,400))+'</small></p>':'')+'<p><small>run it again: python bench/one.py '+r.n+'</small></p>';
 document.getElementById('card').style.display='block'}
function esc(s){return s.replace(/[&<>]/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[m]))}
c.addEventListener('click',e=>{const b=c.getBoundingClientRect(),mx=e.clientX-b.left,my=e.clientY-b.top;let best=-1,bd=1e9;for(let j=0;j<R.length;j++){const p=pos(j),d=Math.hypot(p[0]-mx,p[1]-my);if(d<bd){bd=d;best=j}}if(bd<S*0.9)show(best)});
document.getElementById('x').onclick=()=>{document.getElementById('card').style.display='none';sel=-1};
document.getElementById('fire').onclick=()=>{t0=performance.now()};addEventListener('resize',fit);fit();requestAnimationFrame(draw);
</script></body></html>
"""

def build(rows):
    keep = ('n', 'family', 'name', 'result', 'question', 'observed', 'numbers', 'assumed', 'sentence', 'command')
    lean = ('n', 'family', 'name', 'result', 'observed', 'numbers', 'sentence', 'command')      # past the first 200 the page carries the short form
    data = [{k: r[k] for k in (keep if r['n'] <= 200 else lean) if k in r} for r in sorted(rows, key=lambda r: r['n'])]
    tally = {}
    for r in data:
        tally[r['result']] = tally.get(r['result'], 0) + 1
    t = html.escape('%d run: ' % len(data) + ', '.join('%d %s' % (v, k.lower()) for k, v in sorted(tally.items())))
    return PAGE.replace('__TALLY__', t).replace('__DATA__', json.dumps(data, separators=(',', ':')).replace('</', '<\\/'))
