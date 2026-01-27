<!doctype html>
<html lang="en" class="no-js">
  <head>
    
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      
        <meta name="description" content="Unified reference documentation for LangChain and LangGraph Python packages.">
      
      
        <meta name="author" content="LangChain">
      
      
        <link rel="canonical" href="https://reference.langchain.com/python/langsmith/observability/sdk/">
      
      
        <link rel="prev" href="../../">
      
      
        <link rel="next" href="client/">
      
      
        
      
      
      <link rel="icon" href="../../../static/brand/docs-favicon.png">
      <meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.7.0">
    
    
  
    <title>LangSmith SDK | LangChain Reference</title>
  

    
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
      
        
        <a href="#quick-reference" class="md-skip">
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
            
              LangSmith SDK
            
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
            
              
            
              
                
  
  
    
  
  
  
    
    
      
        
      
    
    
    
      
      
        
          
          
        
      
    
    
      
    
    <li class="md-nav__item md-nav__item--active md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6_2" checked>
        
          
          <label class="md-nav__link" for="__nav_6_2" id="__nav_6_2_label" tabindex="">
            
  
  
  <span class="md-ellipsis">
    
  
    Observability & Evaluation
  

    
  </span>
  
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="2" aria-labelledby="__nav_6_2_label" aria-expanded="true">
          <label class="md-nav__title" for="__nav_6_2">
            <span class="md-nav__icon md-icon"></span>
            
  
    Observability & Evaluation
  

          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                
  
  
    
  
  
  
    
    
      
        
          
        
      
        
      
        
      
    
    
    
      
      
        
      
    
    
      
    
    <li class="md-nav__item md-nav__item--active md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6_2_1" checked>
        
          
          <div class="md-nav__link md-nav__container">
            <a href="./" class="md-nav__link md-nav__link--active">
              
  
  
  <span class="md-ellipsis">
    
  
    SDK
  

    
  </span>
  
  

            </a>
            
              
              <label class="md-nav__link md-nav__link--active" for="__nav_6_2_1" id="__nav_6_2_1_label" tabindex="0">
                <span class="md-nav__icon md-icon"></span>
              </label>
            
          </div>
        
        <nav class="md-nav" data-md-level="3" aria-labelledby="__nav_6_2_1_label" aria-expanded="true">
          <label class="md-nav__title" for="__nav_6_2_1">
            <span class="md-nav__icon md-icon"></span>
            
  
    SDK
  

          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
            
              
                
  
  
  
  
    
    
      
        
      
        
      
        
      
        
      
        
      
    
    
    
      
      
        
      
    
    
      
        
        
      
    
    <li class="md-nav__item md-nav__item--pruned md-nav__item--nested">
      
        
  
  
  
    <a href="client/" class="md-nav__link">
      
  
  
  <span class="md-ellipsis">
    
  
    Core APIs
  

    
  </span>
  
  

      
        <span class="md-nav__icon md-icon"></span>
      
    </a>
  

      
    </li>
  

              
            
              
                
  
  
  
  
    
    
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
    
      
      
        
      
    
    
      
        
        
      
    
    <li class="md-nav__item md-nav__item--pruned md-nav__item--nested">
      
        
  
  
  
    <a href="schemas/" class="md-nav__link">
      
  
  
  <span class="md-ellipsis">
    
  
    Additional APIs
  

    
  </span>
  
  

      
        <span class="md-nav__icon md-icon"></span>
      
    </a>
  

      
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    
    
      
        
      
        
      
    
    
    
      
      
        
          
          
        
      
    
    
      
    
    <li class="md-nav__item md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6_3" >
        
          
          <label class="md-nav__link" for="__nav_6_3" id="__nav_6_3_label" tabindex="">
            
  
  
  <span class="md-ellipsis">
    
  
    Deployment
  

    
  </span>
  
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="2" aria-labelledby="__nav_6_3_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_6_3">
            <span class="md-nav__icon md-icon"></span>
            
  
    Deployment
  

          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../deployment/sdk/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    SDK
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../deployment/remote_graph/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    RemoteGraph
  

    
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
  <a href="#quick-reference" class="md-nav__link">
    <span class="md-ellipsis">
      
        <span class="md-typeset">
          Quick Reference
        </span>
      
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#core-apis" class="md-nav__link">
    <span class="md-ellipsis">
      
        <span class="md-typeset">
          Core APIs
        </span>
      
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#additional-apis" class="md-nav__link">
    <span class="md-ellipsis">
      
        <span class="md-typeset">
          Additional APIs
        </span>
      
    </span>
  </a>
  
</li>
      
    </ul>
  
