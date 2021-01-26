<template>
  <button id="custom-collapse" type="button" v-on:click="click"
    class="navbar-toggle custom-navbar-toggle" data-target=".navbar-collapse">
    <span class="sr-only">Toggle navigation</span>
    <span class="icon-bar icon-bar-line"></span>
    <span class="icon-bar icon-bar-line"></span>
    <span class="icon-bar icon-bar-line"></span>
  </button>
</template>

<script>
export default {
  name: "CustomCollapse",
  methods:{
    click: function(){
      let mobileSidebar = document.getElementById('mobile-side-bar');
      mobileSidebar.classList.toggle('mobile-side-bar-hidden');
      let contentContainer = document.getElementById('content-container');
      contentContainer.classList.toggle('blur-background');
    }
  }
}
</script>

<style scoped>

</style>