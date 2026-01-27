<!doctype html>
<html lang="en" class="no-js">
  <head>
    
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      
        <meta name="description" content="Unified reference documentation for LangChain and LangGraph Python packages.">
      
      
        <meta name="author" content="LangChain">
      
      
        <link rel="canonical" href="https://reference.langchain.com/python/langsmith/deployment/remote_graph/">
      
      
        <link rel="prev" href="../sdk/">
      
      
      
        
      
      
      <link rel="icon" href="../../../static/brand/docs-favicon.png">
      <meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.7.0">
    
    
  
    <title>RemoteGraph | LangChain Reference</title>
  

    
      <link rel="stylesheet" href="../../../assets/stylesheets/main.618322db.min.css">
      
        
        <link rel="stylesheet" href="../../../assets/stylesheets/palette.ab4e12ef.min.css">
      
      

  
  
  
  
  <style>:root{--md-annotation-icon:url('data:image/svg+xml;charset=utf-8,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20viewBox%3D%220%200%2024%2024%22%3E%3Cpath%20d%3D%22M22%2012a10%2010%200%200%201-10%2010A10%2010%200%200%201%202%2012%2010%2010%200%200%201%2012%202a10%2010%200%200%201%2010%2010m-12%206%206-6-6-6-1.4%201.4%204.6%204.6-4.6%204.6z%22/%3E%3C/svg%3E');}</style>


    
    
      
    
    
      
        
        
        
        <link rel="stylesheet" href="../../../assets/external/fonts.googleapis.com/css.56f7ac64.css">
        <style>:root{--md-text-font:"Inter";--md-code-font:"JetBrains Mono"}</style>
      
    
    
      <link rel="stylesheet" href="../../../assets/_mkdocstrings.css">
    
      <link rel="stylesheet" href="../../../stylesheets/logos.css">
    
      <link rel="stylesheet" href="../../../stylesheets/toc.css">
    
      <link rel="stylesheet" href="../../../stylesheets/sticky_navigation.css">
    
      <link rel="stylesheet" href="../../../stylesheets/version_admonitions.css">
    
      <link rel="stylesheet" href="../../../stylesheets/page_width.css">
    
    <script>__md_scope=new URL("../../..",location),__md_hash=e=>[...e].reduce(((e,_)=>(e<<5)-e+_.charCodeAt(0)),0),__md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e)),__md_set=(e,_,t=localStorage,a=__md_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(_))}catch(e){}}</script>
    
<!-- Google Tag Manager -->
<script>(function (w, d, s, l, i) {
    w[l] = w[l] || []; w[l].push({
      'gtm.start':
        new Date().getTime(), event: 'gtm.js'
    }); var f = d.getElementsByTagName(s)[0],
      j = d.createElement(s), dl = l != 'dataLayer' ? '&l=' + l : ''; j.async = true; j.src =
        'https://www.googletagmanager.com/gtm.js?id=' + i + dl; f.parentNode.insertBefore(j, f);
  })(window, document, 'script', 'dataLayer', 'GTM-MBBX68ST');</script>
<!-- End Google Tag Manager -->
<!-- CookieYes Banner -->
 <!-- (Added functionality for instant nav support) -->
<script>
  (function() {
    // === DEBUG MODE ===
    var CKY_DEBUG = false;

    function log(msg, data) {
      if (CKY_DEBUG) {
        var prefix = '[CookieYes Debug]';
        if (data !== undefined) {
          console.log(prefix, msg, data);
        } else {
          console.log(prefix, msg);
        }
      }
    }

    var ckyStylesBackup = null;

    // Load CookieYes script on initial page load
    function loadCookieYes() {
      if (!document.getElementById('cookieyes')) {
        log('Loading CookieYes script...');
        var script = document.createElement('script');
        script.id = 'cookieyes';
        script.type = 'text/javascript';
        script.src = 'https://cdn-cookieyes.com/client_data/d2e859934c4309be824ea8bb/script.js';
        document.head.appendChild(script);
      } else {
        log('CookieYes script already exists, skipping load');
      }
    }

    // Watch for CookieYes styles to be added and back them up
    var observer = new MutationObserver(function(mutations) {
      var ckyStyle = document.getElementById('cky-style');
      if (ckyStyle && !ckyStylesBackup) {
        ckyStylesBackup = ckyStyle.innerHTML;
        log('Captured CookieYes styles, length:', ckyStylesBackup.length + ' chars');
      }
    });
    observer.observe(document.head, { childList: true });

    // Restore CookieYes styles after instant navigation if missing
    function restoreCkyStyles() {
      var ckyStyle = document.getElementById('cky-style');
      var bannerExists = document.querySelector('.cky-consent-container, .cky-btn-revisit-wrapper');

      log('Navigation detected - checking styles...', {
        stylesExist: !!ckyStyle,
        bannerExists: !!bannerExists,
        backupAvailable: !!ckyStylesBackup
      });

      if (!ckyStyle && ckyStylesBackup) {
        var style = document.createElement('style');
        style.id = 'cky-style';
        style.innerHTML = ckyStylesBackup;
        document.head.appendChild(style);
        log('Restored CookieYes styles successfully');
      } else if (ckyStyle) {
        log('Styles already present, no restore needed');
      } else if (!ckyStylesBackup) {
        log('WARNING: No backup available to restore!');
      }
    }

    // Initial load
    document.addEventListener('DOMContentLoaded', function() {
      log('DOMContentLoaded fired');
      loadCookieYes();
    });

    // Subscribe to MkDocs Material's document$ observable for instant navigation
    // document$ is available after the theme's JS loads
    var checkCount = 0;
    var checkInterval = setInterval(function() {
      checkCount++;
      if (typeof document$ !== 'undefined') {
        clearInterval(checkInterval);
        log('Found document$ observable after ' + checkCount + ' checks');
        document$.subscribe(function() {
          log('document$ emitted (page navigation/load)');
          restoreCkyStyles();
        });
      }
    }, 100);

    // Fallback: stop checking after 10 seconds
    setTimeout(function() {
      if (checkInterval) {
        clearInterval(checkInterval);
        log('WARNING: document$ not found after 10 seconds - instant nav support disabled');
      }
    }, 10000);

    // Expose debug helpers to window for console access
    window.__ckyDebug = {
      getBackup: function() { return ckyStylesBackup; },
      getBackupLength: function() { return ckyStylesBackup ? ckyStylesBackup.length : 0; },
      checkStyles: function() {
        var ckyStyle = document.getElementById('cky-style');
        var banner = document.querySelector('.cky-consent-container, .cky-btn-revisit-wrapper');
        return {
          stylesInDOM: !!ckyStyle,
          stylesLength: ckyStyle ? ckyStyle.innerHTML.length : 0,
          bannerInDOM: !!banner,
          backupLength: ckyStylesBackup ? ckyStylesBackup.length : 0
        };
      },
      forceRestore: function() {
        restoreCkyStyles();
      }
    };
    log('Debug helpers available at window.__ckyDebug');
  })();
</script>

    
  <style>
    @import url("https://fonts.googleapis.com/css2?family=Public+Sans&display=swap");
    :root {
      --md-primary-fg-color: #333333;
      --md-accent-fg-color: #1E88E5;
      --md-default-bg-color: #FFFFFF;
      --md-default-fg-color: #333333;
      --md-text-font-family: "Public Sans", sans-serif;
    }

    body {
      font-family: var(--md-text-font-family);
      background-color: var(--md-default-bg-color);
      color: var(--md-default-fg-color);
    }

    .md-main {
      background-color: #FFFFFF;
    }

    .md-footer {
      background-color: #F5F5F5;
      color: #666666;
    }

    .md-footer-meta {
      background-color: #4d4d4d;
    }

    .md-typeset a {
      color: #1E88E5;
    }

    .md-typeset a:hover {
      color: #1565C0;
    }

    .md-nav__link--active,
    .md-nav__link:active {
      color: #1E88E5;
    }

    .md-search__input {
      background-color: #F5F5F5;
      color: #333333;
    }

    .md-search__input:hover,
    .md-search__input:focus {
      background-color: #EEEEEE;
    }
    /* Table of contents styles */
    .md-nav--secondary .md-nav__item--active > .md-nav__link {
      font-weight: bold;
      color: var(--md-primary-fg-color);
    }

    .md-nav--secondary .md-nav__item--nested > .md-nav__link {
      font-weight: normal;
      color: var(--md-default-fg-color);
    }

    .md-nav--secondary .md-nav__item--nested > .md-nav__link::before {
      content: "";
      display: inline-block;
      width: 6px;
      height: 6px;
      background-color: var(--md-default-fg-color);
      border-radius: 50%;
      margin-right: 0.5rem;
    }

    [data-md-color-scheme="slate"] {
      --md-default-bg-color: #1E1E1E;
      --md-default-fg-color: #FFFFFF;
      --md-accent-fg-color: #64B5F6;
    }

    [data-md-color-scheme="slate"] .md-main {
      background-color: #1E1E1E;
    }

    [data-md-color-scheme="slate"] .navbar {
      background-color: #1E1E1E;
      color: #FFFFFF;
      box-shadow: none;
    }

    [data-md-color-scheme="slate"] .md-footer {
      background-color: #1E1E1E;
      color: #BDBDBD;
    }

    [data-md-color-scheme="slate"] .md-header {
      background-color: #1E1E1E;
      color: #BDBDBD;
    }

    [data-md-color-scheme="slate"] .md-tabs {
      background-color: #1E1E1E;
      color: #BDBDBD;
    }

    [data-md-color-scheme="slate"] .md-search__input {
      background-color: #F5F5F5;
      color: #333333;
    }

    [data-md-color-scheme="slate"] .md-search__icon {
      color: #333333;
    }

    [data-md-color-scheme="slate"] .md-search__input::placeholder {
      color: #333333;
    }

    [data-md-color-scheme="slate"] .md-footer-meta {
      background-color: #4d4d4d;
    }

    [data-md-color-scheme="slate"] .md-typeset a {
      color: #64B5F6;
    }

    [data-md-color-scheme="slate"] .md-typeset a:hover {
      color: #90CAF9;
    }

    [data-md-color-scheme=default] .logo-dark {
      display: none !important;
    }

    [data-md-color-scheme=slate] .logo-light {
      display: none !important;
    }

    .md-banner {
      background-color: #FFAE42;
      color: #000000;
    }

    .md-banner a {
      color: #000000;
      text-decoration: underline;
    }

    .md-banner a:hover {
      color: #000000;
    }

    .md-header__title {
      visibility: hidden;
    }

    /* Dark mode banner styling */
    [data-md-color-scheme="slate"] .md-banner {
      background-color: #CFC9FA; /* Same light purple for both modes */
      color: #000000;
    }

    [data-md-color-scheme="slate"] .md-banner a {
      color: #000000;
    }

    [data-md-color-scheme="slate"] .md-banner a:hover {
      color: #000000;
    }

  </style>

  </head>
  
  
    
    
      
    
    
    
    
    <body dir="ltr" data-md-color-scheme="default" data-md-color-primary="indigo" data-md-color-accent="indigo">
  
    
    <input class="md-toggle" data-md-toggle="drawer" type="checkbox" id="__drawer" autocomplete="off">
    <input class="md-toggle" data-md-toggle="search" type="checkbox" id="__search" autocomplete="off">
    <label class="md-overlay" for="__drawer"></label>
    <div data-md-component="skip">
      
        
        <a href="#langgraph.pregel.remote" class="md-skip">
          Skip to content
        </a>
      
    </div>
    <div data-md-component="announce">
      
    </div>
    
    
      

<header class="md-header" data-md-component="header">
  <nav class="md-header__inner md-grid" aria-label="Header">
    <a href="../../.." title="LangChain Reference" class="md-header__button md-logo" aria-label="LangChain Reference" data-md-component="logo">
      
  <img src="../../../static/brand/reference-light.svg" alt="logo" class="logo-light" />
  <img src="../../../static/brand/reference-dark.svg" alt="logo" class="logo-dark" />

    </a>
    <label class="md-header__button md-icon" for="__drawer">
      
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M3 6h18v2H3zm0 5h18v2H3zm0 5h18v2H3z"/></svg>
    </label>
    <div class="md-header__title" data-md-component="header-title">
      <div class="md-header__ellipsis">
        <div class="md-header__topic">
          <span class="md-ellipsis">
            LangChain Reference
          </span>
        </div>
        <div class="md-header__topic" data-md-component="header-topic">
          <span class="md-ellipsis">
            
              RemoteGraph
            
          </span>
        </div>
      </div>
    </div>
    
      
        <form class="md-header__option" data-md-component="palette">
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme)" data-md-color-scheme="default" data-md-color-primary="indigo" data-md-color-accent="indigo"  aria-label="Switch to light mode"  type="radio" name="__palette" id="__palette_0">
    
      <label class="md-header__button md-icon" title="Switch to light mode" for="__palette_1" hidden>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="m14.3 16-.7-2h-3.2l-.7 2H7.8L11 7h2l3.2 9zM20 8.69V4h-4.69L12 .69 8.69 4H4v4.69L.69 12 4 15.31V20h4.69L12 23.31 15.31 20H20v-4.69L23.31 12zm-9.15 3.96h2.3L12 9z"/></svg>
      </label>
    
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme: light)" data-md-color-scheme="default" data-md-color-primary="white" data-md-color-accent="gray"  aria-label="Switch to dark mode"  type="radio" name="__palette" id="__palette_1">
    
      <label class="md-header__button md-icon" title="Switch to dark mode" for="__palette_2" hidden>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 8a4 4 0 0 0-4 4 4 4 0 0 0 4 4 4 4 0 0 0 4-4 4 4 0 0 0-4-4m0 10a6 6 0 0 1-6-6 6 6 0 0 1 6-6 6 6 0 0 1 6 6 6 6 0 0 1-6 6m8-9.31V4h-4.69L12 .69 8.69 4H4v4.69L.69 12 4 15.31V20h4.69L12 23.31 15.31 20H20v-4.69L23.31 12z"/></svg>
      </label>
    
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme: dark)" data-md-color-scheme="slate" data-md-color-primary="grey" data-md-color-accent="white"  aria-label="Switch to system preference"  type="radio" name="__palette" id="__palette_2">
    
      <label class="md-header__button md-icon" title="Switch to system preference" for="__palette_0" hidden>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 18c-.89 0-1.74-.2-2.5-.55C11.56 16.5 13 14.42 13 12s-1.44-4.5-3.5-5.45C10.26 6.2 11.11 6 12 6a6 6 0 0 1 6 6 6 6 0 0 1-6 6m8-9.31V4h-4.69L12 .69 8.69 4H4v4.69L.69 12 4 15.31V20h4.69L12 23.31 15.31 20H20v-4.69L23.31 12z"/></svg>
      </label>
    
  
</form>
      
    
    
      <script>var palette=__md_get("__palette");if(palette&&palette.color){if("(prefers-color-scheme)"===palette.color.media){var media=matchMedia("(prefers-color-scheme: light)"),input=document.querySelector(media.matches?"[data-md-color-media='(prefers-color-scheme: light)']":"[data-md-color-media='(prefers-color-scheme: dark)']");palette.color.media=input.getAttribute("data-md-color-media"),palette.color.scheme=input.getAttribute("data-md-color-scheme"),palette.color.primary=input.getAttribute("data-md-color-primary"),palette.color.accent=input.getAttribute("data-md-color-accent")}for(var[key,value]of Object.entries(palette.color))document.body.setAttribute("data-md-color-"+key,value)}</script>
    
    
    
      
      
        <label class="md-header__button md-icon" for="__search">
          
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9.5 3A6.5 6.5 0 0 1 16 9.5c0 1.61-.59 3.09-1.56 4.23l.27.27h.79l5 5-1.5 1.5-5-5v-.79l-.27-.27A6.52 6.52 0 0 1 9.5 16 6.5 6.5 0 0 1 3 9.5 6.5 6.5 0 0 1 9.5 3m0 2C7 5 5 7 5 9.5S7 14 9.5 14 14 12 14 9.5 12 5 9.5 5"/></svg>
        </label>
        <div class="md-search" data-md-component="search" role="dialog">
  <label class="md-search__overlay" for="__search"></label>
  <div class="md-search__inner" role="search">
    <form class="md-search__form" name="search">
      <input type="text" class="md-search__input" name="query" aria-label="Search" placeholder="Search" autocapitalize="off" autocorrect="off" autocomplete="off" spellcheck="false" data-md-component="search-query" required>
      <label class="md-search__icon md-icon" for="__search">
        
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9.5 3A6.5 6.5 0 0 1 16 9.5c0 1.61-.59 3.09-1.56 4.23l.27.27h.79l5 5-1.5 1.5-5-5v-.79l-.27-.27A6.52 6.52 0 0 1 9.5 16 6.5 6.5 0 0 1 3 9.5 6.5 6.5 0 0 1 9.5 3m0 2C7 5 5 7 5 9.5S7 14 9.5 14 14 12 14 9.5 12 5 9.5 5"/></svg>
        
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M20 11v2H8l5.5 5.5-1.42 1.42L4.16 12l7.92-7.92L13.5 5.5 8 11z"/></svg>
      </label>
      <nav class="md-search__options" aria-label="Search">
        
          <a href="javascript:void(0)" class="md-search__icon md-icon" title="Share" aria-label="Share" data-clipboard data-clipboard-text="" data-md-component="search-share" tabindex="-1">
            
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M18 16.08c-.76 0-1.44.3-1.96.77L8.91 12.7c.05-.23.09-.46.09-.7s-.04-.47-.09-.7l7.05-4.11c.54.5 1.25.81 2.04.81a3 3 0 0 0 3-3 3 3 0 0 0-3-3 3 3 0 0 0-3 3c0 .24.04.47.09.7L8.04 9.81C7.5 9.31 6.79 9 6 9a3 3 0 0 0-3 3 3 3 0 0 0 3 3c.79 0 1.5-.31 2.04-.81l7.12 4.15c-.05.21-.08.43-.08.66 0 1.61 1.31 2.91 2.92 2.91s2.92-1.3 2.92-2.91A2.92 2.92 0 0 0 18 16.08"/></svg>
          </a>
        
        <button type="reset" class="md-search__icon md-icon" title="Clear" aria-label="Clear" tabindex="-1">
          
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 6.41 17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/></svg>
        </button>
      </nav>
      
        <div class="md-search__suggest" data-md-component="search-suggest"></div>
      
    </form>
    <div class="md-search__output">
      <div class="md-search__scrollwrap" tabindex="0" data-md-scrollfix>
        <div class="md-search-result" data-md-component="search-result">
          <div class="md-search-result__meta">
            Initializing search
          </div>
          <ol class="md-search-result__list" role="presentation"></ol>
        </div>
      </div>
    </div>
  </div>
</div>
      
    
    
      <div class="md-header__source">
        <a href="https://github.com/langchain-ai/docs" title="Go to repository" class="md-source" data-md-component="source" target="_blank" rel="noopener">
  <div class="md-source__icon md-icon">
    
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Free 7.1.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2025 Fonticons, Inc.--><path d="M439.6 236.1 244 40.5c-5.4-5.5-12.8-8.5-20.4-8.5s-15 3-20.4 8.4L162.5 81l51.5 51.5c27.1-9.1 52.7 16.8 43.4 43.7l49.7 49.7c34.2-11.8 61.2 31 35.5 56.7-26.5 26.5-70.2-2.9-56-37.3L240.3 199v121.9c25.3 12.5 22.3 41.8 9.1 55-6.4 6.4-15.2 10.1-24.3 10.1s-17.8-3.6-24.3-10.1c-17.6-17.6-11.1-46.9 11.2-56v-123c-20.8-8.5-24.6-30.7-18.6-45L142.6 101 8.5 235.1C3 240.6 0 247.9 0 255.5s3 15 8.5 20.4l195.6 195.7c5.4 5.4 12.7 8.4 20.4 8.4s15-3 20.4-8.4l194.7-194.7c5.4-5.4 8.4-12.8 8.4-20.4s-3-15-8.4-20.4"/></svg>
  </div>
  <div class="md-source__repository">
    langchain-ai/docs
  </div>
</a>
      </div>
    
  </nav>
  
</header>
    
    <div class="md-container" data-md-component="container">
      
      
        
          
            
<nav class="md-tabs" aria-label="Tabs" data-md-component="tabs">
  <div class="md-grid">
    <ul class="md-tabs__list">
      
        
  
  
  
  
    <li class="md-tabs__item">
      <a href="../../.." class="md-tabs__link">
        
  
  
    
  
  Get started

      </a>
    </li>
  

      
        
  
  
  
  
    
    
      <li class="md-tabs__item">
        <a href="../../../langchain/" class="md-tabs__link">
          
  
  
    
  
  LangChain

        </a>
      </li>
    
  

      
        
  
  
  
  
    
    
      <li class="md-tabs__item">
        <a href="../../../langgraph/" class="md-tabs__link">
          
  
  
    
  
  LangGraph

        </a>
      </li>
    
  

      
        
  
  
  
  
    
    
      <li class="md-tabs__item">
        <a href="../../../deepagents/" class="md-tabs__link">
          
  
  
    
  
  Deep Agents

        </a>
      </li>
    
  

      
        
  
  
  
  
    
    
      <li class="md-tabs__item">
        <a href="../../../integrations/" class="md-tabs__link">
          
  
  
    
  
  Integrations

        </a>
      </li>
    
  

      
        
  
  
  
    
  
  
    
    
      <li class="md-tabs__item md-tabs__item--active">
        <a href="../../" class="md-tabs__link">
          
  
  
    
  
  LangSmith

        </a>
      </li>
    
  

      
    </ul>
  </div>
</nav>
          
        
      
      <main class="md-main" data-md-component="main">
        <div class="md-main__inner md-grid">
          
            
              
              <div class="md-sidebar md-sidebar--primary" data-md-component="sidebar" data-md-type="navigation" >
                <div class="md-sidebar__scrollwrap">
                  <div class="md-sidebar__inner">
                    


  


<nav class="md-nav md-nav--primary md-nav--lifted" aria-label="Navigation" data-md-level="0">
  <label class="md-nav__title" for="__drawer">
    <a href="../../.." title="LangChain Reference" class="md-nav__button md-logo" aria-label="LangChain Reference" data-md-component="logo">
      
  <img src="../../../static/brand/reference-light.svg" alt="logo" class="logo-light" />
  <img src="../../../static/brand/reference-dark.svg" alt="logo" class="logo-dark" />

    </a>
    LangChain Reference
  </label>
  
    <div class="md-nav__source">
      <a href="https://github.com/langchain-ai/docs" title="Go to repository" class="md-source" data-md-component="source" target="_blank" rel="noopener">
  <div class="md-source__icon md-icon">
    
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Free 7.1.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2025 Fonticons, Inc.--><path d="M439.6 236.1 244 40.5c-5.4-5.5-12.8-8.5-20.4-8.5s-15 3-20.4 8.4L162.5 81l51.5 51.5c27.1-9.1 52.7 16.8 43.4 43.7l49.7 49.7c34.2-11.8 61.2 31 35.5 56.7-26.5 26.5-70.2-2.9-56-37.3L240.3 199v121.9c25.3 12.5 22.3 41.8 9.1 55-6.4 6.4-15.2 10.1-24.3 10.1s-17.8-3.6-24.3-10.1c-17.6-17.6-11.1-46.9 11.2-56v-123c-20.8-8.5-24.6-30.7-18.6-45L142.6 101 8.5 235.1C3 240.6 0 247.9 0 255.5s3 15 8.5 20.4l195.6 195.7c5.4 5.4 12.7 8.4 20.4 8.4s15-3 20.4-8.4l194.7-194.7c5.4-5.4 8.4-12.8 8.4-20.4s-3-15-8.4-20.4"/></svg>
  </div>
  <div class="md-source__repository">
    langchain-ai/docs
  </div>
