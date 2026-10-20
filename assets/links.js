// Links to other sites open in a new tab, so readers keep their place here.
// Delegated, so it also covers links the page renders after load.
document.addEventListener("click", e => {
  const a = e.target.closest("a[href]");
  if (!a) return;
  const u = new URL(a.href, location.href);
  if (!/^https?:$/.test(u.protocol) || u.host === location.host) return;
  a.target = "_blank";
  a.rel = "noopener";
}, true);
