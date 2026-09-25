/* Datasphere Dynamics - UI behaviour */
(function(){
  'use strict';

  /* mobile nav */
  var hdr=document.getElementById('hdr'), burger=document.getElementById('burger');
  if(hdr&&burger){
    burger.addEventListener('click',function(){
      var open=hdr.classList.toggle('open');
      burger.setAttribute('aria-expanded',open?'true':'false');
    });
    hdr.querySelectorAll('.nav a').forEach(function(a){
      a.addEventListener('click',function(){hdr.classList.remove('open');burger.setAttribute('aria-expanded','false');});
    });
  }

  /* scroll reveal */
  var items=document.querySelectorAll('.rv');
  if(!items.length) return;
  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(reduce||!('IntersectionObserver' in window)){
    items.forEach(function(el){el.classList.add('in');});
    return;
  }
  var io=new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}
    });
  },{rootMargin:'0px 0px -8% 0px',threshold:0.08});
  items.forEach(function(el){io.observe(el);});
})();