</a>
    </div>
  
  <ul class="md-nav__list" data-md-scrollfix>
    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../.." class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Get started
  

    
  </span>
  
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
    
      
      
        
      
    
    
      
        
        
      
    
    <li class="md-nav__item md-nav__item--pruned md-nav__item--nested">
      
        
  
  
  
    <a href="../../../langchain/" class="md-nav__link">
      
  
  
  <span class="md-ellipsis">
    
  
    LangChain
  

    
  </span>
  
  

      
        <span class="md-nav__icon md-icon"></span>
      
    </a>
  

      
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
    
    
    
      
      
        
      
    
    
      
        
        
      
    
    <li class="md-nav__item md-nav__item--pruned md-nav__item--nested">
      
        
  
  
  
    <a href="../../../langgraph/" class="md-nav__link">
      
  
  
  <span class="md-ellipsis">
    
  
    LangGraph
  

    
  </span>
  
  

      
        <span class="md-nav__icon md-icon"></span>
      
    </a>
  

      
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
    
    
    
      
      
        
      
    
    
      
        
        
      
    
    <li class="md-nav__item md-nav__item--pruned md-nav__item--nested">
      
        
  
  
  
    <a href="../../../deepagents/" class="md-nav__link">
      
  
  
  <span class="md-ellipsis">
    
  
    Deep Agents
  

    
  </span>
  
  

      
        <span class="md-nav__icon md-icon"></span>
      
    </a>
  

      
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
    
    
    
      
      
        
      
    
    
      
        
        
      
    
    <li class="md-nav__item md-nav__item--pruned md-nav__item--nested">
      
        
  
  
  
    <a href="../../../integrations/" class="md-nav__link">
      
  
  
  <span class="md-ellipsis">
    
  
    Integrations
  

    
  </span>
  
  

      
        <span class="md-nav__icon md-icon"></span>
      
    </a>
  

      
    </li>
  

    
      
      
  
  
    
  
  
  
    
    
      
        
          
        
      
        
      
        
      
    
    
    
      
        
        
      
      
        
      
    
    
      
    
    <li class="md-nav__item md-nav__item--active md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6" checked>
        
          
          <div class="md-nav__link md-nav__container">
            <a href="../../" class="md-nav__link ">
              
  
  
  <span class="md-ellipsis">
    
  
    LangSmith
  

    
  </span>
  
  

            </a>
            
              
              <label class="md-nav__link " for="__nav_6" id="__nav_6_label" tabindex="">
                <span class="md-nav__icon md-icon"></span>
              </label>
            
          </div>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_6_label" aria-expanded="true">
          <label class="md-nav__title" for="__nav_6">
            <span class="md-nav__icon md-icon"></span>
            
  
    LangSmith
  

          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
            
              
                
  
  
  
  
    
    
      
        
      
    
    
    
      
      
        
          
          
        
      
    
    
      
    
    <li class="md-nav__item md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6_2" >
        
          
          <label class="md-nav__link" for="__nav_6_2" id="__nav_6_2_label" tabindex="">
            
  
  
  <span class="md-ellipsis">
    
  
    Observability & Evaluation
  

    
  </span>
  
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="2" aria-labelledby="__nav_6_2_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_6_2">
            <span class="md-nav__icon md-icon"></span>
            
  
    Observability & Evaluation
  

          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
    
    
    
      
      
        
      
    
    
      
        
        
      
    
    <li class="md-nav__item md-nav__item--pruned md-nav__item--nested">
      
        
  
  
  
    <a href="../../observability/sdk/" class="md-nav__link">
      
  
  
  <span class="md-ellipsis">
    
  
    SDK
  

    
  </span>
  
  

      
        <span class="md-nav__icon md-icon"></span>
      
    </a>
  

      
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

              
            
              
                
  
  
    
  
  
  
    
    
      
        
      
        
      
    
    
    
      
      
        
          
          
        
      
    
    
      
    
    <li class="md-nav__item md-nav__item--active md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6_3" checked>
        
          
          <label class="md-nav__link" for="__nav_6_3" id="__nav_6_3_label" tabindex="">
            
  
  
  <span class="md-ellipsis">
    
  
    Deployment
  

    
  </span>
  
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="2" aria-labelledby="__nav_6_3_label" aria-expanded="true">
          <label class="md-nav__title" for="__nav_6_3">
            <span class="md-nav__icon md-icon"></span>
            
  
    Deployment
  

          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../sdk/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    SDK
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
    
  
  
  
    <li class="md-nav__item md-nav__item--active">
      
      <input class="md-nav__toggle md-toggle" type="checkbox" id="__toc">
      
      
      
        <label class="md-nav__link md-nav__link--active" for="__toc">
          
  
  
  <span class="md-ellipsis">
    
  
    RemoteGraph
  

    
  </span>
  
  

          <span class="md-nav__icon md-icon"></span>
        </label>
      
      <a href="./" class="md-nav__link md-nav__link--active">
        
  
  
  <span class="md-ellipsis">
    
  
    RemoteGraph
  

    
  </span>
  
  

      </a>
      
        

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc" data-md-scrollfix>
      
        <li class="md-nav__item">
  <a href="#langgraph.pregel.remote" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-module"></code>&nbsp;remote
      
    </span>
  </a>
  
    <nav class="md-nav" aria-label=" remote">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-class"></code>&nbsp;RemoteGraph
      
    </span>
  </a>
  
    <nav class="md-nav" aria-label=" RemoteGraph">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.name" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-attribute"></code>&nbsp;name
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.InputType" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-attribute"></code>&nbsp;InputType
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.OutputType" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-attribute"></code>&nbsp;OutputType
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.input_schema" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-attribute"></code>&nbsp;input_schema
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.output_schema" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-attribute"></code>&nbsp;output_schema
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.config_specs" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-attribute"></code>&nbsp;config_specs
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;__init__
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.with_config" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;with_config
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.get_graph" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;get_graph
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.aget_graph" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;aget_graph
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.get_state" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;get_state
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.aget_state" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;aget_state
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.get_state_history" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;get_state_history
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.aget_state_history" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;aget_state_history
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.update_state" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;update_state
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.aupdate_state" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;aupdate_state
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.stream" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;stream
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.astream" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;astream
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.astream_events" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;astream_events
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.invoke" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;invoke
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.ainvoke" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;ainvoke
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.get_name" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;get_name
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.get_input_schema" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;get_input_schema
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.get_input_jsonschema" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;get_input_jsonschema
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.get_output_schema" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;get_output_schema
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.get_output_jsonschema" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;get_output_jsonschema
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.config_schema" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;config_schema
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.get_config_jsonschema" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;get_config_jsonschema
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.get_prompts" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;get_prompts
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.__or__" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;__or__
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.__ror__" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;__ror__
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.pipe" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;pipe
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.pick" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;pick
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.assign" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;assign
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.batch" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;batch
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.batch_as_completed" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;batch_as_completed
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.abatch" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;abatch
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.abatch_as_completed" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;abatch_as_completed
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.astream_log" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;astream_log
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.transform" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;transform
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.atransform" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;atransform
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.bind" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;bind
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.with_listeners" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;with_listeners
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.with_alisteners" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;with_alisteners
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.with_types" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;with_types
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.with_retry" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;with_retry
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.map" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;map
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.with_fallbacks" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;with_fallbacks
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.as_tool" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;as_tool
      
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
    </ul>
  
</nav>
      
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
  </ul>
</nav>
                  </div>
                </div>
              </div>
            
            
              
              <div class="md-sidebar md-sidebar--secondary" data-md-component="sidebar" data-md-type="toc" >
                <div class="md-sidebar__scrollwrap">
                  <div class="md-sidebar__inner">
                    

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc" data-md-scrollfix>
      
        <li class="md-nav__item">
  <a href="#langgraph.pregel.remote" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-module"></code>&nbsp;remote
      
    </span>
  </a>
  
    <nav class="md-nav" aria-label=" remote">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-class"></code>&nbsp;RemoteGraph
      
    </span>
  </a>
  
    <nav class="md-nav" aria-label=" RemoteGraph">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.name" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-attribute"></code>&nbsp;name
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.InputType" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-attribute"></code>&nbsp;InputType
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.OutputType" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-attribute"></code>&nbsp;OutputType
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.input_schema" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-attribute"></code>&nbsp;input_schema
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.output_schema" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-attribute"></code>&nbsp;output_schema
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.config_specs" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-attribute"></code>&nbsp;config_specs
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;__init__
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.with_config" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;with_config
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.get_graph" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;get_graph
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.aget_graph" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;aget_graph
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.get_state" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;get_state
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.aget_state" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;aget_state
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.get_state_history" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;get_state_history
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.aget_state_history" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;aget_state_history
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.update_state" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;update_state
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.aupdate_state" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;aupdate_state
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.stream" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;stream
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.astream" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;astream
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.astream_events" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;astream_events
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.invoke" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;invoke
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.ainvoke" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;ainvoke
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.get_name" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;get_name
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.get_input_schema" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;get_input_schema
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.get_input_jsonschema" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;get_input_jsonschema
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.get_output_schema" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;get_output_schema
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.get_output_jsonschema" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;get_output_jsonschema
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.config_schema" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;config_schema
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.get_config_jsonschema" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;get_config_jsonschema
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.get_prompts" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;get_prompts
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.__or__" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;__or__
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.__ror__" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;__ror__
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.pipe" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;pipe
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.pick" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;pick
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.assign" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;assign
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.batch" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;batch
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.batch_as_completed" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;batch_as_completed
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.abatch" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;abatch
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.abatch_as_completed" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;abatch_as_completed
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.astream_log" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;astream_log
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.transform" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;transform
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.atransform" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;atransform
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.bind" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;bind
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.with_listeners" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;with_listeners
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.with_alisteners" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;with_alisteners
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.with_types" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;with_types
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.with_retry" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;with_retry
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.map" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;map
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.with_fallbacks" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;with_fallbacks
      
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#langgraph.pregel.remote.RemoteGraph.as_tool" class="md-nav__link">
    <span class="md-ellipsis">
      
        <code class="doc-symbol doc-symbol-toc doc-symbol-method"></code>&nbsp;as_tool
      
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
    </ul>
  
</nav>
                  </div>
                </div>
              </div>
            
          
          
            <div class="md-content" data-md-component="content">
              
              <article class="md-content__inner md-typeset">
                
                  


  
    <a href="https://github.com/langchain-ai/docs/tree/main/reference/python/docs/langsmith/deployment/remote_graph.md" title="Edit this page" class="md-content__button md-icon" rel="edit noopener" target="_blank">
      
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M10 20H6V4h7v5h5v3.1l2-2V8l-6-6H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h4zm10.2-7c.1 0 .3.1.4.2l1.3 1.3c.2.2.2.6 0 .8l-1 1-2.1-2.1 1-1c.1-.1.2-.2.4-.2m0 3.9L14.1 23H12v-2.1l6.1-6.1z"/></svg>
    </a>
  
  


  <h1>RemoteGraph</h1>

<div class="doc doc-object doc-module">



<h2 id="langgraph.pregel.remote" class="doc doc-heading">
<code class="doc-symbol doc-symbol-heading doc-symbol-module"></code>            <span class="doc doc-object-name doc-module-name">remote</span>


<a href="#langgraph.pregel.remote" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h2>

    <div class="doc doc-contents first">

          










  <div class="doc doc-children">









<div class="doc doc-object doc-class">



<h3 id="langgraph.pregel.remote.RemoteGraph" class="doc doc-heading">
<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">RemoteGraph</span>


<a href="#langgraph.pregel.remote.RemoteGraph" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><span title="langgraph.pregel.protocol.PregelProtocol">PregelProtocol</span></code></p>



        <p>The <code>RemoteGraph</code> class is a client implementation for calling remote
APIs that implement the LangGraph Server API specification.</p>
<p>For example, the <code>RemoteGraph</code> class can be used to call APIs from deployments
on LangSmith Deployment.</p>
<p><code>RemoteGraph</code> behaves the same way as a <code>Graph</code> and can be used directly as
a node in another <code>Graph</code>.</p>

          








<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">METHOD</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;__init__&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.__init__&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.__init__">__init__</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Specify <code>url</code>, <code>api_key</code>, and/or <code>headers</code> to create default sync and async clients.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;with_config&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.with_config&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.with_config">with_config</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Bind config to a <code>Runnable</code>, returning a new <code>Runnable</code>.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;get_graph&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.get_graph&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.get_graph">get_graph</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Get graph by graph name.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;aget_graph&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-async&quot;&gt;&lt;code&gt;async&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.aget_graph&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.aget_graph">aget_graph</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Get graph by graph name.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;get_state&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.get_state&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.get_state">get_state</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Get the state of a thread.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;aget_state&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-async&quot;&gt;&lt;code&gt;async&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.aget_state&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.aget_state">aget_state</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Get the state of a thread.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;get_state_history&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.get_state_history&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.get_state_history">get_state_history</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Get the state history of a thread.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;aget_state_history&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-async&quot;&gt;&lt;code&gt;async&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.aget_state_history&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.aget_state_history">aget_state_history</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Get the state history of a thread.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;update_state&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.update_state&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.update_state">update_state</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Update the state of a thread.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;aupdate_state&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-async&quot;&gt;&lt;code&gt;async&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.aupdate_state&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.aupdate_state">aupdate_state</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Update the state of a thread.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;stream&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.stream&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.stream">stream</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Create a run and stream the results.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;astream&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-async&quot;&gt;&lt;code&gt;async&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.astream&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.astream">astream</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Create a run and stream the results.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;astream_events&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-async&quot;&gt;&lt;code&gt;async&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.astream_events&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.astream_events">astream_events</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Generate a stream of events.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;invoke&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.invoke&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.invoke">invoke</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Create a run, wait until it finishes and return the final state.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;ainvoke&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-async&quot;&gt;&lt;code&gt;async&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.ainvoke&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.ainvoke">ainvoke</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Create a run, wait until it finishes and return the final state.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;get_name&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.get_name&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.get_name">get_name</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Get the name of the <code>Runnable</code>.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;get_input_schema&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.get_input_schema&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.get_input_schema">get_input_schema</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Get a Pydantic model that can be used to validate input to the <code>Runnable</code>.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;get_input_jsonschema&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.get_input_jsonschema&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.get_input_jsonschema">get_input_jsonschema</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Get a JSON schema that represents the input to the <code>Runnable</code>.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;get_output_schema&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.get_output_schema&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.get_output_schema">get_output_schema</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Get a Pydantic model that can be used to validate output to the <code>Runnable</code>.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;get_output_jsonschema&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.get_output_jsonschema&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.get_output_jsonschema">get_output_jsonschema</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Get a JSON schema that represents the output of the <code>Runnable</code>.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;config_schema&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.config_schema&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.config_schema">config_schema</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>The type of config this <code>Runnable</code> accepts specified as a Pydantic model.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;get_config_jsonschema&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.get_config_jsonschema&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.get_config_jsonschema">get_config_jsonschema</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Get a JSON schema that represents the config of the <code>Runnable</code>.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;get_prompts&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.get_prompts&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.get_prompts">get_prompts</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Return a list of prompts used by this <code>Runnable</code>.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;__or__&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.__or__&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.__or__">__or__</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Runnable "or" operator.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;__ror__&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.__ror__&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.__ror__">__ror__</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Runnable "reverse-or" operator.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;pipe&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.pipe&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.pipe">pipe</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Pipe <code>Runnable</code> objects.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;pick&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.pick&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.pick">pick</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Pick keys from the output <code>dict</code> of this <code>Runnable</code>.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;assign&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.assign&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.assign">assign</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Assigns new fields to the <code>dict</code> output of this <code>Runnable</code>.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;batch&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.batch&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.batch">batch</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Default implementation runs invoke in parallel using a thread pool executor.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;batch_as_completed&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.batch_as_completed&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.batch_as_completed">batch_as_completed</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Run <code>invoke</code> in parallel on a list of inputs.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;abatch&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-async&quot;&gt;&lt;code&gt;async&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.abatch&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.abatch">abatch</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Default implementation runs <code>ainvoke</code> in parallel using <code>asyncio.gather</code>.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;abatch_as_completed&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-async&quot;&gt;&lt;code&gt;async&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.abatch_as_completed&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.abatch_as_completed">abatch_as_completed</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Run <code>ainvoke</code> in parallel on a list of inputs.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;astream_log&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-async&quot;&gt;&lt;code&gt;async&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.astream_log&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.astream_log">astream_log</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Stream all output from a <code>Runnable</code>, as reported to the callback system.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;transform&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.transform&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.transform">transform</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Transform inputs to outputs.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;atransform&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-async&quot;&gt;&lt;code&gt;async&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.atransform&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.atransform">atransform</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Transform inputs to outputs.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;bind&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.bind&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.bind">bind</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Bind arguments to a <code>Runnable</code>, returning a new <code>Runnable</code>.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;with_listeners&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.with_listeners&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.with_listeners">with_listeners</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Bind lifecycle listeners to a <code>Runnable</code>, returning a new <code>Runnable</code>.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;with_alisteners&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.with_alisteners&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.with_alisteners">with_alisteners</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Bind async lifecycle listeners to a <code>Runnable</code>.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;with_types&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.with_types&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.with_types">with_types</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Bind input and output types to a <code>Runnable</code>, returning a new <code>Runnable</code>.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;with_retry&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.with_retry&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.with_retry">with_retry</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Create a new <code>Runnable</code> that retries the original <code>Runnable</code> on exceptions.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;map&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.map&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.map">map</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Return a new <code>Runnable</code> that maps a list of inputs to a list of outputs.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;with_fallbacks&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.with_fallbacks&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.with_fallbacks">with_fallbacks</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Add fallbacks to a <code>Runnable</code>, returning a new <code>Runnable</code>.</p>
                </div>
              </td>
            </tr>
            <tr class="doc-section-item">
              <td><code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-method&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-function-name&quot;&gt;as_tool&lt;/span&gt; (&lt;code&gt;langgraph.pregel.remote.RemoteGraph.as_tool&lt;/code&gt;)" href="#langgraph.pregel.remote.RemoteGraph.as_tool">as_tool</a></code></td>
              <td class="doc-function-details">
                <div class="doc-md-description">
                  <p>Create a <code>BaseTool</code> from a <code>Runnable</code>.</p>
                </div>
              </td>
            </tr>
      </tbody>
    </table>





  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="langgraph.pregel.remote.RemoteGraph.name" class="doc doc-heading">
<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">name</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

<a href="#langgraph.pregel.remote.RemoteGraph.name" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="n">name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span> <span class="o">|</span> <span class="kc">None</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>The name of the <code>Runnable</code>. Used for debugging and tracing.</p>

          
    </div>

</div>

<div class="doc doc-object doc-attribute">



<h4 id="langgraph.pregel.remote.RemoteGraph.InputType" class="doc doc-heading">
<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">InputType</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

<a href="#langgraph.pregel.remote.RemoteGraph.InputType" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="n">InputType</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type" target="_blank" rel="noopener">type</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.utils.Input">Input</span></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Input type.</p>
<p>The type of input this <code>Runnable</code> accepts specified as a type annotation.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RAISES</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
              <span class="doc-raises-annotation">
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/exceptions.html#TypeError" target="_blank" rel="noopener">TypeError</a></code>
              </span>
            </td>
            <td class="doc-raises-details">
              <div class="doc-md-description">
                <p>If the input type cannot be inferred.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

          
    </div>

</div>

<div class="doc doc-object doc-attribute">



<h4 id="langgraph.pregel.remote.RemoteGraph.OutputType" class="doc doc-heading">
<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">OutputType</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

<a href="#langgraph.pregel.remote.RemoteGraph.OutputType" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="n">OutputType</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type" target="_blank" rel="noopener">type</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.utils.Output">Output</span></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Output Type.</p>
<p>The type of output this <code>Runnable</code> produces specified as a type annotation.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RAISES</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
              <span class="doc-raises-annotation">
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/exceptions.html#TypeError" target="_blank" rel="noopener">TypeError</a></code>
              </span>
            </td>
            <td class="doc-raises-details">
              <div class="doc-md-description">
                <p>If the output type cannot be inferred.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

          
    </div>

</div>

<div class="doc doc-object doc-attribute">



<h4 id="langgraph.pregel.remote.RemoteGraph.input_schema" class="doc doc-heading">
<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">input_schema</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

<a href="#langgraph.pregel.remote.RemoteGraph.input_schema" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="n">input_schema</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type" target="_blank" rel="noopener">type</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;pydantic.BaseModel&lt;/code&gt;" href="https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel" target="_blank" rel="noopener">BaseModel</a></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>The type of input this <code>Runnable</code> accepts specified as a Pydantic model.</p>

          
    </div>

</div>

<div class="doc doc-object doc-attribute">



<h4 id="langgraph.pregel.remote.RemoteGraph.output_schema" class="doc doc-heading">
<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">output_schema</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

<a href="#langgraph.pregel.remote.RemoteGraph.output_schema" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="n">output_schema</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type" target="_blank" rel="noopener">type</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;pydantic.BaseModel&lt;/code&gt;" href="https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel" target="_blank" rel="noopener">BaseModel</a></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Output schema.</p>
<p>The type of output this <code>Runnable</code> produces specified as a Pydantic model.</p>

          
    </div>

</div>

<div class="doc doc-object doc-attribute">



<h4 id="langgraph.pregel.remote.RemoteGraph.config_specs" class="doc doc-heading">
<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">config_specs</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

<a href="#langgraph.pregel.remote.RemoteGraph.config_specs" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="n">config_specs</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list" target="_blank" rel="noopener">list</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.utils.ConfigurableFieldSpec">ConfigurableFieldSpec</span></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>List configurable fields for this <code>Runnable</code>.</p>

          
    </div>

</div>


  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.__init__" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">__init__</span>


<a href="#langgraph.pregel.remote.RemoteGraph.__init__" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">__init__</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="n">assistant_id</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>    <span class="o">/</span><span class="p">,</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>    <span class="o">*</span><span class="p">,</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="n">url</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>    <span class="n">api_key</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a>    <span class="n">headers</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-8"><a id="__codelineno-0-8" name="__codelineno-0-8" href="#__codelineno-0-8"></a>    <span class="n">client</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;LangGraphClient&lt;/span&gt; (&lt;code&gt;langgraph_sdk.client.LangGraphClient&lt;/code&gt;)" href="../sdk/#langgraph_sdk.client.LangGraphClient">LangGraphClient</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-9"><a id="__codelineno-0-9" name="__codelineno-0-9" href="#__codelineno-0-9"></a>    <span class="n">sync_client</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;SyncLangGraphClient&lt;/span&gt; (&lt;code&gt;langgraph_sdk.client.SyncLangGraphClient&lt;/code&gt;)" href="../sdk/#langgraph_sdk.client.SyncLangGraphClient">SyncLangGraphClient</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-10"><a id="__codelineno-0-10" name="__codelineno-0-10" href="#__codelineno-0-10"></a>    <span class="n">config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-11"><a id="__codelineno-0-11" name="__codelineno-0-11" href="#__codelineno-0-11"></a>    <span class="n">name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-12"><a id="__codelineno-0-12" name="__codelineno-0-12" href="#__codelineno-0-12"></a>    <span class="n">distributed_tracing</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool" target="_blank" rel="noopener">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
</span><span id="__span-0-13"><a id="__codelineno-0-13" name="__codelineno-0-13" href="#__codelineno-0-13"></a><span class="p">)</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Specify <code>url</code>, <code>api_key</code>, and/or <code>headers</code> to create default sync and async clients.</p>
<p>If <code>client</code> or <code>sync_client</code> are provided, they will be used instead of the default clients.
See <code>LangGraphClient</code> and <code>SyncLangGraphClient</code> for details on the default clients. At least
one of <code>url</code>, <code>client</code>, or <code>sync_client</code> must be provided.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>assistant_id</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>The assistant ID or graph name of the remote graph to use.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>url</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>The URL of the remote API.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>api_key</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>The API key to use for authentication. If not provided, it will be read from the environment (<code>LANGGRAPH_API_KEY</code>, <code>LANGSMITH_API_KEY</code>, or <code>LANGCHAIN_API_KEY</code>).</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>headers</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Additional headers to include in the requests.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>client</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A <code>LangGraphClient</code> instance to use instead of creating a default client.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;LangGraphClient&lt;/span&gt; (&lt;code&gt;langgraph_sdk.client.LangGraphClient&lt;/code&gt;)" href="../sdk/#langgraph_sdk.client.LangGraphClient">LangGraphClient</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>sync_client</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A <code>SyncLangGraphClient</code> instance to use instead of creating a default client.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;SyncLangGraphClient&lt;/span&gt; (&lt;code&gt;langgraph_sdk.client.SyncLangGraphClient&lt;/code&gt;)" href="../sdk/#langgraph_sdk.client.SyncLangGraphClient">SyncLangGraphClient</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>config</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>An optional <code>RunnableConfig</code> instance with additional configuration.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>name</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Human-readable name to attach to the RemoteGraph instance.
This is useful for adding <code>RemoteGraph</code> as a subgraph via <code>graph.add_node(remote_graph)</code>.
If not provided, defaults to the assistant ID.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>distributed_tracing</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Whether to enable sending LangSmith distributed tracing headers.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool" target="_blank" rel="noopener">bool</a></code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>False</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.with_config" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">with_config</span>


<a href="#langgraph.pregel.remote.RemoteGraph.with_config" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">with_config</span><span class="p">(</span><span class="n">config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing_extensions.Self&lt;/code&gt;" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self" target="_blank" rel="noopener">Self</a></span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Bind config to a <code>Runnable</code>, returning a new <code>Runnable</code>.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>config</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>The config to bind to the <code>Runnable</code>.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>**kwargs</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Additional keyword arguments to pass to the <code>Runnable</code>.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>{}</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a>[<span title="langchain_core.runnables.utils.Input">Input</span>, <span title="langchain_core.runnables.utils.Output">Output</span>]</code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>A new <code>Runnable</code> with the config bound.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.get_graph" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">get_graph</span>


<a href="#langgraph.pregel.remote.RemoteGraph.get_graph" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">get_graph</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="n">config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>    <span class="o">*</span><span class="p">,</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>    <span class="n">xray</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int" target="_blank" rel="noopener">int</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool" target="_blank" rel="noopener">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="n">headers</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>    <span class="n">params</span><span class="p">:</span> <span class="n"><span title="langgraph_sdk.schema.QueryParamTypes">QueryParamTypes</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><span title="langchain_core.runnables.graph.Graph">Graph</span></span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Get graph by graph name.</p>
<p>This method calls <code>GET /assistants/{assistant_id}/graph</code>.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>config</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>This parameter is not used.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>xray</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Include graph representation of subgraphs. If an integer
value is provided, only subgraphs with a depth less than or
equal to the value will be included.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int" target="_blank" rel="noopener">int</a> | <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool" target="_blank" rel="noopener">bool</a></code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>False</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><span title="langchain_core.runnables.graph.Graph">Graph</span></code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>The graph information for the assistant in JSON format.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.aget_graph" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">aget_graph</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

<a href="#langgraph.pregel.remote.RemoteGraph.aget_graph" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">aget_graph</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="n">config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>    <span class="o">*</span><span class="p">,</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>    <span class="n">xray</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int" target="_blank" rel="noopener">int</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool" target="_blank" rel="noopener">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="n">headers</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>    <span class="n">params</span><span class="p">:</span> <span class="n"><span title="langgraph_sdk.schema.QueryParamTypes">QueryParamTypes</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><span title="langchain_core.runnables.graph.Graph">Graph</span></span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Get graph by graph name.</p>
<p>This method calls <code>GET /assistants/{assistant_id}/graph</code>.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>config</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>This parameter is not used.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>xray</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Include graph representation of subgraphs. If an integer
value is provided, only subgraphs with a depth less than or
equal to the value will be included.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int" target="_blank" rel="noopener">int</a> | <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool" target="_blank" rel="noopener">bool</a></code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>False</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><span title="langchain_core.runnables.graph.Graph">Graph</span></code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>The graph information for the assistant in JSON format.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.get_state" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">get_state</span>


