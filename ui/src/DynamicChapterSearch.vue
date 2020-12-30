<template>
  <div id="search">
    <div id="search-header-wrapper" class="search-header-wrapper">
      <input class="search-input" placeholder="Search" v-model="query"
      v-on:keyup.enter="submit" @keyup="doSomething"
      :style="{ background: 'url(' + this.searchSvgPath + ') no-repeat' }" />
    </div>
  </div>
</template>

<script>
export default {
  name: "DynamicChapterSearch",
  el: '#dynamic-chapter-search-container',
  computed: {
    console: () => console,
    window: () => window,
  },
  data: function() {
    let document_previews_value = sessionStorage.getItem('document_previews');
    let search_svg_path = sessionStorage.getItem('search_svg_path');

    return {
        query: '',
        queryMatches: [],
        documentPreviews: JSON.parse(document_previews_value),
        searchSvgPath: search_svg_path,
    };
  },
  privateState:{
    matchCount:0,
    searchBubbleShown:false,
  },
  methods: {
    doSomething: function () {
      this.queryMatches.length = 0;
      this.documentPreviews.forEach(doc_preview => {
        let count = doc_preview.preview.split(this.query).length - 1;

        let searchUrl = window.location.pathname.includes('/chapters/') ?
            doc_preview.document_url.replace('chapters/', '') + '?highlight=' + this.query :
            doc_preview.document_url + '?highlight=' + this.query
        this.queryMatches.push({
          documentName: doc_preview.document_name, count: count,
          documentTitle: doc_preview.document_title, documentUrl: doc_preview.document_url,
          searchUrl: searchUrl
        })

      })

      /*let isMatchFound = false;
      if (this.queryMatches) {
        isMatchFound = !this.queryMatches.every(m => m.count === 0) && this.query;
      }*/

      this.queryMatches.forEach(match=>{
        let chapterBoxElement = document.getElementById(match.documentUrl);
        console.log(match.count);
        if(match.count===0){
          chapterBoxElement.style.opacity = 0.3;
          console.log(chapterBoxElement, match)
        }else{
          chapterBoxElement.style.opacity = 1;
        }
      })
    },
    submit: function () {
      if (this.query) {
        window.location.href = this.searchPath + "?q=" + this.query
      }
    }
  }
}
</script>

<style scoped>

</style>