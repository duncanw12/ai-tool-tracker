(function(){var cur="all",pf="all",q=document.getElementById("q"),c=document.getElementById("cats"),N=document.getElementById("none");
var G=document.querySelectorAll(".grp"),T=document.querySelectorAll(".tool[data-p]");
function r(){var t=q?q.value.toLowerCase().trim():"",any=0;T.forEach(function(el){var p=el.dataset.p;var ok=(cur=="all"||el.dataset.c==cur)&&(pf=="all"||p=="both"||p==pf)&&(!t||el.dataset.s.indexOf(t)>-1);el.hidden=!ok;if(ok)any++});
G.forEach(function(g){g.hidden=!g.querySelector(".tool:not([hidden])")});if(N)N.hidden=!!any;
if(c)[].forEach.call(c.children,function(b){b.classList.toggle("on",b.dataset.c==cur)});
document.querySelectorAll(".pfb").forEach(function(b){var on=b.dataset.p==pf;b.classList.toggle("on",on);b.setAttribute("aria-pressed",on)})}
document.querySelectorAll(".pfb").forEach(function(b){b.addEventListener("click",function(){pf=b.dataset.p;r()})});
if(c)c.addEventListener("click",function(e){var b=e.target.closest(".chip");if(!b)return;e.preventDefault();cur=b.dataset.c;r();document.getElementById("directory").scrollIntoView({block:"start"});history.replaceState(null,"",cur=="all"?"#directory":"#cat-"+cur)});
if(q)q.addEventListener("input",r);r()})();
