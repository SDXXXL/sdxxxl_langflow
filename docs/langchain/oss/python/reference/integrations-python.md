<!doctype html>
<html lang="en" class="no-js">
  <head>
    
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      
        <meta name="description" content="Unified reference documentation for LangChain and LangGraph Python packages.">
      
      
        <meta name="author" content="LangChain">
      
      
        <link rel="canonical" href="https://reference.langchain.com/python/integrations/">
      
      
        <link rel="prev" href="../deepagents/middleware/summarization/">
      
      
        <link rel="next" href="langchain_community/">
      
      
        
      
      
      <link rel="icon" href="../static/brand/docs-favicon.png">
      <meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.7.0">
    
    
  
    <title>Integrations overview | LangChain Reference</title>
  

    
      <link rel="stylesheet" href="../assets/stylesheets/main.618322db.min.css">
      
        
        <link rel="stylesheet" href="../assets/stylesheets/palette.ab4e12ef.min.css">
      
      

  
  
  
  
  <style>:root{--md-annotation-icon:url('data:image/svg+xml;charset=utf-8,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20viewBox%3D%220%200%2024%2024%22%3E%3Cpath%20d%3D%22M22%2012a10%2010%200%200%201-10%2010A10%2010%200%200%201%202%2012%2010%2010%200%200%201%2012%202a10%2010%200%200%201%2010%2010m-12%206%206-6-6-6-1.4%201.4%204.6%204.6-4.6%204.6z%22/%3E%3C/svg%3E');}</style>


    
    
      
    
    
      
        
        
        
        <link rel="stylesheet" href="../assets/external/fonts.googleapis.com/css.56f7ac64.css">
        <style>:root{--md-text-font:"Inter";--md-code-font:"JetBrains Mono"}</style>
      
    
    
      <link rel="stylesheet" href="../assets/_mkdocstrings.css">
    
      <link rel="stylesheet" href="../stylesheets/logos.css">
    
      <link rel="stylesheet" href="../stylesheets/toc.css">
    
      <link rel="stylesheet" href="../stylesheets/sticky_navigation.css">
    
      <link rel="stylesheet" href="../stylesheets/version_admonitions.css">
    
      <link rel="stylesheet" href="../stylesheets/page_width.css">
    
    <script>__md_scope=new URL("..",location),__md_hash=e=>[...e].reduce(((e,_)=>(e<<5)-e+_.charCodeAt(0)),0),__md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e)),__md_set=(e,_,t=localStorage,a=__md_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(_))}catch(e){}}</script>
    
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
      
        
        <a href="#popular-providers" class="md-skip">
          Skip to content
        </a>
      
    </div>
    <div data-md-component="announce">
      
    </div>
    
    
      

