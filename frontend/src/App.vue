<template>
  <header>
    <NavBar />
  </header>
  <footer>
    <FooterOne />
  </footer>
</template>

<script>
import NavBar from "./components/NavBar.vue";
import FooterOne from "./components/FooterOne.vue";

export default {
  components: { NavBar, FooterOne },
};
</script>