</nav>
                  </div>
                </div>
              </div>
            
          
          
            <div class="md-content" data-md-component="content">
              
              <article class="md-content__inner md-typeset">
                
                  


  
    <a href="https://github.com/langchain-ai/docs/tree/main/reference/python/docs/langsmith/observability/sdk/index.md" title="Edit this page" class="md-content__button md-icon" rel="edit noopener" target="_blank">
      
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M10 20H6V4h7v5h5v3.1l2-2V8l-6-6H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h4zm10.2-7c.1 0 .3.1.4.2l1.3 1.3c.2.2.2.6 0 .8l-1 1-2.1-2.1 1-1c.1-.1.2-.2.4-.2m0 3.9L14.1 23H12v-2.1l6.1-6.1z"/></svg>
    </a>
  
  


  <h1>LangSmith SDK reference</h1>

<p><a href="https://pypi.org/project/langsmith/#history" target="_blank" rel="noopener"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/langsmith?label=%20"></a>
<a href="https://opensource.org/licenses/MIT" target="_blank" rel="noopener"><img alt="PyPI - License" src="https://img.shields.io/pypi/l/langsmith"></a>
<a href="https://pypistats.org/packages/langsmith" target="_blank" rel="noopener"><img alt="PyPI - Downloads" src="https://img.shields.io/pepy/dt/langsmith"></a></p>
<p>Welcome to the LangSmith Python SDK reference docs! These pages detail the core interfaces you will use when building with LangSmith's Observability and Evaluations tools.</p>
<p>For user guides, tutorials, and conceptual overviews, please visit the <a href="https://docs.langchain.com/langsmith/home" target="_blank" rel="noopener">LangSmith documentation</a>.</p>
<h2 id="quick-reference">Quick Reference<a class="headerlink" href="#quick-reference" title="Copy anchor link to this section for reference">&para;</a></h2>
<table>
<thead>
<tr>
<th style="text-align: left;">Class/function</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><a href="client/"><code>Client</code></a></td>
<td style="text-align: left;">Synchronous client for interacting with the LangSmith API.</td>
</tr>
<tr>
<td style="text-align: left;"><a href="async_client/"><code>AsyncClient</code></a></td>
<td style="text-align: left;">Asynchronous client for interacting with the LangSmith API.</td>
</tr>
<tr>
<td style="text-align: left;"><a href="run_helpers/"><code>traceable</code></a></td>
<td style="text-align: left;">Wrapper/decorator for tracing any function.</td>
</tr>
<tr>
<td style="text-align: left;"><a href="testing/"><code>@pytest.mark.langsmith</code></a></td>
<td style="text-align: left;">LangSmith <code>pytest</code> integration.</td>
</tr>
<tr>
<td style="text-align: left;"><a href="wrappers/"><code>wrap_openai</code></a></td>
<td style="text-align: left;">Wrapper for OpenAI client, adds LangSmith tracing.</td>
</tr>
<tr>
<td style="text-align: left;"><a href="wrappers/"><code>wrap_anthropic</code></a></td>
<td style="text-align: left;">Wrapper for Anthropic client, adds LangSmith tracing.</td>
</tr>
</tbody>
</table>
<h2 id="core-apis">Core APIs<a class="headerlink" href="#core-apis" title="Copy anchor link to this section for reference">&para;</a></h2>
<p>The primary interfaces for the LangSmith SDK.</p>
<ul>
<li><a href="client/"><code>Client</code></a>: Synchronous client for the LangSmith API.</li>
<li><a href="async_client/"><code>AsyncClient</code></a>: Asynchronous client for the LangSmith API.</li>
<li><a href="run_helpers/">Run Helpers</a>: Functions like <code>traceable</code>, <code>trace</code>, and tracing context management.</li>
<li><a href="run_trees/">Run Trees</a>: Tree structure for representing runs and nested runs.</li>
<li><a href="evaluation/">Evaluation</a>: Tools for evaluating functions and models on datasets.</li>
</ul>
<h2 id="additional-apis">Additional APIs<a class="headerlink" href="#additional-apis" title="Copy anchor link to this section for reference">&para;</a></h2>
<ul>
<li><a href="schemas/">Schemas</a>: Data schemas and type definitions.</li>
<li><a href="utils/">Utilities</a>: Utility classes including error types and thread pool executors.</li>
<li><a href="wrappers/">Wrappers</a>: Tracing wrappers for popular LLM providers.</li>
<li><a href="anonymizer/">Anonymizer</a>: Tools for anonymizing sensitive data.</li>
<li><a href="testing/">Testing</a>: Testing utilities and pytest integration.</li>
<li><a href="expect/">Expect API</a>: Assertions and expectations for testing.</li>
</ul>







  
  






                
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