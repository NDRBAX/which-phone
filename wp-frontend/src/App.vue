<template>
  <div id="app">
    <header>
      <NavBar />
    </header>
    <body>
      <RouterView />
    </body>

    <footer>
      <FooterOne />
    </footer>
  </div>
</template>

<script>
import NavBar from "./components/NavBar.vue";
import FooterOne from "./components/FooterOne.vue";
import { RouterView } from "vue-router";
import { useAuthStore } from "./stores/auth";
import { useCsrfTokenStore } from "./stores/csrftoken";
import axios from "axios";

export default {
  name: "App",
  components: { NavBar, FooterOne, RouterView },
  data() {
    return {
      csrfToken: "",
      username: "",
    };
  },
  methods: {
    getCsrfToken() {
      axios({
        method: "get",
        url: "/wphone/get_csrf_token/",
        withCredentials: true,
      })
        .then((response) => {
          console.log(response.data.token);
          this.csrfToken = response.data.token;
          let store = useCsrfTokenStore();
          store.setCsrfToken(this.csrfToken);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getAcces() {
      const accessData = {
        refresh: useAuthStore().getRefresh,
      };

      console.log(accessData);
      axios
        .post("/auth/jwt/refresh/", accessData)
        .then((response) => {
          console.log(response);
          useAuthStore().setAccess(response.data.access);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  beforeCreate() {
    let authStore = useAuthStore();

    authStore.initializeStore();

    const access = authStore.getAccess;
    console.log(access);

    if (access) {
      axios.defaults.headers.common["Authorization"] = `JWT ${access}`;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },

  mounted() {
    this.getCsrfToken();
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Maven+Pro:wght@400;500;600;700;800;900&display=swap");

body {
  overflow-x: hidden;
  font-family: "Maven Pro", sans-serif;
  min-height: calc(100vh - 4rem);
}

::-webkit-scrollbar {
  width: 12px;
  background-color: #fff;
}

::-webkit-scrollbar-thumb {
  border-radius: 10px;

  background-color: #1de9b6;
}
</style>
