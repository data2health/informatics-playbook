<template>
  <div id="search">
    <div id="search-header-wrapper">
      <input class="dynamic-search-input" placeholder="Search chapters" v-model="query"
      v-on:keyup.enter="submit" @keyup="doSomething"/>
      <div v-if="this.query !== ''">
        <p><b>{{ this.matchCount }}</b> matches found</p>
      </div>
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
        matchCount: 0,
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
      this.matchCount = 0;
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

      this.queryMatches.forEach(match=>{
        let chapterBoxElement = document.getElementById(match.documentUrl);

        // there is an initial flash with the count when the query is "" which basically counts
        // all the characters in the documents
        // this is not really needed, just prevents the flashing
        if(this.query!==""){
          this.matchCount += match.count;
        }

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
.dynamic-search-input{
  background-position: 8px 6px !important;
  border: 0;
  height: 32px;
  border-bottom: 2px solid #3e99af;
  padding: 5px 15px;
  font-size: 1.6rem;
  margin: 25px;
  outline: none;
  transition: all 0.1s;
}

.dynamic-search-input:focus{
  border-bottom: 7px solid #3e99af;
}
</style>