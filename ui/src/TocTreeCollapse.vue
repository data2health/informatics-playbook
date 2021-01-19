<template>
  <button type="button" v-on:click="onClick"
    class="collapse-sidebar" @mouseover="onMouseOver">
    <!--<svg xmlns="http://www.w3.org/2000/svg" style="height:100%;width:100%;" height="384pt" viewBox="0 -53 384 384" width="384pt"><path d="m368 154.667969h-352c-8.832031 0-16-7.167969-16-16s7.167969-16 16-16h352c8.832031 0 16 7.167969 16 16s-7.167969 16-16 16zm0 0"/><path d="m368 32h-352c-8.832031 0-16-7.167969-16-16s7.167969-16 16-16h352c8.832031 0 16 7.167969 16 16s-7.167969 16-16 16zm0 0"/><path d="m368 277.332031h-352c-8.832031 0-16-7.167969-16-16s7.167969-16 16-16h352c8.832031 0 16 7.167969 16 16s-7.167969 16-16 16zm0 0"/></svg>-->
    <svg class="svgCollapseButton" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 477.175 477.175" style="enable-background:new 0 0 477.175 477.175;" xml:space="preserve"
    v-bind:class="{svgOpenSidebar: this.isOpen}">
      <g>
        <path d="M360.731,229.075l-225.1-225.1c-5.3-5.3-13.8-5.3-19.1,0s-5.3,13.8,0,19.1l215.5,215.5l-215.5,215.5   c-5.3,5.3-5.3,13.8,0,19.1c2.6,2.6,6.1,4,9.5,4c3.4,0,6.9-1.3,9.5-4l225.1-225.1C365.931,242.875,365.931,234.275,360.731,229.075z   "/>
      </g>
    </svg>
  </button>
</template>

<script>
export default {
  el: '#toctree-collapse-container',
  data: function (){
    return{
      isOpen: true,

      // two states [free, docked]
      // docked should be static [open] through clicking, defaults to none
      // free is dynamic [open, closed] through mouseover on the side of the page, defaults to closed
      // toggling state should be done through clicking the current top left button (needs to change icon)
      // clicking the button sets the state to static [open] where its permanently open
      // clicking it again sets the state to dynamic [open, closed] where it toggles between [open, closed]
      // when the user hovers his mouse over the side of the page (but not the button)
      state: 'docked',
    }
  },
  computed: {
    console: () => console,
    window: () => window,
  },
   unmounted() {
    window.removeEventListener("resize", this.onResize);
  },
  created () {
    let width = window.innerWidth;
    if(width < 993){
      this.isOpen = true;
    }
    this.setInitialState(true);
    window.addEventListener("resize", this.onResize);
  },
  methods: {
    onMouseOver: function(){
      console.log("over")
    },
    onResize: function(){
      let width = window.innerWidth;
      if(width < 993){
        this.isOpen = true;
        this.setOpen();
      }
    },
    setOpen(created){
      let toctreeElement = document.getElementById('sidebar-wrapper');
      let contentWrapper = document.getElementById('content-wrapper');
      if(this.isOpen){
        toctreeElement.classList.remove('sidebar-group-hidden');
        contentWrapper.classList.remove('content-wrapper-full');
        //contentWrapper.style.width = null;
      }else{
        if(created){
          toctreeElement.style.transition = 'none';
          toctreeElement.classList.add('sidebar-group-hidden');
          // something is wrong here the timeout should not be needed but the css is broken
          // for now providing a lazy fix
          // wait some time for 'sidebar-group-hidden' transition to stop
          setTimeout(()=>{
            toctreeElement.style.transition = null;
          },500)
          contentWrapper.classList.add('content-wrapper-full');
        }else{
          toctreeElement.classList.add('sidebar-group-hidden');
          contentWrapper.classList.add('content-wrapper-full');
          //contentWrapper.style.width = '100%';

        }
      }
    },
    setInitialState (){
      let state = localStorage.getItem('toctreeCollapseState')
      // state is saved a boolean string
      if(state=='true' || window.innerWidth < 993){
        this.isOpen = true;
      }else{
        this.isOpen = false;
      }
      this.setOpen(true);
    },
    
    onClick (){
      this.isOpen = !this.isOpen;
      localStorage.setItem('toctreeCollapseState', this.isOpen)
      this.setOpen();
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
  outline: none;
}

.svgCollapseButton{
  -webkit-transition: transform 0.3s;
  -o-transition: transform 0.3s;
  transition: transform 0.3s;
}

.svgOpenSidebar{
  transform: rotate(180deg);
}

@media all and (max-width: 991px){
  .collapse-sidebar{
    display: none;
  }
}
</style>