<template>
  <div class="header">
    <div style="flex:1;"></div>
    <a target="#" class="header-item">About</a>
  </div>
</template>

<script>
export default {
  name: 'Header',
  el: '#header-container'
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
}
</style>