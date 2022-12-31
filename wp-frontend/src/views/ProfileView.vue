<template>
  <div
    class="flex min-h-full items-center justify-center py-12 px-4 sm:px-6 lg:px-8"
  >
    <div class="grid grid-cols-3 gap-2">
      <div class="col-span-3 space-y-8 mb-12">
        <div>
          <span class="px-5">
            <MessageError
              :errors="errors"
              :close="closeMessageError"
              :type="isError"
          /></span>

          <h2
            class="text-center sm:text-2xl md:text-3xl lg:text-4xl text-4xl font-bold tracking-tight text-gray-900"
          >
            Profile <span class="text-teal-accent-400">Settings</span>
          </h2>
          <p class="mt-2 text-center text-lg text-gray-600">
            If you wish to change your username, email or password, you can do
            so here.
          </p>
        </div>
      </div>

      <!-- ACCOUNTS STATS -->
      <div class="flex justify-center col-span-3 mb-12">
        <div class="stats shadow">
          <div class="stat">
            <div class="stat-figure text-primary">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                class="inline-block w-8 h-8 stroke-current"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
                ></path>
              </svg>
            </div>
            <div class="stat-title">Total in wishlist</div>
            <div class="stat-value text-primary">
              <AnimatedNumber :value="totalWishlist" />
            </div>
            <div class="stat-desc">21% more than last month</div>
          </div>

          <div class="stat">
            <div class="stat-figure text-secondary">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                class="inline-block w-8 h-8 stroke-current"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M13 10V3L4 14h7v7l9-11h-7z"
                ></path>
              </svg>
            </div>
            <div class="stat-title">Search count</div>
            <div class="stat-value text-secondary">
              <AnimatedNumber :value="searchCount" />
            </div>
            <div class="stat-desc">21% more than last month</div>
          </div>

          <div class="stat">
            <div class="stat-figure text-secondary">
              <div class="avatar online z-0">
                <div class="w-16 rounded-full">
                  <img :src="avatar" />
                </div>
              </div>
            </div>
            <div class="stat-value">{{ username }}</div>
            <div class="stat-title">Registred</div>
            <div class="stat-desc text-secondary">Since yesterday</div>
          </div>
        </div>
      </div>
      <!-- GENERAL INFORMATIONS -->
      <div class="col-span-3 text-center text-3xl font-bold mt-2">
        General user informations
        <form
          class="mt-8 space-y-6 w-2/3 mx-auto"
          v-on:submit.prevent="editGeneral"
        >
          <div class="-space-y-px rounded-md shadow-sm">
            <!-- USERNAME -->
            <label
              for="username"
              class="block mb-2 text-sm font-medium text-gray-900 sr-only"
              >Username</label
            >
            <div class="flex">
              <span
                class="inline-flex items-center w-1/4 px-3 text-sm text-gray-900 bg-gray-50 border border-r-0 border-gray-300 rounded-tl-md"
              >
                Username
              </span>
              <input
                type="text"
                id="username"
                class="rounded-none rounded-tr-md border text-gray-900 focus:ring-teal-accent-400 focus:border-teal-accent-400 focus:outline-none focus:z-10 block flex-1 min-w-0 w-full text-sm border-gray-300 px-3 py-2 placeholder-gray-500"
                :placeholder="username"
                v-model="newUsername"
              />
            </div>
            <!-- EMAIL -->
            <label
              for="email"
              class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300 sr-only"
              >Email adress</label
            >
            <div class="flex">
              <span
                class="inline-flex items-center w-1/4 px-3 text-sm text-gray-900 bg-gray-50 border border-r-0 border-gray-300"
              >
                Email adress
              </span>
              <input
                type="text"
                id="email"
                disabled
                class="rounded-none border text-gray-900 focus:ring-teal-accent-400 focus:border-teal-accent-400 focus:outline-none focus:z-10 block flex-1 min-w-0 w-full text-sm border-gray-300 px-3 py-2 placeholder-gray-500"
                :placeholder="email"
                v-model="newEmail"
              />
            </div>

            <!-- AVATAR -->

            <div class="flex">
              <span
                class="inline-flex items-center w-1/4 px-3 py-3 text-sm text-gray-900 bg-gray-50 border border-r-0 border-gray-300 rounded-bl-md"
              >
                <img
                  class="bg-center rounded-full w-20 h-20 object-cover mx-auto"
                  :src="avatar"
                  alt=""
                />
              </span>
              <textarea
                style="overflow: auto; resize: none"
                id="avatar"
                class="rounded-none border text-gray-900 focus:ring-teal-accent-400 focus:border-teal-accent-400 focus:outline-none focus:z-10 block flex-1 min-w-0 w-full text-sm border-gray-300 px-3 py-2 placeholder-gray-500 rounded-br-md"
                :placeholder="avatar"
                v-model="newAvatar"
              ></textarea>
            </div>
          </div>

          <!-- BUTTON -->
          <div>
            <button
              type="submit"
              class="group relative flex w-full justify-center rounded-md border border-transparent bg-teal-accent-400 py-2 px-4 text-sm font-medium text-white hover:bg-teal-accent-600 focus:outline-none focus:ring-2 focus:ring-teal-accent-400 focus:ring-offset-2"
            >
              Save changes
            </button>
          </div>
        </form>
      </div>

      <!-- SECURITY QUESTION/ANSWER -->
      <div class="col-span-3 text-center text-3xl font-bold mt-12">
        Change your password
        <p class="text-base font-normal pt-5">
          If you want to change your password, please answer your security
          question first!
        </p>

        <form
          class="mt-8 space-y-6 w-2/3 mx-auto"
          v-on:submit.prevent="resetPassword"
        >
          <div class="-space-y-px rounded-md shadow-sm">
            <div>
              <label for="emailChangePassword" class="sr-only"
                >Email adress</label
              >
              <input
                id="emailChangePassword"
                name="emailChangePassword"
                type="emailChangePassword"
                class="relative block w-full appearance-none rounded-none rounded-t-md border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-teal-accent-400 focus:outline-none focus:ring-1 focus:ring-teal-accent-400 sm:text-sm"
                placeholder="Email adress"
                v-model="emailChangePassword"
              />
            </div>
            <div>
              <label for="secureQuestion" class="sr-only"
                >Secure question</label
              >
              <input
                id="secureQuestion"
                name="secureQuestion"
                type="secureQuestion"
                required
                class="relative block w-full appearance-none rounded-none border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-teal-accent-400 focus:outline-none focus:ring-teal-accent-400 sm:text-sm"
                placeholder="What is your security question ?"
                v-model="secureQuestion"
              />
            </div>
            <div>
              <label for="secureAnswer" class="sr-only">Secure Answer</label>
              <input
                id="secureAnswer"
                name="secureAnswer"
                type="secureAnswer"
                required=""
                class="relative block w-full appearance-none rounded-none rounded-b-md border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-teal-accent-400 focus:outline-none focus:ring-teal-accent-400 sm:text-sm"
                placeholder="What is your security answer ?"
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
              Confirm password change
            </button>
          </div>
        </form>
      </div>

      <!-- Change Password -->
      <div
        v-if="showChangePassword"
        class="col-span-3 text-center text-3xl font-bold mt-12"
      >
        New password
        <form
          class="mt-8 space-y-6 w-2/3 mx-auto"
          v-on:submit.prevent="submitNewPassword"
        >
          <div class="-space-y-px rounded-md shadow-sm">
            <div>
              <label for="password" class="sr-only">New password</label>
              <input
                id="password"
                name="password"
                type="password"
                autocomplete="current-password"
                required=""
                class="relative block w-full appearance-none rounded-t-md border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-teal-accent-400 focus:outline-none focus:ring-teal-accent-400 sm:text-sm"
                placeholder="New password"
                v-model="newPassword"
              />
            </div>
            <div>
              <label for="re_password" class="sr-only"
                >Confirm new password</label
              >
              <input
                id="re_password"
                name="re_password"
                type="password"
                autocomplete="current-password"
                required=""
                class="relative block w-full appearance-none rounded-none rounded-b-md border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-teal-accent-400 focus:outline-none focus:ring-teal-accent-400 sm:text-sm"
                placeholder="Confirm new password"
                v-model="re_newPassword"
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
              Confirm password change
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { LockClosedIcon } from "@heroicons/vue/20/solid";
import { useAuthStore } from "../stores/auth";
import { useWishlistStore } from "../stores/checked";
import MessageError from "../components/MessageError.vue";
import AnimatedNumber from "../components/AnimatedNumber.vue";
import axios from "axios";
export default {
  name: "ProfileView",
  components: {
    LockClosedIcon,
    MessageError,
    AnimatedNumber,
  },
  data() {
    return {
      newUsername: "",
      store: useAuthStore(),
      wishlistStore: useWishlistStore(),
      newEmail: "",
      newAvatar: "",
      // Change Password
      newPassword: "",
      re_newPassword: "",
      showChangePassword: false,
      emailChangePassword: "",
      secureQuestion: "",
      secureAnswer: "",
      token: "",
      isError: null,
      errors: [],
    };
  },
  computed: {
    avatar() {
      return this.store.getAvatar;
    },
    username() {
      return this.store.getUser;
    },
    email() {
      return this.store.getEmail;
    },
    totalWishlist() {
      return this.wishlistStore.getWishlist.length;
    },
    searchCount() {
      return this.store.getHistoryCount;
    },
  },
  methods: {
    async resetPassword() {
      try {
        const response = await axios.post("/wphone/reset_password", {
          email: this.emailChangePassword,
          question: this.secureQuestion,
          answer: this.secureAnswer,
        });
        if (response.data.token) {
          this.token = response.data.token;
          this.showChangePassword = true;
        } else {
          // show error message
          console.log(response.data.error);
          this.errors = response.data.error;
          this.isError = true;
        }
      } catch (error) {
        console.log(error);
      }
    },
    async submitNewPassword() {
      if (this.newPassword !== this.re_newPassword) {
        // show error message
        console.log("Passwords do not match");
        this.errors = ["Passwords do not match"];
        this.isError = true;
        return;
      } else {
        try {
          const response = await axios.post("/wphone/submit_new_password", {
            password: this.newPassword,
            token: this.token,
          });
          if (response.data === "success") {
            // show success message and clear form
            console.log("Password changed successfully");
            this.errors = ["Password changed successfully"];
            this.isError = false;
            this.newPassword = "";
            this.re_newPassword = "";
            this.showChangePassword = false;
          } else {
            // show error message
            console.log(response.data);
          }
        } catch (error) {
          console.log(error);
        }
      }
    },
    async editGeneral() {
      // check if avatar, or username or email is changed
      if (this.newAvatar === "" && this.newUsername === "") {
        // show error message
        console.log("Nothing to change");
        this.errors = ["Nothing to change"];
        this.isError = true;
        return;
      } else {
        try {
          const response = await axios.post("/wphone/edit_profile", {
            currentUsername: this.username,
            currentEmail: this.email,
            newAvatar: this.newAvatar,
            newUsername: this.newUsername,
          });
          if (response.data === "success") {
            // show success message and clear form
            console.log(
              "Changes saved successfully. You will see the changes next time you login."
            );
            this.errors = [
              "Changes saved successfully. You will see the changes next time you login.",
            ];
            this.isError = false;
            this.newAvatar = "";
            this.newUsername = "";
          } else {
            // show error message
            console.log(response.data);
          }
        } catch (error) {
          console.log(error);
        }
      }
    },
    closeMessageError() {
      this.errors = [];
    },
  },
};
</script>