<header class="md-header" data-md-component="header">
  <nav class="md-header__inner md-grid" aria-label="Header">
    <a href=".." title="LangChain Reference" class="md-header__button md-logo" aria-label="LangChain Reference" data-md-component="logo">
      
  <img src="../static/brand/reference-light.svg" alt="logo" class="logo-light" />
  <img src="../static/brand/reference-dark.svg" alt="logo" class="logo-dark" />

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
            
              Integrations overview
            
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
      <a href=".." class="md-tabs__link">
        
  
  
    
  
  Get started

      </a>
    </li>
  

      
        
  
  
  
  
    
    
      <li class="md-tabs__item">
        <a href="../langchain/" class="md-tabs__link">
          
  
  
    
  
  LangChain

        </a>
      </li>
    
  

      
        
  
  
  
  
    
    
      <li class="md-tabs__item">
        <a href="../langgraph/" class="md-tabs__link">
          
  
  
    
  
  LangGraph

        </a>
      </li>
    
  

      
        
  
  
  
  
    
    
      <li class="md-tabs__item">
        <a href="../deepagents/" class="md-tabs__link">
          
  
  
    
  
  Deep Agents

        </a>
      </li>
    
  

      
        
  
  
  
    
  
  
    
    
      <li class="md-tabs__item md-tabs__item--active">
        <a href="./" class="md-tabs__link">
          
  
  
    
  
  Integrations

        </a>
      </li>
    
  

      
        
  
  
  
  
    
    
      <li class="md-tabs__item">
        <a href="../langsmith/" class="md-tabs__link">
          
  
  
    
  
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
    <a href=".." title="LangChain Reference" class="md-nav__button md-logo" aria-label="LangChain Reference" data-md-component="logo">
      
  <img src="../static/brand/reference-light.svg" alt="logo" class="logo-light" />
  <img src="../static/brand/reference-dark.svg" alt="logo" class="logo-dark" />

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
      <a href=".." class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Get started
  

    
  </span>
  
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
    
      
      
        
      
    
    
      
        
        
      
    
    <li class="md-nav__item md-nav__item--pruned md-nav__item--nested">
      
        
  
  
  
    <a href="../langchain/" class="md-nav__link">
      
  
  
  <span class="md-ellipsis">
    
  
    LangChain
  

    
  </span>
  
  

      
        <span class="md-nav__icon md-icon"></span>
      
    </a>
  

      
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
    
    
    
      
      
        
      
    
    
      
        
        
      
    
    <li class="md-nav__item md-nav__item--pruned md-nav__item--nested">
      
        
  
  
  
    <a href="../langgraph/" class="md-nav__link">
      
  
  
  <span class="md-ellipsis">
    
  
    LangGraph
  

    
  </span>
  
  

      
        <span class="md-nav__icon md-icon"></span>
      
    </a>
  

      
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
    
    
    
      
      
        
      
    
    
      
        
        
      
    
    <li class="md-nav__item md-nav__item--pruned md-nav__item--nested">
      
        
  
  
  
    <a href="../deepagents/" class="md-nav__link">
      
  
  
  <span class="md-ellipsis">
    
  
    Deep Agents
  

    
  </span>
  
  

      
        <span class="md-nav__icon md-icon"></span>
      
    </a>
  

      
    </li>
  

    
      
      
  
  
    
  
  
  
    
    
      
        
          
        
      
        
      
        
      
    
    
    
      
        
        
      
      
        
      
    
    
      
    
    <li class="md-nav__item md-nav__item--active md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_5" checked>
        
          
          <div class="md-nav__link md-nav__container">
            <a href="./" class="md-nav__link md-nav__link--active">
              
  
  
  <span class="md-ellipsis">
    
  
    Integrations
  

    
  </span>
  
  

            </a>
            
              
              <label class="md-nav__link md-nav__link--active" for="__nav_5" id="__nav_5_label" tabindex="">
                <span class="md-nav__icon md-icon"></span>
              </label>
            
          </div>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_5_label" aria-expanded="true">
          <label class="md-nav__title" for="__nav_5">
            <span class="md-nav__icon md-icon"></span>
            
  
    Integrations
  

          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_community/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Community
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    
    
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
    
      
      
        
          
          
        
      
    
    
      
    
    <li class="md-nav__item md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_5_3" >
        
          
          <label class="md-nav__link" for="__nav_5_3" id="__nav_5_3_label" tabindex="">
            
  
  
  <span class="md-ellipsis">
    
  
    Packages
  

    
  </span>
  
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="2" aria-labelledby="__nav_5_3_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_5_3">
            <span class="md-nav__icon md-icon"></span>
            
  
    Packages
  

          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
    
    
    
      
      
        
      
    
    
      
        
        
      
    
    <li class="md-nav__item md-nav__item--pruned md-nav__item--nested">
      
        
  
  
  
    <a href="langchain_anthropic/" class="md-nav__link">
      
  
  
  <span class="md-ellipsis">
    
  
    Anthropic
  

    
  </span>
  
  

      
        <span class="md-nav__icon md-icon"></span>
      
    </a>
  

      
    </li>
  

              
            
              
                
  
  
  
  
    
    
      
        
          
        
      
        
      
    
    
    
      
      
        
      
    
    
      
        
        
      
    
    <li class="md-nav__item md-nav__item--pruned md-nav__item--nested">
      
        
  
  
  
    <a href="langchain_amazon_nova/" class="md-nav__link">
      
  
  
  <span class="md-ellipsis">
    
  
    Amazon Nova
  

    
  </span>
  
  

      
        <span class="md-nav__icon md-icon"></span>
      
    </a>
  

      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_astradb/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    AstraDB
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_aws/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    AWS
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
        
      
    
    
    
      
      
        
      
    
    
      
        
        
      
    
    <li class="md-nav__item md-nav__item--pruned md-nav__item--nested">
      
        
  
  
  
    <a href="langchain_azure/" class="md-nav__link">
      
  
  
  <span class="md-ellipsis">
    
  
    Azure (Microsoft)
  

    
  </span>
  
  

      
        <span class="md-nav__icon md-icon"></span>
      
    </a>
  

      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_cerebras/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Cerebras
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_chroma/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Chroma
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_cohere/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Cohere
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_db2/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Db2
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_deepseek/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    DeepSeek
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_elasticsearch/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Elasticsearch
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_exa/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Exa
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_fireworks/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Fireworks
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
    
    
    
      
      
        
      
    
    
      
        
        
      
    
    <li class="md-nav__item md-nav__item--pruned md-nav__item--nested">
      
        
  
  
  
    <a href="langchain_google/" class="md-nav__link">
      
  
  
  <span class="md-ellipsis">
    
  
    Google
  

    
  </span>
  
  

      
        <span class="md-nav__icon md-icon"></span>
      
    </a>
  

      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_groq/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Groq
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_huggingface/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    HuggingFace
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
    
      
      
        
      
    
    
      
        
        
      
    
    <li class="md-nav__item md-nav__item--pruned md-nav__item--nested">
      
        
  
  
  
    <a href="langchain_ibm/" class="md-nav__link">
      
  
  
  <span class="md-ellipsis">
    
  
    IBM
  

    
  </span>
  
  

      
        <span class="md-nav__icon md-icon"></span>
      
    </a>
  

      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_milvus/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Milvus
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_mistralai/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Mistral AI
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="https://langchain-mongodb.readthedocs.io/en/latest/index.html" class="md-nav__link" target="_blank" rel="noopener">
        
  
  
  <span class="md-ellipsis">
    
  
    MongoDB
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_neo4j/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Neo4J
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_nomic/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Nomic
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_nvidia_ai_endpoints/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Nvidia AI Endpoints
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_ollama/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Ollama
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
    
      
      
        
      
    
    
      
        
        
      
    
    <li class="md-nav__item md-nav__item--pruned md-nav__item--nested">
      
        
  
  
  
    <a href="langchain_openai/" class="md-nav__link">
      
  
  
  <span class="md-ellipsis">
    
  
    OpenAI
  

    
  </span>
  
  

      
        <span class="md-nav__icon md-icon"></span>
      
    </a>
  

      
    </li>
  

              
            
              
                
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
    
    
    
      
      
        
      
    
    
      
        
        
      
    
    <li class="md-nav__item md-nav__item--pruned md-nav__item--nested">
      
        
  
  
  
    <a href="langchain_parallel/" class="md-nav__link">
      
  
  
  <span class="md-ellipsis">
    
  
    Parallel
  

    
  </span>
  
  

      
        <span class="md-nav__icon md-icon"></span>
      
    </a>
  

      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_perplexity/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Perplexity
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_pinecone/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Pinecone
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_postgres/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Postgres
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_prompty/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Prompty
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_qdrant/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Qdrant
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_redis/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Redis
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_sema4/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Sema4
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_snowflake/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Snowflake
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_sqlserver/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    SQLServer
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_tavily/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Tavily
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_together/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Together
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_unstructured/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Unstructured
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_upstage/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Upstage
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_weaviate/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    Weaviate
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="langchain_xai/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    
  
    xAI
  

    
  </span>
  
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
    
    
    
      
      
        
      
    
    
      
        
        
      
    
    <li class="md-nav__item md-nav__item--pruned md-nav__item--nested">
      
        
  
  
  
    <a href="../langsmith/" class="md-nav__link">
      
  
  
  <span class="md-ellipsis">
    
  
    LangSmith
  

    
  </span>
  
  

      
        <span class="md-nav__icon md-icon"></span>
      
    </a>
  

      
    </li>
  

    
  </ul>