<a href="#langgraph.pregel.remote.RemoteGraph.get_state" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">get_state</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="n">config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span><span class="p">,</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>    <span class="o">*</span><span class="p">,</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>    <span class="n">subgraphs</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool" target="_blank" rel="noopener">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="n">headers</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>    <span class="n">params</span><span class="p">:</span> <span class="n"><span title="langgraph_sdk.schema.QueryParamTypes">QueryParamTypes</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;StateSnapshot&lt;/span&gt; (&lt;code&gt;langgraph.types.StateSnapshot&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.StateSnapshot">StateSnapshot</a></span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Get the state of a thread.</p>
<p>This method calls <code>POST /threads/{thread_id}/state/checkpoint</code> if a
checkpoint is specified in the config or <code>GET /threads/{thread_id}/state</code>
if no checkpoint is specified.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>config</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A <code>RunnableConfig</code> that includes <code>thread_id</code> in the
<code>configurable</code> field.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>subgraphs</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Include subgraphs in the state.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool" target="_blank" rel="noopener">bool</a></code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>False</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>headers</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Optional custom headers to include with the request.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>params</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Optional query parameters to include with the request.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><span title="langgraph_sdk.schema.QueryParamTypes">QueryParamTypes</span> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;StateSnapshot&lt;/span&gt; (&lt;code&gt;langgraph.types.StateSnapshot&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.StateSnapshot">StateSnapshot</a></code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>The latest state of the thread.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.aget_state" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">aget_state</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

<a href="#langgraph.pregel.remote.RemoteGraph.aget_state" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">aget_state</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="n">config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span><span class="p">,</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>    <span class="o">*</span><span class="p">,</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>    <span class="n">subgraphs</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool" target="_blank" rel="noopener">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="n">headers</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>    <span class="n">params</span><span class="p">:</span> <span class="n"><span title="langgraph_sdk.schema.QueryParamTypes">QueryParamTypes</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;StateSnapshot&lt;/span&gt; (&lt;code&gt;langgraph.types.StateSnapshot&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.StateSnapshot">StateSnapshot</a></span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Get the state of a thread.</p>
<p>This method calls <code>POST /threads/{thread_id}/state/checkpoint</code> if a
checkpoint is specified in the config or <code>GET /threads/{thread_id}/state</code>
if no checkpoint is specified.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>config</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A <code>RunnableConfig</code> that includes <code>thread_id</code> in the
<code>configurable</code> field.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>subgraphs</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Include subgraphs in the state.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool" target="_blank" rel="noopener">bool</a></code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>False</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>headers</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Optional custom headers to include with the request.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>params</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Optional query parameters to include with the request.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><span title="langgraph_sdk.schema.QueryParamTypes">QueryParamTypes</span> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;StateSnapshot&lt;/span&gt; (&lt;code&gt;langgraph.types.StateSnapshot&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.StateSnapshot">StateSnapshot</a></code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>The latest state of the thread.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.get_state_history" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">get_state_history</span>


<a href="#langgraph.pregel.remote.RemoteGraph.get_state_history" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">get_state_history</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="n">config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span><span class="p">,</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>    <span class="o">*</span><span class="p">,</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>    <span class="nb">filter</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="n">before</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>    <span class="n">limit</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int" target="_blank" rel="noopener">int</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a>    <span class="n">headers</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-8"><a id="__codelineno-0-8" name="__codelineno-0-8" href="#__codelineno-0-8"></a>    <span class="n">params</span><span class="p">:</span> <span class="n"><span title="langgraph_sdk.schema.QueryParamTypes">QueryParamTypes</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-9"><a id="__codelineno-0-9" name="__codelineno-0-9" href="#__codelineno-0-9"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Iterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator" target="_blank" rel="noopener">Iterator</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;StateSnapshot&lt;/span&gt; (&lt;code&gt;langgraph.types.StateSnapshot&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.StateSnapshot">StateSnapshot</a></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Get the state history of a thread.</p>
<p>This method calls <code>POST /threads/{thread_id}/history</code>.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>config</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A <code>RunnableConfig</code> that includes <code>thread_id</code> in the
<code>configurable</code> field.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>filter</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Metadata to filter on.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>before</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A <code>RunnableConfig</code> that includes checkpoint metadata.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>limit</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Max number of states to return.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int" target="_blank" rel="noopener">int</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Iterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator" target="_blank" rel="noopener">Iterator</a>[<a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;StateSnapshot&lt;/span&gt; (&lt;code&gt;langgraph.types.StateSnapshot&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.StateSnapshot">StateSnapshot</a>]</code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>States of the thread.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.aget_state_history" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">aget_state_history</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

<a href="#langgraph.pregel.remote.RemoteGraph.aget_state_history" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">aget_state_history</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="n">config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span><span class="p">,</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>    <span class="o">*</span><span class="p">,</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>    <span class="nb">filter</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="n">before</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>    <span class="n">limit</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int" target="_blank" rel="noopener">int</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a>    <span class="n">headers</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-8"><a id="__codelineno-0-8" name="__codelineno-0-8" href="#__codelineno-0-8"></a>    <span class="n">params</span><span class="p">:</span> <span class="n"><span title="langgraph_sdk.schema.QueryParamTypes">QueryParamTypes</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-9"><a id="__codelineno-0-9" name="__codelineno-0-9" href="#__codelineno-0-9"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.AsyncIterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator" target="_blank" rel="noopener">AsyncIterator</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;StateSnapshot&lt;/span&gt; (&lt;code&gt;langgraph.types.StateSnapshot&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.StateSnapshot">StateSnapshot</a></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Get the state history of a thread.</p>
<p>This method calls <code>POST /threads/{thread_id}/history</code>.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>config</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A <code>RunnableConfig</code> that includes <code>thread_id</code> in the
<code>configurable</code> field.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>filter</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Metadata to filter on.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>before</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A <code>RunnableConfig</code> that includes checkpoint metadata.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>limit</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Max number of states to return.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int" target="_blank" rel="noopener">int</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>headers</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Optional custom headers to include with the request.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>params</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Optional query parameters to include with the request.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><span title="langgraph_sdk.schema.QueryParamTypes">QueryParamTypes</span> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.AsyncIterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator" target="_blank" rel="noopener">AsyncIterator</a>[<a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;StateSnapshot&lt;/span&gt; (&lt;code&gt;langgraph.types.StateSnapshot&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.StateSnapshot">StateSnapshot</a>]</code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>States of the thread.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.update_state" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">update_state</span>


<a href="#langgraph.pregel.remote.RemoteGraph.update_state" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">update_state</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="n">config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span><span class="p">,</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>    <span class="n">values</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>    <span class="n">as_node</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="o">*</span><span class="p">,</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>    <span class="n">headers</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a>    <span class="n">params</span><span class="p">:</span> <span class="n"><span title="langgraph_sdk.schema.QueryParamTypes">QueryParamTypes</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-8"><a id="__codelineno-0-8" name="__codelineno-0-8" href="#__codelineno-0-8"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Update the state of a thread.</p>
<p>This method calls <code>POST /threads/{thread_id}/state</code>.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>config</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A <code>RunnableConfig</code> that includes <code>thread_id</code> in the
<code>configurable</code> field.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>values</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Values to update to the state.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>] | <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a> | None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>as_node</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Update the state as if this node had just executed.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p><code>RunnableConfig</code> for the updated thread.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.aupdate_state" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">aupdate_state</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

<a href="#langgraph.pregel.remote.RemoteGraph.aupdate_state" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">aupdate_state</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="n">config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span><span class="p">,</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>    <span class="n">values</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>    <span class="n">as_node</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="o">*</span><span class="p">,</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>    <span class="n">headers</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a>    <span class="n">params</span><span class="p">:</span> <span class="n"><span title="langgraph_sdk.schema.QueryParamTypes">QueryParamTypes</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-8"><a id="__codelineno-0-8" name="__codelineno-0-8" href="#__codelineno-0-8"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Update the state of a thread.</p>
<p>This method calls <code>POST /threads/{thread_id}/state</code>.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>config</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A <code>RunnableConfig</code> that includes <code>thread_id</code> in the
<code>configurable</code> field.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>values</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Values to update to the state.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>] | <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a> | None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>as_node</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Update the state as if this node had just executed.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p><code>RunnableConfig</code> for the updated thread.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.stream" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">stream</span>


<a href="#langgraph.pregel.remote.RemoteGraph.stream" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">stream</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="nb">input</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">,</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>    <span class="n">config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>    <span class="o">*</span><span class="p">,</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="n">stream_mode</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;StreamMode&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.StreamMode&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.StreamMode">StreamMode</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list" target="_blank" rel="noopener">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;StreamMode&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.StreamMode&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.StreamMode">StreamMode</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>    <span class="n">interrupt_before</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;All&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.All&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.All">All</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a>    <span class="n">interrupt_after</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;All&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.All&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.All">All</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-8"><a id="__codelineno-0-8" name="__codelineno-0-8" href="#__codelineno-0-8"></a>    <span class="n">subgraphs</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool" target="_blank" rel="noopener">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
</span><span id="__span-0-9"><a id="__codelineno-0-9" name="__codelineno-0-9" href="#__codelineno-0-9"></a>    <span class="n">headers</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-10"><a id="__codelineno-0-10" name="__codelineno-0-10" href="#__codelineno-0-10"></a>    <span class="n">params</span><span class="p">:</span> <span class="n"><span title="langgraph_sdk.schema.QueryParamTypes">QueryParamTypes</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-11"><a id="__codelineno-0-11" name="__codelineno-0-11" href="#__codelineno-0-11"></a>    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">,</span>
</span><span id="__span-0-12"><a id="__codelineno-0-12" name="__codelineno-0-12" href="#__codelineno-0-12"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Iterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator" target="_blank" rel="noopener">Iterator</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Create a run and stream the results.</p>
<p>This method calls <code>POST /threads/{thread_id}/runs/stream</code> if a <code>thread_id</code>
is speciffed in the <code>configurable</code> field of the config or
<code>POST /runs/stream</code> otherwise.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>input</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Input to the graph.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>] | <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>config</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A <code>RunnableConfig</code> for graph invocation.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>stream_mode</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Stream mode(s) to use.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;StreamMode&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.StreamMode&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.StreamMode">StreamMode</a> | <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list" target="_blank" rel="noopener">list</a>[<a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;StreamMode&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.StreamMode&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.StreamMode">StreamMode</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>interrupt_before</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Interrupt the graph before these nodes.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;All&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.All&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.All">All</a> | <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>interrupt_after</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Interrupt the graph after these nodes.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;All&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.All&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.All">All</a> | <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>subgraphs</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Stream from subgraphs.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool" target="_blank" rel="noopener">bool</a></code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>False</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>headers</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Additional headers to pass to the request.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>**kwargs</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Additional params to pass to client.runs.stream.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>{}</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">YIELDS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-yields-annotation">
                    <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>] | <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></code>
                </span>
            </td>
            <td class="doc-yields-details">
              <div class="doc-md-description">
                <p>The output of the graph.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.astream" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">astream</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

<a href="#langgraph.pregel.remote.RemoteGraph.astream" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">astream</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="nb">input</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">,</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>    <span class="n">config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>    <span class="o">*</span><span class="p">,</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="n">stream_mode</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;StreamMode&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.StreamMode&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.StreamMode">StreamMode</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list" target="_blank" rel="noopener">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;StreamMode&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.StreamMode&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.StreamMode">StreamMode</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>    <span class="n">interrupt_before</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;All&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.All&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.All">All</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a>    <span class="n">interrupt_after</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;All&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.All&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.All">All</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-8"><a id="__codelineno-0-8" name="__codelineno-0-8" href="#__codelineno-0-8"></a>    <span class="n">subgraphs</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool" target="_blank" rel="noopener">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
</span><span id="__span-0-9"><a id="__codelineno-0-9" name="__codelineno-0-9" href="#__codelineno-0-9"></a>    <span class="n">headers</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-10"><a id="__codelineno-0-10" name="__codelineno-0-10" href="#__codelineno-0-10"></a>    <span class="n">params</span><span class="p">:</span> <span class="n"><span title="langgraph_sdk.schema.QueryParamTypes">QueryParamTypes</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-11"><a id="__codelineno-0-11" name="__codelineno-0-11" href="#__codelineno-0-11"></a>    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">,</span>
</span><span id="__span-0-12"><a id="__codelineno-0-12" name="__codelineno-0-12" href="#__codelineno-0-12"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.AsyncIterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator" target="_blank" rel="noopener">AsyncIterator</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Create a run and stream the results.</p>
<p>This method calls <code>POST /threads/{thread_id}/runs/stream</code> if a <code>thread_id</code>
is speciffed in the <code>configurable</code> field of the config or
<code>POST /runs/stream</code> otherwise.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>input</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Input to the graph.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>] | <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>config</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A <code>RunnableConfig</code> for graph invocation.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>stream_mode</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Stream mode(s) to use.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;StreamMode&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.StreamMode&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.StreamMode">StreamMode</a> | <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list" target="_blank" rel="noopener">list</a>[<a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;StreamMode&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.StreamMode&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.StreamMode">StreamMode</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>interrupt_before</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Interrupt the graph before these nodes.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;All&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.All&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.All">All</a> | <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>interrupt_after</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Interrupt the graph after these nodes.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;All&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.All&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.All">All</a> | <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>subgraphs</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Stream from subgraphs.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool" target="_blank" rel="noopener">bool</a></code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>False</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>headers</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Additional headers to pass to the request.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>**kwargs</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Additional params to pass to client.runs.stream.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>{}</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">YIELDS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-yields-annotation">
                    <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.AsyncIterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator" target="_blank" rel="noopener">AsyncIterator</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>] | <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>]</code>
                </span>
            </td>
            <td class="doc-yields-details">
              <div class="doc-md-description">
                <p>The output of the graph.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.astream_events" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">astream_events</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

<a href="#langgraph.pregel.remote.RemoteGraph.astream_events" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">astream_events</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="nb">input</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">,</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>    <span class="n">config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>    <span class="o">*</span><span class="p">,</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="n">version</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Literal&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Literal" target="_blank" rel="noopener">Literal</a></span><span class="p">[</span><span class="s2">&quot;v1&quot;</span><span class="p">,</span> <span class="s2">&quot;v2&quot;</span><span class="p">],</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>    <span class="n">include_names</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;All&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.All&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.All">All</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a>    <span class="n">include_types</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;All&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.All&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.All">All</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-8"><a id="__codelineno-0-8" name="__codelineno-0-8" href="#__codelineno-0-8"></a>    <span class="n">include_tags</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;All&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.All&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.All">All</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-9"><a id="__codelineno-0-9" name="__codelineno-0-9" href="#__codelineno-0-9"></a>    <span class="n">exclude_names</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;All&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.All&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.All">All</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-10"><a id="__codelineno-0-10" name="__codelineno-0-10" href="#__codelineno-0-10"></a>    <span class="n">exclude_types</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;All&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.All&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.All">All</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-11"><a id="__codelineno-0-11" name="__codelineno-0-11" href="#__codelineno-0-11"></a>    <span class="n">exclude_tags</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;All&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.All&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.All">All</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-12"><a id="__codelineno-0-12" name="__codelineno-0-12" href="#__codelineno-0-12"></a>    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">,</span>
</span><span id="__span-0-13"><a id="__codelineno-0-13" name="__codelineno-0-13" href="#__codelineno-0-13"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.AsyncIterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator" target="_blank" rel="noopener">AsyncIterator</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Generate a stream of events.</p>
<p>Use to create an iterator over <code>StreamEvent</code> that provide real-time information
about the progress of the <code>Runnable</code>, including <code>StreamEvent</code> from intermediate
results.</p>
<p>A <code>StreamEvent</code> is a dictionary with the following schema:</p>
<ul>
<li><code>event</code>: Event names are of the format:
    <code>on_[runnable_type]_(start|stream|end)</code>.</li>
<li><code>name</code>: The name of the <code>Runnable</code> that generated the event.</li>
<li><code>run_id</code>: Randomly generated ID associated with the given execution of the
    <code>Runnable</code> that emitted the event. A child <code>Runnable</code> that gets invoked as
    part of the execution of a parent <code>Runnable</code> is assigned its own unique ID.</li>
<li><code>parent_ids</code>: The IDs of the parent runnables that generated the event. The
    root <code>Runnable</code> will have an empty list. The order of the parent IDs is from
    the root to the immediate parent. Only available for v2 version of the API.
    The v1 version of the API will return an empty list.</li>
<li><code>tags</code>: The tags of the <code>Runnable</code> that generated the event.</li>
<li><code>metadata</code>: The metadata of the <code>Runnable</code> that generated the event.</li>
<li><code>data</code>: The data associated with the event. The contents of this field
    depend on the type of event. See the table below for more details.</li>
</ul>
<p>Below is a table that illustrates some events that might be emitted by various
chains. Metadata fields have been omitted from the table for brevity.
Chain definitions have been included after the table.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This reference table is for the v2 version of the schema.</p>
</div>
<table>
<thead>
<tr>
<th>event</th>
<th>name</th>
<th>chunk</th>
<th>input</th>
<th>output</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>on_chat_model_start</code></td>
<td><code>'[model name]'</code></td>
<td></td>
<td><code>{"messages": [[SystemMessage, HumanMessage]]}</code></td>
<td></td>
</tr>
<tr>
<td><code>on_chat_model_stream</code></td>
<td><code>'[model name]'</code></td>
<td><code>AIMessageChunk(content="hello")</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td><code>on_chat_model_end</code></td>
<td><code>'[model name]'</code></td>
<td></td>
<td><code>{"messages": [[SystemMessage, HumanMessage]]}</code></td>
<td><code>AIMessageChunk(content="hello world")</code></td>
</tr>
<tr>
<td><code>on_llm_start</code></td>
<td><code>'[model name]'</code></td>
<td></td>
<td><code>{'input': 'hello'}</code></td>
<td></td>
</tr>
<tr>
<td><code>on_llm_stream</code></td>
<td><code>'[model name]'</code></td>
<td><code>'Hello'</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td><code>on_llm_end</code></td>
<td><code>'[model name]'</code></td>
<td></td>
<td><code>'Hello human!'</code></td>
<td></td>
</tr>
<tr>
<td><code>on_chain_start</code></td>
<td><code>'format_docs'</code></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><code>on_chain_stream</code></td>
<td><code>'format_docs'</code></td>
<td><code>'hello world!, goodbye world!'</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td><code>on_chain_end</code></td>
<td><code>'format_docs'</code></td>
<td></td>
<td><code>[Document(...)]</code></td>
<td><code>'hello world!, goodbye world!'</code></td>
</tr>
<tr>
<td><code>on_tool_start</code></td>
<td><code>'some_tool'</code></td>
<td></td>
<td><code>{"x": 1, "y": "2"}</code></td>
<td></td>
</tr>
<tr>
<td><code>on_tool_end</code></td>
<td><code>'some_tool'</code></td>
<td></td>
<td></td>
<td><code>{"x": 1, "y": "2"}</code></td>
</tr>
<tr>
<td><code>on_retriever_start</code></td>
<td><code>'[retriever name]'</code></td>
<td></td>
<td><code>{"query": "hello"}</code></td>
<td></td>
</tr>
<tr>
<td><code>on_retriever_end</code></td>
<td><code>'[retriever name]'</code></td>
<td></td>
<td><code>{"query": "hello"}</code></td>
<td><code>[Document(...), ..]</code></td>
</tr>
<tr>
<td><code>on_prompt_start</code></td>
<td><code>'[template_name]'</code></td>
<td></td>
<td><code>{"question": "hello"}</code></td>
<td></td>
</tr>
<tr>
<td><code>on_prompt_end</code></td>
<td><code>'[template_name]'</code></td>
<td></td>
<td><code>{"question": "hello"}</code></td>
<td><code>ChatPromptValue(messages: [SystemMessage, ...])</code></td>
</tr>
</tbody>
</table>
<p>In addition to the standard events, users can also dispatch custom events (see example below).</p>
<p>Custom events will be only be surfaced with in the v2 version of the API!</p>
<p>A custom event has following format:</p>
<table>
<thead>
<tr>
<th>Attribute</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>name</code></td>
<td><code>str</code></td>
<td>A user defined name for the event.</td>
</tr>
<tr>
<td><code>data</code></td>
<td><code>Any</code></td>
<td>The data associated with the event. This can be anything, though we suggest making it JSON serializable.</td>
</tr>
</tbody>
</table>
<p>Here are declarations associated with the standard events shown above:</p>
<p><code>format_docs</code>:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="k">def</span><span class="w"> </span><span class="nf">format_docs</span><span class="p">(</span><span class="n">docs</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">Document</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a><span class="w">    </span><span class="sd">&#39;&#39;&#39;Format the docs.&#39;&#39;&#39;</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>    <span class="k">return</span> <span class="s2">&quot;, &quot;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">doc</span><span class="o">.</span><span class="n">page_content</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">docs</span><span class="p">])</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a><span class="n">format_docs</span> <span class="o">=</span> <span class="n">RunnableLambda</span><span class="p">(</span><span class="n">format_docs</span><span class="p">)</span>
</span></code></pre></div>
<p><code>some_tool</code>:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-1-1"><a id="__codelineno-1-1" name="__codelineno-1-1" href="#__codelineno-1-1"></a><span class="nd">@tool</span>
</span><span id="__span-1-2"><a id="__codelineno-1-2" name="__codelineno-1-2" href="#__codelineno-1-2"></a><span class="k">def</span><span class="w"> </span><span class="nf">some_tool</span><span class="p">(</span><span class="n">x</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">y</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
</span><span id="__span-1-3"><a id="__codelineno-1-3" name="__codelineno-1-3" href="#__codelineno-1-3"></a><span class="w">    </span><span class="sd">&#39;&#39;&#39;Some_tool.&#39;&#39;&#39;</span>
</span><span id="__span-1-4"><a id="__codelineno-1-4" name="__codelineno-1-4" href="#__codelineno-1-4"></a>    <span class="k">return</span> <span class="p">{</span><span class="s2">&quot;x&quot;</span><span class="p">:</span> <span class="n">x</span><span class="p">,</span> <span class="s2">&quot;y&quot;</span><span class="p">:</span> <span class="n">y</span><span class="p">}</span>
</span></code></pre></div>
<p><code>prompt</code>:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-2-1"><a id="__codelineno-2-1" name="__codelineno-2-1" href="#__codelineno-2-1"></a><span class="n">template</span> <span class="o">=</span> <span class="n">ChatPromptTemplate</span><span class="o">.</span><span class="n">from_messages</span><span class="p">(</span>
</span><span id="__span-2-2"><a id="__codelineno-2-2" name="__codelineno-2-2" href="#__codelineno-2-2"></a>    <span class="p">[</span>
</span><span id="__span-2-3"><a id="__codelineno-2-3" name="__codelineno-2-3" href="#__codelineno-2-3"></a>        <span class="p">(</span><span class="s2">&quot;system&quot;</span><span class="p">,</span> <span class="s2">&quot;You are Cat Agent 007&quot;</span><span class="p">),</span>
</span><span id="__span-2-4"><a id="__codelineno-2-4" name="__codelineno-2-4" href="#__codelineno-2-4"></a>        <span class="p">(</span><span class="s2">&quot;human&quot;</span><span class="p">,</span> <span class="s2">&quot;</span><span class="si">{question}</span><span class="s2">&quot;</span><span class="p">),</span>
</span><span id="__span-2-5"><a id="__codelineno-2-5" name="__codelineno-2-5" href="#__codelineno-2-5"></a>    <span class="p">]</span>
</span><span id="__span-2-6"><a id="__codelineno-2-6" name="__codelineno-2-6" href="#__codelineno-2-6"></a><span class="p">)</span><span class="o">.</span><span class="n">with_config</span><span class="p">({</span><span class="s2">&quot;run_name&quot;</span><span class="p">:</span> <span class="s2">&quot;my_template&quot;</span><span class="p">,</span> <span class="s2">&quot;tags&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;my_template&quot;</span><span class="p">]})</span>
</span></code></pre></div>
<div class="admonition example">
<p class="admonition-title">Example</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-3-1"><a id="__codelineno-3-1" name="__codelineno-3-1" href="#__codelineno-3-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">langchain_core.runnables</span><span class="w"> </span><span class="kn">import</span> <span class="n">RunnableLambda</span>
</span><span id="__span-3-2"><a id="__codelineno-3-2" name="__codelineno-3-2" href="#__codelineno-3-2"></a>
</span><span id="__span-3-3"><a id="__codelineno-3-3" name="__codelineno-3-3" href="#__codelineno-3-3"></a>
</span><span id="__span-3-4"><a id="__codelineno-3-4" name="__codelineno-3-4" href="#__codelineno-3-4"></a><span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">reverse</span><span class="p">(</span><span class="n">s</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="__span-3-5"><a id="__codelineno-3-5" name="__codelineno-3-5" href="#__codelineno-3-5"></a>    <span class="k">return</span> <span class="n">s</span><span class="p">[::</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
</span><span id="__span-3-6"><a id="__codelineno-3-6" name="__codelineno-3-6" href="#__codelineno-3-6"></a>
</span><span id="__span-3-7"><a id="__codelineno-3-7" name="__codelineno-3-7" href="#__codelineno-3-7"></a>
</span><span id="__span-3-8"><a id="__codelineno-3-8" name="__codelineno-3-8" href="#__codelineno-3-8"></a><span class="n">chain</span> <span class="o">=</span> <span class="n">RunnableLambda</span><span class="p">(</span><span class="n">func</span><span class="o">=</span><span class="n">reverse</span><span class="p">)</span>
</span><span id="__span-3-9"><a id="__codelineno-3-9" name="__codelineno-3-9" href="#__codelineno-3-9"></a>
</span><span id="__span-3-10"><a id="__codelineno-3-10" name="__codelineno-3-10" href="#__codelineno-3-10"></a><span class="n">events</span> <span class="o">=</span> <span class="p">[</span>
</span><span id="__span-3-11"><a id="__codelineno-3-11" name="__codelineno-3-11" href="#__codelineno-3-11"></a>    <span class="n">event</span> <span class="k">async</span> <span class="k">for</span> <span class="n">event</span> <span class="ow">in</span> <span class="n">chain</span><span class="o">.</span><span class="n">astream_events</span><span class="p">(</span><span class="s2">&quot;hello&quot;</span><span class="p">,</span> <span class="n">version</span><span class="o">=</span><span class="s2">&quot;v2&quot;</span><span class="p">)</span>
</span><span id="__span-3-12"><a id="__codelineno-3-12" name="__codelineno-3-12" href="#__codelineno-3-12"></a><span class="p">]</span>
</span><span id="__span-3-13"><a id="__codelineno-3-13" name="__codelineno-3-13" href="#__codelineno-3-13"></a>
</span><span id="__span-3-14"><a id="__codelineno-3-14" name="__codelineno-3-14" href="#__codelineno-3-14"></a><span class="c1"># Will produce the following events</span>
</span><span id="__span-3-15"><a id="__codelineno-3-15" name="__codelineno-3-15" href="#__codelineno-3-15"></a><span class="c1"># (run_id, and parent_ids has been omitted for brevity):</span>
</span><span id="__span-3-16"><a id="__codelineno-3-16" name="__codelineno-3-16" href="#__codelineno-3-16"></a><span class="p">[</span>
</span><span id="__span-3-17"><a id="__codelineno-3-17" name="__codelineno-3-17" href="#__codelineno-3-17"></a>    <span class="p">{</span>
</span><span id="__span-3-18"><a id="__codelineno-3-18" name="__codelineno-3-18" href="#__codelineno-3-18"></a>        <span class="s2">&quot;data&quot;</span><span class="p">:</span> <span class="p">{</span><span class="s2">&quot;input&quot;</span><span class="p">:</span> <span class="s2">&quot;hello&quot;</span><span class="p">},</span>
</span><span id="__span-3-19"><a id="__codelineno-3-19" name="__codelineno-3-19" href="#__codelineno-3-19"></a>        <span class="s2">&quot;event&quot;</span><span class="p">:</span> <span class="s2">&quot;on_chain_start&quot;</span><span class="p">,</span>
</span><span id="__span-3-20"><a id="__codelineno-3-20" name="__codelineno-3-20" href="#__codelineno-3-20"></a>        <span class="s2">&quot;metadata&quot;</span><span class="p">:</span> <span class="p">{},</span>
</span><span id="__span-3-21"><a id="__codelineno-3-21" name="__codelineno-3-21" href="#__codelineno-3-21"></a>        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;reverse&quot;</span><span class="p">,</span>
</span><span id="__span-3-22"><a id="__codelineno-3-22" name="__codelineno-3-22" href="#__codelineno-3-22"></a>        <span class="s2">&quot;tags&quot;</span><span class="p">:</span> <span class="p">[],</span>
</span><span id="__span-3-23"><a id="__codelineno-3-23" name="__codelineno-3-23" href="#__codelineno-3-23"></a>    <span class="p">},</span>
</span><span id="__span-3-24"><a id="__codelineno-3-24" name="__codelineno-3-24" href="#__codelineno-3-24"></a>    <span class="p">{</span>
</span><span id="__span-3-25"><a id="__codelineno-3-25" name="__codelineno-3-25" href="#__codelineno-3-25"></a>        <span class="s2">&quot;data&quot;</span><span class="p">:</span> <span class="p">{</span><span class="s2">&quot;chunk&quot;</span><span class="p">:</span> <span class="s2">&quot;olleh&quot;</span><span class="p">},</span>
</span><span id="__span-3-26"><a id="__codelineno-3-26" name="__codelineno-3-26" href="#__codelineno-3-26"></a>        <span class="s2">&quot;event&quot;</span><span class="p">:</span> <span class="s2">&quot;on_chain_stream&quot;</span><span class="p">,</span>
</span><span id="__span-3-27"><a id="__codelineno-3-27" name="__codelineno-3-27" href="#__codelineno-3-27"></a>        <span class="s2">&quot;metadata&quot;</span><span class="p">:</span> <span class="p">{},</span>
</span><span id="__span-3-28"><a id="__codelineno-3-28" name="__codelineno-3-28" href="#__codelineno-3-28"></a>        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;reverse&quot;</span><span class="p">,</span>
</span><span id="__span-3-29"><a id="__codelineno-3-29" name="__codelineno-3-29" href="#__codelineno-3-29"></a>        <span class="s2">&quot;tags&quot;</span><span class="p">:</span> <span class="p">[],</span>
</span><span id="__span-3-30"><a id="__codelineno-3-30" name="__codelineno-3-30" href="#__codelineno-3-30"></a>    <span class="p">},</span>
</span><span id="__span-3-31"><a id="__codelineno-3-31" name="__codelineno-3-31" href="#__codelineno-3-31"></a>    <span class="p">{</span>
</span><span id="__span-3-32"><a id="__codelineno-3-32" name="__codelineno-3-32" href="#__codelineno-3-32"></a>        <span class="s2">&quot;data&quot;</span><span class="p">:</span> <span class="p">{</span><span class="s2">&quot;output&quot;</span><span class="p">:</span> <span class="s2">&quot;olleh&quot;</span><span class="p">},</span>
</span><span id="__span-3-33"><a id="__codelineno-3-33" name="__codelineno-3-33" href="#__codelineno-3-33"></a>        <span class="s2">&quot;event&quot;</span><span class="p">:</span> <span class="s2">&quot;on_chain_end&quot;</span><span class="p">,</span>
</span><span id="__span-3-34"><a id="__codelineno-3-34" name="__codelineno-3-34" href="#__codelineno-3-34"></a>        <span class="s2">&quot;metadata&quot;</span><span class="p">:</span> <span class="p">{},</span>
</span><span id="__span-3-35"><a id="__codelineno-3-35" name="__codelineno-3-35" href="#__codelineno-3-35"></a>        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;reverse&quot;</span><span class="p">,</span>
</span><span id="__span-3-36"><a id="__codelineno-3-36" name="__codelineno-3-36" href="#__codelineno-3-36"></a>        <span class="s2">&quot;tags&quot;</span><span class="p">:</span> <span class="p">[],</span>
</span><span id="__span-3-37"><a id="__codelineno-3-37" name="__codelineno-3-37" href="#__codelineno-3-37"></a>    <span class="p">},</span>
</span><span id="__span-3-38"><a id="__codelineno-3-38" name="__codelineno-3-38" href="#__codelineno-3-38"></a><span class="p">]</span>
</span></code></pre></div>
</div>
<div class="language-python highlight"><span class="filename">Dispatch custom event</span><pre><span></span><code><span id="__span-4-1"><a id="__codelineno-4-1" name="__codelineno-4-1" href="#__codelineno-4-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">langchain_core.callbacks.manager</span><span class="w"> </span><span class="kn">import</span> <span class="p">(</span>
</span><span id="__span-4-2"><a id="__codelineno-4-2" name="__codelineno-4-2" href="#__codelineno-4-2"></a>    <span class="n">adispatch_custom_event</span><span class="p">,</span>
</span><span id="__span-4-3"><a id="__codelineno-4-3" name="__codelineno-4-3" href="#__codelineno-4-3"></a><span class="p">)</span>
</span><span id="__span-4-4"><a id="__codelineno-4-4" name="__codelineno-4-4" href="#__codelineno-4-4"></a><span class="kn">from</span><span class="w"> </span><span class="nn">langchain_core.runnables</span><span class="w"> </span><span class="kn">import</span> <span class="n">RunnableLambda</span><span class="p">,</span> <span class="n">RunnableConfig</span>
</span><span id="__span-4-5"><a id="__codelineno-4-5" name="__codelineno-4-5" href="#__codelineno-4-5"></a><span class="kn">import</span><span class="w"> </span><span class="nn">asyncio</span>
</span><span id="__span-4-6"><a id="__codelineno-4-6" name="__codelineno-4-6" href="#__codelineno-4-6"></a>
</span><span id="__span-4-7"><a id="__codelineno-4-7" name="__codelineno-4-7" href="#__codelineno-4-7"></a>
</span><span id="__span-4-8"><a id="__codelineno-4-8" name="__codelineno-4-8" href="#__codelineno-4-8"></a><span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">slow_thing</span><span class="p">(</span><span class="n">some_input</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">config</span><span class="p">:</span> <span class="n">RunnableConfig</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="__span-4-9"><a id="__codelineno-4-9" name="__codelineno-4-9" href="#__codelineno-4-9"></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Do something that takes a long time.&quot;&quot;&quot;</span>
</span><span id="__span-4-10"><a id="__codelineno-4-10" name="__codelineno-4-10" href="#__codelineno-4-10"></a>    <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span> <span class="c1"># Placeholder for some slow operation</span>
</span><span id="__span-4-11"><a id="__codelineno-4-11" name="__codelineno-4-11" href="#__codelineno-4-11"></a>    <span class="k">await</span> <span class="n">adispatch_custom_event</span><span class="p">(</span>
</span><span id="__span-4-12"><a id="__codelineno-4-12" name="__codelineno-4-12" href="#__codelineno-4-12"></a>        <span class="s2">&quot;progress_event&quot;</span><span class="p">,</span>
</span><span id="__span-4-13"><a id="__codelineno-4-13" name="__codelineno-4-13" href="#__codelineno-4-13"></a>        <span class="p">{</span><span class="s2">&quot;message&quot;</span><span class="p">:</span> <span class="s2">&quot;Finished step 1 of 3&quot;</span><span class="p">},</span>
</span><span id="__span-4-14"><a id="__codelineno-4-14" name="__codelineno-4-14" href="#__codelineno-4-14"></a>        <span class="n">config</span><span class="o">=</span><span class="n">config</span> <span class="c1"># Must be included for python &lt; 3.10</span>
</span><span id="__span-4-15"><a id="__codelineno-4-15" name="__codelineno-4-15" href="#__codelineno-4-15"></a>    <span class="p">)</span>
</span><span id="__span-4-16"><a id="__codelineno-4-16" name="__codelineno-4-16" href="#__codelineno-4-16"></a>    <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span> <span class="c1"># Placeholder for some slow operation</span>
</span><span id="__span-4-17"><a id="__codelineno-4-17" name="__codelineno-4-17" href="#__codelineno-4-17"></a>    <span class="k">await</span> <span class="n">adispatch_custom_event</span><span class="p">(</span>
</span><span id="__span-4-18"><a id="__codelineno-4-18" name="__codelineno-4-18" href="#__codelineno-4-18"></a>        <span class="s2">&quot;progress_event&quot;</span><span class="p">,</span>
</span><span id="__span-4-19"><a id="__codelineno-4-19" name="__codelineno-4-19" href="#__codelineno-4-19"></a>        <span class="p">{</span><span class="s2">&quot;message&quot;</span><span class="p">:</span> <span class="s2">&quot;Finished step 2 of 3&quot;</span><span class="p">},</span>
</span><span id="__span-4-20"><a id="__codelineno-4-20" name="__codelineno-4-20" href="#__codelineno-4-20"></a>        <span class="n">config</span><span class="o">=</span><span class="n">config</span> <span class="c1"># Must be included for python &lt; 3.10</span>
</span><span id="__span-4-21"><a id="__codelineno-4-21" name="__codelineno-4-21" href="#__codelineno-4-21"></a>    <span class="p">)</span>
</span><span id="__span-4-22"><a id="__codelineno-4-22" name="__codelineno-4-22" href="#__codelineno-4-22"></a>    <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span> <span class="c1"># Placeholder for some slow operation</span>
</span><span id="__span-4-23"><a id="__codelineno-4-23" name="__codelineno-4-23" href="#__codelineno-4-23"></a>    <span class="k">return</span> <span class="s2">&quot;Done&quot;</span>
</span><span id="__span-4-24"><a id="__codelineno-4-24" name="__codelineno-4-24" href="#__codelineno-4-24"></a>
</span><span id="__span-4-25"><a id="__codelineno-4-25" name="__codelineno-4-25" href="#__codelineno-4-25"></a><span class="n">slow_thing</span> <span class="o">=</span> <span class="n">RunnableLambda</span><span class="p">(</span><span class="n">slow_thing</span><span class="p">)</span>
</span><span id="__span-4-26"><a id="__codelineno-4-26" name="__codelineno-4-26" href="#__codelineno-4-26"></a>
</span><span id="__span-4-27"><a id="__codelineno-4-27" name="__codelineno-4-27" href="#__codelineno-4-27"></a><span class="k">async</span> <span class="k">for</span> <span class="n">event</span> <span class="ow">in</span> <span class="n">slow_thing</span><span class="o">.</span><span class="n">astream_events</span><span class="p">(</span><span class="s2">&quot;some_input&quot;</span><span class="p">,</span> <span class="n">version</span><span class="o">=</span><span class="s2">&quot;v2&quot;</span><span class="p">):</span>
</span><span id="__span-4-28"><a id="__codelineno-4-28" name="__codelineno-4-28" href="#__codelineno-4-28"></a>    <span class="nb">print</span><span class="p">(</span><span class="n">event</span><span class="p">)</span>
</span></code></pre></div>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>input</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>The input to the <code>Runnable</code>.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>config</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>The config to use for the <code>Runnable</code>.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>version</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>The version of the schema to use, either <code>'v2'</code> or <code>'v1'</code>.</p>
<p>Users should use <code>'v2'</code>.</p>
<p><code>'v1'</code> is for backwards compatibility and will be deprecated
in <code>0.4.0</code>.</p>
<p>No default will be assigned until the API is stabilized.
custom events will only be surfaced in <code>'v2'</code>.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Literal&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Literal" target="_blank" rel="noopener">Literal</a>[&#39;v1&#39;, &#39;v2&#39;]</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>&#39;v2&#39;</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_names</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Only include events from <code>Runnable</code> objects with matching names.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_types</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Only include events from <code>Runnable</code> objects with matching types.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_tags</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Only include events from <code>Runnable</code> objects with matching tags.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>exclude_names</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Exclude events from <code>Runnable</code> objects with matching names.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>exclude_types</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Exclude events from <code>Runnable</code> objects with matching types.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>exclude_tags</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Exclude events from <code>Runnable</code> objects with matching tags.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>**kwargs</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Additional keyword arguments to pass to the <code>Runnable</code>.</p>
<p>These will be passed to <code>astream_log</code> as this implementation
of <code>astream_events</code> is built on top of <code>astream_log</code>.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>{}</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">YIELDS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-yields-annotation">
                    <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.AsyncIterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator" target="_blank" rel="noopener">AsyncIterator</a>[<span title="langchain_core.runnables.schema.StreamEvent">StreamEvent</span>]</code>
                </span>
            </td>
            <td class="doc-yields-details">
              <div class="doc-md-description">
                <p>An async stream of <code>StreamEvent</code>.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RAISES</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
              <span class="doc-raises-annotation">
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/exceptions.html#NotImplementedError" target="_blank" rel="noopener">NotImplementedError</a></code>
              </span>
            </td>
            <td class="doc-raises-details">
              <div class="doc-md-description">
                <p>If the version is not <code>'v1'</code> or <code>'v2'</code>.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.invoke" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">invoke</span>


<a href="#langgraph.pregel.remote.RemoteGraph.invoke" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">invoke</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="nb">input</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">,</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>    <span class="n">config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>    <span class="o">*</span><span class="p">,</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="n">interrupt_before</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;All&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.All&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.All">All</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>    <span class="n">interrupt_after</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;All&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.All&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.All">All</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a>    <span class="n">headers</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-8"><a id="__codelineno-0-8" name="__codelineno-0-8" href="#__codelineno-0-8"></a>    <span class="n">params</span><span class="p">:</span> <span class="n"><span title="langgraph_sdk.schema.QueryParamTypes">QueryParamTypes</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-9"><a id="__codelineno-0-9" name="__codelineno-0-9" href="#__codelineno-0-9"></a>    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">,</span>
</span><span id="__span-0-10"><a id="__codelineno-0-10" name="__codelineno-0-10" href="#__codelineno-0-10"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Create a run, wait until it finishes and return the final state.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>input</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Input to the graph.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>] | <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>config</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A <code>RunnableConfig</code> for graph invocation.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>interrupt_before</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Interrupt the graph before these nodes.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;All&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.All&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.All">All</a> | <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>interrupt_after</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Interrupt the graph after these nodes.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;All&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.All&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.All">All</a> | <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>headers</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Additional headers to pass to the request.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>**kwargs</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Additional params to pass to RemoteGraph.stream.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>{}</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>] | <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>The output of the graph.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.ainvoke" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">ainvoke</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

<a href="#langgraph.pregel.remote.RemoteGraph.ainvoke" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">ainvoke</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="nb">input</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">,</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>    <span class="n">config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>    <span class="o">*</span><span class="p">,</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="n">interrupt_before</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;All&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.All&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.All">All</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>    <span class="n">interrupt_after</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;All&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.All&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.All">All</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a>    <span class="n">headers</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-8"><a id="__codelineno-0-8" name="__codelineno-0-8" href="#__codelineno-0-8"></a>    <span class="n">params</span><span class="p">:</span> <span class="n"><span title="langgraph_sdk.schema.QueryParamTypes">QueryParamTypes</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-9"><a id="__codelineno-0-9" name="__codelineno-0-9" href="#__codelineno-0-9"></a>    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">,</span>
</span><span id="__span-0-10"><a id="__codelineno-0-10" name="__codelineno-0-10" href="#__codelineno-0-10"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Create a run, wait until it finishes and return the final state.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>input</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Input to the graph.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>] | <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>config</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A <code>RunnableConfig</code> for graph invocation.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>interrupt_before</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Interrupt the graph before these nodes.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;All&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.All&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.All">All</a> | <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>interrupt_after</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Interrupt the graph after these nodes.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-attribute&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-attribute-name&quot;&gt;All&lt;/span&gt;


  &lt;span class=&quot;doc doc-labels&quot;&gt;
      &lt;small class=&quot;doc doc-label doc-label-module-attribute&quot;&gt;&lt;code&gt;module-attribute&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;langgraph.types.All&lt;/code&gt;)" href="../../../langgraph/types/#langgraph.types.All">All</a> | <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>headers</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Additional headers to pass to the request.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>**kwargs</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Additional params to pass to RemoteGraph.astream.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>{}</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>] | <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>The output of the graph.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.get_name" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">get_name</span>


