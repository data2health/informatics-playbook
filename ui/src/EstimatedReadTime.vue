<template>
  <div class="estimated-read-time">
    {{ this.estimatedReadTime }} minutes read
  </div>
</template>

<script>
export default {
  name: "EstimatedReadTime",
  el:'#estimated-read-time-container',
  created () {
    this.estimatedReadTime = this.getEstimatedReadTime()
  },
  data: function (){
    return{
      estimatedReadTime:0,
    }
  },
  methods: {
    getEstimatedReadTime() {
      try{ // first time will throw exception, just ignore it
        let contentBody = document.getElementsByClassName('body')[0];
        let content = contentBody.firstElementChild;
        const wordsPerMinute = 200; // Average case.
        let result;
        let textLength = content.innerText.split(" ").length; // Split by words
        if(textLength > 0){
          let value = Math.ceil(textLength / wordsPerMinute);
          result = value;
        }
        return result
      }catch (e) {
        return 0
      }
    }
  }
}
</script>

<style scoped>
.estimated-read-time{
    color: #191919;
    background-color: #d6d6d6;
    width: fit-content;
    padding: 5px 15px;
    border-radius: 100px;
    font-weight: bold;
}
</style>