<template>
  <div id="go-to-top" v-on:click="goToTop" role="button" class="go-to-top flex center-items">
    <div class="arrow-svg">
      <svg fill="white" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 477.175 477.175" style="enable-background:new 0 0 477.175 477.175;transform: rotate(90deg);" xml:space="preserve">
        <g>
          <path d="M145.188,238.575l215.5-215.5c5.3-5.3,5.3-13.8,0-19.1s-13.8-5.3-19.1,0l-225.1,225.1c-5.3,5.3-5.3,13.8,0,19.1l225.1,225   c2.6,2.6,6.1,4,9.5,4s6.9-1.3,9.5-4c5.3-5.3,5.3-13.8,0-19.1L145.188,238.575z"/>
        </g>
      </svg>
      </div>
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

  .go-to-top{
      height: 50px;
      width: 50px;
      -webkit-box-shadow: 0 0.2px 0.4px rgba(0, 0, 0, 0.02), 0 0.6px 0.9px rgba(0, 0, 0, 0.028), 0 1.1px 1.8px rgba(0, 0, 0, 0.035), 0 2px 3.1px rgba(0, 0, 0, 0.042), 0 3.8px 5.8px rgba(0, 0, 0, 0.05), 0 9px 14px rgba(0, 0, 0, 0.07);
      box-shadow: 0 0.2px 0.4px rgba(0, 0, 0, 0.02), 0 0.6px 0.9px rgba(0, 0, 0, 0.028), 0 1.1px 1.8px rgba(0, 0, 0, 0.035), 0 2px 3.1px rgba(0, 0, 0, 0.042), 0 3.8px 5.8px rgba(0, 0, 0, 0.05), 0 9px 14px rgba(0, 0, 0, 0.07);
      position: fixed;
      bottom: 0;
      right: 0;
      margin: 60px;
      border-radius: 100%;
      background-color: #3e99af
  }
</style>