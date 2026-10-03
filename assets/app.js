const menu=document.getElementById('menu');
menu?.addEventListener('click',()=>{const state=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(state));document.getElementById('chapters').classList.toggle('visible',state)});
document.querySelectorAll('details.card').forEach(el=>el.addEventListener('toggle',()=>{if(el.open)el.querySelectorAll('iframe[data-src]').forEach(frame=>{frame.src=frame.dataset.src;delete frame.dataset.src})}));
function openHash(){if(!location.hash)return;const el=document.getElementById(decodeURIComponent(location.hash.slice(1)));if(!el)return;for(let p=el;p;p=p.parentElement)if(p.tagName==='DETAILS')p.open=true;el.scrollIntoView({block:'start'})}
addEventListener('hashchange',openHash);openHash();
