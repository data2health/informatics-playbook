<template>
  <button type="button" v-on:click="onClick"
    class="collapse-sidebar">
    <svg xmlns="http://www.w3.org/2000/svg" style="height:100%;width:100%;" height="384pt" viewBox="0 -53 384 384" width="384pt"><path d="m368 154.667969h-352c-8.832031 0-16-7.167969-16-16s7.167969-16 16-16h352c8.832031 0 16 7.167969 16 16s-7.167969 16-16 16zm0 0"/><path d="m368 32h-352c-8.832031 0-16-7.167969-16-16s7.167969-16 16-16h352c8.832031 0 16 7.167969 16 16s-7.167969 16-16 16zm0 0"/><path d="m368 277.332031h-352c-8.832031 0-16-7.167969-16-16s7.167969-16 16-16h352c8.832031 0 16 7.167969 16 16s-7.167969 16-16 16zm0 0"/></svg>
  </button>
</template>

<script>
export default {
  el: '#toctree-collapse-container',
  data: function (){
    return{
      isOpen: true,
    }
  },
  methods: {
    onClick (){
      this.isOpen = !this.isOpen;
      let toctreeElement = document.getElementById('sidebar-wrapper');
      let contentWrapper = document.getElementById('content-wrapper');
      if(this.isOpen){
        toctreeElement.classList.remove('sidebar-group-hidden')
        contentWrapper.style.width = null;
      }else{
        toctreeElement.classList.add('sidebar-group-hidden')
        contentWrapper.style.width = '100%';
        
      }
    }
  }
}
</script>
<style scoped>
.collapse-sidebar{
  padding: 10px;
  border: 0;
  width: 40px;
  height: 40px;
  position: fixed;
  top: 0;
  left: 0;
  margin: 20px;
  margin-top: 15px;
  background-color: #cce2e8;
  border-radius: 50%;
  margin-left: 13px;
  z-index: 1000;
}

@media all and (max-width: 991px){
  .collapse-sidebar{
    display: none;
  }
}
</style>