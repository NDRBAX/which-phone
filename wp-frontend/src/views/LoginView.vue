<template>
  <div
    class="flex min-h-full items-center justify-center py-12 px-4 sm:px-6 lg:px-8"
  >
    <div class="w-full max-w-md space-y-8">
      <div>
        <img
          class="mx-auto h-12 w-auto"
          src="../assets/logo.svg"
          alt="Which Phone"
        />
        <h2
          class="mt-6 text-center text-3xl font-bold tracking-tight text-gray-900"
        >
          Sign in to your account
        </h2>
        <p class="mt-2 text-center text-sm text-gray-600">
          Or
          {{ " " }}
          <RouterLink
            to="/register"
            class="font-medium text-teal-accent-400 hover:text-teal-accent-600"
            >create an account to unclock all features</RouterLink
          >
        </p>
        <MessageError
          :errors="errors"
          :close="closeMessageError"
          :type="isError"
        />
      </div>
      <form class="mt-8 space-y-6" v-on:submit.prevent="submitForm">
        <input type="hidden" name="remember" value="true" />
        <div class="-space-y-px rounded-md shadow-sm">
          <div>
            <label for="email-address" class="sr-only">Email address</label>
            <input
              id="email-address"
              name="email"
              type="email"
              autocomplete="email"
              required=""
              class="relative block w-full appearance-none rounded-none rounded-t-md border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-teal-accent-400 focus:outline-none focus:ring-teal-accent-400 sm:text-sm"
              placeholder="Email address"
              v-model="email"
            />
          </div>
          <div>
            <label for="password" class="sr-only">Password</label>
            <input
              id="password"
              name="password"
              type="password"
              autocomplete="current-password"
              required=""
              class="relative block w-full appearance-none rounded-none rounded-b-md border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-teal-accent-400 focus:outline-none focus:ring-teal-accent-400 sm:text-sm"
              placeholder="Password"
              v-model="password"
            />
          </div>
        </div>
        <!-- 
        <div class="text-sm text-center">
          <a
            href="#"
            class="font-medium text-teal-accent-400 hover:text-teal-accent-700"
            >Forgot your password?</a
          >
        </div> -->

        <div>
          <button
            type="submit"
            class="group relative flex w-full justify-center rounded-md border border-transparent bg-teal-accent-400 py-2 px-4 text-sm font-medium text-white hover:bg-teal-accent-600 focus:outline-none focus:ring-2 focus:ring-teal-accent-400 focus:ring-offset-2"
          >
            <span class="absolute inset-y-0 left-0 flex items-center pl-3">
              <LockClosedIcon class="h-5 w-5 text-white" aria-hidden="true" />
            </span>
            Sign in
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { LockClosedIcon } from "@heroicons/vue/20/solid";
import { useAuthStore } from "../stores/auth";
import { useWishlistStore } from "../stores/checked";
import MessageError from "../components/MessageError.vue";
import axios from "axios";

export default {
  name: "LoginView",
  components: {
    LockClosedIcon,
    MessageError,
  },
  data() {
    return {
      email: "",
      password: "",
      errors: [],
      wishlist: useWishlistStore(),
      isError: null,
    };
  },
  methods: {
    submitForm() {
      const formData = {
        email: this.email,
        password: this.password,
      };

      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("access");

      axios
        .post("/auth/jwt/create/", formData)
        .then((response) => {
          const access = response.data.access;
          const refresh = response.data.refresh;
          let authStore = useAuthStore();
          authStore.setAccess(access);
          authStore.setRefresh(refresh);
          axios.defaults.headers.common["Authorization"] = `JWT ${access}`;

          axios.get("/auth/users/me/").then((response) => {
            const user = response.data.username;
            const avatar = response.data.avatar_url;
            const email = response.data.email;
            const history = response.data.history;

            console.log(user, avatar, email, history.length);
            authStore.setUser(user);
            authStore.setAvatar(avatar);
            authStore.setEmail(email);
            authStore.setHistoryCount(history.length);
            this.wishlist.initializeWishlist();
          });
          this.$router.push("/");
        })
        .catch((error) => {
          this.errors = error.response.data;
          this.isError = true;
        });
    },
    closeMessageError() {
      this.errors = [];
    },
  },
};
</script>
