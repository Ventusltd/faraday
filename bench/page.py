#!/usr/bin/env python3
"""bench/page.py - the bench as cells, with a command bar. A small static page that FETCHES its data, as GridAtlas fetches its config:

    index.html      the page: cells placed by the Kuiper's law, a pulse, a card, and the bar (choose a sentence, or type a command)
    commands.json   THE COMMAND LIST (config): sentences a person reads, each with the command it stands for. Edit this file, or let
                    the runner rebuild it, and the list in the page changes. Nothing about the list is written into the page.
    records.json    every saved simulation, short form
    ../fire.js      the commands that RUN IN THE VISITOR'S BROWSER (and ../fire_site.js when it exists)

White to ice blue = CONFIRMED; the one warning colour = REFUTED; grey = anything else. Black between every dot.
"""
import json
import time

PAGE = r"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Bench</title>
<style>
html,body{margin:0;background:#000;color:#dfe9f5;font:15px/1.5 Consolas,Menlo,monospace}
#wrap{position:relative}canvas{display:block;width:100%;touch-action:manipulation}
#card{position:absolute;left:12px;right:12px;top:12px;max-width:680px;margin:auto;background:#02080c;border:1px solid #1d5560;padding:12px 14px;display:none;max-height:62vh;overflow:auto}
#card h2{margin:0 0 4px;font-size:16px;color:#fff}.r{display:inline-block;padding:0 6px;border:1px solid;margin-right:8px;font-size:12px}
#card p{margin:6px 0}small{color:#8aa}#x{position:absolute;right:10px;top:6px;cursor:pointer;color:#8aa}
#bar{display:flex;flex-wrap:wrap;gap:8px;padding:10px 12px;border-top:1px solid #14323a;background:#02080c}
#bar select,#bar input,#bar button{background:#000;color:#dfe9f5;border:1px solid #1d5560;padding:9px 10px;font:inherit}
#bar select{flex:1 1 260px;min-width:0}#bar input{flex:3 1 420px;min-width:0;color:#22e0ff}#bar button{color:#22e0ff;letter-spacing:.08em}
#foot{padding:8px 12px;color:#667;font-size:12px}
</style></head><body>
<div id="wrap"><canvas id="c"></canvas><div id="card"><span id="x">x</span><h2 id="h"></h2><div id="b"></div></div></div>
<div id="bar"><select id="ex"><option value="">- choose an example sentence -</option></select>
<input id="cmd" spellcheck="false" placeholder='type a command:  fire cable-withstand {"metal":"al","size_mm2":185,"seconds":1,"fault_ka":16}  -  help'>
<button id="go">FIRE</button><button id="all">WHOLE VIEW</button></div>
<div id="foot"><span id="tally"></span> &nbsp; Estimates from stated figures; change any number in a command and fire it again: it runs on your device and nothing you type leaves it. Provided as is, without warranty of any kind; a chart, not a design.</div>
<script src="../fire.js"></script><script src="../fire_site.js" onerror="void 0"></script>
<script>
let R=[],W,H,S,t0=performance.now(),sel=-1,fam=null;const G=Math.PI*(3-Math.sqrt(5)),c=document.getElementById('c'),x=c.getContext('2d'),$=id=>document.getElementById(id);
function fit(){const d=devicePixelRatio||1;W=c.clientWidth;H=Math.max(260,Math.min(innerHeight-150,W));c.width=W*d;c.height=H*d;c.style.height=H+'px';x.setTransform(d,0,0,d,0,0);S=Math.min(W,H)*0.47/Math.sqrt(R.length+1)}
function pos(j){const r=Math.sqrt(j+0.5)*S,a=j*G;return[W/2+r*Math.cos(a),H/2-r*Math.sin(a)]}
function col(r){return r.result==='CONFIRMED'?'#eaf6ff':r.result==='REFUTED'?'#ff8a3c':'#56626b'}
function draw(now){x.clearRect(0,0,W,H);const front=(now-t0)/1000*Math.sqrt(R.length+1)*S*0.9,dot=Math.max(1.2,S*0.30);
 if(front<Math.sqrt(R.length+1)*S*1.1){x.strokeStyle='rgba(34,224,255,.6)';x.lineWidth=2;x.beginPath();x.arc(W/2,H/2,front,0,7);x.stroke()}
 for(let j=0;j<R.length;j++){const p=pos(j),lit=Math.hypot(p[0]-W/2,p[1]-H/2)<=front&&(!fam||R[j].family===fam);x.globalAlpha=lit?1:0.10;x.fillStyle=lit?col(R[j]):'#9fb3c0';
  x.beginPath();x.arc(p[0],p[1],j===sel?dot*1.6:dot,0,7);x.fill()}x.globalAlpha=1;requestAnimationFrame(draw)}
function esc(s){return String(s).replace(/[&<>]/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[m]))}
function nums(n){return n?Object.entries(n).map(e=>e[0].replace(/_/g,' ')+': '+(typeof e[1]==='object'&&e[1]?JSON.stringify(e[1]):e[1])).join(' - '):''}
function card(title,tag,colour,body){$('h').textContent=title;$('b').innerHTML='<span class="r" style="color:'+colour+'">'+tag+'</span>'+body;$('card').style.display='block'}
function show(j){sel=j;const r=R[j];card(r.n+' - '+(r.family||'')+': '+(r.name||''),r.result,col(r),(r.question?'<p>'+esc(r.question)+'</p>':'')+'<p><b>Seen:</b> '+esc(r.observed||'')+'</p><p><small>'+esc(nums(r.numbers))+'</small></p>'+(r.command?'<p><small><b>pop command</b> (tap to put it in the bar): <a href="#" id="use" style="color:#22e0ff">'+esc(r.command.slice(0,300))+'</a></small></p>':''));
 const u=$('use');if(u)u.onclick=e=>{e.preventDefault();$('cmd').value=r.command;$('cmd').focus()}}
