<template>
  <div id="app">
    <header>
      <NavBar :username="username" />
    </header>
    <RouterView />
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
  beforeMount() {
    this.username = useAuthStore().getUser;
  },
};
</script>

<style>
body {
  overflow-x: hidden;
}
</style>