</nav>
                  </div>
                </div>
              </div>
            
            
              
                
              
              <div class="md-sidebar md-sidebar--secondary" data-md-component="sidebar" data-md-type="toc" hidden>
                <div class="md-sidebar__scrollwrap">
                  <div class="md-sidebar__inner">
                    

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc" data-md-scrollfix>
      
        <li class="md-nav__item">
  <a href="#popular-providers" class="md-nav__link">
    <span class="md-ellipsis">
      
        <span class="md-typeset">
          Popular providers
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
                
                  
  



  
    <a href="https://github.com/langchain-ai/docs/tree/main/reference/python/docs/integrations/index.md" title="Edit this page" class="md-content__button md-icon" rel="edit noopener" target="_blank">
      
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M10 20H6V4h7v5h5v3.1l2-2V8l-6-6H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h4zm10.2-7c.1 0 .3.1.4.2l1.3 1.3c.2.2.2.6 0 .8l-1 1-2.1-2.1 1-1c.1-.1.2-.2.4-.2m0 3.9L14.1 23H12v-2.1l6.1-6.1z"/></svg>
    </a>
  
  


  <h1>LangChain integrations</h1>

<p>Welcome! These pages include reference documentation for all <code>langchain-*</code> Python integration packages.</p>
<p>To learn more about integrations in LangChain, visit the <a href="https://docs.langchain.com/oss/python/integrations/providers/overview" target="_blank" rel="noopener">Integrations overview</a>.</p>
<div class="admonition tip">
<p class="admonition-title">Model Context Protocol (MCP)</p>
<p>LangChain supports the Model Context Protocol (MCP). This lets external tools work with LangChain and LangGraph applications through a standard interface.</p>
<p>To use MCP tools in your project, see <a href="../langchain_mcp_adapters/"><code>langchain-mcp-adapters</code></a>.</p>
</div>
<hr />
<h2 id="popular-providers">Popular providers<a class="headerlink" href="#popular-providers" title="Copy anchor link to this section for reference">&para;</a></h2>
<div class="grid cards">
<ul>
<li>
<p><span class="twemoji lg middle"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><!--! Font Awesome Free 7.1.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2025 Fonticons, Inc.--><path d="M196.4 185.8v-48.6c0-4.1 1.5-7.2 5.1-9.2l97.8-56.3c13.3-7.7 29.2-11.3 45.6-11.3 61.4 0 100.4 47.6 100.4 98.3 0 3.6 0 7.7-.5 11.8l-101.5-59.4c-6.1-3.6-12.3-3.6-18.4 0zm228.3 189.4V259c0-7.2-3.1-12.3-9.2-15.9L287 168.4l42-24.1c3.6-2 6.7-2 10.2 0l97.8 56.4c28.2 16.4 47.1 51.2 47.1 85 0 38.9-23 74.8-59.4 89.6zM166.2 272.8l-42-24.6c-3.6-2-5.1-5.1-5.1-9.2V126.4c0-54.8 42-96.3 98.8-96.3 21.5 0 41.5 7.2 58.4 20l-100.9 58.4c-6.1 3.6-9.2 8.7-9.2 15.9v148.5zm90.4 52.2-60.2-33.8v-71.7l60.2-33.8 60.2 33.8v71.7zm38.7 155.7c-21.5 0-41.5-7.2-58.4-20l100.9-58.4c6.1-3.6 9.2-8.7 9.2-15.9V237.9l42.5 24.6c3.6 2 5.1 5.1 5.1 9.2v112.6c0 54.8-42.5 96.3-99.3 96.3zM173.8 366.5l-97.7-56.3C47.9 293.8 29 259 29 225.2c0-39.4 23.6-74.8 59.9-89.6v116.7c0 7.2 3.1 12.3 9.2 15.9l128 74.2-42 24.1c-3.6 2-6.7 2-10.2 0zm-5.6 84c-57.9 0-100.4-43.5-100.4-97.3 0-4.1.5-8.2 1-12.3l100.9 58.4c6.1 3.6 12.3 3.6 18.4 0l128.5-74.2v48.6c0 4.1-1.5 7.2-5.1 9.2l-97.8 56.3c-13.3 7.7-29.2 11.3-45.6 11.3zm127 60.9c62 0 113.7-44 125.4-102.4 57.3-14.9 94.2-68.6 94.2-123.4 0-35.8-15.4-70.7-43-95.7 2.6-10.8 4.1-21.5 4.1-32.3 0-73.2-59.4-128-128-128-13.8 0-27.1 2-40.4 6.7-23-22.5-54.8-36.9-89.6-36.9-62 0-113.7 44-125.4 102.4-57.3 14.8-94.2 68.6-94.2 123.4 0 35.8 15.4 70.7 43 95.7-2.6 10.8-4.1 21.5-4.1 32.3 0 73.2 59.4 128 128 128 13.8 0 27.1-2 40.4-6.7 23 22.5 54.8 36.9 89.6 36.9"/></svg></span> <strong><code>langchain-openai</code></strong></p>
<hr />
<p>Interact with OpenAI (completions, responses) and OpenAI compatible APIs.</p>
<p><a href="langchain_openai/"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M13.22 19.03a.75.75 0 0 1 0-1.06L18.19 13H3.75a.75.75 0 0 1 0-1.5h14.44l-4.97-4.97a.749.749 0 0 1 .326-1.275.75.75 0 0 1 .734.215l6.25 6.25a.75.75 0 0 1 0 1.06l-6.25 6.25a.75.75 0 0 1-1.06 0"/></svg></span> Reference</a></p>
</li>
<li>
<p><span class="twemoji lg middle"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="m4.714 15.956 4.718-2.648.079-.23-.08-.128h-.23l-.79-.048-2.695-.073-2.337-.097-2.265-.122-.57-.121-.535-.704.055-.353.48-.321.685.06 1.518.104 2.277.157 1.651.098 2.447.255h.389l.054-.158-.133-.097-.103-.098-2.356-1.596-2.55-1.688-1.336-.972-.722-.491L2 6.223l-.158-1.008.656-.722.88.06.224.061.893.686 1.906 1.476 2.49 1.833.364.304.146-.104.018-.072-.164-.274-1.354-2.446-1.445-2.49-.644-1.032-.17-.619a3 3 0 0 1-.103-.729L6.287.133 6.7 0l.995.134.42.364.619 1.415L9.735 4.14l1.555 3.03.455.898.243.832.09.255h.159V9.01l.127-1.706.237-2.095.23-2.695.08-.76.376-.91.747-.492.583.28.48.685-.067.444-.286 1.851-.558 2.903-.365 1.942h.213l.243-.242.983-1.306 1.652-2.064.728-.82.85-.904.547-.431h1.032l.759 1.129-.34 1.166-1.063 1.347-.88 1.142-1.263 1.7-.79 1.36.074.11.188-.02 2.853-.606 1.542-.28 1.84-.315.832.388.09.395-.327.807-1.967.486-2.307.462-3.436.813-.043.03.049.061 1.548.146.662.036h1.62l3.018.225.79.522.473.638-.08.485-1.213.62-1.64-.389-3.825-.91-1.31-.329h-.183v.11l1.093 1.068 2.003 1.81 2.508 2.33.127.578-.321.455-.34-.049-2.204-1.657-.85-.747-1.925-1.62h-.127v.17l.443.649 2.343 3.521.122 1.08-.17.353-.607.213-.668-.122-1.372-1.924-1.415-2.168-1.141-1.943-.14.08-.674 7.254-.316.37-.728.28-.607-.461-.322-.747.322-1.476.388-1.924.316-1.53.285-1.9.17-.632-.012-.042-.14.018-1.432 1.967-2.18 2.945-1.724 1.845-.413.164-.716-.37.066-.662.401-.589 2.386-3.036 1.439-1.882.929-1.086-.006-.158h-.055L4.138 18.56l-1.13.146-.485-.456.06-.746.231-.243 1.907-1.312Z"/></svg></span> <strong><code>langchain-anthropic</code></strong></p>
<hr />
<p>Interact with Claude (Anthropic) APIs.</p>
<p><a href="langchain_anthropic/"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M13.22 19.03a.75.75 0 0 1 0-1.06L18.19 13H3.75a.75.75 0 0 1 0-1.5h14.44l-4.97-4.97a.749.749 0 0 1 .326-1.275.75.75 0 0 1 .734.215l6.25 6.25a.75.75 0 0 1 0 1.06l-6.25 6.25a.75.75 0 0 1-1.06 0"/></svg></span> Reference</a></p>
</li>
<li>
<p><span class="twemoji lg middle"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M11.04 19.32Q12 21.51 12 24q0-2.49.93-4.68.96-2.19 2.58-3.81t3.81-2.55Q21.51 12 24 12q-2.49 0-4.68-.93a12.3 12.3 0 0 1-3.81-2.58 12.3 12.3 0 0 1-2.58-3.81Q12 2.49 12 0q0 2.49-.96 4.68-.93 2.19-2.55 3.81a12.3 12.3 0 0 1-3.81 2.58Q2.49 12 0 12q2.49 0 4.68.96 2.19.93 3.81 2.55t2.55 3.81"/></svg></span> <strong><code>langchain-google-genai</code></strong></p>
<hr />
<p>Access Google Gemini models via the Google Gen AI SDK.</p>
<p><a href="langchain_google_genai/"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M13.22 19.03a.75.75 0 0 1 0-1.06L18.19 13H3.75a.75.75 0 0 1 0-1.5h14.44l-4.97-4.97a.749.749 0 0 1 .326-1.275.75.75 0 0 1 .734.215l6.25 6.25a.75.75 0 0 1 0 1.06l-6.25 6.25a.75.75 0 0 1-1.06 0"/></svg></span> Reference</a></p>
</li>
<li>
<p><span class="twemoji lg middle"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M7.64 10.38c0 .25.02.45.07.62.05.12.12.28.21.46.04.04.05.1.05.15 0 .07-.04.13-.13.2l-.42.28c-.06.04-.12.06-.17.06-.07 0-.13-.04-.2-.1-.09-.1-.17-.2-.24-.31-.06-.11-.13-.24-.2-.39-.52.61-1.17.92-1.96.92-.56 0-1-.16-1.33-.48-.32-.32-.49-.75-.49-1.29 0-.55.2-1 .6-1.36.41-.34.95-.52 1.63-.52.23 0 .44.02.71.06.23.03.5.08.76.14v-.48c0-.51-.1-.84-.31-1.07-.22-.21-.57-.3-1.08-.3-.24 0-.48.03-.72.08-.25.06-.49.13-.72.23-.11.04-.2.07-.23.08-.05.02-.08.02-.11.02-.09 0-.14-.06-.14-.2v-.33c0-.1.01-.18.05-.23q.045-.075.18-.12c.24-.14.51-.24.84-.32a4 4 0 0 1 1.04-.13q1.185 0 1.74.54c.37.36.55.91.55 1.64v2.15zm-2.7 1.02c.22 0 .44-.04.68-.12s.45-.23.63-.43c.11-.13.19-.27.25-.43 0-.16.05-.35.05-.58v-.27c-.2-.07-.4-.07-.62-.12a7 7 0 0 0-.62-.04c-.45 0-.77.09-.99.27s-.32.43-.32.76c0 .32.07.56.24.71.16.17.39.25.7.25m5.34.71a.6.6 0 0 1-.28-.06c-.03-.05-.08-.14-.12-.26L8.32 6.65c-.04-.15-.06-.22-.06-.27 0-.11.05-.17.16-.17h.65c.13 0 .22.02.26.07.06.04.1.13.14.26l1.11 4.4 1.04-4.4c.03-.13.07-.22.13-.26.05-.04.14-.07.25-.07h.55c.12 0 .21.02.26.07.05.04.1.13.13.26L14 11l1.14-4.46c.04-.13.09-.22.13-.26.06-.04.14-.07.26-.07h.62c.11 0 .17.06.17.17 0 .03-.01.07-.02.12 0 0-.02.08-.04.15l-1.61 5.14c-.04.14-.08.21-.15.26-.04.04-.13.07-.24.07h-.57c-.13 0-.19-.02-.27-.07a.45.45 0 0 1-.12-.26L12.27 7.5l-1.03 4.28q-.045.195-.12.27a.5.5 0 0 1-.27.06zm8.55.18c-.33 0-.7-.04-1.03-.12s-.59-.17-.76-.26a.5.5 0 0 1-.21-.19.4.4 0 0 1-.04-.18v-.34c0-.14.05-.2.15-.2h.12c.04 0 .1.05.17.08.22.1.47.18.73.23.27.05.54.08.79.08.42 0 .75-.07.97-.22.23-.17.35-.36.35-.63 0-.19-.07-.34-.18-.47-.12-.12-.35-.24-.67-.34l-.97-.3c-.48-.16-.84-.38-1.06-.68a1.58 1.58 0 0 1-.33-.97c0-.28.06-.52.18-.73.12-.22.28-.4.46-.55.22-.15.44-.26.71-.34q.39-.12.84-.12.21 0 .45.03c.14.02.28.05.42.07.14.04.26.07.38.11s.2.08.28.12c.09.05.16.1.2.16s.06.13.06.22v.32q0 .21-.15.21c-.05 0-.14-.03-.26-.08-.37-.17-.8-.26-1.27-.26-.38 0-.66.06-.89.19-.2.12-.31.32-.31.59 0 .19.07.35.2.47.13.13.38.25.73.37l.95.3c.48.14.82.36 1.03.64q.3.405.3.93c0 .28-.06.54-.17.77-.12.22-.28.42-.5.58-.19.17-.44.29-.72.38s-.62.13-.95.13m1.25 3.24C17.89 17.14 14.71 18 12 18c-3.85 0-7.3-1.42-9.91-3.77-.21-.19-.02-.44.23-.29 2.82 1.63 6.29 2.62 9.89 2.62 2.43 0 5.1-.5 7.55-1.56.37-.15.68.26.32.53M21 14.5c-.29-.37-1.86-.18-2.57-.1-.21.03-.24-.16-.05-.3 1.25-.87 3.31-.6 3.54-.33.24.3-.06 2.36-1.23 3.34-.19.15-.36.07-.28-.11.27-.68.86-2.16.59-2.5"/></svg></span> <strong><code>langchain-aws</code></strong></p>
<hr />
<p>Use integrations related to the AWS platform such as Bedrock, S3, and more.</p>
<p><a href="langchain_aws/"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M13.22 19.03a.75.75 0 0 1 0-1.06L18.19 13H3.75a.75.75 0 0 1 0-1.5h14.44l-4.97-4.97a.749.749 0 0 1 .326-1.275.75.75 0 0 1 .734.215l6.25 6.25a.75.75 0 0 1 0 1.06l-6.25 6.25a.75.75 0 0 1-1.06 0"/></svg></span> Reference</a></p>
</li>
<li>
<p><span class="twemoji lg middle"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12.025 1.13c-5.77 0-10.449 4.647-10.449 10.378 0 1.112.178 2.181.503 3.185.064-.222.203-.444.416-.577a.96.96 0 0 1 .524-.15c.293 0 .584.124.84.284.278.173.48.408.71.694.226.282.458.611.684.951v-.014c.017-.324.106-.622.264-.874s.403-.487.762-.543c.3-.047.596.06.787.203s.31.313.4.467c.15.257.212.468.233.542.01.026.653 1.552 1.657 2.54.616.605 1.01 1.223 1.082 1.912.055.537-.096 1.059-.38 1.572.637.121 1.294.187 1.967.187.657 0 1.298-.063 1.921-.178-.287-.517-.44-1.041-.384-1.581.07-.69.465-1.307 1.081-1.913 1.004-.987 1.647-2.513 1.657-2.539.021-.074.083-.285.233-.542.09-.154.208-.323.4-.467a1.08 1.08 0 0 1 .787-.203c.359.056.604.29.762.543s.247.55.265.874v.015c.225-.34.457-.67.683-.952.23-.286.432-.52.71-.694.257-.16.547-.284.84-.285a.97.97 0 0 1 .524.151c.228.143.373.388.43.625l.006.04a10.3 10.3 0 0 0 .534-3.273c0-5.731-4.678-10.378-10.449-10.378M8.327 6.583a1.5 1.5 0 0 1 .713.174 1.487 1.487 0 0 1 .617 2.013c-.183.343-.762-.214-1.102-.094-.38.134-.532.914-.917.71a1.487 1.487 0 0 1 .69-2.803m7.486 0a1.487 1.487 0 0 1 .689 2.803c-.385.204-.536-.576-.916-.71-.34-.12-.92.437-1.103.094a1.487 1.487 0 0 1 .617-2.013 1.5 1.5 0 0 1 .713-.174m-10.68 1.55a.96.96 0 1 1 0 1.921.96.96 0 0 1 0-1.92m13.838 0a.96.96 0 1 1 0 1.92.96.96 0 0 1 0-1.92M8.489 11.458c.588.01 1.965 1.157 3.572 1.164 1.607-.007 2.984-1.155 3.572-1.164.196-.003.305.12.305.454 0 .886-.424 2.328-1.563 3.202-.22-.756-1.396-1.366-1.63-1.32q-.011.001-.02.006l-.044.026-.01.008-.03.024q-.018.017-.035.036l-.032.04a1 1 0 0 0-.058.09l-.014.025q-.049.088-.11.19a1 1 0 0 1-.083.116 1.2 1.2 0 0 1-.173.18q-.035.029-.075.058a1.3 1.3 0 0 1-.251-.243 1 1 0 0 1-.076-.107c-.124-.193-.177-.363-.337-.444-.034-.016-.104-.008-.2.022q-.094.03-.216.087-.06.028-.125.063l-.13.074q-.067.04-.136.086a3 3 0 0 0-.135.096 3 3 0 0 0-.26.219 2 2 0 0 0-.12.121 2 2 0 0 0-.106.128l-.002.002a2 2 0 0 0-.09.132l-.001.001a1.2 1.2 0 0 0-.105.212q-.013.036-.024.073c-1.139-.875-1.563-2.317-1.563-3.203 0-.334.109-.457.305-.454m.836 10.354c.824-1.19.766-2.082-.365-3.194-1.13-1.112-1.789-2.738-1.789-2.738s-.246-.945-.806-.858-.97 1.499.202 2.362c1.173.864-.233 1.45-.685.64-.45-.812-1.683-2.896-2.322-3.295s-1.089-.175-.938.647 2.822 2.813 2.562 3.244-1.176-.506-1.176-.506-2.866-2.567-3.49-1.898.473 1.23 2.037 2.16c1.564.932 1.686 1.178 1.464 1.53s-3.675-2.511-4-1.297c-.323 1.214 3.524 1.567 3.287 2.405-.238.839-2.71-1.587-3.216-.642-.506.946 3.49 2.056 3.522 2.064 1.29.33 4.568 1.028 5.713-.624m5.349 0c-.824-1.19-.766-2.082.365-3.194 1.13-1.112 1.789-2.738 1.789-2.738s.246-.945.806-.858.97 1.499-.202 2.362c-1.173.864.233 1.45.685.64.451-.812 1.683-2.896 2.322-3.295s1.089-.175.938.647-2.822 2.813-2.562 3.244 1.176-.506 1.176-.506 2.866-2.567 3.49-1.898-.473 1.23-2.037 2.16c-1.564.932-1.686 1.178-1.464 1.53s3.675-2.511 4-1.297c.323 1.214-3.524 1.567-3.287 2.405.238.839 2.71-1.587 3.216-.642.506.946-3.49 2.056-3.522 2.064-1.29.33-4.568 1.028-5.713-.624"/></svg></span> <strong><code>langchain-huggingface</code></strong></p>
<hr />
<p>Access HuggingFace-hosted models in LangChain.</p>
<p><a href="langchain_huggingface/"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M13.22 19.03a.75.75 0 0 1 0-1.06L18.19 13H3.75a.75.75 0 0 1 0-1.5h14.44l-4.97-4.97a.749.749 0 0 1 .326-1.275.75.75 0 0 1 .734.215l6.25 6.25a.75.75 0 0 1 0 1.06l-6.25 6.25a.75.75 0 0 1-1.06 0"/></svg></span> Reference</a></p>
</li>
<li>
<p><span class="twemoji lg middle"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M20 2H4a2 2 0 0 0-2 2v18l4-4h14a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2"/></svg></span> <strong><code>langchain-groq</code></strong></p>
<hr />
<p>Interface to Groq Cloud.</p>
<p><a href="langchain_groq/"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M13.22 19.03a.75.75 0 0 1 0-1.06L18.19 13H3.75a.75.75 0 0 1 0-1.5h14.44l-4.97-4.97a.749.749 0 0 1 .326-1.275.75.75 0 0 1 .734.215l6.25 6.25a.75.75 0 0 1 0 1.06l-6.25 6.25a.75.75 0 0 1-1.06 0"/></svg></span> Reference</a></p>
</li>
<li>
<p><span class="twemoji lg middle"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M16.361 10.26a.9.9 0 0 0-.558.47l-.072.148.001.207c0 .193.004.217.059.353.076.193.152.312.291.448.24.238.51.3.872.205a.86.86 0 0 0 .517-.436.75.75 0 0 0 .08-.498c-.064-.453-.33-.782-.724-.897a1.1 1.1 0 0 0-.466 0m-9.203.005c-.305.096-.533.32-.65.639a1.2 1.2 0 0 0-.06.52c.057.309.31.59.598.667.362.095.632.033.872-.205.14-.136.215-.255.291-.448.055-.136.059-.16.059-.353l.001-.207-.072-.148a.9.9 0 0 0-.565-.472 1 1 0 0 0-.474.007m4.184 2c-.131.071-.223.25-.195.383.031.143.157.288.353.407.105.063.112.072.117.136.004.038-.01.146-.029.243-.02.094-.036.194-.036.222.002.074.07.195.143.253.064.052.076.054.255.059.164.005.198.001.264-.03.169-.082.212-.234.15-.525-.052-.243-.042-.28.087-.355.137-.08.281-.219.324-.314a.365.365 0 0 0-.175-.48.4.4 0 0 0-.181-.033c-.126 0-.207.03-.355.124l-.085.053-.053-.032c-.219-.13-.259-.145-.391-.143a.4.4 0 0 0-.193.032m.39-2.195c-.373.036-.475.05-.654.086a4.5 4.5 0 0 0-.951.328c-.94.46-1.589 1.226-1.787 2.114-.04.176-.045.234-.045.53 0 .294.005.357.043.524.264 1.16 1.332 2.017 2.714 2.173.3.033 1.596.033 1.896 0 1.11-.125 2.064-.727 2.493-1.571.114-.226.169-.372.22-.602.039-.167.044-.23.044-.523 0-.297-.005-.355-.045-.531-.288-1.29-1.539-2.304-3.072-2.497a7 7 0 0 0-.855-.031zm.645.937a3.3 3.3 0 0 1 1.44.514c.223.148.537.458.671.662.166.251.26.508.303.82.02.143.01.251-.043.482-.08.345-.332.705-.672.957a3 3 0 0 1-.689.348c-.382.122-.632.144-1.525.138-.582-.006-.686-.01-.853-.042q-.856-.16-1.35-.68c-.264-.28-.385-.535-.45-.946-.03-.192.025-.509.137-.776.136-.326.488-.73.836-.963.403-.269.934-.46 1.422-.512.187-.02.586-.02.773-.002m-5.503-11a1.65 1.65 0 0 0-.683.298C5.617.74 5.173 1.666 4.985 2.819c-.07.436-.119 1.04-.119 1.503 0 .544.064 1.24.155 1.721.02.107.031.202.023.208l-.187.152a5.3 5.3 0 0 0-.949 1.02 5.5 5.5 0 0 0-.94 2.339 6.6 6.6 0 0 0-.023 1.357c.091.78.325 1.438.727 2.04l.13.195-.037.064c-.269.452-.498 1.105-.605 1.732-.084.496-.095.629-.095 1.294 0 .67.009.803.088 1.266.095.555.288 1.143.503 1.534.071.128.243.393.264.407.007.003-.014.067-.046.141a7.4 7.4 0 0 0-.548 1.873 5 5 0 0 0-.071.991c0 .56.031.832.148 1.279L3.42 24h1.478l-.05-.091c-.297-.552-.325-1.575-.068-2.597.117-.472.25-.819.498-1.296l.148-.29v-.177c0-.165-.003-.184-.057-.293a.9.9 0 0 0-.194-.25 1.7 1.7 0 0 1-.385-.543c-.424-.92-.506-2.286-.208-3.451.124-.486.329-.918.544-1.154a.8.8 0 0 0 .223-.531c0-.195-.07-.355-.224-.522a3.14 3.14 0 0 1-.817-1.729c-.14-.96.114-2.005.69-2.834.563-.814 1.353-1.336 2.237-1.475.199-.033.57-.028.776.01.226.04.367.028.512-.041.179-.085.268-.19.374-.431.093-.215.165-.333.36-.576.234-.29.46-.489.822-.729.413-.27.884-.467 1.352-.561.17-.035.25-.04.569-.04s.398.005.569.04a4.07 4.07 0 0 1 1.914.997c.117.109.398.457.488.602.034.057.095.177.132.267.105.241.195.346.374.43.14.068.286.082.503.045.343-.058.607-.053.943.016 1.144.23 2.14 1.173 2.581 2.437.385 1.108.276 2.267-.296 3.153-.097.15-.193.27-.333.419-.301.322-.301.722-.001 1.053.493.539.801 1.866.708 3.036-.062.772-.26 1.463-.533 1.854a2 2 0 0 1-.224.258.9.9 0 0 0-.194.25c-.054.109-.057.128-.057.293v.178l.148.29c.248.476.38.823.498 1.295.253 1.008.231 2.01-.059 2.581a1 1 0 0 0-.044.098c0 .006.329.009.732.009h.73l.02-.074.036-.134c.019-.076.057-.3.088-.516a9 9 0 0 0 0-1.258c-.11-.875-.295-1.57-.597-2.226-.032-.074-.053-.138-.046-.141a1.4 1.4 0 0 0 .108-.152c.376-.569.607-1.284.724-2.228.031-.26.031-1.378 0-1.628-.083-.645-.182-1.082-.348-1.525a6 6 0 0 0-.329-.7l-.038-.064.131-.194c.402-.604.636-1.262.727-2.04a6.6 6.6 0 0 0-.024-1.358 5.5 5.5 0 0 0-.939-2.339 5.3 5.3 0 0 0-.95-1.02l-.186-.152a.7.7 0 0 1 .023-.208c.208-1.087.201-2.443-.017-3.503-.19-.924-.535-1.658-.98-2.082-.354-.338-.716-.482-1.15-.455-.996.059-1.8 1.205-2.116 3.01a7 7 0 0 0-.097.726c0 .036-.007.066-.015.066a1 1 0 0 1-.149-.078A4.86 4.86 0 0 0 12 3.03c-.832 0-1.687.243-2.456.698a1 1 0 0 1-.148.078c-.008 0-.015-.03-.015-.066a7 7 0 0 0-.097-.725C8.997 1.392 8.337.319 7.46.048a2 2 0 0 0-.585-.041Zm.293 1.402c.248.197.523.759.682 1.388.03.113.06.244.069.292.007.047.026.152.041.233.067.365.098.76.102 1.24l.002.475-.12.175-.118.178h-.278c-.324 0-.646.041-.954.124l-.238.06c-.033.007-.038-.003-.057-.144a8.4 8.4 0 0 1 .016-2.323c.124-.788.413-1.501.696-1.711.067-.05.079-.049.157.013m9.825-.012c.17.126.358.46.498.888.28.854.36 2.028.212 3.145-.019.14-.024.151-.057.144l-.238-.06a3.7 3.7 0 0 0-.954-.124h-.278l-.119-.178-.119-.175.002-.474c.004-.669.066-1.19.214-1.772.157-.623.434-1.185.68-1.382.078-.062.09-.063.159-.012"/></svg></span> <strong><code>langchain-ollama</code></strong></p>
<hr />
<p>Use locally hosted models via Ollama.</p>
<p><a href="langchain_ollama/"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M13.22 19.03a.75.75 0 0 1 0-1.06L18.19 13H3.75a.75.75 0 0 1 0-1.5h14.44l-4.97-4.97a.749.749 0 0 1 .326-1.275.75.75 0 0 1 .734.215l6.25 6.25a.75.75 0 0 1 0 1.06l-6.25 6.25a.75.75 0 0 1-1.06 0"/></svg></span> Reference</a></p>
</li>
</ul>
</div>
<p>Other providers, including <code>langchain-community</code>, are listed in the section navigation (left sidebar).</p>
<div class="admonition question">
<p class="admonition-title">"I don't see the integration I'm looking for"</p>
<p>LangChain has hundreds of integrations, but not all are documented on this site. If you don't see the integration you're looking for, refer to their <a href="https://docs.langchain.com/oss/python/integrations/providers/all_providers" target="_blank" rel="noopener">provider page in the LangChain docs</a>. Furthermore, many community maintained integrations are available in the <a href="langchain_community/"><code>langchain-community</code></a> package.</p>
</div>
<div class="admonition note">
<p class="admonition-title">Create new integrations</p>
<p>For information on contributing new integrations, see <a href="https://docs.langchain.com/oss/python/contributing/integrations-langchain" target="_blank" rel="noopener">the guide</a>.</p>
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
    
    
    
      
      
      <script id="__config" type="application/json">{"annotate": null, "base": "..", "features": ["announce.dismiss", "content.action.edit", "content.code.copy", "content.code.select", "content.code.annotate", "content.tabs.link", "content.tooltips", "navigation.indexes", "navigation.sections", "navigation.instant", "navigation.instant.prefetch", "navigation.instant.progress", "navigation.tabs", "navigation.top", "navigation.prune", "navigation.tracking", "toc.follow", "search.suggest", "search.highlight", "search.share"], "search": "../assets/javascripts/workers/search.7a47a382.min.js", "tags": null, "translations": {"clipboard.copied": "Copied to clipboard", "clipboard.copy": "Copy to clipboard", "search.result.more.one": "1 more on this page", "search.result.more.other": "# more on this page", "search.result.none": "No matching documents", "search.result.one": "1 matching document", "search.result.other": "# matching documents", "search.result.placeholder": "Type to start searching", "search.result.term.missing": "Missing", "select.version": "Select version"}, "version": null}</script>
    
    
      <script src="../assets/javascripts/bundle.e71a0d61.min.js"></script>
      
        <script src="../javascripts/shortcuts.js"></script>
      
    
  </body>
</html>