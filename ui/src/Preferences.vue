<template>
  <div class="flex center-items menu-wrapper">
    <div class="flex center-items" v-on:click="handleMenuClick">
      <svg style="height: 20px; width: 20px; cursor:pointer;" xmlns="http://www.w3.org/2000/svg" height="517pt" viewBox="0 -45 517.33333 517" width="517pt"><path d="m240 384.167969h-21.332031v-341.335938h128v21.335938c0 11.796875 9.535156 21.332031 21.332031 21.332031s21.332031-9.535156 21.332031-21.332031v-42.667969c0-11.796875-9.535156-21.332031-21.332031-21.332031h-346.667969c-11.796875 0-21.332031 9.535156-21.332031 21.332031v42.667969c0 11.796875 9.535156 21.332031 21.332031 21.332031s21.335938-9.535156 21.335938-21.332031v-21.335938h133.332031v341.335938h-21.332031c-11.796875 0-21.335938 9.535156-21.335938 21.332031s9.539063 21.332031 21.335938 21.332031h85.332031c11.796875 0 21.332031-9.535156 21.332031-21.332031s-9.535156-21.332031-21.332031-21.332031zm0 0"/><path d="m496 192.167969h-170.667969c-11.796875 0-21.332031 9.535156-21.332031 21.332031v37.332031c0 11.796875 9.535156 21.335938 21.332031 21.335938s21.335938-9.539063 21.335938-21.335938v-16h42.664062v149.335938h-10.664062c-11.796875 0-21.335938 9.535156-21.335938 21.332031s9.539063 21.332031 21.335938 21.332031h64c11.796875 0 21.332031-9.535156 21.332031-21.332031s-9.535156-21.332031-21.332031-21.332031h-10.667969v-149.335938h42.667969v10.667969c0 11.796875 9.535156 21.332031 21.332031 21.332031s21.332031-9.535156 21.332031-21.332031v-32c0-11.796875-9.535156-21.332031-21.332031-21.332031zm0 0"/></svg>
    </div>
      <div class="menu-bubble" v-if="menuOpen">
      <span class="menu-title">
        Font
      </span>
      <div class="menu-item-wrapper">
        <div class="menu-item" v-for="(font, index) in fonts" :key="font.message"
           v-on:click="()=>handleFontChange(font)"
           v-bind:style="{ borderBottom: index===fonts.length-1?'none':'1px solid #d6d6d6' }">
          <span class="menu-text" style="font-family: system-ui, serif;">
            {{ font }}
          </span>
          <div v-if="font==selectedFont" class="tick-container">
            <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Layer_1" x="0px" y="0px" viewBox="0 0 512 512" style="enable-background:new 0 0 512 512; height:40%;" xml:space="preserve">
              <path d="M504.502,75.496c-9.997-9.998-26.205-9.998-36.204,0L161.594,382.203L43.702,264.311c-9.997-9.998-26.205-9.997-36.204,0    c-9.998,9.997-9.998,26.205,0,36.203l135.994,135.992c9.994,9.997,26.214,9.99,36.204,0L504.502,111.7    C514.5,101.703,514.499,85.494,504.502,75.496z"/>
            </svg>
          </div>
        </div>
      </div>
      <span class="menu-title">
        Size
      </span>
      <div class="menu-item-wrapper-row">
        <div class="flex center-items" style="width: 50%; border-right: 1px solid #d6d6d6; cursor:pointer;"
        v-on:click="decreaseFontSize">
          a
        </div>
        <div class="flex center-items" style="width: 50%; cursor:pointer;"
        v-on:click="increaseFontSize">
          A
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Preferences",
  el: "#preferences-container",
  computed: {
    console: () => console,
    window: () => window,
  },
  created () {
    this.setInitialPreferences();
  },
  data(){
    return {
      fonts:["system-ui", `'Roboto'`, 'sans-serif'],
      selectedFont: `'Roboto'`,
      iconFontSize: require('./assets/icon-font-size.svg'),
      menuOpen: false,
    }
  },
  methods: {
    handleMenuClick: function () {
      this.menuOpen = !this.menuOpen;
    },
    handleFontChange: function (font){
      let body = document.body;
      body.style.fontFamily = font;
      localStorage.setItem('fontFamilyPreference', font);
      this.selectedFont = font;
    },
    setInitialPreferences: function (){
      let body = document.body;
      if(localStorage.getItem('fontFamilyPreference')){
        body.style.fontFamily = localStorage.getItem('fontFamilyPreference');
        this.selectedFont = localStorage.getItem('fontFamilyPreference');
      }
      if(localStorage.getItem('fontSize')){
        let html = document.documentElement;
        html.setAttribute('style', `font-size:${localStorage.getItem('fontSize')}px !important`);
      }
    },
    getGlobalFontSize: function (){
      let html = document.documentElement;
      let fontSize = window.getComputedStyle(html).fontSize;
      // we only want the number so we remove the rest
      fontSize = fontSize.replace('!important', '').replace(/\s+/, '').replace('px', '')
      console.log(fontSize);
      return parseInt(fontSize)
    },
    increaseFontSize: function (){
      let fontSize = this.getGlobalFontSize();
      let html = document.documentElement;
      fontSize = fontSize + 1;
      html.setAttribute('style', `font-size:${fontSize}px !important`);
      localStorage.setItem('fontSize', fontSize)
    },
    decreaseFontSize: function (){
      let fontSize = this.getGlobalFontSize();
      let html = document.documentElement;
      fontSize = fontSize - 1;
      html.setAttribute('style', `font-size:${fontSize}px !important`);
      localStorage.setItem('fontSize', fontSize)
    },
  }
}
</script>

<style scoped>
.menu-wrapper{
  position: relative;
}

.menu-bubble{
  position: absolute;
  width: 150px;
  height: auto;
  background-color: white;
  top: 30px;
  right: -15px;
  padding: 10px;
  box-shadow:
    0 0.3px 0.5px rgba(0, 0, 0, 0.017),
    0 0.9px 1.3px rgba(0, 0, 0, 0.025),
    0 2.1px 3px rgba(0, 0, 0, 0.033),
    0 7px 10px rgba(0, 0, 0, 0.05);
  border-radius: 5px;
}

.menu-item{
  display: flex;
  cursor: pointer;
  width: 100%;
  height: 30px;
  border-bottom: 1px solid #d6d6d6;
}

.menu-text{
  display: flex;
  align-items: center;
  flex: 1;
  height: 100%;
  padding: 0 10px;
}

.menu-title{
  font-size: 0.8em;
  margin-bottom: 5px;
  margin-top: 10px;
  display: block;
  color: #777777;
}

.menu-item-wrapper{
  border: 1px solid #d6d6d6;
  display: flex;
  flex-flow: column;
  border-radius: 5px;
}

.menu-item-wrapper-row{
  border: 1px solid #d6d6d6;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-flow: row;
  border-radius: 5px;
}

.tick-container{
  height: 100%;
  margin: 0 10px;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>