<a href="#langgraph.pregel.remote.RemoteGraph.get_name" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">get_name</span><span class="p">(</span><span class="n">suffix</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Get the name of the <code>Runnable</code>.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>suffix</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>An optional suffix to append to the name.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>name</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>An optional name to use instead of the <code>Runnable</code>'s name.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>The name of the <code>Runnable</code>.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.get_input_schema" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">get_input_schema</span>


<a href="#langgraph.pregel.remote.RemoteGraph.get_input_schema" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">get_input_schema</span><span class="p">(</span><span class="n">config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type" target="_blank" rel="noopener">type</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;pydantic.BaseModel&lt;/code&gt;" href="https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel" target="_blank" rel="noopener">BaseModel</a></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Get a Pydantic model that can be used to validate input to the <code>Runnable</code>.</p>
<p><code>Runnable</code> objects that leverage the <code>configurable_fields</code> and
<code>configurable_alternatives</code> methods will have a dynamic input schema that
depends on which configuration the <code>Runnable</code> is invoked with.</p>
<p>This method allows to get an input schema for a specific configuration.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>config</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A config to use when generating the schema.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type" target="_blank" rel="noopener">type</a>[<a class="autorefs autorefs-external" title="&lt;code&gt;pydantic.BaseModel&lt;/code&gt;" href="https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel" target="_blank" rel="noopener">BaseModel</a>]</code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>A Pydantic model that can be used to validate input.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.get_input_jsonschema" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">get_input_jsonschema</span>


<a href="#langgraph.pregel.remote.RemoteGraph.get_input_jsonschema" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">get_input_jsonschema</span><span class="p">(</span><span class="n">config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Get a JSON schema that represents the input to the <code>Runnable</code>.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>config</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A config to use when generating the schema.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>]</code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>A JSON schema that represents the input to the <code>Runnable</code>.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>


