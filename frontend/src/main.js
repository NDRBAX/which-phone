import { createApp } from "vue";
import { createPinia } from "pinia";
import App from "./App.vue";
import router from "./router";
import dataENG from "../dataENG";
// import "./assets/main.css";
import "./assets/tailwind.css";

/* import the fontawesome core */
import { library } from "@fortawesome/fontawesome-svg-core";

/* import font awesome icon component */
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

/* import specific icons */
import {
  faShop,
  faUsers,
  faMobileScreenButton,
  faCommentsDollar,
  faBrain,
  faHandHoldingDollar,
  faCheck,
  faChild,
} from "@fortawesome/free-solid-svg-icons";

/* add icons to the library */
library.add(
  faShop,
  faUsers,
  faMobileScreenButton,
  faCommentsDollar,
  faBrain,
  faHandHoldingDollar,
  faCheck,
  faChild
);

const app = createApp(App);

app.config.globalProperties.$dataENG = dataENG;
app.provide("dataENG", dataENG);

app.use(createPinia());
app.use(router);
app.component("font-awesome-icon", FontAwesomeIcon);

app.mount("#app");
