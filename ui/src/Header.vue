<template>
  <div class="header">
    <a :href="pathto('index')" class="header-item">Home</a>      
    <div style="flex:1;"></div>
    <!-- <a :href="pathto('about')" class="header-item">About</a> -->
  </div>
</template>

<script>
export default {
  name: 'Header',
  methods: {
    pathto (to){
      let pathname = window.location.pathname;
      if(to.includes('#')){
        return to;
      }
      if(pathname.includes('index.html')){
        let index = pathname.substring(0,  pathname.indexOf("index.html"));
        return index + `${to}.html`;
      }
      if(pathname.includes('about.html')){
        let index = pathname.substring(0,  pathname.indexOf("about.html"));
        return index + `${to}.html`;
      }
    },
  }
}
</script>

<style scoped>
.header{
  height: 60px;
  display: flex;
  flex-flow: row;
  justify-content: center;
  align-items: center;
}

.header-item{
  /*padding: 0px 20px;*/
  cursor: pointer;
  text-decoration: none;
  color: black !important;
}
</style>