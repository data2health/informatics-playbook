<template>
  <footer class="footer">
    <div class="footer-items-wrapper">
      <div class="footer-item">
        <h3 class="footer-title">
          Sponsor
        </h3>
        <span>Stuff</span>
        <span>about</span>
        <span>sponsor</span>
      </div>
      <div class="footer-item">
        <h3 class="footer-title">
          Col 2
        </h3>
      </div>
    </div>
    <div style="margin-top: 30px;">
      <small>&copy; Copyright {{currentYear}}, Reusable data best practices</small>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer',
  el: '#footer-container',
  created () {
    this.getCurrentYear = this.getCurrentYear()
  },
  data: ()=>{
    return{
      currentYear: null
    }
  },
  methods: {
    getCurrentYear(){
      let date = new Date();
      this.currentYear = date.getFullYear();
    }
  }
}
</script>

<style scoped>
.footer{
  width: 100%;
  min-height: 200px;
  margin-top: 60px;
  background-color: #469db214;
  padding: 30px 10%;
  display: flex;
  flex-flow: column;
  align-items: flex-start;
}

.footer-items-wrapper{
  display: flex;
  width: 100%;
  height: 100%;
  flex-flow: row wrap;
}

.footer-item{
  display: flex;
  flex-flow: column;
  min-width: 30%;
  margin-right: 30px;
  align-items: flex-start;
}


.footer-title{
  font-weight: bold;
}
</style>