import Vue from 'vue'
//import App from './App.vue'
//import App2 from './App2'
import Search from "./Search";
Vue.config.productionTip = false

/*new Vue({
  render: h => h(App),
}).$mount('#app2')

new Vue({
  render: h => h(App2),
}).$mount('#app2')
*/

new Vue({
  render: h => h(Search),
}).$mount('#search-container')

