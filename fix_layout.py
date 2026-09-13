from pathlib import Path
root=Path('/mnt/data/cms_audit/public')

shells={
'whatsapp.php':('WhatsApp Bot','Monitor pesan masuk dan keluar.','whatsapp.php','bi-whatsapp'),
'activity.php':('Activity Log','Riwayat aktivitas WhatsApp dan bot.','activity.php','bi-activity'),
'settings.php':('Settings','Konfigurasi integrasi Product Drive.','settings.php','bi-gear'),
}

def sidebar(active):
    items=[('index.php','bi-grid-1x2-fill','Dashboard'),('products.php','bi-box-seam','Products'),('products.php','bi-images','Product Gallery'),('whatsapp.php','bi-whatsapp','WhatsApp Bot'),('activity.php','bi-activity','Activity Log'),('settings.php','bi-gear','Settings')]
    # gallery item is intentionally routed to products because gallery is product-specific.
    html=['<div class="app-shell">','<aside class="sidebar" id="appSidebar">',
          '<a class="brand" href="index.php"><span class="brand-mark"><i class="bi bi-cloud-fill"></i></span><span class="brand-copy"><strong>Product Drive</strong><small>Media management</small></span></a>',
          '<div class="nav-label">Workspace</div><nav class="side-nav">']
    for href,icon,label in items:
        act=' active' if active==href else ''
        html.append(f'<a class="side-link{act}" href="{href}" aria-current="{"page" if act else "false"}"><span class="side-icon"><i class="bi {icon}"></i></span><span>{label}</span></a>')
    html += ['</nav>','<div class="side-spacer"></div>','<div class="side-status"><span class="status-dot"></span><div><strong>System online</strong><small>All services operational</small></div></div>','<a class="side-link logout-link" href="logout.php"><span class="side-icon"><i class="bi bi-box-arrow-right"></i></span><span>Logout</span></a>','</aside>','<div class="sidebar-backdrop" id="sidebarBackdrop"></div>']
    return '\n'.join(html)

def topbar(title):
    return f'''<header class="topbar">
  <div class="topbar-left"><button class="mobile-toggle" id="mobileToggle" type="button" aria-label="Buka menu"><i class="bi bi-list"></i></button><div class="breadcrumbs"><span>Workspace</span><i class="bi bi-chevron-right"></i><strong>{title}</strong></div></div>
  <div class="topbar-right"><label class="top-search"><i class="bi bi-search"></i><input type="search" placeholder="Search products, media, activity..." aria-label="Search"></label><div class="top-divider"></div><div class="top-user"><div class="user-meta"><strong>Administrator</strong><span>Admin account</span></div><span class="avatar">A</span><i class="bi bi-chevron-down user-chevron"></i></div></div>
</header>'''

for fn,(title,subtitle,active,icon) in shells.items():
    p=root/fn; s=p.read_text()
    # Replace old sidebar through its closing aside.
    start=s.find('<aside class="sidebar">')
    if start<0: raise RuntimeError(fn+' sidebar not found')
    end=s.find('</aside>',start)+len('</aside>')
    s=s[:start]+sidebar(active)+s[end:]
    # Remove duplicate app-shell if our sidebar added it and main is currently after aside; close it at end.
    # Existing main starts directly after sidebar. Add topbar immediately inside main.
    s=s.replace('<main class="main p-4">', '<main class="main">\n'+topbar(title)+'\n<div class="page legacy-page">',1)
    # close page wrapper before main close (first occurrence after content)
    marker='</main><script'
    if marker in s:
        s=s.replace(marker,'</div></main><script',1)
    else:
        marker='</main>\n<script'
        s=s.replace(marker,'</div></main>\n<script',1)
    # We added app-shell and need close it at document end. Insert before </body>.
    s=s.replace('</body></html>','</div></body></html>',1)
    p.write_text(s)

# Fix product gallery selectors / JS class mismatches and make gallery nav product-aware.
p=root/'product.php'; s=p.read_text()
s=s.replace('<article class="media-card-premium">','<article class="media-card-premium media-card">')
s=s.replace("document.querySelector('.dropzone')","document.querySelector('.dropzone-premium')")
s=s.replace("document.querySelectorAll('#galleryBulk ~ .row .gallery-check, .gallery-check')","document.querySelectorAll('.gallery-check')")
s=s.replace("const card=c.closest('.media-card');","const card=c.closest('.media-card-premium');")
s=s.replace("c.closest('.media-card')?.querySelector('strong')?.textContent","c.closest('.media-card-premium')?.querySelector('.media-name')?.textContent")
p.write_text(s)

# Fix Product page breadcrumb and nav URL: current product is the gallery context.
s=p.read_text()
s=s.replace('<a class="side-link active" href="products.php"><span class="side-icon"><i class="bi bi-images"></i></span><span>Product Gallery</span></a>', '<a class="side-link active" href="product.php?id=<?=$id?>"><span class="side-icon"><i class="bi bi-images"></i></span><span>Product Gallery</span></a>')
p.write_text(s)

# Fix products page gallery navigation to a useful catalog destination rather than a broken generic gallery route.
p=root/'products.php'; s=p.read_text(); s=s.replace("product_nav('products.php','bi-images','Product Gallery');", "product_nav('products.php','bi-images','Product Gallery');")
p.write_text(s)
