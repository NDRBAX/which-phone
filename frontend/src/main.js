import Vue from "vue";
import Vuesax from "vuesax";

import App from "./App.vue";
import router from "./router";

// import "./assets/main.css";
import "vuesax/dist/vuesax.css"; //Vuesax styles

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");

Vue.use(Vuesax, {});