<details class="example" open>
  <summary>Example</summary>
  <div class="language-python highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">langchain_core.runnables</span><span class="w"> </span><span class="kn">import</span> <span class="n">RunnableLambda</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a><span class="k">def</span><span class="w"> </span><span class="nf">add_one</span><span class="p">(</span><span class="n">x</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="k">return</span> <span class="n">x</span> <span class="o">+</span> <span class="mi">1</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a>
</span><span id="__span-0-8"><a id="__codelineno-0-8" name="__codelineno-0-8" href="#__codelineno-0-8"></a><span class="n">runnable</span> <span class="o">=</span> <span class="n">RunnableLambda</span><span class="p">(</span><span class="n">add_one</span><span class="p">)</span>
</span><span id="__span-0-9"><a id="__codelineno-0-9" name="__codelineno-0-9" href="#__codelineno-0-9"></a>
</span><span id="__span-0-10"><a id="__codelineno-0-10" name="__codelineno-0-10" href="#__codelineno-0-10"></a><span class="nb">print</span><span class="p">(</span><span class="n">runnable</span><span class="o">.</span><span class="n">get_input_jsonschema</span><span class="p">())</span>
</span></code></pre></div>
</details>        <div class="admonition version-added">
<p class="admonition-title">Added in <code>langchain-core</code> 0.3.0</p>
</div>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.get_output_schema" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">get_output_schema</span>


<a href="#langgraph.pregel.remote.RemoteGraph.get_output_schema" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">get_output_schema</span><span class="p">(</span><span class="n">config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type" target="_blank" rel="noopener">type</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;pydantic.BaseModel&lt;/code&gt;" href="https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel" target="_blank" rel="noopener">BaseModel</a></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Get a Pydantic model that can be used to validate output to the <code>Runnable</code>.</p>
<p><code>Runnable</code> objects that leverage the <code>configurable_fields</code> and
<code>configurable_alternatives</code> methods will have a dynamic output schema that
depends on which configuration the <code>Runnable</code> is invoked with.</p>
<p>This method allows to get an output schema for a specific configuration.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>config</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A config to use when generating the schema.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type" target="_blank" rel="noopener">type</a>[<a class="autorefs autorefs-external" title="&lt;code&gt;pydantic.BaseModel&lt;/code&gt;" href="https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel" target="_blank" rel="noopener">BaseModel</a>]</code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>A Pydantic model that can be used to validate output.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.get_output_jsonschema" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">get_output_jsonschema</span>


<a href="#langgraph.pregel.remote.RemoteGraph.get_output_jsonschema" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">get_output_jsonschema</span><span class="p">(</span><span class="n">config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Get a JSON schema that represents the output of the <code>Runnable</code>.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>config</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A config to use when generating the schema.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>]</code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>A JSON schema that represents the output of the <code>Runnable</code>.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>


<details class="example" open>
  <summary>Example</summary>
  <div class="language-python highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">langchain_core.runnables</span><span class="w"> </span><span class="kn">import</span> <span class="n">RunnableLambda</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a><span class="k">def</span><span class="w"> </span><span class="nf">add_one</span><span class="p">(</span><span class="n">x</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="k">return</span> <span class="n">x</span> <span class="o">+</span> <span class="mi">1</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a>
</span><span id="__span-0-8"><a id="__codelineno-0-8" name="__codelineno-0-8" href="#__codelineno-0-8"></a><span class="n">runnable</span> <span class="o">=</span> <span class="n">RunnableLambda</span><span class="p">(</span><span class="n">add_one</span><span class="p">)</span>
</span><span id="__span-0-9"><a id="__codelineno-0-9" name="__codelineno-0-9" href="#__codelineno-0-9"></a>
</span><span id="__span-0-10"><a id="__codelineno-0-10" name="__codelineno-0-10" href="#__codelineno-0-10"></a><span class="nb">print</span><span class="p">(</span><span class="n">runnable</span><span class="o">.</span><span class="n">get_output_jsonschema</span><span class="p">())</span>
</span></code></pre></div>
</details>        <div class="admonition version-added">
<p class="admonition-title">Added in <code>langchain-core</code> 0.3.0</p>
</div>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.config_schema" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">config_schema</span>


<a href="#langgraph.pregel.remote.RemoteGraph.config_schema" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">config_schema</span><span class="p">(</span><span class="o">*</span><span class="p">,</span> <span class="n">include</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type" target="_blank" rel="noopener">type</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;pydantic.BaseModel&lt;/code&gt;" href="https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel" target="_blank" rel="noopener">BaseModel</a></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>The type of config this <code>Runnable</code> accepts specified as a Pydantic model.</p>
<p>To mark a field as configurable, see the <code>configurable_fields</code>
and <code>configurable_alternatives</code> methods.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>include</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A list of fields to include in the config schema.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type" target="_blank" rel="noopener">type</a>[<a class="autorefs autorefs-external" title="&lt;code&gt;pydantic.BaseModel&lt;/code&gt;" href="https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel" target="_blank" rel="noopener">BaseModel</a>]</code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>A Pydantic model that can be used to validate config.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.get_config_jsonschema" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">get_config_jsonschema</span>


<a href="#langgraph.pregel.remote.RemoteGraph.get_config_jsonschema" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">get_config_jsonschema</span><span class="p">(</span><span class="o">*</span><span class="p">,</span> <span class="n">include</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Get a JSON schema that represents the config of the <code>Runnable</code>.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>include</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A list of fields to include in the config schema.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>]</code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>A JSON schema that represents the config of the <code>Runnable</code>.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>
        <div class="admonition version-added">
<p class="admonition-title">Added in <code>langchain-core</code> 0.3.0</p>
</div>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.get_prompts" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">get_prompts</span>


<a href="#langgraph.pregel.remote.RemoteGraph.get_prompts" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">get_prompts</span><span class="p">(</span><span class="n">config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list" target="_blank" rel="noopener">list</a></span><span class="p">[</span><span class="n"><span title="langchain_core.prompts.base.BasePromptTemplate">BasePromptTemplate</span></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Return a list of prompts used by this <code>Runnable</code>.</p>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.__or__" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">__or__</span>


<a href="#langgraph.pregel.remote.RemoteGraph.__or__" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">__or__</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="n">other</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">,</span> <span class="n"><span title="langchain_core.runnables.base.Other">Other</span></span><span class="p">]</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>    <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a></span><span class="p">[[</span><span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Iterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator" target="_blank" rel="noopener">Iterator</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]],</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Iterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator" target="_blank" rel="noopener">Iterator</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.base.Other">Other</span></span><span class="p">]]</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>    <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a></span><span class="p">[[</span><span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.AsyncIterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator" target="_blank" rel="noopener">AsyncIterator</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]],</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.AsyncIterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator" target="_blank" rel="noopener">AsyncIterator</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.base.Other">Other</span></span><span class="p">]]</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a></span><span class="p">[[</span><span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">],</span> <span class="n"><span title="langchain_core.runnables.base.Other">Other</span></span><span class="p">]</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>    <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Mapping&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping" target="_blank" rel="noopener">Mapping</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">,</span> <span class="n"><span title="langchain_core.runnables.base.Other">Other</span></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a></span><span class="p">[[</span><span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">],</span> <span class="n"><span title="langchain_core.runnables.base.Other">Other</span></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">],</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableSerializable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.RunnableSerializable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.RunnableSerializable">RunnableSerializable</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.utils.Input">Input</span></span><span class="p">,</span> <span class="n"><span title="langchain_core.runnables.base.Other">Other</span></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Runnable "or" operator.</p>
<p>Compose this <code>Runnable</code> with another object to create a
<code>RunnableSequence</code>.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>other</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Another <code>Runnable</code> or a <code>Runnable</code>-like object.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a>[<a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>, <span title="langchain_core.runnables.base.Other">Other</span>] | <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a>[[<a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Iterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator" target="_blank" rel="noopener">Iterator</a>[<a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>]], <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Iterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator" target="_blank" rel="noopener">Iterator</a>[<span title="langchain_core.runnables.base.Other">Other</span>]] | <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a>[[<a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.AsyncIterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator" target="_blank" rel="noopener">AsyncIterator</a>[<a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>]], <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.AsyncIterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator" target="_blank" rel="noopener">AsyncIterator</a>[<span title="langchain_core.runnables.base.Other">Other</span>]] | <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a>[[<a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>], <span title="langchain_core.runnables.base.Other">Other</span>] | <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Mapping&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping" target="_blank" rel="noopener">Mapping</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a>[<a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>, <span title="langchain_core.runnables.base.Other">Other</span>] | <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a>[[<a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>], <span title="langchain_core.runnables.base.Other">Other</span>] | <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>]</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableSerializable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.RunnableSerializable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.RunnableSerializable">RunnableSerializable</a>[<span title="langchain_core.runnables.utils.Input">Input</span>, <span title="langchain_core.runnables.base.Other">Other</span>]</code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>A new <code>Runnable</code>.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.__ror__" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">__ror__</span>


<a href="#langgraph.pregel.remote.RemoteGraph.__ror__" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">__ror__</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="n">other</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.base.Other">Other</span></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>    <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a></span><span class="p">[[</span><span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Iterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator" target="_blank" rel="noopener">Iterator</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.base.Other">Other</span></span><span class="p">]],</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Iterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator" target="_blank" rel="noopener">Iterator</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]]</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>    <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a></span><span class="p">[[</span><span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.AsyncIterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator" target="_blank" rel="noopener">AsyncIterator</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.base.Other">Other</span></span><span class="p">]],</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.AsyncIterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator" target="_blank" rel="noopener">AsyncIterator</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]]</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a></span><span class="p">[[</span><span class="n"><span title="langchain_core.runnables.base.Other">Other</span></span><span class="p">],</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>    <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Mapping&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping" target="_blank" rel="noopener">Mapping</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.base.Other">Other</span></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a></span><span class="p">[[</span><span class="n"><span title="langchain_core.runnables.base.Other">Other</span></span><span class="p">],</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">],</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableSerializable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.RunnableSerializable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.RunnableSerializable">RunnableSerializable</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.base.Other">Other</span></span><span class="p">,</span> <span class="n"><span title="langchain_core.runnables.utils.Output">Output</span></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Runnable "reverse-or" operator.</p>
<p>Compose this <code>Runnable</code> with another object to create a
<code>RunnableSequence</code>.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>other</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Another <code>Runnable</code> or a <code>Runnable</code>-like object.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a>[<span title="langchain_core.runnables.base.Other">Other</span>, <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>] | <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a>[[<a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Iterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator" target="_blank" rel="noopener">Iterator</a>[<span title="langchain_core.runnables.base.Other">Other</span>]], <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Iterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator" target="_blank" rel="noopener">Iterator</a>[<a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>]] | <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a>[[<a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.AsyncIterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator" target="_blank" rel="noopener">AsyncIterator</a>[<span title="langchain_core.runnables.base.Other">Other</span>]], <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.AsyncIterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator" target="_blank" rel="noopener">AsyncIterator</a>[<a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>]] | <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a>[[<span title="langchain_core.runnables.base.Other">Other</span>], <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>] | <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Mapping&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping" target="_blank" rel="noopener">Mapping</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a>[<span title="langchain_core.runnables.base.Other">Other</span>, <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>] | <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a>[[<span title="langchain_core.runnables.base.Other">Other</span>], <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>] | <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>]</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableSerializable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.RunnableSerializable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.RunnableSerializable">RunnableSerializable</a>[<span title="langchain_core.runnables.base.Other">Other</span>, <span title="langchain_core.runnables.utils.Output">Output</span>]</code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>A new <code>Runnable</code>.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.pipe" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">pipe</span>


<a href="#langgraph.pregel.remote.RemoteGraph.pipe" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">pipe</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="o">*</span><span class="n">others</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">,</span> <span class="n"><span title="langchain_core.runnables.base.Other">Other</span></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a></span><span class="p">[[</span><span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">],</span> <span class="n"><span title="langchain_core.runnables.base.Other">Other</span></span><span class="p">],</span> <span class="n">name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableSerializable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.RunnableSerializable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.RunnableSerializable">RunnableSerializable</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.utils.Input">Input</span></span><span class="p">,</span> <span class="n"><span title="langchain_core.runnables.base.Other">Other</span></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Pipe <code>Runnable</code> objects.</p>
<p>Compose this <code>Runnable</code> with <code>Runnable</code>-like objects to make a
<code>RunnableSequence</code>.</p>
<p>Equivalent to <code>RunnableSequence(self, *others)</code> or <code>self | others[0] | ...</code></p>


<details class="example" open>
  <summary>Example</summary>
  <div class="language-python highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">langchain_core.runnables</span><span class="w"> </span><span class="kn">import</span> <span class="n">RunnableLambda</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a><span class="k">def</span><span class="w"> </span><span class="nf">add_one</span><span class="p">(</span><span class="n">x</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="k">return</span> <span class="n">x</span> <span class="o">+</span> <span class="mi">1</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a>
</span><span id="__span-0-8"><a id="__codelineno-0-8" name="__codelineno-0-8" href="#__codelineno-0-8"></a><span class="k">def</span><span class="w"> </span><span class="nf">mul_two</span><span class="p">(</span><span class="n">x</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="__span-0-9"><a id="__codelineno-0-9" name="__codelineno-0-9" href="#__codelineno-0-9"></a>    <span class="k">return</span> <span class="n">x</span> <span class="o">*</span> <span class="mi">2</span>
</span><span id="__span-0-10"><a id="__codelineno-0-10" name="__codelineno-0-10" href="#__codelineno-0-10"></a>
</span><span id="__span-0-11"><a id="__codelineno-0-11" name="__codelineno-0-11" href="#__codelineno-0-11"></a>
</span><span id="__span-0-12"><a id="__codelineno-0-12" name="__codelineno-0-12" href="#__codelineno-0-12"></a><span class="n">runnable_1</span> <span class="o">=</span> <span class="n">RunnableLambda</span><span class="p">(</span><span class="n">add_one</span><span class="p">)</span>
</span><span id="__span-0-13"><a id="__codelineno-0-13" name="__codelineno-0-13" href="#__codelineno-0-13"></a><span class="n">runnable_2</span> <span class="o">=</span> <span class="n">RunnableLambda</span><span class="p">(</span><span class="n">mul_two</span><span class="p">)</span>
</span><span id="__span-0-14"><a id="__codelineno-0-14" name="__codelineno-0-14" href="#__codelineno-0-14"></a><span class="n">sequence</span> <span class="o">=</span> <span class="n">runnable_1</span><span class="o">.</span><span class="n">pipe</span><span class="p">(</span><span class="n">runnable_2</span><span class="p">)</span>
</span><span id="__span-0-15"><a id="__codelineno-0-15" name="__codelineno-0-15" href="#__codelineno-0-15"></a><span class="c1"># Or equivalently:</span>
</span><span id="__span-0-16"><a id="__codelineno-0-16" name="__codelineno-0-16" href="#__codelineno-0-16"></a><span class="c1"># sequence = runnable_1 | runnable_2</span>
</span><span id="__span-0-17"><a id="__codelineno-0-17" name="__codelineno-0-17" href="#__codelineno-0-17"></a><span class="c1"># sequence = RunnableSequence(first=runnable_1, last=runnable_2)</span>
</span><span id="__span-0-18"><a id="__codelineno-0-18" name="__codelineno-0-18" href="#__codelineno-0-18"></a><span class="n">sequence</span><span class="o">.</span><span class="n">invoke</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</span><span id="__span-0-19"><a id="__codelineno-0-19" name="__codelineno-0-19" href="#__codelineno-0-19"></a><span class="k">await</span> <span class="n">sequence</span><span class="o">.</span><span class="n">ainvoke</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</span><span id="__span-0-20"><a id="__codelineno-0-20" name="__codelineno-0-20" href="#__codelineno-0-20"></a><span class="c1"># -&gt; 4</span>
</span><span id="__span-0-21"><a id="__codelineno-0-21" name="__codelineno-0-21" href="#__codelineno-0-21"></a>
</span><span id="__span-0-22"><a id="__codelineno-0-22" name="__codelineno-0-22" href="#__codelineno-0-22"></a><span class="n">sequence</span><span class="o">.</span><span class="n">batch</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">])</span>
</span><span id="__span-0-23"><a id="__codelineno-0-23" name="__codelineno-0-23" href="#__codelineno-0-23"></a><span class="k">await</span> <span class="n">sequence</span><span class="o">.</span><span class="n">abatch</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">])</span>
</span><span id="__span-0-24"><a id="__codelineno-0-24" name="__codelineno-0-24" href="#__codelineno-0-24"></a><span class="c1"># -&gt; [4, 6, 8]</span>
</span></code></pre></div>
</details>

<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>*others</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Other <code>Runnable</code> or <code>Runnable</code>-like objects to compose</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a>[<a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>, <span title="langchain_core.runnables.base.Other">Other</span>] | <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a>[[<a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>], <span title="langchain_core.runnables.base.Other">Other</span>]</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>()</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>name</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>An optional name for the resulting <code>RunnableSequence</code>.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableSerializable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.RunnableSerializable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.RunnableSerializable">RunnableSerializable</a>[<span title="langchain_core.runnables.utils.Input">Input</span>, <span title="langchain_core.runnables.base.Other">Other</span>]</code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>A new <code>Runnable</code>.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.pick" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">pick</span>


<a href="#langgraph.pregel.remote.RemoteGraph.pick" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">pick</span><span class="p">(</span><span class="n">keys</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list" target="_blank" rel="noopener">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableSerializable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.RunnableSerializable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.RunnableSerializable">RunnableSerializable</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Pick keys from the output <code>dict</code> of this <code>Runnable</code>.</p>
<div class="admonition example">
<p class="admonition-title">Pick a single key</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="kn">import</span><span class="w"> </span><span class="nn">json</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a><span class="kn">from</span><span class="w"> </span><span class="nn">langchain_core.runnables</span><span class="w"> </span><span class="kn">import</span> <span class="n">RunnableLambda</span><span class="p">,</span> <span class="n">RunnableMap</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a><span class="n">as_str</span> <span class="o">=</span> <span class="n">RunnableLambda</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a><span class="n">as_json</span> <span class="o">=</span> <span class="n">RunnableLambda</span><span class="p">(</span><span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">)</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a><span class="n">chain</span> <span class="o">=</span> <span class="n">RunnableMap</span><span class="p">(</span><span class="nb">str</span><span class="o">=</span><span class="n">as_str</span><span class="p">,</span> <span class="n">json</span><span class="o">=</span><span class="n">as_json</span><span class="p">)</span>
</span><span id="__span-0-8"><a id="__codelineno-0-8" name="__codelineno-0-8" href="#__codelineno-0-8"></a>
</span><span id="__span-0-9"><a id="__codelineno-0-9" name="__codelineno-0-9" href="#__codelineno-0-9"></a><span class="n">chain</span><span class="o">.</span><span class="n">invoke</span><span class="p">(</span><span class="s2">&quot;[1, 2, 3]&quot;</span><span class="p">)</span>
</span><span id="__span-0-10"><a id="__codelineno-0-10" name="__codelineno-0-10" href="#__codelineno-0-10"></a><span class="c1"># -&gt; {&quot;str&quot;: &quot;[1, 2, 3]&quot;, &quot;json&quot;: [1, 2, 3]}</span>
</span><span id="__span-0-11"><a id="__codelineno-0-11" name="__codelineno-0-11" href="#__codelineno-0-11"></a>
</span><span id="__span-0-12"><a id="__codelineno-0-12" name="__codelineno-0-12" href="#__codelineno-0-12"></a><span class="n">json_only_chain</span> <span class="o">=</span> <span class="n">chain</span><span class="o">.</span><span class="n">pick</span><span class="p">(</span><span class="s2">&quot;json&quot;</span><span class="p">)</span>
</span><span id="__span-0-13"><a id="__codelineno-0-13" name="__codelineno-0-13" href="#__codelineno-0-13"></a><span class="n">json_only_chain</span><span class="o">.</span><span class="n">invoke</span><span class="p">(</span><span class="s2">&quot;[1, 2, 3]&quot;</span><span class="p">)</span>
</span><span id="__span-0-14"><a id="__codelineno-0-14" name="__codelineno-0-14" href="#__codelineno-0-14"></a><span class="c1"># -&gt; [1, 2, 3]</span>
</span></code></pre></div>
</div>
<div class="admonition example">
<p class="admonition-title">Pick a list of keys</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-1-1"><a id="__codelineno-1-1" name="__codelineno-1-1" href="#__codelineno-1-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">typing</span><span class="w"> </span><span class="kn">import</span> <span class="n">Any</span>
</span><span id="__span-1-2"><a id="__codelineno-1-2" name="__codelineno-1-2" href="#__codelineno-1-2"></a>
</span><span id="__span-1-3"><a id="__codelineno-1-3" name="__codelineno-1-3" href="#__codelineno-1-3"></a><span class="kn">import</span><span class="w"> </span><span class="nn">json</span>
</span><span id="__span-1-4"><a id="__codelineno-1-4" name="__codelineno-1-4" href="#__codelineno-1-4"></a>
</span><span id="__span-1-5"><a id="__codelineno-1-5" name="__codelineno-1-5" href="#__codelineno-1-5"></a><span class="kn">from</span><span class="w"> </span><span class="nn">langchain_core.runnables</span><span class="w"> </span><span class="kn">import</span> <span class="n">RunnableLambda</span><span class="p">,</span> <span class="n">RunnableMap</span>
</span><span id="__span-1-6"><a id="__codelineno-1-6" name="__codelineno-1-6" href="#__codelineno-1-6"></a>
</span><span id="__span-1-7"><a id="__codelineno-1-7" name="__codelineno-1-7" href="#__codelineno-1-7"></a><span class="n">as_str</span> <span class="o">=</span> <span class="n">RunnableLambda</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span>
</span><span id="__span-1-8"><a id="__codelineno-1-8" name="__codelineno-1-8" href="#__codelineno-1-8"></a><span class="n">as_json</span> <span class="o">=</span> <span class="n">RunnableLambda</span><span class="p">(</span><span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">)</span>
</span><span id="__span-1-9"><a id="__codelineno-1-9" name="__codelineno-1-9" href="#__codelineno-1-9"></a>
</span><span id="__span-1-10"><a id="__codelineno-1-10" name="__codelineno-1-10" href="#__codelineno-1-10"></a>
</span><span id="__span-1-11"><a id="__codelineno-1-11" name="__codelineno-1-11" href="#__codelineno-1-11"></a><span class="k">def</span><span class="w"> </span><span class="nf">as_bytes</span><span class="p">(</span><span class="n">x</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
</span><span id="__span-1-12"><a id="__codelineno-1-12" name="__codelineno-1-12" href="#__codelineno-1-12"></a>    <span class="k">return</span> <span class="nb">bytes</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s2">&quot;utf-8&quot;</span><span class="p">)</span>
</span><span id="__span-1-13"><a id="__codelineno-1-13" name="__codelineno-1-13" href="#__codelineno-1-13"></a>
</span><span id="__span-1-14"><a id="__codelineno-1-14" name="__codelineno-1-14" href="#__codelineno-1-14"></a>
</span><span id="__span-1-15"><a id="__codelineno-1-15" name="__codelineno-1-15" href="#__codelineno-1-15"></a><span class="n">chain</span> <span class="o">=</span> <span class="n">RunnableMap</span><span class="p">(</span>
</span><span id="__span-1-16"><a id="__codelineno-1-16" name="__codelineno-1-16" href="#__codelineno-1-16"></a>    <span class="nb">str</span><span class="o">=</span><span class="n">as_str</span><span class="p">,</span> <span class="n">json</span><span class="o">=</span><span class="n">as_json</span><span class="p">,</span> <span class="nb">bytes</span><span class="o">=</span><span class="n">RunnableLambda</span><span class="p">(</span><span class="n">as_bytes</span><span class="p">)</span>
</span><span id="__span-1-17"><a id="__codelineno-1-17" name="__codelineno-1-17" href="#__codelineno-1-17"></a><span class="p">)</span>
</span><span id="__span-1-18"><a id="__codelineno-1-18" name="__codelineno-1-18" href="#__codelineno-1-18"></a>
</span><span id="__span-1-19"><a id="__codelineno-1-19" name="__codelineno-1-19" href="#__codelineno-1-19"></a><span class="n">chain</span><span class="o">.</span><span class="n">invoke</span><span class="p">(</span><span class="s2">&quot;[1, 2, 3]&quot;</span><span class="p">)</span>
</span><span id="__span-1-20"><a id="__codelineno-1-20" name="__codelineno-1-20" href="#__codelineno-1-20"></a><span class="c1"># -&gt; {&quot;str&quot;: &quot;[1, 2, 3]&quot;, &quot;json&quot;: [1, 2, 3], &quot;bytes&quot;: b&quot;[1, 2, 3]&quot;}</span>
</span><span id="__span-1-21"><a id="__codelineno-1-21" name="__codelineno-1-21" href="#__codelineno-1-21"></a>
</span><span id="__span-1-22"><a id="__codelineno-1-22" name="__codelineno-1-22" href="#__codelineno-1-22"></a><span class="n">json_and_bytes_chain</span> <span class="o">=</span> <span class="n">chain</span><span class="o">.</span><span class="n">pick</span><span class="p">([</span><span class="s2">&quot;json&quot;</span><span class="p">,</span> <span class="s2">&quot;bytes&quot;</span><span class="p">])</span>
</span><span id="__span-1-23"><a id="__codelineno-1-23" name="__codelineno-1-23" href="#__codelineno-1-23"></a><span class="n">json_and_bytes_chain</span><span class="o">.</span><span class="n">invoke</span><span class="p">(</span><span class="s2">&quot;[1, 2, 3]&quot;</span><span class="p">)</span>
</span><span id="__span-1-24"><a id="__codelineno-1-24" name="__codelineno-1-24" href="#__codelineno-1-24"></a><span class="c1"># -&gt; {&quot;json&quot;: [1, 2, 3], &quot;bytes&quot;: b&quot;[1, 2, 3]&quot;}</span>
</span></code></pre></div>
</div>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>keys</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A key or list of keys to pick from the output dict.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a> | <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list" target="_blank" rel="noopener">list</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>]</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableSerializable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.RunnableSerializable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.RunnableSerializable">RunnableSerializable</a>[<a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>, <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>]</code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>a new <code>Runnable</code>.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.assign" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">assign</span>


<a href="#langgraph.pregel.remote.RemoteGraph.assign" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">assign</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">],</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>    <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a></span><span class="p">[[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]],</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>    <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Mapping&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping" target="_blank" rel="noopener">Mapping</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">],</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a></span><span class="p">[[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]],</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]],</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableSerializable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.RunnableSerializable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.RunnableSerializable">RunnableSerializable</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Assigns new fields to the <code>dict</code> output of this <code>Runnable</code>.</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">langchain_core.language_models.fake</span><span class="w"> </span><span class="kn">import</span> <span class="n">FakeStreamingListLLM</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a><span class="kn">from</span><span class="w"> </span><span class="nn">langchain_core.output_parsers</span><span class="w"> </span><span class="kn">import</span> <span class="n">StrOutputParser</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a><span class="kn">from</span><span class="w"> </span><span class="nn">langchain_core.prompts</span><span class="w"> </span><span class="kn">import</span> <span class="n">SystemMessagePromptTemplate</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a><span class="kn">from</span><span class="w"> </span><span class="nn">langchain_core.runnables</span><span class="w"> </span><span class="kn">import</span> <span class="n">Runnable</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a><span class="kn">from</span><span class="w"> </span><span class="nn">operator</span><span class="w"> </span><span class="kn">import</span> <span class="n">itemgetter</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a><span class="n">prompt</span> <span class="o">=</span> <span class="p">(</span>
</span><span id="__span-0-8"><a id="__codelineno-0-8" name="__codelineno-0-8" href="#__codelineno-0-8"></a>    <span class="n">SystemMessagePromptTemplate</span><span class="o">.</span><span class="n">from_template</span><span class="p">(</span><span class="s2">&quot;You are a nice assistant.&quot;</span><span class="p">)</span>
</span><span id="__span-0-9"><a id="__codelineno-0-9" name="__codelineno-0-9" href="#__codelineno-0-9"></a>    <span class="o">+</span> <span class="s2">&quot;</span><span class="si">{question}</span><span class="s2">&quot;</span>
</span><span id="__span-0-10"><a id="__codelineno-0-10" name="__codelineno-0-10" href="#__codelineno-0-10"></a><span class="p">)</span>
</span><span id="__span-0-11"><a id="__codelineno-0-11" name="__codelineno-0-11" href="#__codelineno-0-11"></a><span class="n">model</span> <span class="o">=</span> <span class="n">FakeStreamingListLLM</span><span class="p">(</span><span class="n">responses</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;foo-lish&quot;</span><span class="p">])</span>
</span><span id="__span-0-12"><a id="__codelineno-0-12" name="__codelineno-0-12" href="#__codelineno-0-12"></a>
</span><span id="__span-0-13"><a id="__codelineno-0-13" name="__codelineno-0-13" href="#__codelineno-0-13"></a><span class="n">chain</span><span class="p">:</span> <span class="n">Runnable</span> <span class="o">=</span> <span class="n">prompt</span> <span class="o">|</span> <span class="n">model</span> <span class="o">|</span> <span class="p">{</span><span class="s2">&quot;str&quot;</span><span class="p">:</span> <span class="n">StrOutputParser</span><span class="p">()}</span>
</span><span id="__span-0-14"><a id="__codelineno-0-14" name="__codelineno-0-14" href="#__codelineno-0-14"></a>
</span><span id="__span-0-15"><a id="__codelineno-0-15" name="__codelineno-0-15" href="#__codelineno-0-15"></a><span class="n">chain_with_assign</span> <span class="o">=</span> <span class="n">chain</span><span class="o">.</span><span class="n">assign</span><span class="p">(</span><span class="n">hello</span><span class="o">=</span><span class="n">itemgetter</span><span class="p">(</span><span class="s2">&quot;str&quot;</span><span class="p">)</span> <span class="o">|</span> <span class="n">model</span><span class="p">)</span>
</span><span id="__span-0-16"><a id="__codelineno-0-16" name="__codelineno-0-16" href="#__codelineno-0-16"></a>
</span><span id="__span-0-17"><a id="__codelineno-0-17" name="__codelineno-0-17" href="#__codelineno-0-17"></a><span class="nb">print</span><span class="p">(</span><span class="n">chain_with_assign</span><span class="o">.</span><span class="n">input_schema</span><span class="o">.</span><span class="n">model_json_schema</span><span class="p">())</span>
</span><span id="__span-0-18"><a id="__codelineno-0-18" name="__codelineno-0-18" href="#__codelineno-0-18"></a><span class="c1"># {&#39;title&#39;: &#39;PromptInput&#39;, &#39;type&#39;: &#39;object&#39;, &#39;properties&#39;:</span>
</span><span id="__span-0-19"><a id="__codelineno-0-19" name="__codelineno-0-19" href="#__codelineno-0-19"></a><span class="p">{</span><span class="s1">&#39;question&#39;</span><span class="p">:</span> <span class="p">{</span><span class="s1">&#39;title&#39;</span><span class="p">:</span> <span class="s1">&#39;Question&#39;</span><span class="p">,</span> <span class="s1">&#39;type&#39;</span><span class="p">:</span> <span class="s1">&#39;string&#39;</span><span class="p">}}}</span>
</span><span id="__span-0-20"><a id="__codelineno-0-20" name="__codelineno-0-20" href="#__codelineno-0-20"></a><span class="nb">print</span><span class="p">(</span><span class="n">chain_with_assign</span><span class="o">.</span><span class="n">output_schema</span><span class="o">.</span><span class="n">model_json_schema</span><span class="p">())</span>
</span><span id="__span-0-21"><a id="__codelineno-0-21" name="__codelineno-0-21" href="#__codelineno-0-21"></a><span class="c1"># {&#39;title&#39;: &#39;RunnableSequenceOutput&#39;, &#39;type&#39;: &#39;object&#39;, &#39;properties&#39;:</span>
</span><span id="__span-0-22"><a id="__codelineno-0-22" name="__codelineno-0-22" href="#__codelineno-0-22"></a><span class="p">{</span><span class="s1">&#39;str&#39;</span><span class="p">:</span> <span class="p">{</span><span class="s1">&#39;title&#39;</span><span class="p">:</span> <span class="s1">&#39;Str&#39;</span><span class="p">,</span>
</span><span id="__span-0-23"><a id="__codelineno-0-23" name="__codelineno-0-23" href="#__codelineno-0-23"></a><span class="s1">&#39;type&#39;</span><span class="p">:</span> <span class="s1">&#39;string&#39;</span><span class="p">},</span> <span class="s1">&#39;hello&#39;</span><span class="p">:</span> <span class="p">{</span><span class="s1">&#39;title&#39;</span><span class="p">:</span> <span class="s1">&#39;Hello&#39;</span><span class="p">,</span> <span class="s1">&#39;type&#39;</span><span class="p">:</span> <span class="s1">&#39;string&#39;</span><span class="p">}}}</span>
</span></code></pre></div>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>**kwargs</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A mapping of keys to <code>Runnable</code> or <code>Runnable</code>-like objects
that will be invoked with the entire output dict of this <code>Runnable</code>.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>], <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>] | <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a>[[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>]], <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>] | <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Mapping&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping" target="_blank" rel="noopener">Mapping</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>], <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>] | <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a>[[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>]], <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>]]</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>{}</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableSerializable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.RunnableSerializable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.RunnableSerializable">RunnableSerializable</a>[<a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>, <a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a>]</code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>A new <code>Runnable</code>.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.batch" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">batch</span>


<a href="#langgraph.pregel.remote.RemoteGraph.batch" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">batch</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="n">inputs</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list" target="_blank" rel="noopener">list</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.utils.Input">Input</span></span><span class="p">],</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>    <span class="n">config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list" target="_blank" rel="noopener">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>    <span class="o">*</span><span class="p">,</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="n">return_exceptions</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool" target="_blank" rel="noopener">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list" target="_blank" rel="noopener">list</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.utils.Output">Output</span></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Default implementation runs invoke in parallel using a thread pool executor.</p>
<p>The default implementation of batch works well for IO bound runnables.</p>
<p>Subclasses must override this method if they can batch more efficiently;
e.g., if the underlying <code>Runnable</code> uses an API which supports a batch mode.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>inputs</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A list of inputs to the <code>Runnable</code>.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list" target="_blank" rel="noopener">list</a>[<span title="langchain_core.runnables.utils.Input">Input</span>]</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>config</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A config to use when invoking the <code>Runnable</code>. The config supports
standard keys like <code>'tags'</code>, <code>'metadata'</code> for
tracing purposes, <code>'max_concurrency'</code> for controlling how much work
to do in parallel, and other keys.</p>
<p>Please refer to <code>RunnableConfig</code> for more details.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a> | <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list" target="_blank" rel="noopener">list</a>[<a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_exceptions</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Whether to return exceptions instead of raising them.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool" target="_blank" rel="noopener">bool</a></code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>False</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>**kwargs</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Additional keyword arguments to pass to the <code>Runnable</code>.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>{}</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list" target="_blank" rel="noopener">list</a>[<span title="langchain_core.runnables.utils.Output">Output</span>]</code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>A list of outputs from the <code>Runnable</code>.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.batch_as_completed" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">batch_as_completed</span>


<a href="#langgraph.pregel.remote.RemoteGraph.batch_as_completed" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">batch_as_completed</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="n">inputs</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.utils.Input">Input</span></span><span class="p">],</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>    <span class="n">config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>    <span class="o">*</span><span class="p">,</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="n">return_exceptions</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool" target="_blank" rel="noopener">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Iterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator" target="_blank" rel="noopener">Iterator</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#tuple" target="_blank" rel="noopener">tuple</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int" target="_blank" rel="noopener">int</a></span><span class="p">,</span> <span class="n"><span title="langchain_core.runnables.utils.Output">Output</span></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/exceptions.html#Exception" target="_blank" rel="noopener">Exception</a></span><span class="p">]]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Run <code>invoke</code> in parallel on a list of inputs.</p>
<p>Yields results as they complete.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>inputs</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A list of inputs to the <code>Runnable</code>.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a>[<span title="langchain_core.runnables.utils.Input">Input</span>]</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>config</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A config to use when invoking the <code>Runnable</code>.</p>
<p>The config supports standard keys like <code>'tags'</code>, <code>'metadata'</code> for
tracing purposes, <code>'max_concurrency'</code> for controlling how much work to
do in parallel, and other keys.</p>
<p>Please refer to <code>RunnableConfig</code> for more details.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a> | <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a>[<a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_exceptions</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Whether to return exceptions instead of raising them.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool" target="_blank" rel="noopener">bool</a></code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>False</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>**kwargs</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Additional keyword arguments to pass to the <code>Runnable</code>.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>{}</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">YIELDS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-yields-annotation">
                    <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#tuple" target="_blank" rel="noopener">tuple</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int" target="_blank" rel="noopener">int</a>, <span title="langchain_core.runnables.utils.Output">Output</span> | <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/exceptions.html#Exception" target="_blank" rel="noopener">Exception</a>]</code>
                </span>
            </td>
            <td class="doc-yields-details">
              <div class="doc-md-description">
                <p>Tuples of the index of the input and the output from the <code>Runnable</code>.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.abatch" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">abatch</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

<a href="#langgraph.pregel.remote.RemoteGraph.abatch" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">abatch</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="n">inputs</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list" target="_blank" rel="noopener">list</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.utils.Input">Input</span></span><span class="p">],</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>    <span class="n">config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list" target="_blank" rel="noopener">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>    <span class="o">*</span><span class="p">,</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="n">return_exceptions</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool" target="_blank" rel="noopener">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list" target="_blank" rel="noopener">list</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.utils.Output">Output</span></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Default implementation runs <code>ainvoke</code> in parallel using <code>asyncio.gather</code>.</p>
<p>The default implementation of <code>batch</code> works well for IO bound runnables.</p>
<p>Subclasses must override this method if they can batch more efficiently;
e.g., if the underlying <code>Runnable</code> uses an API which supports a batch mode.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>inputs</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A list of inputs to the <code>Runnable</code>.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list" target="_blank" rel="noopener">list</a>[<span title="langchain_core.runnables.utils.Input">Input</span>]</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>config</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A config to use when invoking the <code>Runnable</code>.</p>
<p>The config supports standard keys like <code>'tags'</code>, <code>'metadata'</code> for
tracing purposes, <code>'max_concurrency'</code> for controlling how much work to
do in parallel, and other keys.</p>
<p>Please refer to <code>RunnableConfig</code> for more details.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a> | <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list" target="_blank" rel="noopener">list</a>[<a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_exceptions</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Whether to return exceptions instead of raising them.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool" target="_blank" rel="noopener">bool</a></code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>False</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>**kwargs</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Additional keyword arguments to pass to the <code>Runnable</code>.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>{}</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list" target="_blank" rel="noopener">list</a>[<span title="langchain_core.runnables.utils.Output">Output</span>]</code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>A list of outputs from the <code>Runnable</code>.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.abatch_as_completed" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">abatch_as_completed</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

<a href="#langgraph.pregel.remote.RemoteGraph.abatch_as_completed" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">abatch_as_completed</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="n">inputs</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.utils.Input">Input</span></span><span class="p">],</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>    <span class="n">config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>    <span class="o">*</span><span class="p">,</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="n">return_exceptions</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool" target="_blank" rel="noopener">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.AsyncIterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator" target="_blank" rel="noopener">AsyncIterator</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#tuple" target="_blank" rel="noopener">tuple</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int" target="_blank" rel="noopener">int</a></span><span class="p">,</span> <span class="n"><span title="langchain_core.runnables.utils.Output">Output</span></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/exceptions.html#Exception" target="_blank" rel="noopener">Exception</a></span><span class="p">]]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Run <code>ainvoke</code> in parallel on a list of inputs.</p>
<p>Yields results as they complete.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>inputs</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A list of inputs to the <code>Runnable</code>.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a>[<span title="langchain_core.runnables.utils.Input">Input</span>]</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>config</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A config to use when invoking the <code>Runnable</code>.</p>
<p>The config supports standard keys like <code>'tags'</code>, <code>'metadata'</code> for
tracing purposes, <code>'max_concurrency'</code> for controlling how much work to
do in parallel, and other keys.</p>
<p>Please refer to <code>RunnableConfig</code> for more details.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a> | <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a>[<a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_exceptions</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Whether to return exceptions instead of raising them.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool" target="_blank" rel="noopener">bool</a></code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>False</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>**kwargs</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Additional keyword arguments to pass to the <code>Runnable</code>.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>{}</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">YIELDS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-yields-annotation">
                    <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.AsyncIterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator" target="_blank" rel="noopener">AsyncIterator</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#tuple" target="_blank" rel="noopener">tuple</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int" target="_blank" rel="noopener">int</a>, <span title="langchain_core.runnables.utils.Output">Output</span> | <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/exceptions.html#Exception" target="_blank" rel="noopener">Exception</a>]]</code>
                </span>
            </td>
            <td class="doc-yields-details">
              <div class="doc-md-description">
                <p>A tuple of the index of the input and the output from the <code>Runnable</code>.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.astream_log" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">astream_log</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

<a href="#langgraph.pregel.remote.RemoteGraph.astream_log" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">astream_log</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="nb">input</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">,</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>    <span class="n">config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>    <span class="o">*</span><span class="p">,</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="n">diff</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool" target="_blank" rel="noopener">bool</a></span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>    <span class="n">with_streamed_output_list</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool" target="_blank" rel="noopener">bool</a></span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a>    <span class="n">include_names</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-8"><a id="__codelineno-0-8" name="__codelineno-0-8" href="#__codelineno-0-8"></a>    <span class="n">include_types</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-9"><a id="__codelineno-0-9" name="__codelineno-0-9" href="#__codelineno-0-9"></a>    <span class="n">include_tags</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-10"><a id="__codelineno-0-10" name="__codelineno-0-10" href="#__codelineno-0-10"></a>    <span class="n">exclude_names</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-11"><a id="__codelineno-0-11" name="__codelineno-0-11" href="#__codelineno-0-11"></a>    <span class="n">exclude_types</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-12"><a id="__codelineno-0-12" name="__codelineno-0-12" href="#__codelineno-0-12"></a>    <span class="n">exclude_tags</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-13"><a id="__codelineno-0-13" name="__codelineno-0-13" href="#__codelineno-0-13"></a>    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">,</span>
</span><span id="__span-0-14"><a id="__codelineno-0-14" name="__codelineno-0-14" href="#__codelineno-0-14"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.AsyncIterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator" target="_blank" rel="noopener">AsyncIterator</a></span><span class="p">[</span><span class="n"><span title="langchain_core.tracers.log_stream.RunLogPatch">RunLogPatch</span></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.AsyncIterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator" target="_blank" rel="noopener">AsyncIterator</a></span><span class="p">[</span><span class="n"><span title="langchain_core.tracers.log_stream.RunLog">RunLog</span></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Stream all output from a <code>Runnable</code>, as reported to the callback system.</p>
<p>This includes all inner runs of LLMs, Retrievers, Tools, etc.</p>
<p>Output is streamed as Log objects, which include a list of
Jsonpatch ops that describe how the state of the run has changed in each
step, and the final state of the run.</p>
<p>The Jsonpatch ops can be applied in order to construct state.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>input</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>The input to the <code>Runnable</code>.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>config</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>The config to use for the <code>Runnable</code>.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>diff</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Whether to yield diffs between each step or the current state.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool" target="_blank" rel="noopener">bool</a></code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>True</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>with_streamed_output_list</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Whether to yield the <code>streamed_output</code> list.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool" target="_blank" rel="noopener">bool</a></code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>True</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_names</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Only include logs with these names.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_types</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Only include logs with these types.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_tags</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Only include logs with these tags.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>exclude_names</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Exclude logs with these names.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>exclude_types</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Exclude logs with these types.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>exclude_tags</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Exclude logs with these tags.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>**kwargs</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Additional keyword arguments to pass to the <code>Runnable</code>.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>{}</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">YIELDS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-yields-annotation">
                    <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.AsyncIterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator" target="_blank" rel="noopener">AsyncIterator</a>[<span title="langchain_core.tracers.log_stream.RunLogPatch">RunLogPatch</span>] | <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.AsyncIterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator" target="_blank" rel="noopener">AsyncIterator</a>[<span title="langchain_core.tracers.log_stream.RunLog">RunLog</span>]</code>
                </span>
            </td>
            <td class="doc-yields-details">
              <div class="doc-md-description">
                <p>A <code>RunLogPatch</code> or <code>RunLog</code> object.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.transform" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">transform</span>


<a href="#langgraph.pregel.remote.RemoteGraph.transform" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">transform</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="nb">input</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Iterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator" target="_blank" rel="noopener">Iterator</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.utils.Input">Input</span></span><span class="p">],</span> <span class="n">config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span> <span class="o">|</span> <span class="kc">None</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Iterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator" target="_blank" rel="noopener">Iterator</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.utils.Output">Output</span></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Transform inputs to outputs.</p>
<p>Default implementation of transform, which buffers input and calls <code>astream</code>.</p>
<p>Subclasses must override this method if they can start producing output while
input is still being generated.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>input</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>An iterator of inputs to the <code>Runnable</code>.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Iterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator" target="_blank" rel="noopener">Iterator</a>[<span title="langchain_core.runnables.utils.Input">Input</span>]</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>config</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>The config to use for the <code>Runnable</code>.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>**kwargs</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Additional keyword arguments to pass to the <code>Runnable</code>.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>{}</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">YIELDS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-yields-annotation">
                    <code><span title="langchain_core.runnables.utils.Output">Output</span></code>
                </span>
            </td>
            <td class="doc-yields-details">
              <div class="doc-md-description">
                <p>The output of the <code>Runnable</code>.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.atransform" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">atransform</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

<a href="#langgraph.pregel.remote.RemoteGraph.atransform" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">atransform</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="nb">input</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.AsyncIterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator" target="_blank" rel="noopener">AsyncIterator</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.utils.Input">Input</span></span><span class="p">],</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>    <span class="n">config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.AsyncIterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator" target="_blank" rel="noopener">AsyncIterator</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.utils.Output">Output</span></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Transform inputs to outputs.</p>
<p>Default implementation of atransform, which buffers input and calls <code>astream</code>.</p>
<p>Subclasses must override this method if they can start producing output while
input is still being generated.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>input</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>An async iterator of inputs to the <code>Runnable</code>.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.AsyncIterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator" target="_blank" rel="noopener">AsyncIterator</a>[<span title="langchain_core.runnables.utils.Input">Input</span>]</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>config</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>The config to use for the <code>Runnable</code>.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>**kwargs</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Additional keyword arguments to pass to the <code>Runnable</code>.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>{}</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">YIELDS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-yields-annotation">
                    <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.AsyncIterator&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator" target="_blank" rel="noopener">AsyncIterator</a>[<span title="langchain_core.runnables.utils.Output">Output</span>]</code>
                </span>
            </td>
            <td class="doc-yields-details">
              <div class="doc-md-description">
                <p>The output of the <code>Runnable</code>.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.bind" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">bind</span>


<a href="#langgraph.pregel.remote.RemoteGraph.bind" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">bind</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.utils.Input">Input</span></span><span class="p">,</span> <span class="n"><span title="langchain_core.runnables.utils.Output">Output</span></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Bind arguments to a <code>Runnable</code>, returning a new <code>Runnable</code>.</p>
<p>Useful when a <code>Runnable</code> in a chain requires an argument that is not
in the output of the previous <code>Runnable</code> or included in the user input.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>**kwargs</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>The arguments to bind to the <code>Runnable</code>.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;typing.Any&lt;/code&gt;" href="https://docs.python.org/3/library/typing.html#typing.Any" target="_blank" rel="noopener">Any</a></code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>{}</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a>[<span title="langchain_core.runnables.utils.Input">Input</span>, <span title="langchain_core.runnables.utils.Output">Output</span>]</code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>A new <code>Runnable</code> with the arguments bound.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>


<details class="example" open>
  <summary>Example</summary>
  <div class="language-python highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">langchain_ollama</span><span class="w"> </span><span class="kn">import</span> <span class="n">ChatOllama</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a><span class="kn">from</span><span class="w"> </span><span class="nn">langchain_core.output_parsers</span><span class="w"> </span><span class="kn">import</span> <span class="n">StrOutputParser</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a><span class="n">model</span> <span class="o">=</span> <span class="n">ChatOllama</span><span class="p">(</span><span class="n">model</span><span class="o">=</span><span class="s2">&quot;llama3.1&quot;</span><span class="p">)</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a><span class="c1"># Without bind</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a><span class="n">chain</span> <span class="o">=</span> <span class="n">model</span> <span class="o">|</span> <span class="n">StrOutputParser</span><span class="p">()</span>
</span><span id="__span-0-8"><a id="__codelineno-0-8" name="__codelineno-0-8" href="#__codelineno-0-8"></a>
</span><span id="__span-0-9"><a id="__codelineno-0-9" name="__codelineno-0-9" href="#__codelineno-0-9"></a><span class="n">chain</span><span class="o">.</span><span class="n">invoke</span><span class="p">(</span><span class="s2">&quot;Repeat quoted words exactly: &#39;One two three four five.&#39;&quot;</span><span class="p">)</span>
</span><span id="__span-0-10"><a id="__codelineno-0-10" name="__codelineno-0-10" href="#__codelineno-0-10"></a><span class="c1"># Output is &#39;One two three four five.&#39;</span>
</span><span id="__span-0-11"><a id="__codelineno-0-11" name="__codelineno-0-11" href="#__codelineno-0-11"></a>
</span><span id="__span-0-12"><a id="__codelineno-0-12" name="__codelineno-0-12" href="#__codelineno-0-12"></a><span class="c1"># With bind</span>
</span><span id="__span-0-13"><a id="__codelineno-0-13" name="__codelineno-0-13" href="#__codelineno-0-13"></a><span class="n">chain</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="n">stop</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;three&quot;</span><span class="p">])</span> <span class="o">|</span> <span class="n">StrOutputParser</span><span class="p">()</span>
</span><span id="__span-0-14"><a id="__codelineno-0-14" name="__codelineno-0-14" href="#__codelineno-0-14"></a>
</span><span id="__span-0-15"><a id="__codelineno-0-15" name="__codelineno-0-15" href="#__codelineno-0-15"></a><span class="n">chain</span><span class="o">.</span><span class="n">invoke</span><span class="p">(</span><span class="s2">&quot;Repeat quoted words exactly: &#39;One two three four five.&#39;&quot;</span><span class="p">)</span>
</span><span id="__span-0-16"><a id="__codelineno-0-16" name="__codelineno-0-16" href="#__codelineno-0-16"></a><span class="c1"># Output is &#39;One two&#39;</span>
</span></code></pre></div>
</details>
    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.with_listeners" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">with_listeners</span>


<a href="#langgraph.pregel.remote.RemoteGraph.with_listeners" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">with_listeners</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="o">*</span><span class="p">,</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>    <span class="n">on_start</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a></span><span class="p">[[</span><span class="n"><span title="langchain_core.tracers.schemas.Run">Run</span></span><span class="p">],</span> <span class="kc">None</span><span class="p">]</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>    <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a></span><span class="p">[[</span><span class="n"><span title="langchain_core.tracers.schemas.Run">Run</span></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span><span class="p">],</span> <span class="kc">None</span><span class="p">]</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>    <span class="n">on_end</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a></span><span class="p">[[</span><span class="n"><span title="langchain_core.tracers.schemas.Run">Run</span></span><span class="p">],</span> <span class="kc">None</span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a></span><span class="p">[[</span><span class="n"><span title="langchain_core.tracers.schemas.Run">Run</span></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span><span class="p">],</span> <span class="kc">None</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a>    <span class="n">on_error</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a></span><span class="p">[[</span><span class="n"><span title="langchain_core.tracers.schemas.Run">Run</span></span><span class="p">],</span> <span class="kc">None</span><span class="p">]</span>
</span><span id="__span-0-8"><a id="__codelineno-0-8" name="__codelineno-0-8" href="#__codelineno-0-8"></a>    <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a></span><span class="p">[[</span><span class="n"><span title="langchain_core.tracers.schemas.Run">Run</span></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a></span><span class="p">],</span> <span class="kc">None</span><span class="p">]</span>
</span><span id="__span-0-9"><a id="__codelineno-0-9" name="__codelineno-0-9" href="#__codelineno-0-9"></a>    <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-10"><a id="__codelineno-0-10" name="__codelineno-0-10" href="#__codelineno-0-10"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.utils.Input">Input</span></span><span class="p">,</span> <span class="n"><span title="langchain_core.runnables.utils.Output">Output</span></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Bind lifecycle listeners to a <code>Runnable</code>, returning a new <code>Runnable</code>.</p>
<p>The Run object contains information about the run, including its <code>id</code>,
<code>type</code>, <code>input</code>, <code>output</code>, <code>error</code>, <code>start_time</code>, <code>end_time</code>, and
any tags or metadata added to the run.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>on_start</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Called before the <code>Runnable</code> starts running, with the <code>Run</code>
object.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a>[[<span title="langchain_core.tracers.schemas.Run">Run</span>], None] | <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a>[[<span title="langchain_core.tracers.schemas.Run">Run</span>, <a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a>], None] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_end</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Called after the <code>Runnable</code> finishes running, with the <code>Run</code>
object.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a>[[<span title="langchain_core.tracers.schemas.Run">Run</span>], None] | <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a>[[<span title="langchain_core.tracers.schemas.Run">Run</span>, <a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a>], None] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_error</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Called if the <code>Runnable</code> throws an error, with the <code>Run</code>
object.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a>[[<span title="langchain_core.tracers.schemas.Run">Run</span>], None] | <a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Callable&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable" target="_blank" rel="noopener">Callable</a>[[<span title="langchain_core.tracers.schemas.Run">Run</span>, <a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;RunnableConfig&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.config.RunnableConfig&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig">RunnableConfig</a>], None] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a>[<span title="langchain_core.runnables.utils.Input">Input</span>, <span title="langchain_core.runnables.utils.Output">Output</span>]</code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>A new <code>Runnable</code> with the listeners bound.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>


<details class="example" open>
  <summary>Example</summary>
  <div class="language-python highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">langchain_core.runnables</span><span class="w"> </span><span class="kn">import</span> <span class="n">RunnableLambda</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a><span class="kn">from</span><span class="w"> </span><span class="nn">langchain_core.tracers.schemas</span><span class="w"> </span><span class="kn">import</span> <span class="n">Run</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a><span class="kn">import</span><span class="w"> </span><span class="nn">time</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a><span class="k">def</span><span class="w"> </span><span class="nf">test_runnable</span><span class="p">(</span><span class="n">time_to_sleep</span><span class="p">:</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="__span-0-8"><a id="__codelineno-0-8" name="__codelineno-0-8" href="#__codelineno-0-8"></a>    <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="n">time_to_sleep</span><span class="p">)</span>
</span><span id="__span-0-9"><a id="__codelineno-0-9" name="__codelineno-0-9" href="#__codelineno-0-9"></a>
</span><span id="__span-0-10"><a id="__codelineno-0-10" name="__codelineno-0-10" href="#__codelineno-0-10"></a>
</span><span id="__span-0-11"><a id="__codelineno-0-11" name="__codelineno-0-11" href="#__codelineno-0-11"></a><span class="k">def</span><span class="w"> </span><span class="nf">fn_start</span><span class="p">(</span><span class="n">run_obj</span><span class="p">:</span> <span class="n">Run</span><span class="p">):</span>
</span><span id="__span-0-12"><a id="__codelineno-0-12" name="__codelineno-0-12" href="#__codelineno-0-12"></a>    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;start_time:&quot;</span><span class="p">,</span> <span class="n">run_obj</span><span class="o">.</span><span class="n">start_time</span><span class="p">)</span>
</span><span id="__span-0-13"><a id="__codelineno-0-13" name="__codelineno-0-13" href="#__codelineno-0-13"></a>
</span><span id="__span-0-14"><a id="__codelineno-0-14" name="__codelineno-0-14" href="#__codelineno-0-14"></a>
</span><span id="__span-0-15"><a id="__codelineno-0-15" name="__codelineno-0-15" href="#__codelineno-0-15"></a><span class="k">def</span><span class="w"> </span><span class="nf">fn_end</span><span class="p">(</span><span class="n">run_obj</span><span class="p">:</span> <span class="n">Run</span><span class="p">):</span>
</span><span id="__span-0-16"><a id="__codelineno-0-16" name="__codelineno-0-16" href="#__codelineno-0-16"></a>    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;end_time:&quot;</span><span class="p">,</span> <span class="n">run_obj</span><span class="o">.</span><span class="n">end_time</span><span class="p">)</span>
</span><span id="__span-0-17"><a id="__codelineno-0-17" name="__codelineno-0-17" href="#__codelineno-0-17"></a>
</span><span id="__span-0-18"><a id="__codelineno-0-18" name="__codelineno-0-18" href="#__codelineno-0-18"></a>
</span><span id="__span-0-19"><a id="__codelineno-0-19" name="__codelineno-0-19" href="#__codelineno-0-19"></a><span class="n">chain</span> <span class="o">=</span> <span class="n">RunnableLambda</span><span class="p">(</span><span class="n">test_runnable</span><span class="p">)</span><span class="o">.</span><span class="n">with_listeners</span><span class="p">(</span>
</span><span id="__span-0-20"><a id="__codelineno-0-20" name="__codelineno-0-20" href="#__codelineno-0-20"></a>    <span class="n">on_start</span><span class="o">=</span><span class="n">fn_start</span><span class="p">,</span> <span class="n">on_end</span><span class="o">=</span><span class="n">fn_end</span>
</span><span id="__span-0-21"><a id="__codelineno-0-21" name="__codelineno-0-21" href="#__codelineno-0-21"></a><span class="p">)</span>
</span><span id="__span-0-22"><a id="__codelineno-0-22" name="__codelineno-0-22" href="#__codelineno-0-22"></a><span class="n">chain</span><span class="o">.</span><span class="n">invoke</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
</span></code></pre></div>
</details>
    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.with_alisteners" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">with_alisteners</span>


<a href="#langgraph.pregel.remote.RemoteGraph.with_alisteners" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">with_alisteners</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="o">*</span><span class="p">,</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>    <span class="n">on_start</span><span class="p">:</span> <span class="n"><span title="langchain_core.tracers.root_listeners.AsyncListener">AsyncListener</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>    <span class="n">on_end</span><span class="p">:</span> <span class="n"><span title="langchain_core.tracers.root_listeners.AsyncListener">AsyncListener</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="n">on_error</span><span class="p">:</span> <span class="n"><span title="langchain_core.tracers.root_listeners.AsyncListener">AsyncListener</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.utils.Input">Input</span></span><span class="p">,</span> <span class="n"><span title="langchain_core.runnables.utils.Output">Output</span></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Bind async lifecycle listeners to a <code>Runnable</code>.</p>
<p>Returns a new <code>Runnable</code>.</p>
<p>The Run object contains information about the run, including its <code>id</code>,
<code>type</code>, <code>input</code>, <code>output</code>, <code>error</code>, <code>start_time</code>, <code>end_time</code>, and
any tags or metadata added to the run.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>on_start</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Called asynchronously before the <code>Runnable</code> starts running,
with the <code>Run</code> object.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><span title="langchain_core.tracers.root_listeners.AsyncListener">AsyncListener</span> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_end</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Called asynchronously after the <code>Runnable</code> finishes running,
with the <code>Run</code> object.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><span title="langchain_core.tracers.root_listeners.AsyncListener">AsyncListener</span> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_error</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Called asynchronously if the <code>Runnable</code> throws an error,
with the <code>Run</code> object.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><span title="langchain_core.tracers.root_listeners.AsyncListener">AsyncListener</span> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a>[<span title="langchain_core.runnables.utils.Input">Input</span>, <span title="langchain_core.runnables.utils.Output">Output</span>]</code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>A new <code>Runnable</code> with the listeners bound.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>


<details class="example" open>
  <summary>Example</summary>
  <div class="language-python highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">langchain_core.runnables</span><span class="w"> </span><span class="kn">import</span> <span class="n">RunnableLambda</span><span class="p">,</span> <span class="n">Runnable</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a><span class="kn">from</span><span class="w"> </span><span class="nn">datetime</span><span class="w"> </span><span class="kn">import</span> <span class="n">datetime</span><span class="p">,</span> <span class="n">timezone</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a><span class="kn">import</span><span class="w"> </span><span class="nn">time</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a><span class="kn">import</span><span class="w"> </span><span class="nn">asyncio</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a><span class="k">def</span><span class="w"> </span><span class="nf">format_t</span><span class="p">(</span><span class="n">timestamp</span><span class="p">:</span> <span class="nb">float</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="__span-0-8"><a id="__codelineno-0-8" name="__codelineno-0-8" href="#__codelineno-0-8"></a>    <span class="k">return</span> <span class="n">datetime</span><span class="o">.</span><span class="n">fromtimestamp</span><span class="p">(</span><span class="n">timestamp</span><span class="p">,</span> <span class="n">tz</span><span class="o">=</span><span class="n">timezone</span><span class="o">.</span><span class="n">utc</span><span class="p">)</span><span class="o">.</span><span class="n">isoformat</span><span class="p">()</span>
</span><span id="__span-0-9"><a id="__codelineno-0-9" name="__codelineno-0-9" href="#__codelineno-0-9"></a>
</span><span id="__span-0-10"><a id="__codelineno-0-10" name="__codelineno-0-10" href="#__codelineno-0-10"></a>
</span><span id="__span-0-11"><a id="__codelineno-0-11" name="__codelineno-0-11" href="#__codelineno-0-11"></a><span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">test_runnable</span><span class="p">(</span><span class="n">time_to_sleep</span><span class="p">:</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="__span-0-12"><a id="__codelineno-0-12" name="__codelineno-0-12" href="#__codelineno-0-12"></a>    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Runnable[</span><span class="si">{</span><span class="n">time_to_sleep</span><span class="si">}</span><span class="s2">s]: starts at </span><span class="si">{</span><span class="n">format_t</span><span class="p">(</span><span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">())</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</span><span id="__span-0-13"><a id="__codelineno-0-13" name="__codelineno-0-13" href="#__codelineno-0-13"></a>    <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="n">time_to_sleep</span><span class="p">)</span>
</span><span id="__span-0-14"><a id="__codelineno-0-14" name="__codelineno-0-14" href="#__codelineno-0-14"></a>    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Runnable[</span><span class="si">{</span><span class="n">time_to_sleep</span><span class="si">}</span><span class="s2">s]: ends at </span><span class="si">{</span><span class="n">format_t</span><span class="p">(</span><span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">())</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</span><span id="__span-0-15"><a id="__codelineno-0-15" name="__codelineno-0-15" href="#__codelineno-0-15"></a>
</span><span id="__span-0-16"><a id="__codelineno-0-16" name="__codelineno-0-16" href="#__codelineno-0-16"></a>
</span><span id="__span-0-17"><a id="__codelineno-0-17" name="__codelineno-0-17" href="#__codelineno-0-17"></a><span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">fn_start</span><span class="p">(</span><span class="n">run_obj</span><span class="p">:</span> <span class="n">Runnable</span><span class="p">):</span>
</span><span id="__span-0-18"><a id="__codelineno-0-18" name="__codelineno-0-18" href="#__codelineno-0-18"></a>    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;on start callback starts at </span><span class="si">{</span><span class="n">format_t</span><span class="p">(</span><span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">())</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</span><span id="__span-0-19"><a id="__codelineno-0-19" name="__codelineno-0-19" href="#__codelineno-0-19"></a>    <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
</span><span id="__span-0-20"><a id="__codelineno-0-20" name="__codelineno-0-20" href="#__codelineno-0-20"></a>    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;on start callback ends at </span><span class="si">{</span><span class="n">format_t</span><span class="p">(</span><span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">())</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</span><span id="__span-0-21"><a id="__codelineno-0-21" name="__codelineno-0-21" href="#__codelineno-0-21"></a>
</span><span id="__span-0-22"><a id="__codelineno-0-22" name="__codelineno-0-22" href="#__codelineno-0-22"></a>
</span><span id="__span-0-23"><a id="__codelineno-0-23" name="__codelineno-0-23" href="#__codelineno-0-23"></a><span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">fn_end</span><span class="p">(</span><span class="n">run_obj</span><span class="p">:</span> <span class="n">Runnable</span><span class="p">):</span>
</span><span id="__span-0-24"><a id="__codelineno-0-24" name="__codelineno-0-24" href="#__codelineno-0-24"></a>    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;on end callback starts at </span><span class="si">{</span><span class="n">format_t</span><span class="p">(</span><span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">())</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</span><span id="__span-0-25"><a id="__codelineno-0-25" name="__codelineno-0-25" href="#__codelineno-0-25"></a>    <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
</span><span id="__span-0-26"><a id="__codelineno-0-26" name="__codelineno-0-26" href="#__codelineno-0-26"></a>    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;on end callback ends at </span><span class="si">{</span><span class="n">format_t</span><span class="p">(</span><span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">())</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</span><span id="__span-0-27"><a id="__codelineno-0-27" name="__codelineno-0-27" href="#__codelineno-0-27"></a>
</span><span id="__span-0-28"><a id="__codelineno-0-28" name="__codelineno-0-28" href="#__codelineno-0-28"></a>
</span><span id="__span-0-29"><a id="__codelineno-0-29" name="__codelineno-0-29" href="#__codelineno-0-29"></a><span class="n">runnable</span> <span class="o">=</span> <span class="n">RunnableLambda</span><span class="p">(</span><span class="n">test_runnable</span><span class="p">)</span><span class="o">.</span><span class="n">with_alisteners</span><span class="p">(</span>
</span><span id="__span-0-30"><a id="__codelineno-0-30" name="__codelineno-0-30" href="#__codelineno-0-30"></a>    <span class="n">on_start</span><span class="o">=</span><span class="n">fn_start</span><span class="p">,</span> <span class="n">on_end</span><span class="o">=</span><span class="n">fn_end</span>
</span><span id="__span-0-31"><a id="__codelineno-0-31" name="__codelineno-0-31" href="#__codelineno-0-31"></a><span class="p">)</span>
</span><span id="__span-0-32"><a id="__codelineno-0-32" name="__codelineno-0-32" href="#__codelineno-0-32"></a>
</span><span id="__span-0-33"><a id="__codelineno-0-33" name="__codelineno-0-33" href="#__codelineno-0-33"></a>
</span><span id="__span-0-34"><a id="__codelineno-0-34" name="__codelineno-0-34" href="#__codelineno-0-34"></a><span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">concurrent_runs</span><span class="p">():</span>
</span><span id="__span-0-35"><a id="__codelineno-0-35" name="__codelineno-0-35" href="#__codelineno-0-35"></a>    <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="n">runnable</span><span class="o">.</span><span class="n">ainvoke</span><span class="p">(</span><span class="mi">2</span><span class="p">),</span> <span class="n">runnable</span><span class="o">.</span><span class="n">ainvoke</span><span class="p">(</span><span class="mi">3</span><span class="p">))</span>
</span><span id="__span-0-36"><a id="__codelineno-0-36" name="__codelineno-0-36" href="#__codelineno-0-36"></a>
</span><span id="__span-0-37"><a id="__codelineno-0-37" name="__codelineno-0-37" href="#__codelineno-0-37"></a>
</span><span id="__span-0-38"><a id="__codelineno-0-38" name="__codelineno-0-38" href="#__codelineno-0-38"></a><span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">concurrent_runs</span><span class="p">())</span>
</span><span id="__span-0-39"><a id="__codelineno-0-39" name="__codelineno-0-39" href="#__codelineno-0-39"></a><span class="c1"># Result:</span>
</span><span id="__span-0-40"><a id="__codelineno-0-40" name="__codelineno-0-40" href="#__codelineno-0-40"></a><span class="c1"># on start callback starts at 2025-03-01T07:05:22.875378+00:00</span>
</span><span id="__span-0-41"><a id="__codelineno-0-41" name="__codelineno-0-41" href="#__codelineno-0-41"></a><span class="c1"># on start callback starts at 2025-03-01T07:05:22.875495+00:00</span>
</span><span id="__span-0-42"><a id="__codelineno-0-42" name="__codelineno-0-42" href="#__codelineno-0-42"></a><span class="c1"># on start callback ends at 2025-03-01T07:05:25.878862+00:00</span>
</span><span id="__span-0-43"><a id="__codelineno-0-43" name="__codelineno-0-43" href="#__codelineno-0-43"></a><span class="c1"># on start callback ends at 2025-03-01T07:05:25.878947+00:00</span>
</span><span id="__span-0-44"><a id="__codelineno-0-44" name="__codelineno-0-44" href="#__codelineno-0-44"></a><span class="c1"># Runnable[2s]: starts at 2025-03-01T07:05:25.879392+00:00</span>
</span><span id="__span-0-45"><a id="__codelineno-0-45" name="__codelineno-0-45" href="#__codelineno-0-45"></a><span class="c1"># Runnable[3s]: starts at 2025-03-01T07:05:25.879804+00:00</span>
</span><span id="__span-0-46"><a id="__codelineno-0-46" name="__codelineno-0-46" href="#__codelineno-0-46"></a><span class="c1"># Runnable[2s]: ends at 2025-03-01T07:05:27.881998+00:00</span>
</span><span id="__span-0-47"><a id="__codelineno-0-47" name="__codelineno-0-47" href="#__codelineno-0-47"></a><span class="c1"># on end callback starts at 2025-03-01T07:05:27.882360+00:00</span>
</span><span id="__span-0-48"><a id="__codelineno-0-48" name="__codelineno-0-48" href="#__codelineno-0-48"></a><span class="c1"># Runnable[3s]: ends at 2025-03-01T07:05:28.881737+00:00</span>
</span><span id="__span-0-49"><a id="__codelineno-0-49" name="__codelineno-0-49" href="#__codelineno-0-49"></a><span class="c1"># on end callback starts at 2025-03-01T07:05:28.882428+00:00</span>
</span><span id="__span-0-50"><a id="__codelineno-0-50" name="__codelineno-0-50" href="#__codelineno-0-50"></a><span class="c1"># on end callback ends at 2025-03-01T07:05:29.883893+00:00</span>
</span><span id="__span-0-51"><a id="__codelineno-0-51" name="__codelineno-0-51" href="#__codelineno-0-51"></a><span class="c1"># on end callback ends at 2025-03-01T07:05:30.884831+00:00</span>
</span></code></pre></div>
</details>
    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.with_types" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">with_types</span>


<a href="#langgraph.pregel.remote.RemoteGraph.with_types" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">with_types</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="o">*</span><span class="p">,</span> <span class="n">input_type</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type" target="_blank" rel="noopener">type</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.utils.Input">Input</span></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">output_type</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type" target="_blank" rel="noopener">type</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.utils.Output">Output</span></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.utils.Input">Input</span></span><span class="p">,</span> <span class="n"><span title="langchain_core.runnables.utils.Output">Output</span></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Bind input and output types to a <code>Runnable</code>, returning a new <code>Runnable</code>.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>input_type</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>The input type to bind to the <code>Runnable</code>.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type" target="_blank" rel="noopener">type</a>[<span title="langchain_core.runnables.utils.Input">Input</span>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>output_type</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>The output type to bind to the <code>Runnable</code>.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type" target="_blank" rel="noopener">type</a>[<span title="langchain_core.runnables.utils.Output">Output</span>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a>[<span title="langchain_core.runnables.utils.Input">Input</span>, <span title="langchain_core.runnables.utils.Output">Output</span>]</code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>A new <code>Runnable</code> with the types bound.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.with_retry" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">with_retry</span>


<a href="#langgraph.pregel.remote.RemoteGraph.with_retry" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">with_retry</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="o">*</span><span class="p">,</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>    <span class="n">retry_if_exception_type</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#tuple" target="_blank" rel="noopener">tuple</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type" target="_blank" rel="noopener">type</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/exceptions.html#BaseException" target="_blank" rel="noopener">BaseException</a></span><span class="p">],</span> <span class="o">...</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/exceptions.html#Exception" target="_blank" rel="noopener">Exception</a></span><span class="p">,),</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>    <span class="n">wait_exponential_jitter</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool" target="_blank" rel="noopener">bool</a></span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="n">exponential_jitter_params</span><span class="p">:</span> <span class="n"><span title="langchain_core.runnables.retry.ExponentialJitterParams">ExponentialJitterParams</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>    <span class="n">stop_after_attempt</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int" target="_blank" rel="noopener">int</a></span> <span class="o">=</span> <span class="mi">3</span><span class="p">,</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.utils.Input">Input</span></span><span class="p">,</span> <span class="n"><span title="langchain_core.runnables.utils.Output">Output</span></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Create a new <code>Runnable</code> that retries the original <code>Runnable</code> on exceptions.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>retry_if_exception_type</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A tuple of exception types to retry on.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#tuple" target="_blank" rel="noopener">tuple</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type" target="_blank" rel="noopener">type</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/exceptions.html#BaseException" target="_blank" rel="noopener">BaseException</a>], ...]</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>(<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/exceptions.html#Exception" target="_blank" rel="noopener">Exception</a>,)</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>wait_exponential_jitter</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Whether to add jitter to the wait
time between retries.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool" target="_blank" rel="noopener">bool</a></code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>True</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>stop_after_attempt</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>The maximum number of attempts to make before
giving up.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int" target="_blank" rel="noopener">int</a></code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>3</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>exponential_jitter_params</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>Parameters for
<code>tenacity.wait_exponential_jitter</code>. Namely: <code>initial</code>, <code>max</code>,
<code>exp_base</code>, and <code>jitter</code> (all <code>float</code> values).</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><span title="langchain_core.runnables.retry.ExponentialJitterParams">ExponentialJitterParams</span> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a>[<span title="langchain_core.runnables.utils.Input">Input</span>, <span title="langchain_core.runnables.utils.Output">Output</span>]</code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>A new <code>Runnable</code> that retries the original <code>Runnable</code> on exceptions.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>


<details class="example" open>
  <summary>Example</summary>
  <div class="language-python highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">langchain_core.runnables</span><span class="w"> </span><span class="kn">import</span> <span class="n">RunnableLambda</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a><span class="n">count</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a><span class="k">def</span><span class="w"> </span><span class="nf">_lambda</span><span class="p">(</span><span class="n">x</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a>    <span class="k">global</span> <span class="n">count</span>
</span><span id="__span-0-8"><a id="__codelineno-0-8" name="__codelineno-0-8" href="#__codelineno-0-8"></a>    <span class="n">count</span> <span class="o">=</span> <span class="n">count</span> <span class="o">+</span> <span class="mi">1</span>
</span><span id="__span-0-9"><a id="__codelineno-0-9" name="__codelineno-0-9" href="#__codelineno-0-9"></a>    <span class="k">if</span> <span class="n">x</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="__span-0-10"><a id="__codelineno-0-10" name="__codelineno-0-10" href="#__codelineno-0-10"></a>        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">&quot;x is 1&quot;</span><span class="p">)</span>
</span><span id="__span-0-11"><a id="__codelineno-0-11" name="__codelineno-0-11" href="#__codelineno-0-11"></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="__span-0-12"><a id="__codelineno-0-12" name="__codelineno-0-12" href="#__codelineno-0-12"></a>        <span class="k">pass</span>
</span><span id="__span-0-13"><a id="__codelineno-0-13" name="__codelineno-0-13" href="#__codelineno-0-13"></a>
</span><span id="__span-0-14"><a id="__codelineno-0-14" name="__codelineno-0-14" href="#__codelineno-0-14"></a>
</span><span id="__span-0-15"><a id="__codelineno-0-15" name="__codelineno-0-15" href="#__codelineno-0-15"></a><span class="n">runnable</span> <span class="o">=</span> <span class="n">RunnableLambda</span><span class="p">(</span><span class="n">_lambda</span><span class="p">)</span>
</span><span id="__span-0-16"><a id="__codelineno-0-16" name="__codelineno-0-16" href="#__codelineno-0-16"></a><span class="k">try</span><span class="p">:</span>
</span><span id="__span-0-17"><a id="__codelineno-0-17" name="__codelineno-0-17" href="#__codelineno-0-17"></a>    <span class="n">runnable</span><span class="o">.</span><span class="n">with_retry</span><span class="p">(</span>
</span><span id="__span-0-18"><a id="__codelineno-0-18" name="__codelineno-0-18" href="#__codelineno-0-18"></a>        <span class="n">stop_after_attempt</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
</span><span id="__span-0-19"><a id="__codelineno-0-19" name="__codelineno-0-19" href="#__codelineno-0-19"></a>        <span class="n">retry_if_exception_type</span><span class="o">=</span><span class="p">(</span><span class="ne">ValueError</span><span class="p">,),</span>
</span><span id="__span-0-20"><a id="__codelineno-0-20" name="__codelineno-0-20" href="#__codelineno-0-20"></a>    <span class="p">)</span><span class="o">.</span><span class="n">invoke</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</span><span id="__span-0-21"><a id="__codelineno-0-21" name="__codelineno-0-21" href="#__codelineno-0-21"></a><span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
</span><span id="__span-0-22"><a id="__codelineno-0-22" name="__codelineno-0-22" href="#__codelineno-0-22"></a>    <span class="k">pass</span>
</span><span id="__span-0-23"><a id="__codelineno-0-23" name="__codelineno-0-23" href="#__codelineno-0-23"></a>
</span><span id="__span-0-24"><a id="__codelineno-0-24" name="__codelineno-0-24" href="#__codelineno-0-24"></a><span class="k">assert</span> <span class="n">count</span> <span class="o">==</span> <span class="mi">2</span>
</span></code></pre></div>
</details>
    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.map" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">map</span>


<a href="#langgraph.pregel.remote.RemoteGraph.map" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">map</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list" target="_blank" rel="noopener">list</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.utils.Input">Input</span></span><span class="p">],</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list" target="_blank" rel="noopener">list</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.utils.Output">Output</span></span><span class="p">]]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Return a new <code>Runnable</code> that maps a list of inputs to a list of outputs.</p>
<p>Calls <code>invoke</code> with each input.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list" target="_blank" rel="noopener">list</a>[<span title="langchain_core.runnables.utils.Input">Input</span>], <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list" target="_blank" rel="noopener">list</a>[<span title="langchain_core.runnables.utils.Output">Output</span>]]</code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>A new <code>Runnable</code> that maps a list of inputs to a list of outputs.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>


<details class="example" open>
  <summary>Example</summary>
  <div class="language-python highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">langchain_core.runnables</span><span class="w"> </span><span class="kn">import</span> <span class="n">RunnableLambda</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a><span class="k">def</span><span class="w"> </span><span class="nf">_lambda</span><span class="p">(</span><span class="n">x</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="k">return</span> <span class="n">x</span> <span class="o">+</span> <span class="mi">1</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a>
</span><span id="__span-0-8"><a id="__codelineno-0-8" name="__codelineno-0-8" href="#__codelineno-0-8"></a><span class="n">runnable</span> <span class="o">=</span> <span class="n">RunnableLambda</span><span class="p">(</span><span class="n">_lambda</span><span class="p">)</span>
</span><span id="__span-0-9"><a id="__codelineno-0-9" name="__codelineno-0-9" href="#__codelineno-0-9"></a><span class="nb">print</span><span class="p">(</span><span class="n">runnable</span><span class="o">.</span><span class="n">map</span><span class="p">()</span><span class="o">.</span><span class="n">invoke</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]))</span>  <span class="c1"># [2, 3, 4]</span>
</span></code></pre></div>
</details>
    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.with_fallbacks" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">with_fallbacks</span>


<a href="#langgraph.pregel.remote.RemoteGraph.with_fallbacks" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">with_fallbacks</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="n">fallbacks</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.utils.Input">Input</span></span><span class="p">,</span> <span class="n"><span title="langchain_core.runnables.utils.Output">Output</span></span><span class="p">]],</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>    <span class="o">*</span><span class="p">,</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>    <span class="n">exceptions_to_handle</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#tuple" target="_blank" rel="noopener">tuple</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type" target="_blank" rel="noopener">type</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/exceptions.html#BaseException" target="_blank" rel="noopener">BaseException</a></span><span class="p">],</span> <span class="o">...</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/exceptions.html#Exception" target="_blank" rel="noopener">Exception</a></span><span class="p">,),</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="n">exception_key</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><span title="langchain_core.runnables.fallbacks.RunnableWithFallbacks">RunnableWithFallbacks</span></span><span class="p">[</span><span class="n"><span title="langchain_core.runnables.utils.Input">Input</span></span><span class="p">,</span> <span class="n"><span title="langchain_core.runnables.utils.Output">Output</span></span><span class="p">]</span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Add fallbacks to a <code>Runnable</code>, returning a new <code>Runnable</code>.</p>
<p>The new <code>Runnable</code> will try the original <code>Runnable</code>, and then each fallback
in order, upon failures.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>fallbacks</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A sequence of runnables to try if the original <code>Runnable</code>
fails.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a>[<a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a>[<span title="langchain_core.runnables.utils.Input">Input</span>, <span title="langchain_core.runnables.utils.Output">Output</span>]]</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>exceptions_to_handle</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A tuple of exception types to handle.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#tuple" target="_blank" rel="noopener">tuple</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type" target="_blank" rel="noopener">type</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/exceptions.html#BaseException" target="_blank" rel="noopener">BaseException</a>], ...]</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>(<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/exceptions.html#Exception" target="_blank" rel="noopener">Exception</a>,)</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>exception_key</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>If <code>string</code> is specified then handled exceptions will be
passed to fallbacks as part of the input under the specified key.</p>
<p>If <code>None</code>, exceptions will not be passed to fallbacks.</p>
<p>If used, the base <code>Runnable</code> and its fallbacks must accept a
dictionary as input.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><span title="langchain_core.runnables.fallbacks.RunnableWithFallbacks">RunnableWithFallbacks</span>[<span title="langchain_core.runnables.utils.Input">Input</span>, <span title="langchain_core.runnables.utils.Output">Output</span>]</code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>A new <code>Runnable</code> that will try the original <code>Runnable</code>, and then each
Fallback in order, upon failures.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>


<details class="example" open>
  <summary>Example</summary>
  <div class="language-python highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">typing</span><span class="w"> </span><span class="kn">import</span> <span class="n">Iterator</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a><span class="kn">from</span><span class="w"> </span><span class="nn">langchain_core.runnables</span><span class="w"> </span><span class="kn">import</span> <span class="n">RunnableGenerator</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a><span class="k">def</span><span class="w"> </span><span class="nf">_generate_immediate_error</span><span class="p">(</span><span class="nb">input</span><span class="p">:</span> <span class="n">Iterator</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Iterator</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a>    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">()</span>
</span><span id="__span-0-8"><a id="__codelineno-0-8" name="__codelineno-0-8" href="#__codelineno-0-8"></a>    <span class="k">yield</span> <span class="s2">&quot;&quot;</span>
</span><span id="__span-0-9"><a id="__codelineno-0-9" name="__codelineno-0-9" href="#__codelineno-0-9"></a>
</span><span id="__span-0-10"><a id="__codelineno-0-10" name="__codelineno-0-10" href="#__codelineno-0-10"></a>
</span><span id="__span-0-11"><a id="__codelineno-0-11" name="__codelineno-0-11" href="#__codelineno-0-11"></a><span class="k">def</span><span class="w"> </span><span class="nf">_generate</span><span class="p">(</span><span class="nb">input</span><span class="p">:</span> <span class="n">Iterator</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Iterator</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
</span><span id="__span-0-12"><a id="__codelineno-0-12" name="__codelineno-0-12" href="#__codelineno-0-12"></a>    <span class="k">yield from</span> <span class="s2">&quot;foo bar&quot;</span>
</span><span id="__span-0-13"><a id="__codelineno-0-13" name="__codelineno-0-13" href="#__codelineno-0-13"></a>
</span><span id="__span-0-14"><a id="__codelineno-0-14" name="__codelineno-0-14" href="#__codelineno-0-14"></a>
</span><span id="__span-0-15"><a id="__codelineno-0-15" name="__codelineno-0-15" href="#__codelineno-0-15"></a><span class="n">runnable</span> <span class="o">=</span> <span class="n">RunnableGenerator</span><span class="p">(</span><span class="n">_generate_immediate_error</span><span class="p">)</span><span class="o">.</span><span class="n">with_fallbacks</span><span class="p">(</span>
</span><span id="__span-0-16"><a id="__codelineno-0-16" name="__codelineno-0-16" href="#__codelineno-0-16"></a>    <span class="p">[</span><span class="n">RunnableGenerator</span><span class="p">(</span><span class="n">_generate</span><span class="p">)]</span>
</span><span id="__span-0-17"><a id="__codelineno-0-17" name="__codelineno-0-17" href="#__codelineno-0-17"></a><span class="p">)</span>
</span><span id="__span-0-18"><a id="__codelineno-0-18" name="__codelineno-0-18" href="#__codelineno-0-18"></a><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">runnable</span><span class="o">.</span><span class="n">stream</span><span class="p">({})))</span>  <span class="c1"># foo bar</span>
</span></code></pre></div>
</details>

<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>fallbacks</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A sequence of runnables to try if the original <code>Runnable</code>
fails.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" title="&lt;code&gt;collections.abc.Sequence&lt;/code&gt;" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence" target="_blank" rel="noopener">Sequence</a>[<a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;Runnable&lt;/span&gt; (&lt;code&gt;langchain_core.runnables.base.Runnable&lt;/code&gt;)" href="../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable">Runnable</a>[<span title="langchain_core.runnables.utils.Input">Input</span>, <span title="langchain_core.runnables.utils.Output">Output</span>]]</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>exceptions_to_handle</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A tuple of exception types to handle.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#tuple" target="_blank" rel="noopener">tuple</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type" target="_blank" rel="noopener">type</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/exceptions.html#BaseException" target="_blank" rel="noopener">BaseException</a>], ...]</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>(<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/exceptions.html#Exception" target="_blank" rel="noopener">Exception</a>,)</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>exception_key</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>If <code>string</code> is specified then handled exceptions will be
passed to fallbacks as part of the input under the specified key.</p>
<p>If <code>None</code>, exceptions will not be passed to fallbacks.</p>
<p>If used, the base <code>Runnable</code> and its fallbacks must accept a
dictionary as input.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><span title="langchain_core.runnables.fallbacks.RunnableWithFallbacks">RunnableWithFallbacks</span>[<span title="langchain_core.runnables.utils.Input">Input</span>, <span title="langchain_core.runnables.utils.Output">Output</span>]</code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>A new <code>Runnable</code> that will try the original <code>Runnable</code>, and then each
Fallback in order, upon failures.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>

    </div>

</div>  

<div class="doc doc-object doc-function">

<h4 id="langgraph.pregel.remote.RemoteGraph.as_tool" class="doc doc-heading">      
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code>            <span class="doc doc-object-name doc-function-name">as_tool</span>


<a href="#langgraph.pregel.remote.RemoteGraph.as_tool" class="headerlink" title="Copy anchor link to this section for reference">&para;</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="nf">as_tool</span><span class="p">(</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a>    <span class="n">args_schema</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type" target="_blank" rel="noopener">type</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" title="&lt;code&gt;pydantic.BaseModel&lt;/code&gt;" href="https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel" target="_blank" rel="noopener">BaseModel</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>    <span class="o">*</span><span class="p">,</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>    <span class="n">name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a>    <span class="n">description</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>    <span class="n">arg_types</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type" target="_blank" rel="noopener">type</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;BaseTool&lt;/span&gt; (&lt;code&gt;langchain_core.tools.BaseTool&lt;/code&gt;)" href="../../../langchain/tools/#langchain.tools.BaseTool">BaseTool</a></span>
</span></code></pre></div>

    <div class="doc doc-contents ">

        <p>Create a <code>BaseTool</code> from a <code>Runnable</code>.</p>
<p><code>as_tool</code> will instantiate a <code>BaseTool</code> with a name, description, and
<code>args_schema</code> from a <code>Runnable</code>. Where possible, schemas are inferred
from <code>runnable.get_input_schema</code>.</p>
<p>Alternatively (e.g., if the <code>Runnable</code> takes a dict as input and the specific
<code>dict</code> keys are not typed), the schema can be specified directly with
<code>args_schema</code>.</p>
<p>You can also pass <code>arg_types</code> to just specify the required arguments and their
types.</p>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">PARAMETER</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>args_schema</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>The schema for the tool.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type" target="_blank" rel="noopener">type</a>[<a class="autorefs autorefs-external" title="&lt;code&gt;pydantic.BaseModel&lt;/code&gt;" href="https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel" target="_blank" rel="noopener">BaseModel</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>name</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>The name of the tool.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>description</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>The description of the tool.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a> | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>arg_types</code>
            </td>
            <td class="doc-param-details">
              <div class="doc-md-description">
                <p>A dictionary of argument names to types.</p>
              </div>
              <p>
                  <span class="doc-param-annotation">
                    <b>TYPE:</b>
                      <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict" target="_blank" rel="noopener">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str" target="_blank" rel="noopener">str</a>, <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type" target="_blank" rel="noopener">type</a>] | None</code>
                  </span>
                  <span class="doc-param-default">
                    <b>DEFAULT:</b>
                      <code>None</code>
                  </span>
              </p>
            </td>
          </tr>
      </tbody>
    </table>


<table>
      <thead>
        <tr>
          <th><span class="doc-section-title">RETURNS</span></th>
          <th><span>DESCRIPTION</span></th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <span class="doc-returns-annotation">
                    <code><a class="autorefs autorefs-internal" title="&lt;code class=&quot;doc-symbol doc-symbol-heading doc-symbol-class&quot;&gt;&lt;/code&gt;            &lt;span class=&quot;doc doc-object-name doc-class-name&quot;&gt;BaseTool&lt;/span&gt; (&lt;code&gt;langchain_core.tools.BaseTool&lt;/code&gt;)" href="../../../langchain/tools/#langchain.tools.BaseTool">BaseTool</a></code>
                </span>
            </td>
            <td class="doc-returns-details">
              <div class="doc-md-description">
                <p>A <code>BaseTool</code> instance.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>
        <div class="admonition example">
<p class="admonition-title"><code>TypedDict</code> input</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">typing_extensions</span><span class="w"> </span><span class="kn">import</span> <span class="n">TypedDict</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a><span class="kn">from</span><span class="w"> </span><span class="nn">langchain_core.runnables</span><span class="w"> </span><span class="kn">import</span> <span class="n">RunnableLambda</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4" href="#__codelineno-0-4"></a>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5" href="#__codelineno-0-5"></a><span class="k">class</span><span class="w"> </span><span class="nc">Args</span><span class="p">(</span><span class="n">TypedDict</span><span class="p">):</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6" href="#__codelineno-0-6"></a>    <span class="n">a</span><span class="p">:</span> <span class="nb">int</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7" href="#__codelineno-0-7"></a>    <span class="n">b</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span>
</span><span id="__span-0-8"><a id="__codelineno-0-8" name="__codelineno-0-8" href="#__codelineno-0-8"></a>
</span><span id="__span-0-9"><a id="__codelineno-0-9" name="__codelineno-0-9" href="#__codelineno-0-9"></a>
</span><span id="__span-0-10"><a id="__codelineno-0-10" name="__codelineno-0-10" href="#__codelineno-0-10"></a><span class="k">def</span><span class="w"> </span><span class="nf">f</span><span class="p">(</span><span class="n">x</span><span class="p">:</span> <span class="n">Args</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="__span-0-11"><a id="__codelineno-0-11" name="__codelineno-0-11" href="#__codelineno-0-11"></a>    <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="n">x</span><span class="p">[</span><span class="s2">&quot;a&quot;</span><span class="p">]</span> <span class="o">*</span> <span class="nb">max</span><span class="p">(</span><span class="n">x</span><span class="p">[</span><span class="s2">&quot;b&quot;</span><span class="p">]))</span>
</span><span id="__span-0-12"><a id="__codelineno-0-12" name="__codelineno-0-12" href="#__codelineno-0-12"></a>
</span><span id="__span-0-13"><a id="__codelineno-0-13" name="__codelineno-0-13" href="#__codelineno-0-13"></a>
</span><span id="__span-0-14"><a id="__codelineno-0-14" name="__codelineno-0-14" href="#__codelineno-0-14"></a><span class="n">runnable</span> <span class="o">=</span> <span class="n">RunnableLambda</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
</span><span id="__span-0-15"><a id="__codelineno-0-15" name="__codelineno-0-15" href="#__codelineno-0-15"></a><span class="n">as_tool</span> <span class="o">=</span> <span class="n">runnable</span><span class="o">.</span><span class="n">as_tool</span><span class="p">()</span>
</span><span id="__span-0-16"><a id="__codelineno-0-16" name="__codelineno-0-16" href="#__codelineno-0-16"></a><span class="n">as_tool</span><span class="o">.</span><span class="n">invoke</span><span class="p">({</span><span class="s2">&quot;a&quot;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span> <span class="s2">&quot;b&quot;</span><span class="p">:</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">]})</span>
</span></code></pre></div>
</div>
<div class="admonition example">
<p class="admonition-title"><code>dict</code> input, specifying schema via <code>args_schema</code></p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-1-1"><a id="__codelineno-1-1" name="__codelineno-1-1" href="#__codelineno-1-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">typing</span><span class="w"> </span><span class="kn">import</span> <span class="n">Any</span>
</span><span id="__span-1-2"><a id="__codelineno-1-2" name="__codelineno-1-2" href="#__codelineno-1-2"></a><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic</span><span class="w"> </span><span class="kn">import</span> <span class="n">BaseModel</span><span class="p">,</span> <span class="n">Field</span>
</span><span id="__span-1-3"><a id="__codelineno-1-3" name="__codelineno-1-3" href="#__codelineno-1-3"></a><span class="kn">from</span><span class="w"> </span><span class="nn">langchain_core.runnables</span><span class="w"> </span><span class="kn">import</span> <span class="n">RunnableLambda</span>
</span><span id="__span-1-4"><a id="__codelineno-1-4" name="__codelineno-1-4" href="#__codelineno-1-4"></a>
</span><span id="__span-1-5"><a id="__codelineno-1-5" name="__codelineno-1-5" href="#__codelineno-1-5"></a><span class="k">def</span><span class="w"> </span><span class="nf">f</span><span class="p">(</span><span class="n">x</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="__span-1-6"><a id="__codelineno-1-6" name="__codelineno-1-6" href="#__codelineno-1-6"></a>    <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="n">x</span><span class="p">[</span><span class="s2">&quot;a&quot;</span><span class="p">]</span> <span class="o">*</span> <span class="nb">max</span><span class="p">(</span><span class="n">x</span><span class="p">[</span><span class="s2">&quot;b&quot;</span><span class="p">]))</span>
</span><span id="__span-1-7"><a id="__codelineno-1-7" name="__codelineno-1-7" href="#__codelineno-1-7"></a>
</span><span id="__span-1-8"><a id="__codelineno-1-8" name="__codelineno-1-8" href="#__codelineno-1-8"></a><span class="k">class</span><span class="w"> </span><span class="nc">FSchema</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
</span><span id="__span-1-9"><a id="__codelineno-1-9" name="__codelineno-1-9" href="#__codelineno-1-9"></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Apply a function to an integer and list of integers.&quot;&quot;&quot;</span>
</span><span id="__span-1-10"><a id="__codelineno-1-10" name="__codelineno-1-10" href="#__codelineno-1-10"></a>
</span><span id="__span-1-11"><a id="__codelineno-1-11" name="__codelineno-1-11" href="#__codelineno-1-11"></a>    <span class="n">a</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="o">...</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Integer&quot;</span><span class="p">)</span>
</span><span id="__span-1-12"><a id="__codelineno-1-12" name="__codelineno-1-12" href="#__codelineno-1-12"></a>    <span class="n">b</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="o">...</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">&quot;List of ints&quot;</span><span class="p">)</span>
</span><span id="__span-1-13"><a id="__codelineno-1-13" name="__codelineno-1-13" href="#__codelineno-1-13"></a>
</span><span id="__span-1-14"><a id="__codelineno-1-14" name="__codelineno-1-14" href="#__codelineno-1-14"></a><span class="n">runnable</span> <span class="o">=</span> <span class="n">RunnableLambda</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
</span><span id="__span-1-15"><a id="__codelineno-1-15" name="__codelineno-1-15" href="#__codelineno-1-15"></a><span class="n">as_tool</span> <span class="o">=</span> <span class="n">runnable</span><span class="o">.</span><span class="n">as_tool</span><span class="p">(</span><span class="n">FSchema</span><span class="p">)</span>
</span><span id="__span-1-16"><a id="__codelineno-1-16" name="__codelineno-1-16" href="#__codelineno-1-16"></a><span class="n">as_tool</span><span class="o">.</span><span class="n">invoke</span><span class="p">({</span><span class="s2">&quot;a&quot;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span> <span class="s2">&quot;b&quot;</span><span class="p">:</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">]})</span>
</span></code></pre></div>
</div>
<div class="admonition example">
<p class="admonition-title"><code>dict</code> input, specifying schema via <code>arg_types</code></p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-2-1"><a id="__codelineno-2-1" name="__codelineno-2-1" href="#__codelineno-2-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">typing</span><span class="w"> </span><span class="kn">import</span> <span class="n">Any</span>
</span><span id="__span-2-2"><a id="__codelineno-2-2" name="__codelineno-2-2" href="#__codelineno-2-2"></a><span class="kn">from</span><span class="w"> </span><span class="nn">langchain_core.runnables</span><span class="w"> </span><span class="kn">import</span> <span class="n">RunnableLambda</span>
</span><span id="__span-2-3"><a id="__codelineno-2-3" name="__codelineno-2-3" href="#__codelineno-2-3"></a>
</span><span id="__span-2-4"><a id="__codelineno-2-4" name="__codelineno-2-4" href="#__codelineno-2-4"></a>
</span><span id="__span-2-5"><a id="__codelineno-2-5" name="__codelineno-2-5" href="#__codelineno-2-5"></a><span class="k">def</span><span class="w"> </span><span class="nf">f</span><span class="p">(</span><span class="n">x</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="__span-2-6"><a id="__codelineno-2-6" name="__codelineno-2-6" href="#__codelineno-2-6"></a>    <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="n">x</span><span class="p">[</span><span class="s2">&quot;a&quot;</span><span class="p">]</span> <span class="o">*</span> <span class="nb">max</span><span class="p">(</span><span class="n">x</span><span class="p">[</span><span class="s2">&quot;b&quot;</span><span class="p">]))</span>
</span><span id="__span-2-7"><a id="__codelineno-2-7" name="__codelineno-2-7" href="#__codelineno-2-7"></a>
</span><span id="__span-2-8"><a id="__codelineno-2-8" name="__codelineno-2-8" href="#__codelineno-2-8"></a>
</span><span id="__span-2-9"><a id="__codelineno-2-9" name="__codelineno-2-9" href="#__codelineno-2-9"></a><span class="n">runnable</span> <span class="o">=</span> <span class="n">RunnableLambda</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
</span><span id="__span-2-10"><a id="__codelineno-2-10" name="__codelineno-2-10" href="#__codelineno-2-10"></a><span class="n">as_tool</span> <span class="o">=</span> <span class="n">runnable</span><span class="o">.</span><span class="n">as_tool</span><span class="p">(</span><span class="n">arg_types</span><span class="o">=</span><span class="p">{</span><span class="s2">&quot;a&quot;</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="s2">&quot;b&quot;</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="nb">int</span><span class="p">]})</span>
</span><span id="__span-2-11"><a id="__codelineno-2-11" name="__codelineno-2-11" href="#__codelineno-2-11"></a><span class="n">as_tool</span><span class="o">.</span><span class="n">invoke</span><span class="p">({</span><span class="s2">&quot;a&quot;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span> <span class="s2">&quot;b&quot;</span><span class="p">:</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">]})</span>
</span></code></pre></div>
</div>
<div class="admonition example">
<p class="admonition-title"><code>str</code> input</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-3-1"><a id="__codelineno-3-1" name="__codelineno-3-1" href="#__codelineno-3-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">langchain_core.runnables</span><span class="w"> </span><span class="kn">import</span> <span class="n">RunnableLambda</span>
</span><span id="__span-3-2"><a id="__codelineno-3-2" name="__codelineno-3-2" href="#__codelineno-3-2"></a>
</span><span id="__span-3-3"><a id="__codelineno-3-3" name="__codelineno-3-3" href="#__codelineno-3-3"></a>
</span><span id="__span-3-4"><a id="__codelineno-3-4" name="__codelineno-3-4" href="#__codelineno-3-4"></a><span class="k">def</span><span class="w"> </span><span class="nf">f</span><span class="p">(</span><span class="n">x</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="__span-3-5"><a id="__codelineno-3-5" name="__codelineno-3-5" href="#__codelineno-3-5"></a>    <span class="k">return</span> <span class="n">x</span> <span class="o">+</span> <span class="s2">&quot;a&quot;</span>
</span><span id="__span-3-6"><a id="__codelineno-3-6" name="__codelineno-3-6" href="#__codelineno-3-6"></a>
</span><span id="__span-3-7"><a id="__codelineno-3-7" name="__codelineno-3-7" href="#__codelineno-3-7"></a>
</span><span id="__span-3-8"><a id="__codelineno-3-8" name="__codelineno-3-8" href="#__codelineno-3-8"></a><span class="k">def</span><span class="w"> </span><span class="nf">g</span><span class="p">(</span><span class="n">x</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="__span-3-9"><a id="__codelineno-3-9" name="__codelineno-3-9" href="#__codelineno-3-9"></a>    <span class="k">return</span> <span class="n">x</span> <span class="o">+</span> <span class="s2">&quot;z&quot;</span>
</span><span id="__span-3-10"><a id="__codelineno-3-10" name="__codelineno-3-10" href="#__codelineno-3-10"></a>
</span><span id="__span-3-11"><a id="__codelineno-3-11" name="__codelineno-3-11" href="#__codelineno-3-11"></a>
</span><span id="__span-3-12"><a id="__codelineno-3-12" name="__codelineno-3-12" href="#__codelineno-3-12"></a><span class="n">runnable</span> <span class="o">=</span> <span class="n">RunnableLambda</span><span class="p">(</span><span class="n">f</span><span class="p">)</span> <span class="o">|</span> <span class="n">g</span>
</span><span id="__span-3-13"><a id="__codelineno-3-13" name="__codelineno-3-13" href="#__codelineno-3-13"></a><span class="n">as_tool</span> <span class="o">=</span> <span class="n">runnable</span><span class="o">.</span><span class="n">as_tool</span><span class="p">()</span>
</span><span id="__span-3-14"><a id="__codelineno-3-14" name="__codelineno-3-14" href="#__codelineno-3-14"></a><span class="n">as_tool</span><span class="o">.</span><span class="n">invoke</span><span class="p">(</span><span class="s2">&quot;b&quot;</span><span class="p">)</span>
</span></code></pre></div>
</div>

    </div>

</div>



  </div>

    </div>

</div>




  </div>

    </div>

</div>












                
              </article>
            </div>
          
          
  <script>var tabs=__md_get("__tabs");if(Array.isArray(tabs))e:for(var set of document.querySelectorAll(".tabbed-set")){var labels=set.querySelector(".tabbed-labels");for(var tab of tabs)for(var label of labels.getElementsByTagName("label"))if(label.innerText.trim()===tab){var input=document.getElementById(label.htmlFor);input.checked=!0;continue e}}</script>

<script>var target=document.getElementById(location.hash.slice(1));target&&target.name&&(target.checked=target.name.startsWith("__tabbed_"))</script>
        </div>
        
          <button type="button" class="md-top md-icon" data-md-component="top" hidden>
  
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M13 20h-2V8l-5.5 5.5-1.42-1.42L12 4.16l7.92 7.92-1.42 1.42L13 8z"/></svg>
  Back to top
</button>
        
      </main>
      
        <footer class="md-footer">
  
  <div class="md-footer-meta md-typeset">
    <div class="md-footer-meta__inner md-grid">
      <div class="md-copyright">
  
  
</div>
      
        
<div class="md-social">
  
    
    
    
    
    <a href="https://github.com/langchain-ai/langchain" target="_blank" rel="noopener" title="LangChain on GitHub" class="md-social__link">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><!--! Font Awesome Free 7.1.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2025 Fonticons, Inc.--><path d="M173.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6m-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3m44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9M252.8 8C114.1 8 8 113.3 8 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C436.2 457.8 504 362.9 504 252 504 113.3 391.5 8 252.8 8M105.2 352.9c-1.3 1-1 3.3.7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1m-10.8-8.1c-.7 1.3.3 2.9 2.3 3.9 1.6 1 3.6.7 4.3-.7.7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3.7m32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3.7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1m-11.4-14.7c-1.6 1-1.6 3.6 0 5.9s4.3 3.3 5.6 2.3c1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2"/></svg>
    </a>
  
    
    
    
    
    <a href="https://www.langchain.com/join-community" target="_blank" rel="noopener" title="LangChain Community Slack" class="md-social__link">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Free 7.1.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2025 Fonticons, Inc.--><path d="M94.1 315.1c0 25.9-21.2 47.1-47.1 47.1S0 341 0 315.1 21.2 268 47.1 268h47.1v47.1zm23.7 0c0-25.9 21.2-47.1 47.1-47.1s47.1 21.2 47.1 47.1v117.8c0 25.9-21.2 47.1-47.1 47.1s-47.1-21.2-47.1-47.1zm47.1-189c-25.9 0-47.1-21.2-47.1-47.1s21.2-47 47.1-47S212 53.2 212 79.1v47.1h-47.1zm0 23.7c25.9 0 47.1 21.2 47.1 47.1S190.8 244 164.9 244H47.1C21.2 244 0 222.8 0 196.9s21.2-47.1 47.1-47.1zm189 47.1c0-25.9 21.2-47.1 47.1-47.1s47 21.2 47 47.1-21.2 47.1-47.1 47.1h-47.1v-47.1zm-23.7 0c0 25.9-21.2 47.1-47.1 47.1S236 222.8 236 196.9V79.1c0-25.9 21.2-47.1 47.1-47.1s47.1 21.2 47.1 47.1zm-47.1 189c25.9 0 47.1 21.2 47.1 47.1s-21.2 47-47.1 47-47.1-21.2-47.1-47.1v-47.1h47.1zm0-23.7c-25.9 0-47.1-21.2-47.1-47.1s21.2-47.1 47.1-47.1h117.8c25.9 0 47.1 21.2 47.1 47.1s-21.2 47.1-47.1 47.1z"/></svg>
    </a>
  
    
    
    
    
    <a href="https://twitter.com/LangChainAI" target="_blank" rel="noopener" title="LangChain on Twitter / X" class="md-social__link">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Free 7.1.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2025 Fonticons, Inc.--><path d="M357.2 48h70.6L273.6 224.2 455 464H313L201.7 318.6 74.5 464H3.8l164.9-188.5L-5.2 48h145.6l100.5 132.9zm-24.8 373.8h39.1L119.1 88h-42z"/></svg>
    </a>
  
    
    
    
    
    <a href="https://www.linkedin.com/company/langchain/" target="_blank" rel="noopener" title="LangChain on LinkedIn" class="md-social__link">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Free 7.1.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2025 Fonticons, Inc.--><path d="M416 32H31.9C14.3 32 0 46.5 0 64.3v383.4C0 465.5 14.3 480 31.9 480H416c17.6 0 32-14.5 32-32.3V64.3c0-17.8-14.4-32.3-32-32.3M135.4 416H69V202.2h66.5V416zM102.2 96a38.5 38.5 0 1 1 0 77 38.5 38.5 0 1 1 0-77m282.1 320h-66.4V312c0-24.8-.5-56.7-34.5-56.7-34.6 0-39.9 27-39.9 54.9V416h-66.4V202.2h63.7v29.2h.9c8.9-16.8 30.6-34.5 62.9-34.5 67.2 0 79.7 44.3 79.7 101.9z"/></svg>
    </a>
  
    
    
    
    
    <a href="https://www.youtube.com/@LangChain" target="_blank" rel="noopener" title="LangChain on YouTube" class="md-social__link">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><!--! Font Awesome Free 7.1.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2025 Fonticons, Inc.--><path d="M549.7 124.1c-6.2-23.7-24.8-42.3-48.3-48.6C458.9 64 288.1 64 288.1 64S117.3 64 74.7 75.5c-23.5 6.3-42 24.9-48.3 48.6C15 167 15 256.4 15 256.4s0 89.4 11.4 132.3c6.3 23.6 24.8 41.5 48.3 47.8C117.3 448 288.1 448 288.1 448s170.8 0 213.4-11.5c23.5-6.3 42-24.2 48.3-47.8 11.4-42.9 11.4-132.3 11.4-132.3s0-89.4-11.4-132.3zM232.2 337.6V175.2l142.7 81.2z"/></svg>
    </a>
  
</div>
      
    </div>
  </div>
</footer>
      
    </div>
    <div class="md-dialog" data-md-component="dialog">
      <div class="md-dialog__inner md-typeset"></div>
    </div>
    
      <div class="md-progress" data-md-component="progress" role="progressbar"></div>
    
    
    
      
      
      <script id="__config" type="application/json">{"annotate": null, "base": "../../..", "features": ["announce.dismiss", "content.action.edit", "content.code.copy", "content.code.select", "content.code.annotate", "content.tabs.link", "content.tooltips", "navigation.indexes", "navigation.sections", "navigation.instant", "navigation.instant.prefetch", "navigation.instant.progress", "navigation.tabs", "navigation.top", "navigation.prune", "navigation.tracking", "toc.follow", "search.suggest", "search.highlight", "search.share"], "search": "../../../assets/javascripts/workers/search.7a47a382.min.js", "tags": null, "translations": {"clipboard.copied": "Copied to clipboard", "clipboard.copy": "Copy to clipboard", "search.result.more.one": "1 more on this page", "search.result.more.other": "# more on this page", "search.result.none": "No matching documents", "search.result.one": "1 matching document", "search.result.other": "# matching documents", "search.result.placeholder": "Type to start searching", "search.result.term.missing": "Missing", "select.version": "Select version"}, "version": null}</script>
    
    
      <script src="../../../assets/javascripts/bundle.e71a0d61.min.js"></script>
      
        <script src="../../../javascripts/shortcuts.js"></script>
      
    
  </body>
</html>