function fire(){const text=$('cmd').value.trim();if(!text)return;
 if(/^help$/i.test(text)){card('Commands','HELP','#22e0ff','<p>Type <b>fire</b>, a name, and the inputs in { }. Choose a sentence on the left to see one, change any number, press FIRE.</p><p><small>These run on your device: '+esc((window.FIRE?FIRE.names:[]).join(', '))+'. Others show their saved result.</small></p>');return}
 try{const o=FIRE.fire(text);const same=R.findIndex(q=>q.command===text);
  if(o.ran){fam=o.family;sel=same;t0=performance.now();card('fire '+o.name,'RAN ON YOUR DEVICE','#eaf6ff','<p><b>'+esc(o.said)+'</b></p><p><small>'+esc(nums(o.numbers))+'</small></p><p><small>how: '+esc(o.how)+'</small></p><p><small>inputs: '+esc(JSON.stringify(o.inputs))+' - change any of them in the bar and fire again</small></p>')}
  else if(same>=0){fam=R[same].family;t0=performance.now();show(same);$('b').insertAdjacentHTML('afterbegin','<span class="r" style="color:#8aa">SAVED RESULT</span><small> this model runs in Python tonight; its browser version is next. </small>')}
  else card('fire '+o.name,'NOT YET','#8aa','<p>This command does not run on your device yet, and no saved result has exactly these inputs. Choose a sentence on the left, or type help.</p>')}
 catch(e){card('That did not run','CHECK THE COMMAND','#ff8a3c','<p>'+esc(e.message)+'</p>')}}
c.addEventListener('click',e=>{const b=c.getBoundingClientRect(),mx=e.clientX-b.left,my=e.clientY-b.top;let best=-1,bd=1e9;for(let j=0;j<R.length;j++){const p=pos(j),d=Math.hypot(p[0]-mx,p[1]-my);if(d<bd){bd=d;best=j}}if(bd<Math.max(8,S*0.9))show(best)});
$('x').onclick=()=>{$('card').style.display='none';sel=-1};$('go').onclick=fire;$('cmd').addEventListener('keydown',e=>{if(e.key==='Enter')fire()});
$('all').onclick=()=>{fam=null;sel=-1;t0=performance.now();$('card').style.display='none'};
$('ex').onchange=e=>{if(e.target.value){$('cmd').value=e.target.value;fire();e.target.selectedIndex=0}};
addEventListener('resize',fit);
Promise.all([fetch('records.json').then(r=>r.json()),fetch('commands.json').then(r=>r.json())]).then(([rec,cfg])=>{R=rec.records;$('tally').textContent=rec.tally;
 let g=null,og=null;for(const k of cfg.commands){if(k.family!==g){g=k.family;og=document.createElement('optgroup');og.label=g;$('ex').appendChild(og)}const o=document.createElement('option');o.value=k.command;o.textContent=k.sentence;og.appendChild(o)}
 fit();t0=performance.now();requestAnimationFrame(draw);const q=new URLSearchParams(location.search).get('fire');if(q){$('cmd').value='fire '+q;fire()}})
 .catch(e=>{document.body.insertAdjacentHTML('afterbegin','<p style="padding:16px">The records could not be loaded: '+esc(e.message)+'</p>')});
</script></body></html>
"""

def build_files(rows):
    """Returns {file name: text} for bench/results/: the page, the command list (config) and the records."""
    rows = sorted(rows, key=lambda r: r['n'])
    keep = ('n', 'family', 'name', 'result', 'question', 'observed', 'numbers', 'sentence', 'command')
    lean = ('n', 'family', 'name', 'result', 'observed', 'numbers', 'command')
    recs = [{k: r[k] for k in (keep if r['n'] <= 200 else lean) if k in r} for r in rows]
    tally = {}
    for r in rows:
        tally[r['result']] = tally.get(r['result'], 0) + 1
    t = '%d saved simulations: ' % len(rows) + ', '.join('%d %s' % (v, k.lower()) for k, v in sorted(tally.items()))
    commands, seen = [], {}
    for r in rows:                                          # the known answers first, then up to eight a family, in record order
        if 'command' not in r or 'sentence' not in r:
            continue
        fam = r.get('family', '')
        known = 'known answer' in r.get('name', '')
        if known or seen.get(fam, 0) < 8:
            seen[fam] = seen.get(fam, 0) + (0 if known else 1)
            commands.append(dict(family=fam, sentence=r['sentence'], command=r['command'], record=r['n']))
    commands.sort(key=lambda k: (k['family'], 'known' not in k['sentence'], k['record']))
    cfg = dict(schema='bench.commands.v1', what_it_is='The list in "choose an example sentence". One entry = the sentence a person reads and the command it stands for. The page fetches this file; nothing about the list is written into the page.',
               generated_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), commands=commands)
    return {'index.html': PAGE, 'commands.json': json.dumps(cfg, indent=1), 'records.json': json.dumps(dict(tally=t, records=recs), separators=(',', ':'))}
