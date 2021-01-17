<template>
  <div class="flex center-items menu-wrapper">
    <div class="flex center-items" v-on:click="handleMenuClick">
      <svg style="height: 20px; width: 20px; cursor:pointer;" xmlns="http://www.w3.org/2000/svg" height="517pt" viewBox="0 -45 517.33333 517" width="517pt"><path d="m240 384.167969h-21.332031v-341.335938h128v21.335938c0 11.796875 9.535156 21.332031 21.332031 21.332031s21.332031-9.535156 21.332031-21.332031v-42.667969c0-11.796875-9.535156-21.332031-21.332031-21.332031h-346.667969c-11.796875 0-21.332031 9.535156-21.332031 21.332031v42.667969c0 11.796875 9.535156 21.332031 21.332031 21.332031s21.335938-9.535156 21.335938-21.332031v-21.335938h133.332031v341.335938h-21.332031c-11.796875 0-21.335938 9.535156-21.335938 21.332031s9.539063 21.332031 21.335938 21.332031h85.332031c11.796875 0 21.332031-9.535156 21.332031-21.332031s-9.535156-21.332031-21.332031-21.332031zm0 0"/><path d="m496 192.167969h-170.667969c-11.796875 0-21.332031 9.535156-21.332031 21.332031v37.332031c0 11.796875 9.535156 21.335938 21.332031 21.335938s21.335938-9.539063 21.335938-21.335938v-16h42.664062v149.335938h-10.664062c-11.796875 0-21.335938 9.535156-21.335938 21.332031s9.539063 21.332031 21.335938 21.332031h64c11.796875 0 21.332031-9.535156 21.332031-21.332031s-9.535156-21.332031-21.332031-21.332031h-10.667969v-149.335938h42.667969v10.667969c0 11.796875 9.535156 21.332031 21.332031 21.332031s21.332031-9.535156 21.332031-21.332031v-32c0-11.796875-9.535156-21.332031-21.332031-21.332031zm0 0"/></svg>
    </div>
      <div class="menu-bubble" v-if="menuOpen" v-click-outside="outsideClick">
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
        <div class="menu-item-wrapper-row" style="border: none; justify-content: flex-start;">
          <div role="button" class="menu-item-backgroundcolor" style="background-color:white; border:1px solid #d6d6d6;"
          v-on:click="()=>changeBackgroundColor('white')">
          </div>
          <div role="button" class="menu-item-backgroundcolor" style="background-color:black; border:1px solid #d6d6d6;"
          v-on:click="()=>changeBackgroundColor('black')">
          </div>
        </div>
      </span>
      <span class="menu-title">
        Font size
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
      <span class="menu-title">
        Size
      </span>
      <div class="menu-item-wrapper-row">
        <div class="flex center-items" style="width: 50%; border-right: 1px solid #d6d6d6; cursor:pointer;" v-on:click="decreaseDocumentSize">
          <svg style="height: 22px; width: 22px;" xmlns="http://www.w3.org/2000/svg" id="Layer" enable-background="new 0 0 64 64" height="512" viewBox="0 0 64 64" width="512"><path d="m52.586 8.586-14.586 14.586v-5.172c0-1.104-.896-2-2-2s-2 .896-2 2v10c0 1.104.896 2 2 2h10c1.104 0 2-.896 2-2s-.896-2-2-2h-5.172l14.586-14.586c.781-.781.781-2.047 0-2.828s-2.047-.781-2.828 0z"/><path d="m10 56c.512 0 1.023-.195 1.414-.586l14.586-14.586v5.172c0 1.104.896 2 2 2s2-.896 2-2v-10c0-1.104-.896-2-2-2h-10c-1.104 0-2 .896-2 2s.896 2 2 2h5.172l-14.586 14.586c-.781.781-.781 2.047 0 2.828.391.391.902.586 1.414.586z"/></svg>
        </div>
        <div class="flex center-items" style="width: 50%; cursor:pointer;"  v-on:click="increaseDocumentSize">
          <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 512 512" style="enable-background:new 0 0 512 512; height:15px; width:25px;" xml:space="preserve">
          <g>
            <g>
              <path d="M492,0H344.212c-11.046,0-20,8.954-20,20s8.954,20,20,20h99.503L283.394,200.322c-7.811,7.811-7.811,20.474,0,28.284    c7.81,7.81,20.473,7.811,28.284,0L472,68.284v99.503c0,11.046,8.954,20,20,20c11.046,0,20-8.954,20-20V20    C512,9.115,503.154,0,492,0z"/>
            </g>
          </g>
          <g>
            <g>
              <path d="M228.606,283.394c-7.811-7.81-20.474-7.811-28.284,0L40,443.716v-99.503c0-11.046-8.954-20-20-20s-20,8.954-20,20V492    c0,10.866,8.853,20,20,20h147.788c11.046,0,20-8.954,20-20c0-11.046-8.954-20-20-20H68.284l160.322-160.322    C236.417,303.867,236.417,291.204,228.606,283.394z"/>
            </g>
          </g>
          </svg>        
        </div>
      </div>
      <button v-on:click="resetToDefault" class="menu-title menu-item-wrapper-row"
      style="background-color: white;">Reset to default</button>
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
      fonts:["Helvetica", `'Roboto'`, 'Quicksand', `'Open Sans'`],
      selectedFont: `'Roboto'`,
      iconFontSize: require('./assets/icon-font-size.svg'),
      menuOpen: false,
    }
  },
  methods: {
    outsideClick: function (){
      this.menuOpen = false;
    },
    handleMenuClick: function () {
      this.menuOpen = !this.menuOpen;
    },
    handleFontChange: function (font){
      let element = document.getElementsByClassName('bodywrapper')[0];
      element.style.fontFamily = font;
      localStorage.setItem('fontFamilyPreference', font);
      this.selectedFont = font;
    },
    setInitialPreferences: function (){
      //let body = document.body;
      if(localStorage.getItem('fontFamilyPreference')){
        let element = document.getElementsByClassName('bodywrapper')[0];
        element.style.fontFamily = localStorage.getItem('fontFamilyPreference');
        this.selectedFont = localStorage.getItem('fontFamilyPreference');
      }
      if(localStorage.getItem('fontSize')){
        let element = document.getElementsByClassName('bodywrapper')[0];
        element.setAttribute('style', `font-size:${localStorage.getItem('fontSize')}px !important`);
      }
      if(localStorage.getItem('maxWidth')){
        let documentWrapper = document.getElementsByClassName('documentwrapper')[0];
        documentWrapper.setAttribute('style', `max-width: ${localStorage.getItem('maxWidth')}px`)
      }
    },
    getGlobalFontSize: function (){
      let html = document.documentElement;
      let fontSize = window.getComputedStyle(html).fontSize;
      // we only want the number so we remove the rest
      fontSize = fontSize.replace('!important', '').replace(/\s+/, '').replace('px', '')
      return parseInt(fontSize)
    },
    getBodyFontSize: function (){
      let element = document.getElementsByClassName('bodywrapper')[0];
      let fontSize = window.getComputedStyle(element).fontSize;
      fontSize = fontSize.replace('!important', '').replace(/\s+/, '').replace('px', '')
      return parseInt(fontSize)
    },
    getDocumentSize: function (){
      let documentWrapper = document.getElementsByClassName('documentwrapper')[0];
      let maxWidth = window.getComputedStyle(documentWrapper).maxWidth.replace('!important', '').replace(/\s+/, '').replace('px', '');
      return parseInt(maxWidth);
    },
    increaseDocumentSize: function (){ 
      let documentWrapper = document.getElementsByClassName('documentwrapper')[0];
      let maxWidth = this.getDocumentSize();
      
      
      // on large screens set max bounding to 1200
      // on smaller screens set to 840
      if(window.innerWidth > 2000){
        maxWidth = Math.min(maxWidth + 100, 1200);
      }else{
        maxWidth = Math.min(maxWidth + 100, 840);
      }
      
      documentWrapper.setAttribute('style', `max-width: ${maxWidth}px`)
      localStorage.setItem('maxWidth', maxWidth)
    },
    decreaseDocumentSize: function (){
      let documentWrapper = document.getElementsByClassName('documentwrapper')[0];
      let maxWidth = this.getDocumentSize();

      // setting min bound to 400
      maxWidth = Math.max(maxWidth - 100, 400);
      documentWrapper.setAttribute('style', `max-width: ${maxWidth}px`)
      localStorage.setItem('maxWidth', maxWidth)
    },
    increaseFontSize: function (){
      let fontSize = this.getBodyFontSize();
      let element = document.getElementsByClassName('bodywrapper')[0];      
      fontSize = Math.min(fontSize + 1, 20);
      element.style.fontSize = `${fontSize}px`;
      localStorage.setItem('fontSize', fontSize)
    },
    decreaseFontSize: function (){
      let fontSize = this.getBodyFontSize();
      let element = document.getElementsByClassName('bodywrapper')[0];      
      fontSize = Math.max(fontSize - 1, 12);
      element.style.fontSize = `${fontSize}px`;
      localStorage.setItem('fontSize', fontSize)
    },
    changeBackgroundColor: function (color){
      let body = document.body;
      body.className = "";
      if(color=='black'){
        body.classList.add('black-container');
      }else if(color=='white'){
        body.classList.add('white-container');
      }
    },
    resetToDefault: function (){
      // take values from classes (default values) instead of inline style
      let element = document.getElementsByClassName('bodywrapper')[0];
      let documentWrapper = document.getElementsByClassName('documentwrapper')[0];
      element.style.fontFamily = null;
      element.style.fontSize = null;
      documentWrapper.style.maxWidth = null;

      // also reset localstorage saved values
      localStorage.clear();
    }
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
  color: black;
}

.menu-item{
  display: flex;
  cursor: pointer;
  width: 100%;
  height: 30px;
  border-bottom: 1px solid #d6d6d6;
}

.menu-item-backgroundcolor{
  display: flex;
  cursor: pointer;
  width: 24%;
  height: 30px;
  border-bottom: 1px solid #d6d6d6;
  margin: 0 5px;
  border-radius: 5px;
  margin-left: 0;
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

<style>
.black-container{
  background-color: #1c1b1d;
  color: rgb(206, 206, 206);
}

.black-container svg{
  fill: white;
}

.white-container{
  background-color: white;
}
</style>