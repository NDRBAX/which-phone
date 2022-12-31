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
            class="font-medium text-teal-accent-400 hover:text-teal-accent-600"
            >login to your account</RouterLink
          >
        </p>
        <MessageError :errors="errors" :close="closeMessageError" />
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
              required
              class="relative block w-full appearance-none rounded-none rounded-t-md border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-teal-accent-400 focus:outline-none focus:ring-teal-accent-400 sm:text-sm focus:ring-1"
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
              required
              class="relative block w-full appearance-none rounded-none border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-teal-accent-400 focus:outline-none focus:ring-teal-accent-400 sm:text-sm"
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
              required
              class="relative block w-full appearance-none rounded-none border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-teal-accent-400 focus:outline-none focus:ring-teal-accent-400 sm:text-sm"
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
              required
              class="relative block w-full appearance-none rounded-none rounded-b-md border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-teal-accent-400 focus:outline-none focus:ring-teal-accent-400 sm:text-sm"
              placeholder="Confirm Password"
              v-model="re_password"
            />
          </div>
        </div>

        <div class="break-words text-md text-gray-900">
          <p class="font-bold text-center py-5">
            Please set a secure question and answer to make your account more
            safe
          </p>
          <ul class="text-sm list-disc px-9 text-justify">
            <li class="py-2">
              The question should be specific and personal, not something that
              could be easily guessed by others. It should contain at least 10
              characters.
            </li>
            <li>
              The answer should be something that you will remember, but not
              something that could be easily discovered by others. It should
              contain at least 5 characters.
            </li>
          </ul>
        </div>
        <!-- SECURE QUESTION/ANSWER -->
        <div class="-space-y-px rounded-md shadow-sm">
          <div>
            <label for="secureQuestion" class="sr-only">Secure Question</label>
            <input
              id="secureQuestion"
              minlength="10"
              maxlength="255"
              required
              class="relative block w-full appearance-none rounded-none rounded-t-md border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-teal-accent-400 focus:outline-none focus:ring-teal-accent-400 sm:text-sm focus:ring-1"
              placeholder="Secure Question"
              v-model="secureQuestion"
            />
          </div>
          <div>
            <label for="secureAnswer" class="sr-only">Secure Answer</label>
            <input
              id="secureAnswer"
              minlength="5"
              maxlength="255"
              required
              class="relative block w-full appearance-none rounded-none rounded-b-md border border-gray-300 px-3 py-2 focus:ring-1 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-teal-accent-400 focus:outline-none focus:ring-teal-accent-400 sm:text-sm"
              placeholder="Secure Answer"
              v-model="secureAnswer"
            />
          </div>
        </div>
        <div>
          <button
            type="submit"
            class="group relative flex w-full justify-center rounded-md border border-transparent bg-teal-accent-400 py-2 px-4 text-sm font-medium text-white hover:bg-teal-accent-600 focus:outline-none focus:ring-2 focus:ring-teal-accent-400 focus:ring-offset-2"
          >
            <span class="absolute inset-y-0 left-0 flex items-center pl-3">
              <LockClosedIcon class="h-5 w-5 text-white" aria-hidden="true" />
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
      secureQuestion: "",
      secureAnswer: "",
      errors: [],
    };
  },
  methods: {
    async submitForm() {
      try {
        const authResponse = await axios.post("/auth/users/", {
          email: this.email,
          username: this.username,
          password: this.password,
          re_password: this.re_password,
        });
        console.log(authResponse);

        try {
          const secureResponse = await axios.post("/wphone/set_secure", {
            username: this.username,
            question: this.secureQuestion,
            answer: this.secureAnswer,
          });
          console.log(secureResponse);
          this.$router.push("/");
        } catch (error) {
          console.log(error);
          // handle error
        }
      } catch (error) {
        console.log(error);
        this.errors = error.response.data;
      }
    },

    closeMessageError() {
      this.errors = [];
    },
  },
};
</script>
