<template>
  <div class="sidebar-group">
    <p class="caption">
      <span class="caption-text"><a :href="pathto('index')">Reusable data best practices</a></span>
    </p>
    <div style="margin:16px;">
        <div id="search-container" ></div>
    </div>
      <div class="flex" style="flex-direction: column;">
        <p class="sidebar-header">Contribute</p>
        <a class="sidebar-button" href="https://github.com/newgene/reusable-data-best-practices/">
            Contribute to our github page
        </a>
    </div>
    <p class="sidebar-header">Chapters</p>
    <ul v-bind:class="{ current: toc.current }">
      <li v-for="entry in toc.entries" :key="entry.name" class="toctree-l1" v-bind:class="{current: entry.current}">
        <a :href="pathto(entry.name)" class="reference internal" v-bind:class="{current: entry.current}">{{ entry.title }}</a>
        <ul v-if="entry.children">
          <li v-for="entry2 in entry.children" :key="entry2.name" class="toctree-l2">
            <a :href="pathto(entry2.href)" class="reference internal">{{ entry2.title }}</a>
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  el: '#toctree-container',
  data: function (){
    let toctree_data = JSON.parse(sessionStorage.getItem('toctree_data_json'))
    return {
      toc: toctree_data[0],
    }
  },
  methods: {
    // can't access sphinx's pathto function so we have to compromise with our own
    pathto (to){
      let pathname = window.location.pathname;
      if(to.includes('#')){
        return to;
      }
      if(pathname.includes('chapters')){
        let index = pathname.substring(0,  pathname.indexOf("chapters"));
        return index + `${to}.html`;
      }

      if(pathname.includes('index.html')){
        let index = pathname.substring(0,  pathname.indexOf("index.html"));
        return index + `${to}.html`;
      }

      if(pathname.includes('search.html')){
        let index = pathname.substring(0,  pathname.indexOf("search.html"));
        return index + `${to}.html`;
      }
      return pathname + `${to}.html`;
    }
  },
}
</script>

<style scoped>
  
</style>