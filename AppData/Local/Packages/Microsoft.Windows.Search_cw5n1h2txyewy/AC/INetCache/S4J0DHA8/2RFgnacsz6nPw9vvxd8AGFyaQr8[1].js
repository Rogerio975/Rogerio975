var ProgressiveImages;(function(){function n(){for(var n,t,r=_d.getElementsByTagName("img"),i=0;i<r.length;i++)n=r[i],t=n.getAttribute("data-src-hq"),t&&n.src!=t&&(n.src=t)}sj_evt.bind("onP1",n,1);sj_evt.bind("ajax.postload",n,1);sj_evt.bind("loadProgImages",n,1)})(ProgressiveImages||(ProgressiveImages={}))