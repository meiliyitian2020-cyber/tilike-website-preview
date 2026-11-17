// Keep source text slots and navigation widths fixed when product copy changes.
function alignProductSlots(){
 const reference=ALIGN_REFERENCE[lang];if(!reference)return;
 const issues=[];
 function reserve(element,referenceHtml,availableWidth){
  if(!element)return;
  element.style.removeProperty('height');element.style.removeProperty('min-height');
  const width=availableWidth||element.getBoundingClientRect().width;if(!width)return;
  const probe=element.cloneNode(false);probe.innerHTML=referenceHtml;
  probe.setAttribute('aria-hidden','true');probe.inert=true;
  Object.assign(probe.style,{position:'fixed',left:'0',top:'-99999px',width:width+'px',height:'auto',minHeight:'0',maxHeight:'none',visibility:'hidden',pointerEvents:'none'});
  element.parentElement.appendChild(probe);
  const height=probe.getBoundingClientRect().height,referenceScrollHeight=probe.scrollHeight;probe.remove();
  element.style.height=height+'px';element.style.minHeight=height+'px';
  if(element.scrollHeight>referenceScrollHeight+2)issues.push({selector:element.tagName+'.'+element.className,text:element.textContent,referenceHeight:height,actualHeight:element.scrollHeight});
 }
 reserve($('.entity-name'),'Chivalyouth Technology PTE.LTD.');
 reserve($('.entity-address'),'Registered office: 65 CHULIA STREET #38-02/03 OCBC CENTRE, SINGAPORE 049513',$('.entity-address')?.parentElement.clientWidth);
 if(activePage==='home'){
  reserve($('#hello h1'),reference.home.title);reserve($('#hello .hero-description'),reference.home.description);
  reference.home.scenes.forEach(s=>{
   reserve($('#'+s.id+' .scene-copy h2'),s.title);reserve($('#'+s.id+' .scene-copy>p'),s.description);
  });
  const referenceLabels=[reference.nav.home,...reference.home.scenes.map(s=>s.title)];
  $$('.screen-nav button').forEach((button,i)=>{
   button.style.removeProperty('width');button.style.removeProperty('min-width');
   const probe=button.cloneNode(true);$('span',probe).textContent=referenceLabels[i];
   probe.setAttribute('aria-hidden','true');probe.inert=true;
   Object.assign(probe.style,{position:'fixed',left:'0',top:'-99999px',width:'auto',visibility:'hidden',pointerEvents:'none'});
   button.parentElement.appendChild(probe);const width=probe.getBoundingClientRect().width;probe.remove();
   button.style.width=width+'px';button.style.minWidth=width+'px';
  });
  fitMobileHome(true);
 }else{
  let introText=reference[activePage]?.intro;
  if(activePage.startsWith('policy/'))introText=reference.policyDescriptions[activePage.split('/')[1]];
  if(activePage==='law-enforcement')introText=reference.policyDescriptions.law;
  if(introText)reserve($('.page-intro>.wrap>p'),introText);
  if(activePage==='about'){
   reserve($('.about-copy h2'),reference.about.heading);
   $$('.about-copy>p').forEach((p,i)=>reserve(p,reference.about.paragraphs[i]));
   $$('.about-values article').forEach((article,i)=>{reserve($('h3',article),reference.about.values[i][0]);reserve($('p',article),reference.about.values[i][1]);});
  }
  reserve($('.footer-brand>p'),reference.footer.tagline);
  if(window.innerWidth<=680)reserve($('.download-band p'),reference.home.downloadText);
  if(activePage==='safety'){
   $$('.policy-row p').forEach((p,i)=>reserve(p,reference.policyDescriptions[['terms','privacy','children','community','bullying','cookies','law'][i]]));
  }
  if(activePage==='contact'){
   $$('.contact-choice h2').forEach((h,i)=>reserve(h,i===0?reference.contact.supportTitle:reference.contact.businessTitle));
   const email=$('.contact-choice a[href^="mailto:"]');
   if(email){
    // v19 mail control measured at both required viewports, with bundled fonts.
    const width=lang==='hi'?215.546875:216.234375;
    email.style.width=width+'px';email.style.justifyContent='space-between';
   }
  }
 }
 window.TILIKE_ALIGNMENT={sourceVersion:19,issues};
 document.documentElement.setAttribute('data-alignment-issues',JSON.stringify(issues));
 document.documentElement.setAttribute('data-alignment-language',lang);
 document.documentElement.setAttribute('data-alignment-width',String(window.innerWidth));
}
const renderAlignedProduct=render;
render=function(){renderAlignedProduct();requestAnimationFrame(alignProductSlots);document.fonts?.ready.then(alignProductSlots);};
window.addEventListener('resize',()=>requestAnimationFrame(alignProductSlots));
