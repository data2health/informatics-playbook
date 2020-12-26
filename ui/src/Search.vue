<template>
  <div id="search">
    <div id="search-header-wrapper" class="search-header-wrapper">
      <input class="search-input" placeholder="Search" v-model="query"
      v-on:keyup.enter="submit" @keyup="doSomething"
      :style="{ background: 'url(' + this.searchSvgPath + ') no-repeat' }" />
      <div id="search-result-bubble" class="search-result-bubble search-result-bubble-hidden">
        <ul id="example-2" style="list-style: none; padding: 10px !important;
        height: 100%; overflow:auto;">
          <li class="search-list-item" v-for="(item, index) in this.queryMatches" :key="index">
            <a v-bind:href="item.searchUrl">
                <span class="search-matches-found">{{ item.count }} matches found</span>
                <span class="search-title">{{ item.documentTitle }}</span>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
//style="background: url(this.searchPath) no-repeat;" 
//remember to add update the icons svgs on mount
export default {
  el: '#search-container',
  computed: {
    console: () => console,
    window: () => window,
  },
  data: function() {
    let document_previews_value = sessionStorage.getItem('document_previews');
    let search_path = sessionStorage.getItem('search_path');
    let search_svg_path = sessionStorage.getItem('search_svg_path');
    //let document_previews = document.getElementById('document_previews_value').getAttribute('value');
    //console.log(JSON.parse(document_previews_value));
    return {
        query: '',
        queryMatches: [],
        documentPreviews: JSON.parse(document_previews_value),
        searchPath: search_path,
        searchSvgPath: search_svg_path,
    };
  },
  privateState:{
    matchCount:0,
    searchBubbleShown:false,
  },
  methods:{
    doSomething: function(){
      this.queryMatches.length = 0;
      this.documentPreviews.forEach(doc_preview=>{
        let count = doc_preview.preview.split(this.query).length - 1;
        //let replace = this.query;
        //let re = new RegExp(replace,"g");
        //var count = (doc_preview.preview.match(re) || []).length;
        let searchUrl = window.location.pathname.includes('/chapters/') ?
          doc_preview.document_url.replace('chapters/', '') + '?highlight=' + this.query :
          doc_preview.document_url + '?highlight=' + this.query
        if(count!==0){
          this.queryMatches.push({documentName: doc_preview.document_name, count:count,
          documentTitle:doc_preview.document_title, documentUrl:doc_preview.document_url,
          searchUrl:searchUrl})
        }
      })
      

      let isMatchFound = false;
      if(this.queryMatches){
        isMatchFound = !this.queryMatches.every(m=>m.count===0) && this.query;
      }
      if(isMatchFound){
        document.getElementById('search-result-bubble').classList.remove('search-result-bubble-hidden')
      }else{
        document.getElementById('search-result-bubble').classList.add('search-result-bubble-hidden')
      }
    },
    submit: function(){
      if(this.query) {
        window.location.href = this.searchPath + "?q=" + this.query
      }
    }
  }
}
</script>