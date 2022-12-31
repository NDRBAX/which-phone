import { createApp } from "vue";
import { createPinia } from "pinia";

import axios from "axios";
import VueCookies from "vue3-cookies";

import App from "./App.vue";
import router from "./router";
import dataENG from "../dataENG";
// import "./assets/main.css";
import "./assets/tailwind.css";

/* import the fontawesome core */
import { library } from "@fortawesome/fontawesome-svg-core";
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
  faHeart as faHeartSolid,
  faBatteryThreeQuarters,
  faMicrochip,
  faMemory,
  faCamera,
  faArrowDownWideShort,
  faArrowUpShortWide,
  faFilterCircleDollar,
  faHardDrive,
  faImagePortrait,
  faIndustry,
} from "@fortawesome/free-solid-svg-icons";

import { faHeart } from "@fortawesome/free-regular-svg-icons";

/* add icons to the library */
library.add(
  faShop,
  faUsers,
  faMobileScreenButton,
  faCommentsDollar,
  faBrain,
  faHandHoldingDollar,
  faCheck,
  faChild,
  faHeart,
  faHeartSolid,
  faBatteryThreeQuarters,
  faMicrochip,
  faMemory,
  faCamera,
  faArrowDownWideShort,
  faArrowUpShortWide,
  faFilterCircleDollar,
  faHardDrive,
  faImagePortrait,
  faIndustry
);

axios.defaults.baseURL = "http://127.0.0.1:8000";
axios.defaults.withCredentials = true;

const app = createApp(App);

app.config.globalProperties.$dataENG = dataENG;
app.provide("dataENG", dataENG);

app.use(VueCookies);

app.use(createPinia());
app.use(router, axios);

app.component("font-awesome-icon", FontAwesomeIcon);

app.mount("#app");
