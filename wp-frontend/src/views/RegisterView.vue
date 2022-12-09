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
          Register an account
        </h2>
        <p class="mt-2 text-center text-sm text-gray-600">
          Or
          {{ " " }}
          <RouterLink
            to="/login"
            class="font-medium text-green-600 hover:text-green-500"
            >login to your account</RouterLink
          >
        </p>
        <MessageError :errors="errors" @close="closeMessageError" />
      </div>
      <form class="mt-8 space-y-6" v-on:submit.prevent="submitForm">
        <input type="hidden" name="remember" value="true" />
        <div class="-space-y-px rounded-md shadow-sm">
          <div>
            <label for="email-address" class="sr-only">Username</label>
            <input
              id="username"
              name="username"
              type="username"
              autocomplete="username"
              required=""
              class="relative block w-full appearance-none rounded-none rounded-t-md border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-green-500 focus:outline-none focus:ring-green-500 sm:text-sm"
              placeholder="Username"
              v-model="username"
            />
          </div>
          <div>
            <label for="email-address" class="sr-only">Email address</label>
            <input
              id="email-address"
              name="email"
              type="email"
              autocomplete="email"
              required=""
              class="relative block w-full appearance-none rounded-none border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-green-500 focus:outline-none focus:ring-green-500 sm:text-sm"
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
              class="relative block w-full appearance-none rounded-none border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-green-500 focus:outline-none focus:ring-green-500 sm:text-sm"
              placeholder="Password"
              v-model="password"
            />
          </div>
          <div>
            <label for="password" class="sr-only">Password</label>
            <input
              id="re_password"
              name="re_password"
              type="password"
              autocomplete="current-password"
              required=""
              class="relative block w-full appearance-none rounded-none rounded-b-md border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-green-500 focus:outline-none focus:ring-green-500 sm:text-sm"
              placeholder="Confirm Password"
              v-model="re_password"
            />
          </div>
        </div>

        <div>
          <button
            type="submit"
            class="group relative flex w-full justify-center rounded-md border border-transparent bg-green-600 py-2 px-4 text-sm font-medium text-white hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2"
          >
            <span class="absolute inset-y-0 left-0 flex items-center pl-3">
              <LockClosedIcon
                class="h-5 w-5 text-green-500 group-hover:text-green-400"
                aria-hidden="true"
              />
            </span>
            Register
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { LockClosedIcon } from "@heroicons/vue/20/solid";
import axios from "axios";
import MessageError from "../components/MessageError.vue";

export default {
  name: "RegisterView",
  components: {
    LockClosedIcon,
    MessageError,
  },
  data() {
    return {
      username: "",
      email: "",
      password: "",
      re_password: "",
      errors: {},
    };
  },
  methods: {
    submitForm() {
      const formData = {
        username: this.username,
        email: this.email,
        password: this.password,
        re_password: this.re_password,
      };

      axios
        .post("/auth/users/", formData)
        .then((response) => {
          console.log(response);
          this.$router.push("/");
        })
        .catch((error) => {
          this.errors = error.response.data;
        });
    },
    closeMessageError() {
      this.errors = {};
    },
  },
};
</script>
