<template>
  <header>
    <NavBar />
  </header>
  <RouterView />
  <footer>
    <FooterOne />
  </footer>
</template>

<script>
import NavBar from "./components/NavBar.vue";
import FooterOne from "./components/FooterOne.vue";
import { RouterView } from "vue-router";
export default {
  components: { NavBar, FooterOne, RouterView },
};
</script>
