import Vue from 'vue'
import CustomCollapse from './CustomCollapse';
import Search from "./Search";
import GoToTop from './GoToTop';
import ScrollProgression from "./ScrollProgression";
import EstimatedReadTime from "./EstimatedReadTime";
import DynamicChapterSearch from "./DynamicChapterSearch";
import Preferences from "./Preferences";
import Header from './Header';
import Footer from './Footer';

Vue.config.productionTip = false

new Vue({
  render: h => h(Search),
}).$mount('#search-container')

new Vue({
  render: h => h(GoToTop),
}).$mount('#go-to-top-container')

new Vue({
  render: h => h(CustomCollapse),
}).$mount('#custom-collapse-container')

new Vue({
  render: h => h(ScrollProgression),
}).$mount('#scroll-progression-container')

new Vue({
  render: h => h(EstimatedReadTime),
}).$mount('#estimated-read-time-container')

new Vue({
  render: h => h(DynamicChapterSearch),
}).$mount('#dynamic-chapter-search-container')

new Vue({
  render: h => h(Preferences),
}).$mount('#preferences-container')

new Vue({
  render: h => h(Header),
}).$mount('#header-container')

new Vue({
  render: h => h(Footer),
}).$mount('#footer-container')
