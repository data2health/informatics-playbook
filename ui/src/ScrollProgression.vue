<template>
  <div class="progress-bar-fixed-wrapper">
    <div class="progress-bar" v-bind:style="{ width: scrollPercentage }">

    </div>
  </div>
</template>

<script>
export default {
  name: "ScrollProgression",
  el:'#scroll-progression-container',
  created () {
    window.addEventListener('scroll', this.handleScroll);
  },
  unmounted () {
    window.removeEventListener('scroll', this.handleScroll);
  },
  data: function () {
    return{
      scrollPercentage: '0%',
    }
  },
  methods: {
    handleScroll () {
      let scrollPosition = window.scrollY;
      let maxHeight = document.body.scrollHeight;
      let scrollPercentage = (scrollPosition/(maxHeight - window.innerHeight))*100
      this.scrollPercentage = `${scrollPercentage}%`
      // Any code to be executed when the window is scrolled
    }
  }
}
</script>

<style scoped>
.progress-bar-fixed-wrapper{
  width: 100%;
  position: fixed;
  top: 0;
  left: 0;
}
.progress-bar{
  width: 0%;
  height: 10px;
  webkit-transition: width .1s ease;
  -o-transition: width .1s ease;
  transition: width .1s ease;
  box-shadow: none;
}

@media all and (max-width: 767px){
  .progress-bar-fixed-wrapper{
    top:51px;
  }
}
</style>