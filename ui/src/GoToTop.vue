<template>
  <div id="go-to-top" v-on:click="goToTop" role="button" class="go-to-top flex center-items">
    <img src="_static/svg/arrow.svg" class="arrow-svg"/>
  </div>
</template>

<script>
export default {
  name: "GoToTop",
  el:'#go-to-top-container',
  methods:{
    goToTop: function(){
      window.scrollTo({top:0 ,behavior:'smooth'})
    }
  }
}
</script>

<style scoped>

</style>