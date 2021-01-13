<template>
  <div class="sidebar-group">
    <p class="caption">
      <span class="caption-text"><a href="{{ pathto('index') }}">{{ shorttitle|e }}</a></span>
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
        <a></a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  el: '#toc-tree',
  data: function (){
    let toctree_data = JSON.parse(sessionStorage.getItem('toctree_data_json'))
    return {
      toc: toctree_data[0]
    }
  },
}
</script>

<style scoped>
  
</style>