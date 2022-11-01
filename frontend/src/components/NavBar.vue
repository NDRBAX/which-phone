<template>
  <div class="center examplex">
    <vs-navbar
      color="#0be881"
      text-white
      square
      center-collapsed
      v-model="active"
    >
      <template #left>
        <img src="../assets/smartphone.png" alt="" height="30" />
      </template>
      <vs-navbar-item :active="active == 'guide'" id="guide">
        Guide
      </vs-navbar-item>
      <vs-navbar-item :active="active == 'pricing'" id="pricing">
        Pricing
      </vs-navbar-item>
      <vs-navbar-item :active="active == 'wishlist'" id="wishlist">
        Wishlist
      </vs-navbar-item>
      <vs-navbar-item :active="active == 'about'" id="about">
        About
      </vs-navbar-item>
      <template #right>
        <vs-button color="#fff" flat>Login</vs-button>
        <vs-button color="#fff" border>Get Started</vs-button>
      </template>
    </vs-navbar>
    <div class="square">
      <div class="child">child 1</div>
      <div class="child">child 2</div>
      <!-- <div class="child">child 3</div> -->
    </div>
  </div>
</template>

<script>
export default {
  mounted() {
    this.active = this.$route.name;
  },
  data: () => ({
    active: "",
  }),
  name: "NavBar",
};
</script>
